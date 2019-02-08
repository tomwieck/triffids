<template>
  <header class="header layer">
    <router-link :to="{
      path: hasBack
    }">
      <span title="Back" class="back-btn" v-if="hasBack"></span>
    </router-link>
    <h1 v-if="title">{{ title }}</h1>
  </header>
</template>

<script>
export default {
  name: "appHeader",
  props: {
    title: {
      type: String,
      default: ""
    },
    hasBack: {
      type: String,
      default: ""
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  width: 100%;
  background: rgb(27, 201, 152);
  color: white;
  left: 0;
  top: 0;
  position: fixed;
  height: 60px;
  z-index: 99;
  font-size: 0.8em;
}
.back-btn {
  background-image: url("../assets/backwoods.svg");
  width: 32px;
  height: 32px;
  position: absolute;
  bottom: 10%;
  left: 1%;
  font-size: 3em;
  color: white;
}
/* <div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> 
from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> 
is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">
CC 3.0 BY</a></div> */
</style>
