from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import CesiumMapView, MVLayer
from .common import docs_endpoint


@login_required()
def cesium_map_view(request, type='home'):
    """
    Controller for the Cesium Map View page.
    """
    # Get the access token
    cesium_ion_token = request.GET.get('cesium-ion-token', '')

    # Define nav link
    home_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'home'})
    map_layers_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'map_layers'})
    terrain_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'terrain'})
    czml_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'czml'})
    geojson_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'geojson'})
    model_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'model'})
    model2_link = reverse('gizmos:cesium_map_view', kwargs={'type': 'model2'})

    # Add cesium ion token GET parameters of all header links if provided
    if cesium_ion_token:
        home_link += f'?cesium-ion-token={cesium_ion_token}'
        map_layers_link += f'?cesium-ion-token={cesium_ion_token}'
        terrain_link += f'?cesium-ion-token={cesium_ion_token}'
        czml_link += f'?cesium-ion-token={cesium_ion_token}'
        geojson_link += f'?cesium-ion-token={cesium_ion_token}'
        model_link += f'?cesium-ion-token={cesium_ion_token}'
        model2_link += f'?cesium-ion-token={cesium_ion_token}'

    header_link = {"home_link": home_link, "map_layers_link": map_layers_link, "terrain_link": terrain_link,
                   "czml_link": czml_link, "geojson_link": geojson_link, "model_link": model_link,
                   "model2_link": model2_link, "page_type": type}

    # 1. Basic Map
    height = '600px'

    if type == 'home':
        cesium_map_view = CesiumMapView(cesium_ion_token=cesium_ion_token, height=height)

    # 2. Map Layers
    if type == 'map_layers':
        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height=height,
            draw=True,
            options={'shouldAnimate': False, 'timeline': False, 'homeButton': False},
            layers=[
                {'Open Street Map': {
                    'imageryProvider': {'Cesium.OpenStreetMapImageryProvider': {
                        'url': 'https://a.tile.openstreetmap.org/'
                    }}
                }},
                MVLayer(
                    source='ImageWMS',
                    legend_title='US States',
                    options={
                        'url': 'https://demo.geo-solutions.it/geoserver/wms',
                        'params': {'LAYERS': 'topp:states'},
                        'serverType': 'geoserver'
                    },
                )
            ]
        )

    # 3. Terrain
    if type == 'terrain':
        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height=height,
            draw=True,
            options={'shouldAnimate': False, 'timeline': False, 'homeButton': False},
            terrain={'terrainProvider': {'Cesium.createWorldTerrain': {'requestVertexNormals': True,
                                                                       'requestWaterMask': True}}},
            view={'flyTo': {
                'destination': {'Cesium.Cartesian3.fromDegrees': [-122.19, 46.25, 5000.0]},
                'orientation': {
                    'direction': {
                        'Cesium.Cartesian3': [-0.04231243104240401, -0.20123236049443421, -0.97862924300734]
                    },
                    'up': {
                        'Cesium.Cartesian3': [-0.47934589305293746, -0.8553216253114552, 0.1966022179118339]
                    }
                }
            }}
        )

    # 4. CZML Object
    if type == 'czml':
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

        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height=height,
            options={'shouldAnimate': True,
                     'timeline': False,
                     'homeButton': False,
                     'shadows': True,
                     },
            view={'lookAt': {
                'center': {'Cesium.Cartesian3.fromDegrees': [-98.0, 40.0]},
                'offset': {'Cesium.Cartesian3': [0.0, -4790000.0, 3930000.0]},
            }},
            layers={'BingMap': {
                'imageryProvider': {
                    'Cesium.BingMapsImageryProvider': {
                        'url': 'https://dev.virtualearth.net',
                        'key': 'AnYTMwSuR3-CBMzhN0yAYrtl-28rEFe7Kxfg2IWC9csUBCn0nYDFXW1ioNakjX3W',
                        'mapStyle': 'Cesium.BingMapsStyle.AERIAL',
                    },
                }
            }},
            entities=[
                {
                    'source': 'czml',
                    'options': czml_doc
                }
            ],
        )

    # 5. GeoJSON Object
    if type == 'geojson':
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

        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height=height,
            options={'shouldAnimate': True,
                     'timeline': False,
                     'homeButton': False,
                     'shadows': True,
                     },
            view={'flyTo': {
                'destination': {'Cesium.Cartesian3.fromDegrees': [0, 0, 20000000.0]},
            }},
            layers={'BingMap': {
                'imageryProvider': {
                    'Cesium.BingMapsImageryProvider': {
                        'url': 'https://dev.virtualearth.net',
                        'key': 'AnYTMwSuR3-CBMzhN0yAYrtl-28rEFe7Kxfg2IWC9csUBCn0nYDFXW1ioNakjX3W',
                        'mapStyle': 'Cesium.BingMapsStyle.AERIAL',
                    },
                }
            }},
            entities=[
                {
                    'source': 'geojson',
                    'options': geojson_object
                }
            ],
        )

    # 6. Model
    if type == 'model':
        object1 = '/static/tethys_gizmos/cesium_models/CesiumAir/Cesium_Air.glb'
        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height=height,
            options={
                'shouldAnimate': True,
                'timeline': True,
                'homeButton': True,
                'shadows': True,
            },
            primitives=[
                MVLayer(
                    source='CesiumPrimitive',
                    legend_title='Cesium 3D Buildings',
                    options={'Cesium.Cesium3DTileset': {'url': {'Cesium.IonResource.fromAssetId': 96188}}},
                    data={'layer_name': 'Cesium_Buildings', 'layer_variable': 'variable', 'layer_id': 1}
                )
            ],
            layers={'BingMap': {'imageryProvider': {
                'Cesium.BingMapsImageryProvider': [{
                    'url': 'https://dev.virtualearth.net',
                    'key': 'AnYTMwSuR3-CBMzhN0yAYrtl-28rEFe7Kxfg2IWC9csUBCn0nYDFXW1ioNakjX3W',
                    'mapStyle': 'Aerial',
                }],
            }}},
            models=[
                MVLayer(
                    source='CesiumModel',
                    legend_title='Cesium Model',
                    options={'model': {'uri': object1,
                                       'show': True,
                                       'minimumPixelSize': 128,
                                       'maximumScale': 20000,
                                       'shadows': 'enabled'},
                             'name': 'Cesium_Airplane',
                             'orientation': {
                                 'Cesium.Transforms.headingPitchRollQuaternion':
                                     [{'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]},
                                      {'Cesium.HeadingPitchRoll': [{'Cesium.Math.toRadians': 135}, 0, 0]}]},
                             'position': {'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]}
                             },
                    data={'layer_id': "cesium_airplane_id",
                          'layer_name': "Cesium_Airplane",
                          'popup_title': "Cesium Airplane"}
                )
            ],
            clock={'clock': {'Cesium.Clock': {
                'startTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T00:00:00Z']},
                'stopTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T24:00:00Z']},
                'currentTime': {'Cesium.JulianDate.fromIso8601': ['2017-07-11T10:00:00Z']},
                'clockRange': 'Cesium.ClockRange.LOOP_STOP',
                'clockStep': 'Cesium.ClockStep.SYSTEM_CLOCK_MULTIPLIER',
                'multiplier': 1000,
                'shouldAnimate': True
            }}}
        )

    # 7. Multiple Models with data
    if type == 'model2':
        object1 = '/static/tethys_gizmos/cesium_models/CesiumAir/Cesium_Air.glb'
        object2 = '/static/tethys_gizmos/cesium_models/CesiumBalloon/CesiumBalloon.glb'
        cesium_map_view = CesiumMapView(
            cesium_ion_token=cesium_ion_token,
            height='80%',
            width='80%',
            options={'shouldAnimate': True,
                     'timeline': True,
                     'homeButton': True,
                     'shadows': True,
                     },
            layers={'BingMap': {
                'imageryProvider': {'Cesium.BingMapsImageryProvider': [{
                    'url': 'https://dev.virtualearth.net',
                    'key': 'AnYTMwSuR3-CBMzhN0yAYrtl-28rEFe7Kxfg2IWC9csUBCn0nYDFXW1ioNakjX3W',
                    'mapStyle': 'Aerial',
                }]}
            }},
            primitives=[
                {'Cesium_OSM_Buildings': {'Cesium.Cesium3DTileset': {'url': {'Cesium.IonResource.fromAssetId': 96188}}}}
            ],
            models=[
                {'Cesium_Airplane': {
                    'model': {
                        'uri': object1,
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
                }},
                MVLayer(
                    source='CesiumModel',
                    legend_title='Cesium Ballon',
                    options={'model': {
                        'uri': object2,
                        'show': True,
                        'minimumPixelSize': 128,
                        'maximumScale': 20000,
                        'shadows': 'enabled'},
                        'name': 'Cesium_Ballon',
                        'orientation': {
                            'Cesium.Transforms.headingPitchRollQuaternion':
                                [{'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]},
                                 {'Cesium.HeadingPitchRoll': [{'Cesium.Math.toRadians': 135}, 0, 0]}]},
                        'position': {'Cesium.Cartesian3.fromDegrees': [-123.0744619, 44.0503706, 5000]}
                     },
                    data={'layer_id': "cesium_ballon_id",
                          'layer_name': "Cesium_Ballon",
                          'popup_title': "Cesium Ballon"}
                ),
            ],
        )

    submitted_geometry = request.POST.get('geometry', None)

    if submitted_geometry is not None:
        messages.info(request, submitted_geometry)

    context = {
        'docs_endpoint': docs_endpoint,
        'cesium_map_view': cesium_map_view,
        'cesium_ion_token': cesium_ion_token
    }
    context.update(header_link)
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)
