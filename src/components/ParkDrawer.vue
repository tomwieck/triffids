<template>
  <div id="drawer" class="drawer">
    <button class="drawer__button" @click="drawerToggle">
      <Chevron class="rotate"/>
    </button>
    <h1 class="drawer__header">{{ parkName }}</h1>
    <div class="drawer__trees">
      <div class="factbox">
        <div class="icon">
          <img alt="Vue logo" src="../assets/tree2.svg">
        </div>
        <div class="value">{{treeCount}}</div>
        <div class="label">Trees in total</div>
      </div>
      <div class="factbox">
        <div class="icon">
          <img alt="Vue logo" src="../assets/tree1.svg">
        </div>
        <div class="value">{{uniqueCount}}</div>
        <div class="label">Unique species</div>
      </div>
    </div>
    <hr>
    <div class="drawer__about">
      <h2>General info</h2>
      <div class="parkinfo" v-html="parkText"></div>
      <hr>
      <div class="drawer__report">
        <a
          target="_blank"
          href="https://www.bristol.gov.uk/museums-parks-sports-culture/report-problem-in-park"
        >Report an issue with this facility
          <Chevron/>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import Chevron from "./Chevron.vue";
import { parkService } from "../services/Park.service";

export default {
  name: "parkDrawer",
  data: () => {
    return {
      el: "#drawer",
      treeCount: 0,
      uniqueCount: 0,
      parkName: "Loading...",
      parkText: "Loading..."
    };
  },
  props: {
    park: {
      type: Object
    }
  },
  components: {
    Chevron
  },
  // mounted: async function() {
  //   this.parkText = await parkService.parkInfo(this.park.id);
  // },
  methods: {
    drawerToggle: function() {
      const drawer = document.getElementById("drawer");
      this.$emit("toggle-drawer", drawer.classList.contains("closed"));
      drawer.classList.contains("closed")
        ? drawer.classList.remove("closed")
        : drawer.classList.add("closed");
    },
    drawerClose: function() {
      const drawer = document.getElementById("drawer");
      drawer.classList.add("closed");
    },
    loadHTML: async function(parkId) {
      this.parkText = await parkService.parkInfo(parkId);
    }
  },
  watch: {
    park: function() {
      this.parkName = this.park.siteName;
      this.treeCount = this.park.total_trees;
      this.uniqueCount = this.park.unique_trees;
      this.loadHTML(this.park.id);
    }
  }
};
</script>

<!-- this is not scoped as it is applied to the pulled in HTML -->
<style lang="scss">
@import "../styles/variables.scss";
.parkinfo {
  font-family: "HankenGroteskMedium";
  font-size: 1em;
  line-height: 1.6em;
  text-align: left;
  padding: 0 22pt;
  h1 {
    /* this would duplicate the H1 above */
    display: none;
  }
  h2 {
    color: $title-green;
    font-family: "HankenGroteskBold";
    font-weight: normal;
    font-style: normal;
    font-weight: 400;
    font-size: 1.2em;
  }
  ul li {
    padding: 0 22pt;
  }
  a {
    color: $link-color;
    text-decoration: none;
  }
}
</style>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped lang='scss'>
@import "../styles/variables.scss";
.factbox {
  width: 50%;
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 3px;
  .icon {
    grid-column: 1;
    grid-row: 1 / 3;
    justify-self: start;
    align-self: center;
    img {
      height: 40px;
    }
  }
  .value {
    font-size: 1.4em;
    font-weight: bold;
    grid-column: 2;
    grid-row: 1;
    justify-self: start;
    align-self: start;
    color: $dark-primary-color;
  }
  .label {
    grid-column: 2;
    grid-row: 2;
    justify-self: start;
    align-self: start;
  }
}
.drawer {
  background: #fff;
  box-shadow: 0 2px 4px;
  left: 0;
  bottom: 0;
  position: fixed;
  transition: all 0.5s ease;
  height: 50%;
  overflow-y: scroll;
  padding: 16px;
  width: 100%;
  z-index: 100;

  &__header {
    color: $title-green;
    font-family: "HankenGroteskBold";
    font-weight: normal;
    font-style: normal;
    font-weight: 400;
    margin-top: 0;
  }

  &.closed {
    height: 1em;
    button > svg {
      transform: rotate(-90deg);
    }
  }

  &__button {
    background: white;
    padding-bottom: 1em;
    border: none;
    cursor: pointer;
    margin-bottom: 16px;
    width: 100%;

    &:focus {
      outline: none;
    }
  }

  &__about {
    text-align: center;
    h2 {
      color: $title-green;
    }
  }

  &__report {
    padding: 8px 0;
    a {
      color: $link-color;
      font-family: "Helvetica";
      text-decoration: none;
    }
  }

  &__trees {
    display: flex;
    padding: 0 22pt;
  }

  &__tree {
    text-align: left;
    width: 50%;
  }
}

.drawer__tree-title {
  color: $title-green;
  font-family: "Helvetica";
  font-weight: 400;
}

hr {
  border: 1px solid;
  color: #ebebec;
}

ul {
  list-style-type: none;
  display: inline;
  padding-inline-start: 0;
}

li {
  display: inline;
  position: relative;

  &:not(:first-child) {
    padding-left: 18px;

    &:after {
      background-color: #4f6272;
      content: "";
      display: inline-block;
      border-radius: 20px;
      height: 6px;
      width: 6px;
      position: absolute;
      left: 6px;
      top: 8px;
    }
  }
}
</style>
