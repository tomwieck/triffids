<template>
  <div class="hello">
    <Header v-bind:message="name" />
    <h1> {{ name }} </h1>
    <Tmap />
    <ParkDrawer />
  </div>
</template>

<script>
import Tmap from './Tmap.vue';

import Header from './Header.vue'
import ParkDrawer from './ParkDrawer.vue'

export default {
  name: 'ParkPage',
  props: {
    name: {
      type: String,
      default: 'none'
    }
  },
  components: {
  },
  components: {
    Tmap,
    Header,
    ParkDrawer,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
