import json
from django.shortcuts import render
from django.contrib import messages
import geojson
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import MapView, MVView, MVDraw, MVLayer, MVLegendClass
from .common import docs_endpoint


def get_geoserver_wms():
    """
    Try to get the built in geoserver wms for this installation if possible.
    Otherwise point at the chpc geoserver.
    """
    return 'https://tethys2.byu.edu/geoserver/wms'


@controller
def map_view(request):
    """
    Controller for the Map View page.
    """
    # Define view options
    view_options = MVView(
        projection='EPSG:4326',
        center=[-100, 40],
        zoom=3.5,
        maxZoom=18,
        minZoom=2
    )

    # Define drawing options
    drawing_options = MVDraw()

    # Define GeoJSON layer
    geojson_object = {
        'type': 'FeatureCollection',
        'crs': {
            'type': 'name',
            'properties': {
                'name': 'EPSG:3857'
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
                    'coordinates': [[4e6, -2e6], [8e6, 2e6]]
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[[-5e6, -1e6], [-4e6, 1e6], [-3e6, -1e6]]]
                }
            }
        ]
    }

    # Define layers
    map_layers = []

    style_map = {
        'Point': {'ol.style.Style': {
            'image': {'ol.style.Circle': {
                'radius': 5,
                'fill': {'ol.style.Fill': {
                    'color': 'red',
                }},
                'stroke': {'ol.style.Stroke': {
                    'color': 'red',
                    'width': 2
                }}
            }}
        }},
        'LineString': {'ol.style.Style': {
            'stroke': {'ol.style.Stroke': {
                'color': 'green',
                'width': 3
            }}
        }},
        'Polygon': {'ol.style.Style': {
            'stroke': {'ol.style.Stroke': {
                'color': 'blue',
                'width': 1
            }},
            'fill': {'ol.style.Fill': {
                'color': 'rgba(0, 0, 255, 0.1)'
            }}
        }},
    }

    geojson_layer = MVLayer(
        source='GeoJSON',
        options=geojson_object,
        layer_options={'style_map': style_map},
        legend_title='Test GeoJSON',
        legend_extent=[-46.7, -48.5, 74, 59],
        legend_classes=[
            MVLegendClass('polygon', 'Polygons', fill='rgba(0, 0, 255, 0.1)', stroke='blue'),
            MVLegendClass('line', 'Lines', stroke='green'),
            MVLegendClass('point', 'Points', fill='red')
        ]
    )

    map_layers.append(geojson_layer)

    if get_geoserver_wms():
        # Define GeoServer Layer
        geoserver_layer = MVLayer(
            source='ImageWMS',
            options={'url': get_geoserver_wms(),
                    'params': {'LAYERS': 'topp:states'},
                    'serverType': 'geoserver'},
            legend_title='USA Population',
            legend_extent=[-126, 24.5, -66.2, 49],
            legend_classes=[
                MVLegendClass('polygon', 'Low Density', fill='#00ff00', stroke='#000000'),
                MVLegendClass('polygon', 'Medium Density', fill='#ff0000', stroke='#000000'),
                MVLegendClass('polygon', 'High Density', fill='#0000ff', stroke='#000000')
            ]
        )

        map_layers.append(geoserver_layer)

    # Define KML Layer
    kml_layer = MVLayer(
        source='KML',
        options={'url': '/static/gizmo_showcase/data/model.kml'},
        legend_title='Park City Watershed',
        legend_extent=[-111.60, 40.57, -111.43, 40.70],
        legend_classes=[
            MVLegendClass('polygon', 'Watershed Boundary', fill='#ff8000'),
            MVLegendClass('line', 'Stream Network', stroke='#0000ff'),
        ]
    )

    map_layers.append(kml_layer)

    # Tiled ArcGIS REST Layer
    arc_gis_layer = MVLayer(
        source='TileArcGISRest',
        options={'url': 'http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/' +
                        'Specialty/ESRI_StateCityHighway_USA/MapServer'},
        legend_title='ESRI USA Highway',
        legend_extent=[-173, 17, -65, 72]
    )

    map_layers.append(arc_gis_layer)

    # Define map view options
    map_view_options = MapView(
        height='600px',
        width='100%',
        controls=['ZoomSlider', 'Rotate', 'FullScreen',
                  {'MousePosition': {'projection': 'EPSG:4326'}},
                  {'ZoomToExtent': {'projection': 'EPSG:4326', 'extent': [-130, 22, -65, 54]}}],
        layers=map_layers,
        view=view_options,
        basemap=['OpenStreetMap'],
        draw=drawing_options,
        legend=True
    )

    # Get the geometry drawn by the user
    submitted_geometry = request.POST.get('geometry', None)
    
    # Convert GeometryCollection into a FeatureCollection if given
    if submitted_geometry:
        geojson_objs = geojson.loads(submitted_geometry)
        
        # Create a Feature for each geometry
        features = []
        for geometry in geojson_objs.geometries:
            properties = geometry.pop('properties', [])
            features.append({
                'type': 'Feature',
                'geometry': geometry,
                'properties': properties
            })

        # Create FeatureCollection wrapper with list of features
        feature_collection = {
            'type': 'FeatureCollection',
            'features': features
        }
        
        # Set initial features on drawing layer (as geojson string)
        drawing_options.initial_features = json.dumps(feature_collection)
        
        # Log in alert message
        messages.success(request, "Geometry added to the map successfully.")

    context = {
        'docs_endpoint': docs_endpoint,
        'map_view': map_view_options
    }
    return render(request, 'gizmo_showcase/map_view.html', context)
