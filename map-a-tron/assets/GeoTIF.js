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
import View from 'ol/View.js';
import TileLayer from 'ol/layer/WebGLTile.js';
import GeoTIFF from 'ol/source/GeoTIFF.js';

const source1 = new GeoTIFF({
    sources: [{ url: 'https://storage.googleapis.com/hugemunous_file/Corang_COG.tif' }],
});

const source2 = new GeoTIFF({
    sources: [

        
        { url: 'https://storage.googleapis.com/hugemunous_file/Endrick_COG.tif' },

    ],
});



const layer1 = new TileLayer({
    source: source1,
});

const layer2 = new TileLayer({
    source: source2,
});

const view = new View({ center: [16696162.166265408, -4196098.137680702], zoom: 13, });


const map = new Map({
    target: 'map',
    layers: [layer1, layer2],
    view: view,
   // 
});

map.on('click', function (event) {
    const coord = event.coordinate;
    console.log('Clicked coordinates:', coord);
});


