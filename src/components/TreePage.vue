<template>
  <div class="hello">
    <Header v-bind:title="title" v-bind:hasBack="backLink"/>
    <div class="tree" id="photo"></div>
    <TreeDrawer :response="response" :tree="tree"/>
  </div>
</template>

<script>
import Header from "./Header.vue";
import TreeDrawer from "./TreeDrawer.vue";
import { treeService } from "../services/Tree.service.js";
import { treeInfoService as treeInfo } from "../services/TreeInfo.service.js";

export default {
  name: "TreePage",
  props: {
    backLink: {
      type: String,
      default: ""
    }
  },
  async mounted() {
    this.$log.info("TreePage:params: ", this.tree_code);
    if (this.$route.params.treeId) {
      this.getTree(this.$route.params.treeId);
    }
    this.tree = await treeInfo.getTreeInfo(this.tree_code);
    const imgLink = this.tree.wiki_image;
    this.title = this.tree.full_common_name;
    const el = document.getElementById("photo");
    el.style.backgroundImage = `url('${imgLink}')`;
  },
  components: {
    Header,
    TreeDrawer
  },
  data() {
    return {
      treeId: this.$route.params.treeId,
      tree_code: this.$route.params.title,
      tree: {},
      title: "Loading...",
      response: {}
    };
  },
  methods: {
    async getTree(id) {
      this.response = await treeService.tree(id);
      this.title = this.response.fields.full_common_name;
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
#photo {
  width: 100%;
  height: auto;
  min-height: 400px;
  background-size: cover;
}
</style>
