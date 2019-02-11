<template>
  <main class="list">
    <Header v-bind:title="'Choose a park'"/>
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
      page: 1
    };
  },

  beforeMount() {
    this.getParks().then(parks => {
      this.parks = parks;
    });
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
    };
  },

  methods: {
    getParkLink: parkId => `park/${parkId}`,
    async getParks() {
      let parks = await parkService.parks(this.page);
      this.page++;
      return parks;
    }
  },
  components: {
    Header
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
