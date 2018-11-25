<template>
    <div>
        <h1>Map</h1>
        <Tmap class="tmap"></Tmap>
    </div>
</template>

<script>
export default {
  name: 'Tmap',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
tmap {
  width: 100%;
  left: 0;
  top: 0;
}
</style>
