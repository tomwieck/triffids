<template>
  <div>
    <div id="mapid"></div>
  </div>
</template>

<script>
const lat = 51.44080;
const lng = -2.58889;
// const treeIcon = {
//   iconUrl: '../assets/tree-dk.png'
// } 
var mymap;
const ODBUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&rows=20&facet=feature_type_name&facet=common_name`;
// const localUrl = `http://localhost:4242/server/getTrees/?siteCode="VICTPA"&lat=0&long=0`;
function loadTrees() {
  const res = axios.get(ODBUrl)
    .then((resp) => {
      const trees = resp.data.records.map((item) => {
        return item.fields;
      })
      console.log(trees);
      L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
          attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: 'mapbox.streets',
          accessToken: 'pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ'
      }).addTo(mymap);
      trees.forEach(t => {
        let marker = L.marker([t['geo_point_2d'][0], t['geo_point_2d'][1]]).addTo(mymap);
        marker.bindPopup('<a href="#/tree/1234">' + t['common_name']+'</a>');
      });
    }, (err) => {
      console.log('Tmap ajax call: Error loading data: ', err);
    });
}

export default {
  name: 'Tmap',
  mounted: function () {
      const center = lat - 0.005; // this is a temporary hack to center the map above the sliding drawer, use map.panTo() to move it.
      mymap = L.map('mapid').setView([center, lng], 15);
      loadTrees();
  },
  methods: {
    resize: function(full) {
      console.log('Resize triggered')
      if (full) {
        mymap.panTo(lat, lng)
      } else {
        mymap.panTo(lat - 0.005, lng)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.leaflet-popup {
  background-color: lime;
}
.leaflet-popup-content {
  font-size: 1.6em;
}
#mapid {
  height: 100vh;
  width: 100%;
  z-index: 1;
}
</style>

