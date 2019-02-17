<template>
  <main class="list">
    <Header v-bind:title="'Choose a park'"/>
    <Modal v-if="showModal" @close="showModal = false" @confirm="requestUsersLocation()" >
      <h3 slot="header">Get location</h3>
      <p slot="body">Please allow this app to use your location to show you the nearest parks.</p>
    </Modal>
    <ul class="list__container">
      <li
        v-for="park in parks"
        v-bind:key="park.id">
        <router-link
          :to="{
            path: getParkLink(park.id),
          }"
          class="list-item">
          <div class="list-item__inner">
            <div class="list-item__details">
              <h3 class="list-item__header">{{ park.siteName }}</h3>
              <ul class="list-item__stats-container">
                <li class="list-item__stats">
                  {{park.unique_trees}} Unique species
                </li>
                <li class="list-item__stats">
                  {{park.total_trees}} Total trees
                </li>
              </ul>
            </div>
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

<style scoped lang="scss">
@import  '../styles/variables.scss';

.list {
  background-color: $gray-super-light;

  &__container {
    display: block;
    margin: 0 auto;
    max-width: 600px;
    padding-top: 8px;
  }
}

.list-item {
  border-radius: 3px;
  display: block;
  height: 180px;
  list-style-type: none;
  max-width: 600px;
  padding: 16px;
  margin: 8px;
  position: relative;
  text-decoration: none;

  &__inner {
    align-items: flex-end;
    background-image: url("../assets/parks/park-empty.svg");
    background-size: contain;
    background-repeat: no-repeat;
    display: flex;
    height: 100%;
    width: 100%;
    background-position: center;
  }

  &__header {
    color: #fff;
    margin: 8px 0;
  }

  &__details {
    color: #fff;
    text-align: left;
    z-index: 2;
  }

  &__stats-container {
    list-style-type: none;
    padding-inline-start: 0;
    text-align: left;
  }

  &__stats {
    display: inline;
    position: relative;

    &:not(:first-child) {
      padding-left: 18px;

      &:after {
        background-color: #fff;
        content: "";
        display: inline-block;
        border-radius: 20px;
        height: 6px;
        width: 6px;
        position: absolute;
        left: 6px;
        top: 8px;
      }
    }
  }

  &:before {
    background-color: $title-green;
    border-radius: 3px;
    bottom: 0;
    content: '';
    left: 0;
    opacity: 0.8;
    position: absolute;
    right: 0;
    top: 0;
    width: 100%;
    z-index: 1;
  }
}


</style>
