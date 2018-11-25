<template>
  <main class="main">
    <img src="smiley.gif" alt="Smiley face" width="42" height="42" style="display:block; margin: 0 auto; margin-top: 4em;">
  </main>
</template>

<script>
import Header from './Header.vue'

export default {
  name: 'list',
  mounted: () => {
    setTimeout(()=>{
      window.location.href = "/#/parks"
    }, 3000)
  }
}
</script>

<style scoped>

ul {
  padding: 0 1em;
}

.main {
  background: green;
  margin: 0;
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
