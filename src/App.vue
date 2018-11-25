<template>
  <div id="app">
    <Header />
    <router-view></router-view>
    <TreeDrawer />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import ParkDrawer from './components/ParkDrawer.vue'
import TreeDrawer from './components/TreeDrawer.vue'

export default {
  name: 'app',
  components: {
    Header,
    ParkDrawer,
    TreeDrawer
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
