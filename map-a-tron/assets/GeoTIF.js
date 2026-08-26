import 'ol/ol.css'; 
import Map from 'ol/Map.js';
import TileLayer from 'ol/layer/WebGLTile.js';
import GeoTIFF from 'ol/source/GeoTIFF.js';

const source = new GeoTIFF({
    sources: [
        {
            url: 'https://openlayers.org/data/raster/no-overviews.tif',
            overviews: ['https://openlayers.org/data/raster/no-overviews.ovr.tif'],
        },
    ],
});

const map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: source,
        }),
    ],
    view: source.getView(),
});