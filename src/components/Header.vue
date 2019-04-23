<template>
  <header v-if="show" class="header layer">
    <router-link :to="{
      path: hasBack
    }">
      <span title="Back" class="back-btn" v-if="hasBack">
         <Chevron class="rotate"/>
      </span>
    </router-link>
    <h1 v-if="title">{{ title }}</h1>
  </header>
  <header v-else-if="!show" class="header header--hidden">
    <router-link :to="{
        path: hasBack
      }">
      <span title="Back" class="back-btn" v-if="hasBack">
        <Chevron class="rotate"/>
      </span>
    </router-link>
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
    show: {
      type: Boolean,
      default: true
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
  transition: background .2s ease;

  &--hidden {
    background: transparent;
    .back-btn {
      background: white;
      box-shadow: 0px 2px 5px 0px rgba(0,0,0,.25);
      svg #Park-view-with-info {
        fill: rgb(27, 201, 152) !important;
      }
    }
  }

  > h1 {
    color: white;
  }
}

.back-btn {
  position: absolute;
  font-size: 3em;
  color: white;
  top: 0;
  line-height: 1.5em;
  height: 2.5rem;
  width: 2.5rem;
  left: .25rem;
  top: .25rem;
  background: transparent;
  border-radius: 100%;
  box-shadow: 0px 2px 5px 0px rgba(0,0,0,0);
  transition: all .2s ease;
  svg {
    transform: rotate(180deg);
    width: auto;
    height: 18px;
    position: relative;
    left: -2px;
    top: -2px;

    // Specific selection to target SVG element
    #Park-view-with-info {
      fill: white !important;
      transition: fill .2s ease;
    }
  }
}
</style>
