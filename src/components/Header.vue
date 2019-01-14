<template>
  <header class="header layer">
    <router-link :to="{
      path: '/parks'
    }">
      <span class="back-btn" v-if="hasBack"></span>
    </router-link>
    <h1>{{ message }}</h1>
  </header>
</template>

<script>
export default {
  name: "appHeader",
  props: {
    message: String,
    hasBack: Boolean
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
  position: absolute;
  top: 10%;
  left: 1%;
  font-size: 3em;
  color: white;
}
.back-btn:after {
  content: "\02c2";
}
</style>
