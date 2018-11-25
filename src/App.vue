<template>
  <div id="app">
    <router-view></router-view>
    <Drawer />
  </div>
</template>

<script>
import Drawer from './components/Drawer.vue'

export default {
  name: 'app',
  props: {
    name: String
  },
  components: {
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

body {
  margin: 0;
}

.layer {
  box-shadow: 0px 2px 5px 0px rgba(0,0,0,0.25);
}

</style>
