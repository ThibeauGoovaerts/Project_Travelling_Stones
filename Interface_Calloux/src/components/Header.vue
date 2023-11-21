<template>
    <header>
      <v-container>
        <v-app-bar
            elevation="9"
            outlined
            elevate-on-scroll
            app
            top
            fixed
            rounded
            style="background-color: lightgrey;"
        >

          <template v-slot:prepend>
            <router-link tag="li" to="/calloux" exact class="rounded-lg"><v-btn class="rounded-lg">Cailloux</v-btn></router-link>
            <router-link tag="li" to="/decouverte" exact class="rounded-lg"><v-btn class="rounded-lg">Découvertes</v-btn></router-link>
          </template>

          <template v-slot:append>
            <h2>Bonjour {{name}}</h2>
            <router-link tag="li" to="/" exact><v-btn @click="logout">Déconnection</v-btn></router-link>
          </template>
        </v-app-bar>
      </v-container>
    </header>
</template>

<script>
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();

export default {
  name: "Header",
  data (){
    return {
      name: cookies.get("username").charAt(0).toUpperCase() + cookies.get("username").slice(1)
    }
  },
  methods: {
    logout(){
      cookies.remove('access')
      cookies.remove('refresh')
      cookies.remove('username')
    }
  },
}
</script>

<style scoped>
  router-link{
    margin: 5px;
  }

  .router-link-exact-active{
    background-color: grey;
  }

  .v-btn:hover{
    background-color: grey;
  }
  a,
  .v-btn{
    color: black;
    font-weight: bold;
    text-decoration: none;
    margin: 0.5rem;
  }
</style>
