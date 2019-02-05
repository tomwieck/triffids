<template>
  <div class="hello">
    <Header v-bind:title="title"/>
    <div class="tree"></div>
    <TreeDrawer
      :response="response"
      :title="title"
      />
  </div>
</template>

<script>
import Header from "./Header.vue";
import TreeDrawer from "./TreeDrawer.vue";
import { treeService } from "../services/Tree.service.js";

export default {
  name: "TreePage",
  mounted() {
    if(this.$route.params.treeId) {
      this.getTree(this.$route.params.treeId)
    }
  },
  components: {
    Header,
    TreeDrawer
  },
  data() {
    return {
      treeId: this.$route.params.treeId,
      title: this.$route.params.title,
      response: {}
    }
  },
  methods: {
    async getTree(id) {
      this.response = await treeService.tree(id);
    }
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
