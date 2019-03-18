<template>
  <main class="main">
    <img
      :src="image"
      alt="Triffids"
      width="300"
      style="display:block; margin: 0 auto; margin-top: 4em;"
    >
  </main>
</template>

<script>
import image from "../assets/logo.png";

export default {
  name: "splash",
  data: function() {
    return {
      image: image
    };
  },

  mounted: function() {
    if (this.$config.hasGeolocation) {
      this.checkLocation();
    } else {
      setTimeout(function() {
        this.$log.info("Splash: device without Geolocation API");
        window.location.href = "/#/parks";
      }, 1000);
    }
    this.checkLocation();
  },
  methods: {
    checkLocation: function() {
      navigator.geolocation.getCurrentPosition(
        position => {
          this.$log.info("Geolocation SUCCESS!", position);
          this.$config.locationAllowed = true;
          window.location.href = "/#/parks";
        },
        () => {
          this.$log.info("Geolocation FAILED!");
          window.location.href = "/#/parks";
        }
      );
    }
  }
};
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
  color: green;
}
</style>
