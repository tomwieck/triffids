<template>
  <div id="drawer" class="drawer">
    <button class="drawer__button" @click="drawerToggle">
      <Chevron class="rotate"/>
    </button>
    <div class="drawer__trees">
      <div class="drawer__tree">
        <img alt="Vue logo" src="../assets/tree1.svg">
        <div>
          <span class="drawer__tree-title">13</span> Unique species
        </div>
      </div>
      <div class="drawer__tree">
        <img alt="Vue logo" src="../assets/tree2.svg">
        <div>
          <span class="drawer__tree-title">{{treeCount}}</span> Trees in total
        </div>
      </div>
    </div>
    <hr>
    <div class="drawer__about">
      <h1>About Victoria Park</h1>
      <ul>
        <li>Free admission</li>
        <li>Open at all times</li>
      </ul>
      <p>The park was established in the 1880s following the expansion of Bedminster as a residential and industrial area within Bristol. The council bought 51.5 acres (20.8 ha) of land from Sir John Henry Greville Smyth for £20,678 (now £2,110,000), though the land had been used as an unofficial open space and meeting area for some time before this. By 1887, a children's play area had been installed which became immediately popular. The streets around the park were laid out in 1891. By 1898, four rangers were permanently employed in the park, and a bandstand had been installed. Several drinking fountains and a circular pond had also been established.</p>
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
import { treeService } from "../services/Tree.service.js";

export default {
  name: "parkDrawer",
  data: () => {
    return {
      el: "#drawer",
      treeCount: 144
    };
  },
  components: {
    Chevron
  },
  methods: {
    drawerToggle: function() {
      const drawer = document.getElementById("drawer");
      this.$emit("toggle-drawer", drawer.classList.contains("expanded"));
      drawer.classList.contains("expanded")
        ? drawer.classList.remove("expanded")
        : drawer.classList.add("expanded");
    }
  },
  mounted: async function() {
    this.treeCount = await treeService.count("VICTPA");
  }
};
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped lang='scss'>
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
  z-index: 100;

  &.expanded {
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
}

h1,
.drawer__tree-title {
  color: #058e3f;
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
