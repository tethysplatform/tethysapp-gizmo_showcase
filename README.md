# tethysapp-gizmo_showcase
An app with explanations and demonstrations of each of the Tethys Gizmos.

1. Install

```
tethys install
```

2. Download Sample Data

```
python
>>> import bokeh
>>> bokeh.sampledata.download()
```

3. Set up Cesium Ion Token (Optional)

  To view the Cesium Map View demos, you will need to obtain a Cesium Ion Token See [Cesium ion Access Tokens tutorial](https://cesium.com/learn/ion/cesium-ion-access-tokens/) for instructions on obtaining a token. After obtaining a token, navigate to the settings for the Gizmo Showcase, locate the `cesium_ion_token` setting under Custom Settings section, enter the token, and save.

4. GeoServer (Optional)

  The Gizmo Showcase has a Spatial Dataset Service Setting that can be used to link a GeoServer service into the app. When included, the Map View Gizmo and the WMS Cesium demo will display the US States layer. Any GeoServer can be used, so long as it contains the demo layers. See [Assign Spatial Dataset Services](http://docs.tethysplatform.org/en/stable/tethys_sdk/tethys_services/spatial_dataset_services.html#assign-spatial-dataset-service) for how to add a GeoServer as a Spatial Dataset Service and link it to an app.
