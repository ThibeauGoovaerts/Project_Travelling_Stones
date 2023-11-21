<template>
  <v-app>
    <Header/>
    <v-main>
      <v-table>
        <template v-slot:default>
          <thead>
          <tr>
            <th class="text-left">
              Username
            </th>
            <th class="text-left">
              Password
            </th>
            <th class="text-left">
              Hashtag
            </th>
          </tr>
          </thead>
          <tbody>
          <tr
              v-for="(dessert, i) in items"
          >
            <td>{{dessert.username}}</td>
            <td>{{dessert.password}}</td>
            <td>{{dessert.hashtag}}</td>
          </tr>
          </tbody>
        </template>
      </v-table>


    </v-main>
    <Footer />
  </v-app>
</template>

<script lang="ts">
import http from "../http-common.js";
import { defineComponent } from "vue";
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

export default defineComponent({
  name: "Personnes.vue",
  data() {
    return {
      items: [],
    }
  },
  methods: {
    async postData(){
      try{
        //fetch personnes
        const response = await http.get("personne");
        this.items = response.data;
      }catch(error) {
        console.log(error);
      }
    },
    async getData(){
      try{
        //fetch personnes
        const response = await http.get("personne");
        this.items = response.data;
      }catch(error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getData();
  },
  components: {
    Header,
    Footer,
  }
});
</script>

<style>

</style>
