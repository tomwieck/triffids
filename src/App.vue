<template>
  <div id="app">
    <Header />
<<<<<<< HEAD
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <hr>
    <Tmap />

=======
    <router-view></router-view>
    <Drawer />
>>>>>>> master
  </div>
</template>

<script>
import Header from './components/Header.vue'
<<<<<<< HEAD
import Tmap from './components/Tmap.vue'
=======
import Drawer from './components/Drawer.vue'
>>>>>>> master

export default {
  name: 'app',
  components: {
<<<<<<< HEAD
    HelloWorld,
    Header,
    Tmap
=======
    Header,
    Drawer
>>>>>>> master
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
