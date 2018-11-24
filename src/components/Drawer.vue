<template>
  <div id="drawer" class="drawer">
    <button v-on:click="greet"> Ello </button>
    <h1> Drawer. {{counter}} </h1>
  </div>
</template>

<script>
export default {
  name: 'drawer',
  data: () => {
    return {
    counter: 0,
    el: '#drawer',
    }
  },
  methods: {
    greet: function (event) {

      const drawer = document.getElementById('drawer')
      drawer.classList.contains('expanded') ? drawer.classList.remove('expanded') : drawer.classList.add('expanded')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.drawer {
  width: 100%;
  background: yellow;
  left: 0;
  bottom: 0;
  position: fixed;
  transition: all .5s ease;
  height: 60px;

  &.expanded {
    height: 300px;
  }
}
</style>
