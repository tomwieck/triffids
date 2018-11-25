<template>
  <header class="header layer">
    <h1> {{ message }} </h1>
  </header>
</template>

<script>
export default {
  name: 'appHeader',
  props: {
    message: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  width: 100%;
  background: white;
  left: 0;
  top: 0;
  position: fixed;
  height: 60px;
  z-index: 99;
  font-size: .8em;
}
</style>
