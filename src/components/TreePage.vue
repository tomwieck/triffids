<template>
  <div class="hello">
    <Header v-bind:message="name" v-bind:hasBack="backLink"/>
    <div class="tree"></div>
    <TreeDrawer :message="name"/>
  </div>
</template>

<script>
import Header from "./Header.vue";
import TreeDrawer from "./TreeDrawer.vue";

export default {
  name: "TreePage",
  props: {
    name: {
      type: String,
      default: "none"
    },
    backLink: {
      type: String,
      default: ""
    }
  },
  components: {
    Header,
    TreeDrawer
  }
};
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
.tree {
  width: 100%;
  height: auto;
  min-height: 400px;
  background-image: url("https://www.mcfallandberry.com/wp-content/uploads/2016/04/london-plane-tree-1.jpg");
  background-size: cover;
}
</style>
