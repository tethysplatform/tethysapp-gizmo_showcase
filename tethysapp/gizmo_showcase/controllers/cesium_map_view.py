from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import CesiumMapView, MVLayer
from .common import docs_endpoint
from ..app import GizmoShowcase as app

map_height = '600px'


@controller(
    url='gizmo-showcase/cesium-map-view'
)
def cesium_map_view_basic(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 'This example shows a basic Cesium globe.'
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_layers(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    # Pythonized version of the CesiumJS API
    borehole_layer = {'Bore Holes': {
        'imageryProvider': {
            'Cesium.WebMapServiceImageryProvider': {
                'url': 'https://nationalmap.gov.au/proxy/http://geoserver.nationalmap.nicta.com.au/geotopo_250k/ows',
                'layers': 'Hydrography:bores',
                'parameters': {
                    'transparent': True,
                    'format': 'image/png'
                }
            }
        }
    }}
    
    # MVLayer objects (from Map View gizmo) can be used with cesium map views
    us_states_layer = MVLayer(
        source='ImageWMS',
        legend_title='US States',
        options={
            'url': 'https://demo.geo-solutions.it/geoserver/wms',
            'params': {'LAYERS': 'topp:states'},
            'serverType': 'geoserver'
        },
    )
    
    # Use Camera methods like setView, flyTo, lookAt, lookAtTransform, 
    # or viewBoundingSphere, to set the view
    view = {
        'setView': {
            'destination': {
                'Cesium.Rectangle.fromDegrees': [114.591, -45.837, 148.97, -5.73]
            },
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={'shouldAnimate': False, 'timeline': False, 'homeButton': False},
        layers=[borehole_layer, us_states_layer],
        view=view
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 
            'This example displays an Esri basemap service and a WMS service on a Cesium globe. Compare with the ' \
            '<a href="https://sandcastle.cesium.com/?src=Web%20Map%20Service%20(WMS).html" target="_blank">' \
            'Web Map Service (WMS) example on Sandcastle</a>.',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_terrain(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    # Define a terrain provider using the Python equivalent of the CesiumJS API
    terrain_provider = {
        'Cesium.createWorldTerrain': {
            'requestVertexNormals': True,
            'requestWaterMask': True
        }
    }

    # Use Camera methods like setView, flyTo, lookAt, lookAtTransform, 
    # or viewBoundingSphere, to set the view
    view = {
        'flyTo': {
            'destination': {
                'Cesium.Cartesian3.fromDegrees': [-122.19, 46.25, 5000.0]
            },
            'orientation': {
                'direction': {
                    'Cesium.Cartesian3': [-0.04231243104240401, -0.20123236049443421, -0.97862924300734]
                },
                'up': {
                    'Cesium.Cartesian3': [-0.47934589305293746, -0.8553216253114552, 0.1966022179118339]
                }
            }
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={'shouldAnimate': False, 'timeline': False, 'homeButton': False},
        terrain={'terrainProvider': terrain_provider},
        view=view
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 'This example demonstrates the 3D-tiled terrain feature of Cesium globe.',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_czml(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    czml_doc = [
        {
            "id": "document",
            "name": "CZML Geometries: Polygon",
            "version": "1.0"
        },
        {
            "id": "redPolygon",
            "name": "Red polygon on surface",
            "polygon": {
                "positions": {
                    "cartographicDegrees": [
                        -115.0, 37.0, 0,
                        -115.0, 32.0, 0,
                        -107.0, 33.0, 0,
                        -102.0, 31.0, 0,
                        -102.0, 35.0, 0
                    ]
                },
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": [255, 0, 0, 255]
                        }
                    }
                }
            }
        },
        {
            "id": "greenPolygon",
            "name": "Green extruded polygon",
            "polygon": {
                "positions": {
                    "cartographicDegrees": [
                        -108.0, 42.0, 0,
                        -100.0, 42.0, 0,
                        -104.0, 40.0, 0
                    ]
                },
                "material":
                    {
                        "solidColor":
                            {
                                "color": {
                                    "rgba": [0, 255, 0, 255]
                                }
                            }
                    },
                "extrudedHeight": 500000.0,
                "closeTop": False,
                "closeBottom": False
            }
        },
        {
            "id": "orangePolygon",
            "name": "Orange polygon with per-position heights and outline",
            "polygon": {
                "positions": {
                    "cartographicDegrees": [
                        -108.0, 25.0, 100000,
                        -100.0, 25.0, 100000,
                        -100.0, 30.0, 100000,
                        -108.0, 30.0, 300000
                    ]
                },
                "material": {
                    "solidColor": {
                        "color": {
                            "rgba": [255, 100, 0, 100]
                        }
                    }
                },
                "extrudedHeight": 0,
                "perPositionHeight": True,
                "outline": True,
                "outlineColor": {
                    "rgba": [0, 0, 0, 255]
                }
            }
        }
    ]

    czml_layer = {
        'source': 'czml',
        'options': czml_doc
    }
    
    # Use Camera methods like setView, flyTo, lookAt, lookAtTransform, 
    # or viewBoundingSphere, to set the view
    view = {
        'lookAt': {
            'center': {'Cesium.Cartesian3.fromDegrees': [-98.0, 40.0]},
            'offset': {'Cesium.Cartesian3': [0.0, -4790000.0, 3930000.0]},
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={
            'shouldAnimate': True,
            'timeline': False,
            'homeButton': False,
            'shadows': True,
        },
        view=view,
        entities=[czml_layer],
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 
            'This example displays multiple ' \
            '<a href="https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/CZML-Guide" target="_blank">' \
            'CZML documents</a> on a Cesium globe. Compare with the ' \
            '<a href="https://sandcastle.cesium.com/?src=CZML%20Polygon.html" target="_blank">' \
            'CZML Polygon example on Sandcastle</a>.'
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_geojson(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    geojson_object = {
        'type': 'FeatureCollection',
        'crs': {
            'type': 'name',
            'properties': {
                'name': 'EPSG:4326'
            }
        },
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [0, 0]
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [[35.9326113, -17.6789142], [71.8652227, 17.6789142]]
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                        [[-44.9157642, -8.9465739], [-35.9326114, 8.9465739], [-26.9494585, -8.9465739]]
                    ]
                }
            }
        ]
    }

    geojson_layer = {
        'source': 'geojson',
        'options': geojson_object
    }
    
    # Use Camera methods like setView, flyTo, lookAt, lookAtTransform, 
    # or viewBoundingSphere, to set the view
    view = {
        'flyTo': {
            'destination': {
                'Cesium.Cartesian3.fromDegrees': [0, 0, 20000000.0]
            },
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={'shouldAnimate': True,
                    'timeline': False,
                    'homeButton': False,
                    'shadows': True,
                    },
        view=view,
        entities=[
            geojson_layer
        ],
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 'This example shows GeoJSON data being rendered on a Cesium globe.',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_model(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')
    
    # Pythonized version of the CesiumJS API
    aircraft_model = {
        'Cesium_Airplane': {
            'model': {
                'uri': '/static/gizmo_showcase/data/cesium_models/CesiumAir/Cesium_Air.glb',
                'show': True,
                'minimumPixelSize': 128,
                'maximumScale': 20000,
                'shadows': 'enabled',
            },
            'name': 'Cesium Airplane',
            'orientation': {
                'Cesium.Transforms.headingPitchRollQuaternion': [
                    {'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]},
                    {'Cesium.HeadingPitchRoll': [{'Cesium.Math.toRadians': 135}, 0, 0]}]},
            'position': {'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]},
            'tracked': True,  # Force camera to track this model object (only one object can be tracked at a time)
        }
    }
    
    # Alternative method using MVLayer
    balloon_model = MVLayer(
        source='CesiumModel',
        legend_title='Cesium Ballon',
        options={
            'name': 'Cesium_Ballon',
            'model': {
                'uri': '/static/gizmo_showcase/data/cesium_models/CesiumBalloon/CesiumBalloon.glb',
                'show': True,
                'minimumPixelSize': 128,
                'maximumScale': 20000,
                'shadows': 'enabled'
            },
            'orientation': {
                'Cesium.Transforms.headingPitchRollQuaternion':[
                    {'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]},
                    {'Cesium.HeadingPitchRoll': [{'Cesium.Math.toRadians': 135}, 0, 0]}
                ]
            },
            'position': {'Cesium.Cartesian3.fromDegrees': [-123.0748, 44.0507, 4950]}
        },
    )
    
    # Use the clock argument to define starting time, time step, stop time, etc.
    clock = {
        'Cesium.Clock': {
            'startTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T00:00:00Z']},
            'stopTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T24:00:00Z']},
            'currentTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T10:00:00Z']},
            'clockRange': 'Cesium.ClockRange.LOOP_STOP',
            'clockStep': 'Cesium.ClockStep.SYSTEM_CLOCK_MULTIPLIER',
            'multiplier': 1000,
            'shouldAnimate': True
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={
            'shouldAnimate': True,
            'timeline': True,
            'homeButton': True,
            'shadows': True,
        },
        models=[aircraft_model, balloon_model],
        clock={'clock': clock}
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 
            'This example loads 3D models on a Cesium globe from a GLB file. ' \
            'Compare with the <a href="https://sandcastle.cesium.com/?src=3D%20Models.html" target="_blank">' \
            '3D Models example on Sandcastle</a>.',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_ion(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')
    
    # Use Camera methods like setView, flyTo, lookAt, lookAtTransform, 
    # or viewBoundingSphere, to set the view
    view = {
        'setView': {
            'destination': {
                'Cesium.Cartesian3.fromDegrees': [
                    -74.01881302800248, 40.69114333714821, 600
                ]
            },
            'orientation': {
                'Cesium.HeadingPitchRoll.fromDegrees': [
                    21.27879878293835, -12.34390550872461, 0.0716951918898415
                ]
            },
            'endTransform': 'Cesium.Matrix4.IDENTITY'
        }
    }

    # Use the CesiumIon resource to load the Cesium OSM Buildings 
    osm_buildings = {
        'Cesium_OSM_Buildings': {
            'Cesium.Cesium3DTileset': {
                'url': {'Cesium.IonResource.fromAssetId': 96188},
            }
        }
    }

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        options={
            'shouldAnimate': True,
            'timeline': False,
            'homeButton': True,
            'shadows': True,
        },
        primitives=[osm_buildings],
        view=view
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 
            'This example illustrates how to load CesiumIon resources such as the ' \
            'Open Street Map 3D buildings layer displayed below. ',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)


@controller
def cesium_map_view_draw(request):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = app.get_custom_setting('cesium_ion_token')

    cesium_map_view = CesiumMapView(
        cesium_ion_token=cesium_ion_token,
        height=map_height,
        draw=True,  # Turn on drawing tools
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'description': 'This example demonstrates the drawing tools capability of Cesium globe.',
    }
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)
