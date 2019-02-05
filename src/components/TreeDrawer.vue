<template>
  <div id="drawer" class="drawer">
    <div v-if="response.fields" class="drawer__summary">
      <h1>{{ tree.common_name }} ({{ response.fields.common_name }})</h1>
      <h2>{{ response.fields.latin_name }}</h2>
      <ul class="drawer__subtitle">
        <li>Crown Height: {{ response.fields.crown_height }}</li>
        <li>Crown Width: {{ response.fields.crown_width }}</li>
        <li>Location Risk Zone: {{ response.fields.location_risk_zone }}</li>
        <li>Diameter at 1.3 meters: {{ response.fields.dbh }}</li>
        <li v-if="response.fields.crown_area">- {{ response.fields.crown_area }}</li>
      </ul>
    </div>
    <hr>
    <div class="drawer__about">
      <div v-if="special" class="drawer__specialinfo">
        <h2>Special information about this specimen</h2>
        <p>Some info here...</p>
        <hr>
      </div>
      <div class="drawer__generalinfo">
        <h2>General information about this species</h2>
        <p>{{tree.wiki_data}}</p>
        <span class="drawer__source">Source: Wikipedia</span>
      </div>
      <hr>
      <div class="drawer__report">
        <a
          target="_blank"
          href="https://www.bristol.gov.uk/museums-parks-sports-culture/what-to-do-if-you-have-a-problem-with-a-tree"
        >Report an issue with this tree
          <Chevron/>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import Chevron from "./Chevron.vue";
import { treeInfoService as treeInfo } from "../services/TreeInfo.service.js";

export default {
  name: "treeDrawer",
  props: {
    title: {
      type: String,
      default: "None"
    },
    response: {
      type: Object,
      default: () => []
    },
    tree: {
      type: Object,
      default: () => []
    }
  },
  data: () => {
    return {
      el: "#drawer",
      // treeObj: {},
      special: 0
    };
  },
  components: {
    Chevron
  },
  mounted: async function() {
    // this.treeObj = await treeInfo.getTreeInfo(this.code);
    // this.$log.info("TreeDrawer:loading:", this.code);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "../styles/variables.scss";

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

  &.expanded {
    height: 40px;
  }

  &__button {
    background-color: none;
    border: none;
    cursor: pointer;
    width: 100%;

    &:focus {
      outline: none;
    }
  }

  &__subtitle {
    margin-bottom: 16px;
  }

  &__summary {
    padding: 18px 0;
    text-align: center;
  }

  &__about {
    padding-top: 8px;
    text-align: left;
  }

  &__report {
    padding: 8px 0;
    a {
      color: #058e3f;
      font-family: "Helvetica";
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

  &__source {
    color: grey;
  }
}

h1,
h2 {
  color: $title-green;
  font-family: "Helvetica";
  font-weight: 600;
  margin: 4px 0;
}

h2 {
  font-size: 18px;
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
