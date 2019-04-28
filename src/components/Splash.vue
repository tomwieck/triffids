<template>
  <main class="splash-screen">
    <img
      class="splash-screen__image"
      :src="image"
      alt="Triffids"
    >
  </main>
</template>

<script>
import image from "../assets/logo.png";

export default {
  name: "splash",
  data: () => {
    return {
      image: image
    };
  },

  mounted() {
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
    checkLocation() {
      navigator.geolocation.getCurrentPosition(
        position => {
          this.$log.info("Geolocation SUCCESS!", position);
          this.$config.locationAllowed = true;
          this.$router.push('parks');
        },
        () => {
          this.$log.info("Geolocation FAILED!");
          this.$router.push('parks');
        }
      );
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../styles/variables.scss";

.splash-screen {
  background: #1BC998;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  margin: -$header-height;

  &__image {
    max-width: 230px;
    width: 100%;
  }
}
</style>
