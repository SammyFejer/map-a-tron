//import 'ol/ol.css'; 
//import Map from 'ol/Map.js';
//import TileLayer from 'ol/layer/WebGLTile.js';
//import GeoTIFF from 'ol/source/GeoTIFF.js';

//const source = new GeoTIFF({
//    sources: [
//        {
//            url: 'https://sammyfejer.github.io/map-a-tron/map-a-tron/Corang_COG.tif',
            
//        },
//    ],
//});

//const map = new Map({
//    target: 'map',
//    layers: [
//        new TileLayer({
//            source: source,
//        }),
//    ],
//    view: source.getView(),
//});

import Map from 'ol/Map.js';
import { getView, withExtentCenter, withHigherResolutions } from 'ol/View.js';
import TileLayer from 'ol/layer/WebGLTile.js';
import GeoTIFF from 'ol/source/GeoTIFF.js';

const source = new GeoTIFF({
    sources: [
        {
            url: 'gs://hugemunous_file/Corang_COG.tif',
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
    /* view: getView(source, withHigherResolutions(1), withExtentCenter()),*/
   view: new Map().getView(),
});


