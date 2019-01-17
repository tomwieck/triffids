<template>
  <main class="main">
    <img :src="image" alt="Smiley face" width="400" height="400" style="display:block; margin: 0 auto; margin-top: 4em;">
  </main>
</template>

<script>
import image from "../assets/logo.png"

export default {
  name: 'list',
  data: function () {
      return {
          image: image
      }
  },

  mounted: () => {
    setTimeout(()=>{
      window.location.href = "/#/parks"
    }, 2)
  }
}
</script>

<style scoped>

ul {
  padding: 0 1em;
}

.main {
  background: #098e38;
  margin: 0;
  margin-top: -60px;
  text-decoration: none;
  padding: 0.1em;
  min-height: 100vh;
}

a {
  text-decoration: none;
  text-align: left;
  color: #4d6576;
  cursor: pointer;
}

h3 {
  font-size: 1.4em;
  color: green;
  margin: 0;
}

li {
  list-style-type: none;
  background: white;
  border-radius: 10px;
  margin: 1em auto;
  padding: 1.5em;
  max-width: 600px;
}

.small {
  display: block;
  font-size: .8em;
}

.stats {
  display: flex;
}

.stats > span {
  flex: 50%;
  margin-top: 1em;
  border-top: 2px solid #eee;
  padding-top: 1em;
}

.stats > span > b {
  color: green;
}
</style>
