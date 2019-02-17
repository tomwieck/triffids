<template>
  <div>
    <div class="factbox">
      <div class="icon">
        <img id="icon" :alt="'Tree ' + boxtype" :src="icon">
      </div>
      <div class="value">{{value}}</div>
      <div class="label">{{label}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "treeFact",
  props: {
    boxtype: {
      type: String,
      default: "Oranges"
    },
    data: {
      type: String,
      default: "No"
    }
  },
  data: () => {
    return {
      // these are needed so that Webpack will include them
      icon: require("../assets/tree2.svg"),
      iconH: require("../assets/meta_icons/crown_height.svg"),
      iconW: require("../assets/meta_icons/crown_width.svg"),
      iconA: require("../assets/meta_icons/crown_area.svg"),
      iconD: require("../assets/meta_icons/diameter.svg"),
      value: "Unknown",
      label: "Label"
    };
  },
  mounted: function() {
    switch (this.boxtype) {
      case "height":
        this.label = "Crown height";
        this.value = this.data + "m";
        this.icon = this.iconH;
        break;
      case "width":
        this.label = "Crown width";
        this.value = this.data + "m";
        this.icon = this.iconW;
        break;
      case "area":
        this.label = "Crown area";
        this.value = this.data;
        this.icon = this.iconA;
        break;
      case "dbh":
        this.label = "Trunk diameter";
        this.value = this.data;
        this.icon = this.iconD;
        break;
      default:
        break;
    }
    if (this.data.startsWith("No")) {
      this.value = "Unknown";
    }
  }
};
</script>

<style scoped lang="scss">
@import "../styles/variables.scss";

.factbox {
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 3px;
  .icon {
    grid-column: 1;
    grid-row: 1 / 3;
    justify-self: start;
    align-self: center;
    img {
      height: 40px;
    }
  }
  .value {
    grid-column: 2;
    grid-row: 1;
    justify-self: start;
    align-self: start;
    color: $dark-primary-color;
  }
  .label {
    font-size: 0.8em;
    grid-column: 2;
    grid-row: 2;
    justify-self: start;
    align-self: start;
  }
}
</style>
