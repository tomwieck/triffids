<template>
    <div>
        <h1>Map</h1>
        <div v-html="frame"></div>
    </div>
</template>

<script>
export default {
  data: () => {
    return {
      frame: `<iframe frameborder="0" width="800" height="600" src="https://opendata.bristol.gov.uk/map/embed/triffids-01/?&static=true&scrollWheelZoom=true"></iframe>`
    }
  },
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
