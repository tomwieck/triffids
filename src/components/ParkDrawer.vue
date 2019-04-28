<template>
  <div id="drawer" class="drawer">
    <button class="drawer__button" @click="drawerToggle">
      <Chevron class="rotate"/>
    </button>
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

<style scoped lang='scss'>

@import "../styles/variables.scss";

.factbox {
  width: 50%;
  display: grid;
  grid-template-columns: 50px 3fr;
  grid-template-rows: 1fr 1fr;

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
  bottom: 0;
  box-shadow: 0 2px 4px;
  box-sizing: border-box;
  height: 50%;
  left: 0;
  position: fixed;
  overflow-y: scroll;
  padding: 16px;
  transition: all 0.5s ease;
  width: 100%;
  z-index: 100;

  &__header {
    color: $title-green;
    font-weight: normal;
    font-style: normal;
    font-weight: 400;
    margin-top: 0;
    text-align: center;
  }

  &.closed {
    height: 50px;

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
      text-decoration: none;
    }
  }

  &__trees {
    display: flex;
  }

  &__tree {
    text-align: left;
    width: 50%;
  }
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

.parkinfo {
  text-align: left;
  font-weight: normal;
  font-style: normal;
  font-weight: 400;

  /deep/
  h1 {
    color: $title-green;
    font-weight: normal;
    font-style: normal;
    font-weight: 400;
  }

  /deep/
  h2 {
    color: $title-green;
    font-weight: 600;
    font-size: 18px;
  }

  /deep/
  h3 {
    color: $title-green;
    font-weight: 600;
    font-size: 16px;
  }

  /deep/
  ul {
    list-style: circle;
  }
  /deep/
  li {
    margin-inline-start: 20px;
  }
}
</style>
