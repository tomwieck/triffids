<template>
  <div id="mapid">
    <CircleSpinner v-if="loading" size="large"></CircleSpinner>
  </div>
</template>

<script>
import L from "leaflet";
import { CircleSpinner } from "vue-spinners";

import { treeIconService as treeIcons } from "../services/TreeIcon.service";
import { treePhotoService as treePhotos } from "../services/TreePhoto.service";
import { treeService } from "../services/Tree.service";
require("leaflet.locatecontrol");

const personIcon = L.Icon.extend({
  options: {
    iconUrl: require("../assets/person-marker.png"),
    iconSize: [24, 24],
    shadowSize: [24, 24],
    iconAnchor: [20, 12],
    shadowAnchor: [0, 0],
    popupAnchor: [-3, -64],
    className: "personicon"
  }
});

export default {
  name: "Tmap",
  components: { CircleSpinner },
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
        "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}",
      // url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",

      oldCenter: [0, 0],
      center: [this.park.lat, this.park.lng],
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 17,
      bounds: null,
      id: "mapbox.outdoors", // can be: streets, satellite, light, dark, outdoors
      token:
        "pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ",
      mymap: null,
      trees: null,
      treeCount: 0,
      loading: true,
      person: null
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
    treeModal: function(data) {
      let imgsrc = treePhotos.getPhotoFor(data.name);

      // return vue component that gets rendered for more control.

      return `<div class="tree-modal">
            <img src="${imgsrc}"/>
            <div class="full-name">${data.full_name}</div>
            <div class="latin-name">${data.latin}</div>
            <a href="/#/tree/${data.full_name}/${data.id}"
            class="button">Find out more</a>
        </div>`;
    },
    resize: function(full) {
      // not currently used...
      // this.$log.info("Tmap:resize triggered");
      if (full) {
        this.mymap.panBy([0, 0]);
      } else {
        this.mymap.panBy([0, 300]);
      }
    },
    mapLoaded() {
      if (this.mymap) {
        // this.$log.info("Tmap:mapLoaded triggered");
        this.zoom = this.mymap.getZoom();
        this.bounds = this.mymap.getBounds();
        this.center = this.mymap.getCenter();
        this.oldCenter = this.center;
      }
      // this.loading = false;
    },
    mapClicked() {
      // this.$log.info("Tmap:mapClicked triggered");
      this.$emit("close-drawer", false);
    },
    zoomUpdated() {
      // this.$log.info("Tmap:zoomUpdated triggered");
      if (this.mymap) {
        this.zoom = this.mymap.getZoom();
        this.bounds = this.mymap.getBounds();
      }
    },
    moveUpdated() {
      // this.$log.info("Tmap:moveUpdated triggered");
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
          id: val.id,
          name: val.common_name,
          full_name: val.full_common_name,
          girth: val.dbh,
          width: val.crown_area,
          height: val.crown_height,
          latin: val.latin_name,
          latin_code: val.latin_code,
          geo_point: { lat: val.geo_point_2d[0], lng: val.geo_point_2d[1] }
        };
      });
      this.treeCount = response.length;

      // options for popup

      const popupOptions = {
        minWidth: 200,
        maxWidth: 200,
        keepInView: true,
        className: "tree-modal"
      };
      this.trees.forEach(function(tree) {
        const options = {
          icon: treeIcons.getIconFor(tree.name),
          title: tree.full_name // used for tooltip
        };
        L.marker([tree.geo_point.lat, tree.geo_point.lng], options)
          .addTo(this.mymap)
          .bindPopup(this.treeModal(tree), popupOptions);
      }, this);
      this.$log.info(`Tmap:loadTrees ${this.treeCount} loaded`);
      this.loading = false;
    }
  },
  mounted: async function() {
    this.mymap = L.map("mapid");
    this.mymap.on("load", this.mapLoaded); // order is important
    this.mymap.setView(this.center, this.zoom);
    L.control.scale({ position: "topright" }).addTo(this.mymap);
    const loc = L.control
      .locate({ icon: "map-location-control" })
      .addTo(this.mymap);
    loc.stop(); // not needed except for linting.

    L.tileLayer(this.url, {
      attribution: this.attribution,
      maxZoom: 18,
      id: this.id,
      accessToken: this.token
    }).addTo(this.mymap);
    this.mymap.panBy([0, window.innerHeight / 3]); // TODO: this is an estimate!
    this.oldCenter = this.center;

    const personOptions = {
      icon: new personIcon(),
      title: "You are here",
      alt: "You are here!"
    };
    this.person = L.marker(this.center, personOptions).addTo(this.mymap);

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
@import url("../assets/leaflet.css");

#mapid {
  height: 100vh;
  width: 100%;
  z-index: 1;
}

.tree-modal {
  max-height: 200px;
}
</style>

