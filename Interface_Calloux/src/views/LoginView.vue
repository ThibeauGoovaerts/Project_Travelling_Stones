<template>
  <v-app id="app">
    <v-main>
        <v-card class="mx-auto my-lg-10 px-6 py-8" max-width="344">
          <v-form>
            <v-text-field
                :counter=50
                label="Nom d'utilisateur"
                prepend-icon="mdi-head"
                v-model="username"
            ></v-text-field>

            <v-text-field
                type="password"
                label="Mot de passe"
                v-model="password"
                prepend-icon="mdi-lock"
            ></v-text-field>
            <p
                style="color: red;"
            >{{errorCode}}</p>
            <br>

            <v-btn
                color="success"
                class="mr-4"
                @click="postData"
            >
              Se connecter
            </v-btn>
          </v-form>
        </v-card>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script setup>
import {defineComponent} from "vue";
import http from "@/http-login.ts";
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();
import { ref } from "vue";
import { useRouter } from 'vue-router'

const username = ref("");
const password = ref("");
const errorCode = ref("");
const router = useRouter();

const postData = async () => {
  try{
    if (!username.value){
      errorCode.value = "Le nom d'utilisateur est un champs obligatoire!";
      return;
    }
    if (!password.value){
      errorCode.value = "Le mot de passe est un champs obligatoire!";
      return;
    }
    const response = await http.post("token",
        {
          "username": username.value,
          "password": password.value
        }
    )
    cookies.remove('access')
    cookies.remove('refresh')
    cookies.remove('username')
    cookies.set('access', response.data.access)
    cookies.set('refresh', response.data.refresh)
    cookies.set('username', username.value)

    await router.push({name: 'Calloux'})
  }catch(error) {
    let errorMessage;
    try{
      if (error.response.status === 401){
        errorMessage = "Ce utilisateur ou ce mot de passe n'existe pas.";
      }
    }catch(secondError){
      errorMessage = "Erreur de connextion au serveur.";
      console.log(error)
    }finally {
      errorCode.value = errorMessage;
      password.value = "";
    }
  }
}
</script>

<script type="ts">
  import {defineComponent} from "vue";
  import Footer from "@/components/Footer.vue";

  export default defineComponent({
    name: "Personnes.vue",
    components: {
      Footer,
    }
  });
</script>

<style scoped>
  @import "../assets/main.css";
</style>
