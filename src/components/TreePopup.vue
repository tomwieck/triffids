<template>
  <div
    v-if="isPopupVisible && treeData"
    class="tree-popup">
    <div class="tree-popup-container">
      <div
        class="tree-popup-container__image"
        :style="treeStyle"></div>
      <div class="tree-popup-container__content">
        <h2 class="tree-popup-container__name">
          {{ treeData.full_name }}
          </h2>
        <div>
          <span
            class="tree-popup-container__common-name"
            v-if="treeData.name">
            {{ treeData.name }}
          </span>
          <span v-if="treeData.name && treeData.latin">
            &nbsp;&#8226;&nbsp;
          </span>
          <span>
            {{ treeData.latin }}
          </span>
        </div>
        <router-link :to="{
            path: `/tree/${treeData.latin_code}/${treeData.id}?back=/park/${parkId}`,
          }"
          class="tree-popup-container__link">
          Find out more
        </router-link>
      </div>
      <button class="close-icon"><img :src="closeIcon"></button>
    </div>
  </div>
</template>

<script>
import { treePhotoService as treePhotos } from "../services/TreePhoto.service";
export default {
  name: "TreePopup",
  props: {
    isPopupVisible: {
      type: Boolean,
      default: false,
    },
    parkId: {
      type: String,
      default: '',
    },
    treeData: {
      type: Object,
      default: function() {
        return {
          id: 0,
          name: '',
          full_name: 'Unknown Tree',
          girth: 0,
          width: 0,
          height: 0,
          latin: 'Unknown Tree',
          latin_code: '',
          geo_point: {
            lat: 0,
            lng: 0,
          }
        }
      }
    }
  },
  data: function() {
    return {
      treeImage: '',
      treeStyle: '',
      closeIcon: require("../assets/close.svg"),
    }
  },
  methods: {
    getTreePhoto() {
      let img = treePhotos.getPhotoFor(this.treeData.name);
      return `background-image: url(${img};`;
    },
  },
  watch: {
    isPopupVisible(newVal) {
      if (newVal) {
        // this.treeImage = treePhotos.getPhotoFor(this.treeData.name);
        this.treeStyle = this.getTreePhoto(this.treeData.name);
      }
    }
  },
};
</script>

<style scoped lang="scss">
@import "../styles/variables.scss";

.tree-popup {
  position: absolute;
  z-index: 10000;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
}

.tree-popup-container {
  position: relative;
  background-color: $white;
  margin-top: 150px;
  border-radius: 3px;
  margin: 100px 24px;
  padding: 8px;
  text-align: center;
  height: 280px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  &__image {
    height: 180px;
    width: 100%;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
  }

  &__name {
    color: $title-green;
    font-style: normal;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 8px;
  }

  &__link {
    background-color: $primary-color;
    border-radius: 3px;
    color: white;
    display: block;
    font-size: 14px;
    padding: 8px 0;
    margin-top: 8px;
    width: 100%;
  }
}

.close-icon {
  position: absolute;
  top: -12px;
  right: -12px;
  border-radius: 100%;
  padding: 8px;
  background: $white;
  box-shadow: -1px 1px 4px rgba(0, 0, 0, .5);
}

</style>
