<template>
  <header class="header layer">
    <router-link :to="{
      path: hasBack
    }">
      <span title="Back" class="back-btn" v-if="hasBack">
         <Chevron class="rotate"/>
      </span>
    </router-link>
    <h1 v-if="title">{{ title }}</h1>
  </header>
</template>

<script>
import Chevron from "./Chevron.vue";

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
  },
  components: {
    Chevron
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.header {
  background: rgb(27, 201, 152);
  color: white;
  font-size: 0.6em;
  height: 3rem;
  left: 0;
  position: fixed;
  text-align: center;
  top: 0;
  width: 100%;
  z-index: 99;

  > h1 {
    color: white;
  }
}

.back-btn {
  width: 32px;
  height: 32px;
  position: absolute;
  top: 10%;
  left: 1%;
  font-size: 3em;
  color: white;

  svg {
    transform: rotate(180deg);
    width: auto;
    height: 18px;

    // Specific selection to target SVG element
    #Park-view-with-info {
      fill: white !important;
    }
  }
}
</style>
