<template>
  <div id="drawer" class="drawer">
    <div v-if="response.fields" class="drawer__summary">
      <h1>{{ tree.common_name }} ({{ response.fields.common_name }})</h1>
      <h2>{{ response.fields.latin_name }}</h2>
      <div class="treefacts">
        <TreeFact class="fact tl" boxtype="height" v-bind:data="response.fields.crown_height"/>
        <TreeFact class="fact tr" boxtype="width" v-bind:data="response.fields.crown_width"/>
        <TreeFact class="fact bl" boxtype="area" v-bind:data="response.fields.crown_area"/>
        <TreeFact class="fact br" boxtype="dbh" v-bind:data="response.fields.dbh"/>
      </div>
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
      <div class="drawer__readmore">
        <a v-bind:href="tree.wiki_page" target="_blank">read more on Wikipedia
          <Chevron/>
        </a>
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
import TreeFact from "./TreeFact";

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
    Chevron,
    TreeFact
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

.treefacts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 10px;
  width: 70%;
  margin: 20px auto;
  .fact {
    height: 40px;
    justify-self: stretch;
    align-self: start;
  }
  .tl {
    grid-column: 1;
    grid-row: 1;
  }
  .tr {
    grid-column: 2;
    grid-row: 1;
  }
  .bl {
    grid-column: 1;
    grid-row: 2;
  }
  .br {
    grid-column: 2;
    grid-row: 2;
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
  &__readmore {
    padding: 8px 0;
    a {
      color: $dark-primary-color;
      text-decoration: none;
    }
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
</style>
