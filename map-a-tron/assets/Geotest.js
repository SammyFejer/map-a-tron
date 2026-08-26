import 'ol/ol.css';
import ImageLayer from 'ol/layer/Image.js';
import TileLayer from 'ol/layer/Tile.js';
import Map from 'ol/Map.js';
import OSM from 'ol/source/OSM.js';
import Static from 'ol/source/ImageStatic.js';
import View from 'ol/View.js';
import { register } from 'ol/proj/proj4.js';
import { fromArrayBuffer } from 'geotiff';
import proj4 from 'proj4.js';



proj4.defs(
  "EPSG:27700",
  "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 " +
    "+x_0=400000 +y_0=-100000 +ellps=airy " +
    "+towgs84=446.448,-125.157,542.06,0.15,0.247,0.842,-20.489 " +
    "+units=m +no_defs"
);
register(proj4);

const map = new Map({
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  target: "map",
  view: new View({ projection: "EPSG:27700" })
});

let width, height, extent;

fetch("/static/images/8927-3N_Corang_GetlostMap_V15.tif")
  .then(function (response) {
    return response.arrayBuffer();
  })
  .then(function (arrayBuffer) {
    return fromArrayBuffer(arrayBuffer);
  })
  .then(function (tiff) {
    return tiff.getImage();
  })
  .then(function (image) {
    width = image.getWidth();
    height = image.getHeight();
    extent = image.getBoundingBox();
    return image.readRGB();
  })
  .then(function (rgb) {
    const canvas = document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;
    const context = canvas.getContext("2d");
    const data = context.getImageData(0, 0, width, height);
    const rgba = data.data;
    let j = 0;
    for (let i = 0; i < rgb.length; i += 3) {
      rgba[j] = rgb[i];
      rgba[j + 1] = rgb[i + 1];
      rgba[j + 2] = rgb[i + 2];
      rgba[j + 3] = 255;
      j += 4;
    }
    context.putImageData(data, 0, 0);

    map.addLayer(
      new ImageLayer({
        source: new Static({
          url: canvas.toDataURL(),
          projection: "EPSG:27700",
          imageExtent: extent
        })
      })
    );

    map.getView().fit(extent);
  });
