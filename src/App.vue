<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  props: {
    name: String
  },
}
</script>

<style lang="scss">
  @import  'styles/variables.scss';
  @import  'styles/normalize.scss';
  @import  'styles/utils.scss';
</style>
