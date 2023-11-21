<template>
  <v-app>
    <Header/>
      <v-main>
        <v-card>
          <v-tabs
              v-model="tab"
              grow
          >
            <v-tab value="one">Carte de mes decouvertes</v-tab>
            <v-tab value="two">Mes decouvertes</v-tab>
            <v-tab value="three">Ajouter Decouverte</v-tab>
          </v-tabs>
          <v-card-text>
            <v-window v-model="tab">
              <v-window-item value="one" style="width: 100%; height: 70vh;">
                <v-lazy style="width: 100%; height: 100%">
                  <div style="width: 100%; height: 100%" id="map">
                    <h2 style="color: red; margin: auto;">{{errorMessage}}</h2>
                  </div>
                </v-lazy>
              </v-window-item>
              <v-window-item value="two">
                <v-table
                    fixed-header
                    height="75vh"
                    theme="dark"
                    rounded
                    class="rounded-lg"
                >
                  <template v-slot:default>
                    <thead>
                    <tr>
                      <th
                          style="width: 30%;"
                          class="text-center"
                      >
                        Date et heure
                      </th>
                      <th
                          style="width: 30%"
                          class="text-center"
                      >
                        Adresse
                      </th>
                      <th
                          style="width: 30%"
                          class="text-center"
                      >
                        Caillou
                      </th>
                      <th
                          style="width: 10%"
                          class="text-center"
                      >
                        Actions
                      </th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr
                        v-for="(item, i) in items"
                    >
                      <td class="text-center">{{item.datetime}}</td>
                      <td class="text-center">{{item.adresse}}</td>
                      <td class="text-center"><v-img
                          width="200"
                          :aspect-ratio="1"
                          class="img-circle image-not-map"
                          style="margin: 5px auto;"
                          v-if="item.photo!==undefined"
                          v-bind:src="URLStatic + ':8888/media' + item.photo"
                      />
                      </td>
                      <td
                          class="text-center"
                      >
                        <v-btn
                            icon
                            style="margin: 10px;"
                            size="large"
                            @click="deleteData(item.id)"
                        >
                          <v-icon size="large">mdi-delete</v-icon>
                        </v-btn>
                        <v-dialog
                            v-model="dialog"
                        >
                          <template v-slot:activator="{ props }">
                            <v-btn
                                icon
                                style="margin: 10px;"
                                size="large"
                                v-bind="props"
                            >
                              <v-icon size="large">mdi-magnify</v-icon>
                            </v-btn>
                          </template>

                          <v-card
                              style="background-color: #1b211b"
                          >
                            <v-card-text>

                            </v-card-text>
                            <v-card-actions>
                              <v-btn color="red" block @click="dialog = false">Fermer le pop-up</v-btn>
                            </v-card-actions>
                          </v-card>
                        </v-dialog>
                      </td>
                    </tr>
                    </tbody>
                  </template>
                </v-table>
              </v-window-item>
              <v-window-item value="three">
                <v-form ref="form">
                  <v-row
                  >
                    <v-col
                        cols="12"
                        md="4"
                    >
                      <v-text-field
                          :counter=50
                          label="Numéro du caillou"
                          v-model="callouNb"
                          type="number"
                          prepend-icon="mdi-numeric"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        md="8"
                    >
                      <v-text-field
                          :counter=50
                          label="Hashtag du caillou"
                          type="text"
                          prepend-icon="mdi-pound"
                          v-model="hashCallou"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <p
                        style="color: red;"
                    >{{errorCaillou}}</p>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-text-field
                          :counter=50
                          label="Ville"
                          v-model="ville"
                          type="text"
                          prepend-icon="mdi-map-marker"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                          :counter=50
                          label="Lieu Dit"
                          v-model="lieuDit"
                          type="text"
                          prepend-icon="mdi-church"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                        cols="12"
                        md="5"
                    >
                      <v-text-field
                          :counter=50
                          label="Latitude"
                          v-model="longitude"
                          id="longitude"
                          type="text"
                          prepend-icon="mdi-latitude"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        md="5"
                    >
                      <v-text-field
                          :counter=50
                          label="Longitude"
                          v-model="latitude"
                          type="text"
                          prepend-icon="mdi-longitude"
                          id="latitude"
                      ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        md="2"
                    >
                      <v-btn
                          elevation="1"
                          outlined
                          x-large
                          color="primary"
                          height="56px"
                          style="font-weight: bold;"
                      >
                        Position courante
                      </v-btn>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                        cols="12"
                        md="8"
                    >
                      <v-text-field
                          :counter=50
                          label="Pays"
                          v-model="pays"
                          type="text"
                          prepend-icon="mdi-flag"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <p
                        style="color: red;"
                    >{{errorPays}}</p>
                  </v-row>
                  <v-row>
                    <v-col
                        cols="12"
                        md="7"
                    >
                      <v-file-input
                          label="Photo"
                          prepend-icon="mdi-camera"
                          @change="Preview_image()"
                          v-model="photo"
                      ></v-file-input>
                    </v-col>
                    <v-col
                        cols="12"
                        md="5"
                    >
                      <v-img :src="url"
                             height="150"
                             style="margin: auto;"
                             class="image-not-map"
                      ></v-img>
                    </v-col>
                  </v-row>
                  <v-row>
                    <p
                        style="color: red;"
                    >{{errorPhoto}}</p>
                  </v-row>
                  <v-row>
                    <v-col
                    >
                      <v-btn
                          color="success"
                          class="mr-4"
                          @click="postData()"
                          style="top: -50px;"
                      >
                        Valider
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-form>
              </v-window-item>
            </v-window>
          </v-card-text>
        </v-card>
      </v-main>
    <Footer />
  </v-app>
</template>

<script setup>
import { refresh } from "@/http-common";
import View from 'ol/View'
import Map from 'ol/Map'
import TileLayer from 'ol/layer/Tile'
import OSM from 'ol/source/OSM'
import 'ol/ol.css'
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import Feature from 'ol/Feature';
import {fromLonLat} from 'ol/proj';
import Style from 'ol/style/Style';
import Icon from 'ol/style/Icon';
import { useCookies } from "vue3-cookies";
import { boundingExtent } from "ol/extent";
import {Point} from "ol/geom";
import Text from "ol/style/Text";
import { ref } from "vue";
import {useRouter} from "vue-router/dist/vue-router";
import URL from "@/ApiAxios";

const { cookies } = useCookies();
let items = [];
const tab = ref(null);
const http = refresh(cookies.get("access"));
const coord = [];
let midlle = [0,0];
const url = ref("");
const dialog = false;
let errorMessage = "";
const photo = ref(null);
const router = useRouter();
const hashCallou = ref("");
let errorCaillou = ref("");
let errorPays = ref("");
let errorPhoto = ref("");
const callouNb = ref("");
const ville = ref("");
const pays = ref("");
const longitude = ref("");
const lieuDit = ref("");
const latitude = ref("");
const URLStatic = ref(URL)

const Preview_image = () => {
  url.value = window.URL.createObjectURL(photo.value[0])
}

const gps_verify_length = (s) => {
  try{
    if(s.split(".")[1].length > 6){
      s = s.split(".")[0] + "." + s.split(".")[1].slice(0, 5);
    }
  }catch(noPoint){
  }
  return s
}

const verifyForm = () => {

  if (!hashCallou.value){
    console.log(hashCallou.value)
    errorCaillou.value = "Le caillou découvert a besoin d'un hashtag!";
    return false;
  }
  if (!callouNb.value){
    errorCaillou.value = "Le caillou découvert a besoin d'un numéro!";
    return false;
  }
  if (!ville.value){
    errorPays.value = "Le caillou découvert a besoin d'une ville de découverte!";
    return false;
  }
  if (!pays.value){
    errorPays.value = "Le caillou découvert a besoin d'un pays de découverte!";
    return false;
  }
  if (!longitude.value){
    errorPays.value = "Le caillou découvert a besoin d'une longitude!";
    return false;
  }
  if (!latitude.value){
    errorPays.value = "Le caillou découvert a besoin d'une latitude!";
    return false;
  }
  if (!photo.value[0]){
    errorPhoto.value = "Le caillou découvert a besoin d'une photo pour confirmer la découverte!";
    return false;
  }
  return true;
}

const postData = async () => {
  errorPhoto.value = "";
  errorPays.value = "";
  errorCaillou.value = "";

  if (!verifyForm()){
    return;
  }
  const responseAdresse = await http.post("adresse", {
    "ville": ville.value,
    "lieu_dit": lieuDit.value,
    "coord_gps_long": gps_verify_length(longitude.value),
    "coord_gps_lat": gps_verify_length(latitude.value),
    "pays": pays.value
  })
  if (responseAdresse.status === 201){
    const responseDecouverte = await http.post("decouverte", {
      "calloux": {
        "hashtag": hashCallou.value,
        "numero": callouNb.value
      },
      "decouvreur": cookies.get("username"),
      "adresse": responseAdresse.data.id
    })
    if (responseDecouverte.status === 201){
      let data = new FormData();
      data.append('path', photo.value[0]);
      data.append('decouverte', responseDecouverte.data.id);

      const response = await http.post("photo", data, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      if (response.status === 201){
        await router.push({ name: 'decouverteRedirect' })
      }
    }
  }
}

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
          src: URL + ":8888/media/location.png"
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

const getData = async() => {
  try{
    //fetch personnes
    const response = await http.get("decouverte/user/" + cookies.get('username'));
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
    getMiddleCoordinate();
  }catch(error) {
    console.log(error);
  }
}

const deleteData = async (id) => {
  if (confirm("Etes vous sûr de vouloir supprimer cette découverte ?")){
    const response = await http.delete("decouverte/detail/" + id)
    if(response.status === 204){
      await router.push({name: 'decouverteRedirect'})
    }
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
  .img-circle {
    border-radius: 50%;
  }
  .image-not-map:hover {
    transform: scale(2);
  }
  th, td{
    font-size: 2rem;
  }
</style>
