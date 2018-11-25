<template>
  <main class="main">
    <Header v-bind:message="'Choose a park'" />
    <ul>
      <li v-for="park in parks" v-bind:key="park.id" class="layer">
        <router-link :to="{
          path: getParkLink(park.id),
          query: { title: park.title }
        }">
          <h3> {{ park.title }} </h3>
          <span class="small">{{ park.location }}</span>
          <div class="stats">
              <span><b>{{park.trees.unique}}</b> Unique species</span>
              <span><b>{{park.trees.unique}}</b> Total trees</span>
          </div>
        </router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import Header from './Header.vue'

export default {
  name: 'list',
  data: () => {
    return {
      parks: [
        {
          title: 'Victoria park',
          id: 'victoria_park',
          location: 'Bedminster',
          trees: {
            amount: 123,
            unique: 3
          }
        },
        {
          title: 'Clifton downs',
          id: 'clifton_downs',
          location: 'Clifton',
          trees: {
            amount: 123,
            unique: 3
          }
        },
        {
          title: 'Brandon park',
          id: 'brandon_park',
          location: 'Somewhere',
          trees: {
            amount: 123,
            unique: 3
          }
        }
      ]
    }
  },
  methods: {
    getParkLink: (parkId) => `park/${parkId}`
  },
  components: {
    Header,
  },
}
</script>

<style scoped>

ul {
  padding: 0 1em;
}

.main {
  background: #009133;
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
  color: #009133;
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
  color: #009133;
}
</style>
