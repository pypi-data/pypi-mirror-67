import pytest
from pyrosm import get_path


@pytest.fixture
def test_pbf():
    pbf_path = get_path("test_pbf")
    return pbf_path


@pytest.fixture
def helsinki_pbf():
    pbf_path = get_path("helsinki_pbf")
    return pbf_path


@pytest.fixture
def default_filter():
    return {"amenity": True,
            "craft": True,
            "historic": True,
            "leisure": True,
            "shop": True,
            "tourism": True
            }


@pytest.fixture
def test_output_dir():
    import os, tempfile
    return os.path.join(tempfile.gettempdir(), "pyrosm_test_results")


def test_parsing_pois_with_defaults(helsinki_pbf, default_filter):
    from pyrosm import OSM
    from pyrosm.pois import get_poi_data
    from geopandas import GeoDataFrame
    import pyproj
    from pyrosm._arrays import concatenate_dicts_of_arrays
    osm = OSM(filepath=helsinki_pbf)
    osm._read_pbf()
    tags_as_columns = []
    for k in default_filter.keys():
        tags_as_columns += getattr(osm.conf.tags, k)

    nodes = concatenate_dicts_of_arrays(osm._nodes)
    gdf = get_poi_data(nodes,
                       osm._node_coordinates,
                       osm._way_records,
                       osm._relations,
                       tags_as_columns,
                       default_filter,
                       None)

    assert isinstance(gdf, GeoDataFrame)

    # Required keys
    required = ['id', 'geometry']
    for col in required:
        assert col in gdf.columns

    # Test shape
    assert len(gdf) == 1783
    assert gdf.crs == pyproj.CRS.from_epsg(4326)


def test_reading_pois_from_area_having_none(helsinki_pbf):
    from pyrosm import OSM
    from geopandas import GeoDataFrame

    # Bounding box for area that does not have any data
    bbox = [24.940514, 60.173849, 24.942, 60.175892]

    osm = OSM(filepath=helsinki_pbf, bounding_box=bbox)

    # The tool should warn if no buildings were found
    with pytest.warns(UserWarning) as w:
        gdf = osm.get_pois()
        # Check the warning text
        if "could not find any buildings" in str(w):
            pass

    # Result should be None
    assert gdf is None


def test_passing_incorrect_custom_filter(test_pbf):
    from pyrosm import OSM

    osm = OSM(filepath=test_pbf)
    try:
        osm.get_pois(custom_filter="wrong")
    except ValueError as e:
        if "dictionary" in str(e):
            pass
    except Exception as e:
        raise e


def test_adding_extra_attribute(helsinki_pbf):
    from pyrosm import OSM
    from geopandas import GeoDataFrame

    osm = OSM(filepath=helsinki_pbf)
    gdf = osm.get_pois()
    extra_col = "wikidata"
    extra = osm.get_pois(extra_attributes=[extra_col])

    # The extra should have one additional column compared to the original one
    assert extra.shape[1] == gdf.shape[1]+1
    # Should have same number of rows
    assert extra.shape[0] == gdf.shape[0]
    assert extra_col in extra.columns
    assert len(extra[extra_col].dropna().unique()) > 0
    assert isinstance(gdf, GeoDataFrame)