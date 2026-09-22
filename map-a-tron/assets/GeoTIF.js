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
import VectorSource from 'ol/source/Vector';
import Feature from 'ol/Feature.js';
import Point from 'ol/geom/Point.js';
import { fromLonLat } from 'ol/proj';
import VectorLayer from 'ol/layer/Vector.js';
import { toLonLat } from 'ol/proj';

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


var map = new Map({
    target: 'map',
    layers: [layer1, layer2],
    view: view,
   // 
});

map.on('click', function (event) {
    var coord = toLonLat(event.coordinate);
    console.log('Clicked coordinates:', coord);

    var marker = new Feature({
      geometry: new Point(6
          fromLonLat(coord)
      ),  // Cordinates of New York's Town Hall
    });
    var vectorSource = new VectorSource({
      features: [marker]
    });
    var markerVectorLayer = new VectorLayer({
      source: vectorSource,
    });
    map.addLayer(markerVectorLayer);
    
});


