<template>
  <Header />

  <Footer />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'

// Components
export default defineComponent({
  name: 'HomeView',

  components: {
    Header,
    Footer,
  },
});
</script>
