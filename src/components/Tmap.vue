<template>
  <div id="mapid">
    <CircleSpinner v-if="loading" size="large"></CircleSpinner>
    <TreePopup
      :is-popup-visible="isPopupVisible"
      :tree-data="treeData"
      :park-id="park.id"></TreePopup>
  </div>
</template>

<script>
import L from "leaflet";
import { CircleSpinner } from "vue-spinners";

import { treeIconService as treeIcons } from "../services/TreeIcon.service";
import { treeService } from "../services/Tree.service";

import TreePopup from './TreePopup.vue'
require("leaflet.locatecontrol");


export default {
  name: "Tmap",
  components: {
    CircleSpinner,
    TreePopup,
  },
  props: {
    park: {
      type: Object
    },
    drawerState: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      url:
        "https://api.mapbox.com/styles/v1/joshjarr/{id}/tiles/256/{z}/{x}/{y}?access_token={accessToken}",
      // url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      oldCenter: [0, 0],
      center: [this.park.lat, this.park.lng],
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 17,
      bounds: null,
      id: "cjuty2lxl4uig1fphqiwph7oq", // can be: streets, satellite, light, dark, outdoors
      token:
        "pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ",
      mymap: null,
      trees: null,
      treeCount: 0,
      loading: true,
      person: null,
      isPopupVisible: false,
      treeData: {},
    };
  },
  watch: {
    drawerState: function() {
      this.resetPosition();
    }
  },
  methods: {
    resetPosition: function() {
      let moveBy = window.innerHeight / 3;
      moveBy = this.drawerState ? moveBy : -moveBy;
      this.$log.info("Tmap:resetPosition: ", moveBy);
      this.mymap.panBy([0, moveBy]);
      this.oldCenter = this.mymap.getCenter();
    },
    resize: function(full) {
      // not currently used...
      this.$log.info("Tmap:resize triggered");
      if (full) {
        this.mymap.panBy([0, 0]);
      } else {
        this.mymap.panBy([0, 300]);
      }
    },
    mapLoaded() {
      if (this.mymap) {
        this.$log.info("Tmap:mapLoaded triggered");
        this.zoom = this.mymap.getZoom();
        this.bounds = this.mymap.getBounds();
        this.center = this.mymap.getCenter();
        this.oldCenter = this.center;
      }
      // this.loading = false;
    },
    mapClicked() {
      this.$log.info("Tmap:mapClicked triggered");

      this.treeData = {};
      this.$emit("close-drawer", false);
      this.isPopupVisible = false;
    },
    zoomUpdated() {
      this.$log.info("Tmap:zoomUpdated triggered");
      if (this.mymap) {
        this.zoom = this.mymap.getZoom();
        this.bounds = this.mymap.getBounds();
      }
    },
    moveUpdated() {
      this.$log.info("Tmap:moveUpdated triggered");
      if (this.mymap) {
        this.center = this.mymap.getCenter();
        this.bounds = this.mymap.getBounds();
      }
    },
    popupOpen() {
      this.oldCenter = this.mymap.getCenter();
    },
    popupClose() {
      this.mymap.setView(this.oldCenter);
    },
    async loadTrees() {
      // TODO: we need a leaflet.markerCluster here!
      this.$log.info("Tmap:loadTrees triggered");
      const response = await treeService.trees(this.park.id);
      this.trees = response.map(val => {
        return {
          id: val.recordid,
          name: val.fields.common_name,
          full_name: val.fields.full_common_name,
          girth: val.fields.dbh,
          width: val.fields.crown_area,
          height: val.fields.crown_height,
          latin: val.fields.latin_name,
          latin_code: val.fields.latin_code,
          geo_point: {
            lat: val.fields.geo_point_2d[0],
            lng: val.fields.geo_point_2d[1]
          }
        };
      });
      this.treeCount = response.length;
      this.trees.forEach(function(tree) {
        if (tree.latin_code === "NA") {
          tree.name = "Unknown";
          tree.full_name = "Unknown";
          tree.latin_name = "Unknown";
          tree.height = "No";
          tree.width = "No";
          tree.girth = "No";
        }
        const options = {
          icon: treeIcons.getIconFor(tree.name),
          title: tree.full_name // used for tooltip
        };
        L.marker([tree.geo_point.lat, tree.geo_point.lng], options)
          .addTo(this.mymap)
          .on('click', () => {
            this.isPopupVisible = true;
            this.treeData = tree;
            this.$emit("close-drawer", false);
          })
      }, this);
      this.$log.info(`Tmap:loadTrees ${this.treeCount} loaded`);
      this.loading = false;
    }
  },
  mounted: async function() {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty("--vh", `${vh}px`);
    this.mymap = L.map("mapid");
    this.mymap.on("load", this.mapLoaded); // order is important
    this.mymap.setView(this.center, this.zoom);
    L.control.scale({ position: "topright" }).addTo(this.mymap);
    const loc = L.control
      .locate({
        icon: "map-location-control",
        iconLoading: "map-location-control-loading",
        enableHighAccuracy: true
      })
      .addTo(this.mymap);
    //loc.stop(); // not needed except for linting.
    loc.start(); // not needed except for linting.

    L.tileLayer(this.url, {
      attribution: this.attribution,
      maxZoom: 20,
      id: this.id,
      accessToken: this.token
    }).addTo(this.mymap);
    this.mymap.panBy([0, window.innerHeight / 3]); // TODO: this is an estimate!
    this.oldCenter = this.center;

    this.mymap.on("click", this.mapClicked);
    this.mymap.on("zoomend", this.zoomUpdated);
    this.mymap.on("moveend", this.moveUpdated);
    this.mymap.on("popupopen", this.popupOpen);
    this.mymap.on("popupclose", this.popupClose);

    this.loadTrees();
    this.resetPosition();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!-- Put leaflet map styles in the leaflet.css file to avoid the scoped -->
<style scoped>
@import url("../../node_modules/leaflet/dist/leaflet.css");
@import url("../../node_modules/leaflet.locatecontrol/dist/L.Control.Locate.min.css");
@import url("../assets/leaflet.css");

#mapid {
  height: 100vh;
  height: calc(var(--vh, 1vh) * 90);
  width: 100%;
  z-index: 1;
}
</style>
