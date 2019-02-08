<template>
  <div>
    <div class="factbox">
      <div class="icon">
        <img alt="Vue logo" src="../assets/tree2.svg">
      </div>
      <div class="data">{{showData}}</div>
      <div class="label">{{showLabel}}</div>
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
      default: "Blood"
    }
  },
  computed: {
    showData: function() {
      let text = "Unknown";
      switch (this.boxtype) {
        case "height":
          text = this.data + "m";
          break;
        case "width":
          text = this.data + "m";
          break;
        case "area":
          text = this.data;
          break;
        case "dbh":
          text = this.data;
          break;
        default:
          text = "Unknown";
          break;
      }
      return text;
    },
    showLabel: function() {
      let text = "Unknown";
      switch (this.boxtype) {
        case "height":
          text = "Crown height";
          break;
        case "width":
          text = "Crown width";
          break;
        case "area":
          text = "Crown area";
          break;
        case "dbh":
          text = "Trunk diameter";
          break;
        default:
          text = "Unknown";
          break;
      }
      return text;
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
  .data {
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
