<template>
  <main class="main">
    <Header v-bind:title="'Choose a park'"/>
    <input
      type="search"
      placeholder="Search for a park..."
      v-model="search">
    <ul>
      <li v-for="park in parks" v-bind:key="park.id" class="layer">
        <router-link :to="{
          path: getParkLink(park.id),
        }">
          <h3>{{ park.siteName }}</h3>
          <div class="stats">
            <span>
              <b>{{park.unique_trees}}</b> Unique species
            </span>
            <span>
              <b>{{park.total_trees}}</b> Total trees
            </span>
          </div>
        </router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import Header from "./Header.vue";
import { parkService } from "../services/Park.service";

export default {
  name: "list",
  data: () => {
    return {
      parks: [],
      loading: false,
      page: 1,
      search: '',
    };
  },

  beforeMount() {
    this.getParks().then(parks => {
      this.parks = parks;
    });
  },

  watch: {
    search: function(q) {
      this.getSearchedParks(q).then(parks => {
        this.parks = parks;
      })
    }
  },

  mounted() {
    window.onscroll = () => {
      if (
        window.innerHeight + window.scrollY >= document.body.offsetHeight &&
        !this.loading
      ) {
        this.loading = true;
        this.getParks().then(newParks => {
          this.parks.push(...newParks);
          this.loading = false;
        });
      }
    }
  },

  methods: {
    getParkLink: parkId => `park/${parkId}`,
    async getParks() {
      let parks = await parkService.parks(this.page);
      this.page++;
      return parks;
    },
    async getSearchedParks(q) {
      this.page = 0;
      let parks = await parkService.searchParks(this.search);
      console.log(parks)
      return parks;
    }
  },
  components: {
    Header
  }
};
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
  font-size: 0.8em;
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
