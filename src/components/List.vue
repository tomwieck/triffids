<template>
  <main class="main">
    <Header v-bind:title="'Choose a park'"/>
    <Modal v-if="showModal" @close="showModal = false" @confirm="requestUsersLocation()" >
      <h3 slot="header">Get location</h3>
      <p slot="body">Please allow this app to use your location to show you the nearest parks.</p>
    </Modal>
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
      <span v-if="loading" class="spinner"><div></div><div></div></span>
      <span v-if="maxDistReached"> No more parks found! </span>
    </ul>
  </main>
</template>

<script>
import Header from "./Header.vue";
import Modal from "./Modal.vue";
import { parkService } from "../services/Park.service";

export default {
  name: "list",
  data: () => {
    return {
      parks: [],
      loading: true,
      page: 1,
      foundParksByLocation: false,
      maxDistReached: false,
      showModal: false
    };
  },

  beforeMount() {
    this.showModal = !this.$config.locationAllowed;
    this.getParks();
  },

  mounted() {
    window.onscroll = () => {
      if (
        window.innerHeight + window.scrollY >= document.body.offsetHeight &&
        !this.loading
      ) {
        this.loading = true;
        this.getParks().then(() => {
          this.loading = false;
        });
      }
    };
  },

  methods: {
    getParkLink: parkId => `park/${parkId}`,

    async getParks() {
      if (this.$config.locationAllowed) {
        this.$getLocation()
          .then(async coords => {
            try {
              let parks = await parkService.nearestParks(
                this.page,
                coords.lat,
                coords.lng
              );
              if (parks.length > 0) {
                this.page++;

                if (this.parks.length === parks.length) {
                  this.maxDistReached = true;
                }

                this.parks = parks
                this.foundParksByLocation = true;
                this.loading = false;
              }
            } catch (error) {
              if (!this.foundParksByLocation) {
                // Location failed - no nearby parks, get parks by alpha
                this.$config.locationAllowed = false;
                let parks = await parkService.parks(1);
                this.page = 2;
                this.parks = parks;
                this.loading = false;
              } else {
                // Request failed to get more parks by location, show an error
                this.maxDistReached = true;
                this.loading = false;
              }
            }
          })
      } else {
        let parks = await parkService.parks(this.page);
        this.page++;
        this.parks = [...this.parks, ...parks];
        this.loading = false;
      }
    },

    requestUsersLocation() {
      this.showModal = false;
      this.loading = true;
      this.$config.locationAllowed = true;
      this.parks = [];
      this.getParks();
    },

  },
  components: {
    Header,
    Modal
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
