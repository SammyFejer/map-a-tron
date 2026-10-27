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
import { fromUrl } from 'geotiff';



 async function getTiff() {

    const tiff = await fromUrl('https://storage.googleapis.com/hugemunous_file/Corang_COG.tif');

    const image = await tiff.getImage();

    const width = image.getWidth();
    const hight = image.getHeight();
     


    const bbox = image.getBoundingBox();

    var resX = ((bbox[2] - bbox[0]) / width);
    var resY = ((bbox[3] - bbox[1]) / hight);


    return { resX, resY, bbox };
;   
   


}


async function getData(loglatcoords) {

    const url = new URL('https://portal.opentopography.org/API/v1/elevation');

    const params = new URLSearchParams();
    url.searchParams.append('longitude', loglatcoords[0]);
    url.searchParams.append('latitude', loglatcoords[1]);
    url.searchParams.append("API_Key", '0c79ed189e921db0403e68b6114127e9');
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
}



//function coordtopix(coord) {

//    const { resX, resY, bbox } = await getTiff();
    
//    var bboxcoordmin = toLonLat([bbox[0], bbox[1]]);
//    var bboxcoordmax = toLonLat([bbox[2], bbox[3]]);
    

//    var X = Math.floor((bbox[0] - coord[0]) / resX);
//    var Y = Math.floor((coord[1] - bbox[3]) / resY);


//}

const vectorSource = new VectorSource({
    
});
const markerVectorLayer = new VectorLayer({
    source: vectorSource,
});


const source1 = new GeoTIFF({
    sources: [{ url: 'https://storage.googleapis.com/hugemunous_file/Corang_COG.tif' },
        
    ],
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

const view = new View({ center: [16706278.65556357, -4205421.554828521], zoom: 13, });



var map = new Map({
    target: 'map',
    layers: [layer1, layer2, markerVectorLayer],
    view: view,
    // 16703375.910809841, -4207349.395254885
});


//const marker = new Feature({
//    geometry: new Point(
//        [16703375.910809841, -4207349.395254885],
//    ),
//});
//const vectorSource = new VectorSource({
//    features: [marker]
//});
//const markerVectorLayer = new VectorLayer({
//    source: vectorSource,
//});
//map.addLayer(markerVectorLayer);

map.on('click', async function (event) {
    var coord = (event.coordinate);
    
    console.log('Clicked coordinates:', coord);
    const {resX, resY, bbox} = await getTiff();
    
    
    var X = Math.floor((bbox[0] - coord[0]) / resX);
    var Y = Math.floor((coord[1] - bbox[3]) / resY);
    var Xco = -((-2045 * resX) - bbox[0]);
    var Yco = ((-3190 * resY) + bbox[3]);
    console.log('coord from pix:', Xco, Yco);
    const loglatcoords = toLonLat(coord);
    await getData(loglatcoords);

    console.log('pixel:', X, Y);
    var marker = new Feature({
      geometry: new Point(
          (coord)
      ),  
    });
    vectorSource.addFeature(marker);
    
   

    
    const vectorSources = markerVectorLayer.getSource();

    const allFeatures = vectorSources.getFeatures();

    var start = allFeatures[0];

    var geometry = allFeatures[0].getGeometry();

    //if (geometry && geometry.getType() === 'Point') {
    //    var coordinates = geometry.getCoordinates(); 
    //    var startpix = coordtopix(coordinates);
    //} 

    var finish = allFeatures.at[-1];

    

    
   
});


