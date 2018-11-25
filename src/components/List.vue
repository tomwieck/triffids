<template>
  <main class="main">
    <ul>
      <li v-for="park in parks" v-bind:key="park.id">
        <router-link :to="{
          path: getParkLink(park.id),
          query: { title: park.title }
        }">
          {{ park.title }}
        </router-link>
      </li>
    </ul>
  </main>
</template>

<script>
export default {
  name: 'list',
  data: () => {
    return {
      parks: [
        { title: 'Victoria park', id: 'victoria_park'},
        { title: 'Clifton downs', id: 'clifton_downs'},
        { title: 'Brandon park', id: 'brandon_park'},
      ]
    }
  },
  methods: {
    getParkLink: (parkId) => `park/${parkId}`
  }
}
</script>

<style scoped>
</style>
