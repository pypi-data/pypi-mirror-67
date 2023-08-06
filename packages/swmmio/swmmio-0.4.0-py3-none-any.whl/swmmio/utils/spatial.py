from swmmio.defs.config import ROOT_DIR
from swmmio.tests.data import MODEL_FULL_FEATURES_XY
import json
import pandas as pd
from geojson import Point, LineString, Polygon, FeatureCollection, Feature
import os
import shutil


def change_crs(series, in_crs, to_crs):
    """
    Change the projection of a series of coordinates
    :param series:
    :param to_crs:
    :param in_crs:
    :return: series of reprojected coordinates
    >>> import swmmio
    >>> m = swmmio.Model(MODEL_FULL_FEATURES_XY)
    >>> proj4_str = '+proj=tmerc +lat_0=36.16666666666666 +lon_0=-94.5 +k=0.9999411764705882 +x_0=850000 +y_0=0 +datum=NAD83 +units=us-ft +no_defs' #"+init=EPSG:102698"
    >>> m.crs = proj4_str
    >>> nodes = m.nodes()
    >>> change_crs(nodes['coords'], proj4_str, "+init=EPSG:4326")
    Name
    J3    [(39.236286854940964, -94.64346373821752)]
    1      [(39.23851590020802, -94.64756446847099)]
    2       [(39.2382157223383, -94.64468629488778)]
    3      [(39.23878251491925, -94.64640342340165)]
    4     [(39.238353081411915, -94.64603818939938)]
    5      [(39.23797714290924, -94.64589184224722)]
    J2     [(39.23702605103406, -94.64543916929885)]
    J4     [(39.23633648359375, -94.64190240294558)]
    J1     [(39.23723558954326, -94.64583338271147)]
    Name: coords, dtype: object
    """
    try:
        import pyproj
    except ImportError:
        raise ImportError('pyproj module needed. get this package here: ',
                          'https://pypi.python.org/pypi/pyproj')

    # SET UP THE TO AND FROM COORDINATE PROJECTION
    in_proj = pyproj.Proj(in_crs, preserve_units=True)
    to_proj = pyproj.Proj(to_crs)

    # convert coords in coordinates, vertices, and polygons inp sections
    # transform to the typical 'WGS84' coord system
    def get_xys(xy_row):
        # need to reverse to lat/long after conversion
        return [pyproj.transform(in_proj, to_proj, x, y) for x, y in xy_row]

    if isinstance(series, pd.Series):
        return series.apply(lambda row: get_xys(row))
    if isinstance(series, pd.DataFrame):
        zipped_coords = list(zip(series.X, series.Y))
        df = pd.DataFrame(data=get_xys(zipped_coords), columns=["X", "Y"], index=series.index)
        return df
    elif isinstance(series, (list, tuple)):
        if isinstance(series[0], (list, tuple)):
            return get_xys(series)
        else:
            return get_xys([series])


def coords_series_to_geometry(coords, geomtype='linestring', format='geojson'):
    """
    Convert a series of coords (list of list(s)) to a series of geometry objects.
    :param coords: series of lists of xy coordinates
    :param format: format of geometry objects to be created ('geojson', 'shapely')
    :return: series of geometry objects
    >>> import swmmio
    >>> model = swmmio.Model(MODEL_FULL_FEATURES_XY)
    >>> nodes = model.nodes()
    >>> geoms = coords_series_to_geometry(nodes['coords'], geomtype='point')
    >>> geoms.iloc[0]
    {"coordinates": [2748073.3060000003, 1117746.087], "type": "Point"}
    """

    # detect whether LineString or Point should be used
    geomtype = geomtype.lower()
    if geomtype == 'linestring':
        geoms = [LineString(latlngs) for latlngs in coords]
    elif geomtype == 'point':
        geoms = [Point(latlngs[0]) for latlngs in coords]
    elif geomtype == 'polygon':
        geoms = [Polygon([latlngs]) for latlngs in coords]

    if format.lower() == 'shape':
        # convert to shapely objects
        try:
            from shapely.geometry import shape
        except ImportError:
            raise ImportError('shapely module needed. Install it via GeoPandas with conda: ',
                              'conda install geopandas')
        geoms = [shape(g) for g in geoms]

    return pd.Series(index=coords.index, name='geometry', data=geoms)


def write_geojson(df, filename=None, geomtype='linestring'):
    # try:
    #     import pyproj
    # except ImportError:
    #     raise ImportError('pyproj module needed. get this package here: ',
    #                       'https://pypi.python.org/pypi/pyproj')
    #
    # # SET UP THE TO AND FROM COORDINATE PROJECTION
    # pa_plane = pyproj.Proj(init=inproj, preserve_units=True)
    # wgs = pyproj.Proj(proj='longlat', datum='WGS84', ellps='WGS84')  # google maps, etc

    # CONVERT THE DF INTO JSON
    df['Name'] = df.index  # add a name column (we wont have the index)
    records = json.loads(df.to_json(orient='records'))

    # ITERATE THROUGH THE RECORDS AND CREATE GEOJSON OBJECTS
    features = []
    for rec in records:

        coordinates = rec['coords']
        del rec['coords']  # delete the coords so they aren't in the properties

        # transform to the typical 'WGS84' coord system
        # latlngs = [pyproj.transform(pa_plane, wgs, *xy) for xy in coordinates]
        latlngs = coordinates
        # print(latlngs)

        if geomtype == 'linestring':
            geometry = LineString(latlngs)
        elif geomtype == 'point':
            geometry = Point(latlngs)
        elif geomtype == 'polygon':
            geometry = Polygon([latlngs])

        feature = Feature(geometry=geometry, properties=rec)
        features.append(feature)

    if filename is not None:
        with open(filename, 'wb') as f:
            f.write(json.dumps(FeatureCollection(features)))
        return filename

    else:
        return FeatureCollection(features)


def write_shapefile(df, filename, geomtype='line', prj=None):
    """
    create a shapefile given a pandas Dataframe that has coordinate data in a
    column called 'coords'.
    """

    import shapefile
    df['Name'] = df.index

    # create a shp file writer object of geom type 'point'
    if geomtype == 'point':
        w = shapefile.Writer(shapefile.POINT)
    elif geomtype == 'line':
        w = shapefile.Writer(shapefile.POLYLINE)
    elif geomtype == 'polygon':
        w = shapefile.Writer(shapefile.POLYGON)

    # use the helper mode to ensure the # of records equals the # of shapes
    # (shapefile are made up of shapes and records, and need both to be valid)
    w.autoBalance = 1

    # add the fields
    for fieldname in df.columns:
        w.field(fieldname, "C")

    for k, row in df.iterrows():
        w.record(*row.tolist())
        w.line(parts=[row.coords])

    w.save(filename)

    # add projection data to the shapefile,
    if prj is None:
        # if not sepcified, the default, projection is used (PA StatePlane)
        prj = os.path.join(ROOT_DIR, 'swmmio/defs/default.prj')
    prj_filepath = os.path.splitext(filename)[0] + '.prj'
    shutil.copy(prj, prj_filepath)


def read_shapefile(shp_path):
    """
        Read a shapefile into a Pandas dataframe with a 'coords' column holding
        the geometry information. This uses the pyshp package
        """
    import shapefile

    # read file, parse out the records and shapes
    sf = shapefile.Reader(shp_path)
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]

    # write into a dataframe
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    return df
