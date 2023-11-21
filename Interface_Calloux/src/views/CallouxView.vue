<template>
  <v-app>
    <Header/>
    <v-main>
        <v-card>
          <v-tabs
              v-model="tab"
              grow
          >
            <v-tab value="one">Ajouter Caillou</v-tab>
            <v-tab value="two">Mes Cailloux</v-tab>
          </v-tabs>

          <v-card-text>
            <v-window v-model="tab">
              <v-window-item value="one">
                <v-form ref="form">
                  <v-row>
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
                      <v-file-input v-model="photo" label="Photo" prepend-icon="mdi-camera"></v-file-input>
                    </v-col>
                  </v-row>
                  <v-row>
                    <p
                        style="color: red;"
                    >{{error}}</p>
                  </v-row>
                  <v-row>
                    <v-col
                    >
                      <v-btn
                          color="success"
                          class="mr-4"
                          @click="postData()"
                      >
                        Valider
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-form>
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
                          style="width: 45%"
                          class="text-center"
                      >
                        Numéro
                      </th>
                      <th
                          style="width: 45%"
                          class="text-center"
                      >
                        Photo
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
                        :key="photos"
                    >
                      <td class="text-center">{{item.numero}}</td>
                      <td class="text-center"><v-img
                          v-bind:src="photos[i]"
                          width="200"
                          :aspect-ratio="1"
                          class="img-circle image-not-map"
                          style="margin: 5px auto;"
                      /></td>
                      <td
                          class="text-center"
                          color="white"
                      >
                        <v-btn
                            icon
                            style="margin: 10px;"
                            size="large"
                            @click="deleteData(item.numero)"
                        >
                          <v-icon size="large">mdi-delete</v-icon>
                        </v-btn>
                        <v-btn
                            icon
                            style="margin: 10px;"
                            size="large"
                            @click="getDetails(item.numero)"
                        >
                          <v-icon size="large">mdi-magnify</v-icon>
                        </v-btn>
                      </td>
                    </tr>
                    </tbody>
                  </template>
                </v-table>
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
import { useCookies } from "vue3-cookies";
import {useRouter} from "vue-router/dist/vue-router";
import { ref } from "vue";
import URL from "@/ApiAxios";

const { cookies } = useCookies();
let items = [];
const photos = [];
const tab = ref(null);
const http = refresh(cookies.get("access"));
const callouNb = ref("");
const photo = ref(null);
const error = ref("");
const router = useRouter();

const postData = async () => {
  let data = new FormData();

  let file = photo.value[0];
  let nb = callouNb.value;

  if (!file){
    error.value = "Une photo est obligatoire pour ajouter un caillou!";
    return;
  }
  if (!nb){
    error.value = "Un numéro est obligatoire pour ajouter un caillou!";
    return;
  }

  data.append('photo', file);
  data.append('numero', nb);

  data.append('user', cookies.get('username'));

  const response = await http.post("calloux", data, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  })
  if (response.status === 201){
    await router.push({name: 'callouxRedirect'})
  }else{
    error.value = "Une erreur de connextion s'est produit!";
  }
}

const getDetails = (nb) => {
  router.push({
    name: 'mapViewCalloux',
    params: {
      nb: nb
    }
  });
}

const deleteData = async (id) => {
  if (confirm("Etes vous sur de supprimer ce caillou, ceci va également supprimer tous les découvertes de celui-ci ?")){
    const response = await http.delete("calloux/detail/" + cookies.get('username') + "/" + id)
    if(response.status === 204){
      router.push({ name: 'callouxRedirect' })
    }
  }
}

const getData = async () => {
  try{
    //fetch personnes
    const response = await http.get("calloux/user/" + cookies.get('username'));
    items = response.data;
    for (let i=0;i<items.length;i++){
      let cache = URL + ":8888/media" + response.data[i].photo;
      photos.push(cache);
    }
  }catch(error) {
    console.log(error);
  }
}

getData();

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
