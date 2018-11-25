<template>
  <div id="app">
    <Header />
    <router-view></router-view>
    <Drawer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Drawer from './components/Drawer.vue'

export default {
  name: 'app',
  components: {
    Header,
    Drawer
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
