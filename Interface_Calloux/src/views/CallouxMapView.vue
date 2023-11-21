<template>
  <v-app>
    <Header/>
    <v-main>
      <v-container style="width: 100%; height: 100%; margin: auto;">
        <v-lazy style="width: 100%; height: 100%">
          <v-img style="width: 100%; height: 100%" id="map">
          </v-img>
        </v-lazy>
      </v-container>
    </v-main>
    <Footer />
  </v-app>
</template>

<script setup>
import Map from "ol/Map";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import View from "ol/View";
import {fromLonLat} from "ol/proj";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import Feature from "ol/Feature";
import Style from "ol/style/Style";
import Icon from "ol/style/Icon";
import Text from 'ol/style/Text';
import {boundingExtent} from "ol/extent";
import { useRoute } from 'vue-router'
import {refresh} from "@/http-common";
import { useCookies } from "vue3-cookies";
import { Point } from 'ol/geom';
const { cookies } = useCookies();
import URL from "@/ApiAxios";

const route = useRoute()
const http = refresh(cookies.get("access"));
const coord = [];
let items = [];
let midlle = fromLonLat([0, 0]);
const props = defineProps(['caillouNb'])
const caillouNb = props.caillouNb


const getMiddleCoordinate = () => {
  let x=0,y=0,z=0
  for(let i=0;i<items.length;i++){
    let lat = items[i]["x_coord"] * (Math.PI/180)
    let lon = items[i]["y_coord"] * (Math.PI/180)
    x += Math.cos(lat) * Math.cos(lon)
    y += Math.cos(lat) * Math.sin(lon)
    z += Math.sin(lat)
  }
  x = x / items.length;
  y = y / items.length;
  z = z / items.length;
  const lat = Math.atan2(z, Math.sqrt(x*x+y*y))
  const long = Math.atan2(y, x)
  midlle = [lat * (180/Math.PI), long * (180/Math.PI)]
}

const showMap = () => {
  let map = new Map({
    layers: [
      new TileLayer({
        source: new OSM()
      }),
    ],
    view: new View({
      zoom: 10,
      center: fromLonLat(midlle),
      constrainResolution: true
    }),
    target: document.getElementById("map"),
  })
  for(let i=0;i<coord.length; i++){
    let layer = new VectorLayer({
      source: new VectorSource({
        features: [
          new Feature({
            geometry: new Point(
                coord[i]
            ),
          })
        ],
      }),
      style: new Style({
        image: new Icon({
          anchor: [0.5, 1],
          scale: [0.5, 0.5],
          src: URL + ':8888/media/location.png'
        }),
        text: new Text({
          text: String(i+1),
          font: "20px sans-serif",
          offsetY: 10,
        }),
      })
    });
    map.addLayer(layer);
  }
  map.getView().fit(boundingExtent(coord))
}

const getData = async () => {
  try{
    //fetch personnes
    const response = await http.get("decouverte/calloux/" + cookies.get('username') + "/" + route.params.nb);
    let sumLong=0, sumLat=0
    for(let obj of response.data){
      let d = new Date(obj.datetime)
      obj.datetime = d.getDate() + "/" + (d.getMonth()+1) + "/" + d.getFullYear() + " " + d.getHours() + ":" + d.getMinutes();
      let secondResponse = await http.get("adresse/" + obj.adresse +"/");
      obj.adresse = secondResponse.data.ville
      if(secondResponse.data.lieu_dit !== "")
        obj.adresse += " - " + secondResponse.data.lieu_dit
      let thirdResponse = await http.get("decouverte/photo/" + obj.id);
      if (thirdResponse.data[0] !== undefined)
        obj.photo = thirdResponse.data[0].path;
      coord.push(fromLonLat([Number(secondResponse.data.coord_gps_lat), Number(secondResponse.data.coord_gps_long)]))
      obj["x_coord"] = Number(secondResponse.data.coord_gps_lat)
      obj["y_coord"] = Number(secondResponse.data.coord_gps_long)
      sumLong += Number(secondResponse.data.coord_gps_lat)
      sumLat += Number(secondResponse.data.coord_gps_long)
    }
    items = response.data;
    getMiddleCoordinate()
  }catch(error) {
    console.log(error);
  }
}

getData().then(() => {
  if(coord.length > 0)
    showMap();
});
</script>

<script type="ts">
import {defineComponent} from "vue";
import Header from '@/components/Header.vue'
import Footer from "@/components/Footer.vue";

export default defineComponent({
  name: "DecouverteVue",
  components: {
    Header,
    Footer,
  }
});
</script>

<style scoped>
  @import "../assets/main.css";
</style>
