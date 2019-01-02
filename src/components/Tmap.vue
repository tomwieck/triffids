<template>
  <div>
    <div id="mapid">
      <CircleSpinner v-if="loading" size="large"></CircleSpinner>
    </div>
  </div>
</template>

<script>
import L from "leaflet";
import { CircleSpinner } from "vue-spinners";

import { treeIconService as treeIcons } from "../services/TreeIcon.service";
import { treeService } from "../services/Tree.service.js";

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
    drawerState: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      // url: 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={token}',
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      center: [51.44059, -2.58889],
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 16,
      bounds: null,
      id: "mapbox.streets",
      token:
        "pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ",
      mymap: null,
      trees: null,
      treeCount: 0,
      loading: true
    };
  },
  watch: {
    drawerState: function() {
      this.drawerState
        ? this.mymap.panBy([0, 300])
        : this.mymap.panBy([0, -300]);
    }
  },
  methods: {
    resize: function(full) {
      this.$log.info("Tmap:resize triggered");
      if (full) {
        this.mymap.panBy([0, 0]);
      } else {
        this.mymap.panBy([0, 300]);
      }
    },
    mapLoaded() {
      this.$log.info("Tmap:mapLoaded triggered");
      if (this.mymap) {
        this.zoom = this.mymap.getZoom();
        this.bounds = this.mymap.getBounds();
        this.center = this.mymap.getCenter();
      }
      this.loading = false;
    },
    mapClicked() {
      this.$log.info("Tmap:mapClicked triggered");
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
    async loadTrees() {
      this.$log.info("Tmap:loadTrees triggered");
      const response = await treeService.trees("VICTPA");
      this.trees = response.map(val => {
        return {
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
      this.trees.forEach(function(tree) {
        const options = {
          icon: treeIcons.getIconFor(tree.name),
          title: tree.full_name
        };
        L.marker([tree.geo_point.lat, tree.geo_point.lng], options)
          .addTo(this.mymap)
          .bindPopup(
            "<b>" +
              tree.full_name +
              "</b><br>H: " +
              tree.height +
              "<br>W: " +
              tree.girth
          );
      }, this);
      this.$log.info(`Tmap:loadTrees ${this.treeCount} loaded`);
      this.loading = false;
    }
  },
  mounted: function() {
    this.mymap = L.map("mapid").setView(this.center, 16);
    L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
      attribution: this.attribution,
      zoom: this.zoom,
      id: this.id,
      access_token: this.token
    }).addTo(this.mymap);
    this.mymap.panBy([0, 300]); // TODO: this is an estimate!

    const personOptions = {
      icon: new personIcon(),
      title: "You are here",
      alt: "You are here!"
    };
    L.marker(this.center, personOptions).addTo(this.mymap);

    this.mymap.on("load", this.mapLoaded);
    this.mymap.on("click", this.mapClicked);
    this.mymap.on("zoomend", this.zoomUpdated);
    this.mymap.on("moveend", this.moveUpdated);
    this.loadTrees();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url("../../node_modules/leaflet/dist/leaflet.css");

#mapid {
  height: 100vh;
  width: 100%;
  z-index: 1;
}
</style>

