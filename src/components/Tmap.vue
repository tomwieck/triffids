<template>
  <div>
    <div id="mapid"></div>
  </div>
</template>

<script>
const lat = 51.44080;
const lng = -2.58889;
var mymap;
const testUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&facet=feature_type_name&facet=common_name`;
let trees = axios.get(testUrl)
  .then((resp) => {
      const list = resp.data.records.map((item, idx) => {
        return item.fields;
      })
      console.log(list);
      loadTrees(list);
  });

function loadTrees(trees) {
    mymap = L.map('mapid').setView([lat, lng], 16);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ'
    }).addTo(mymap);
    trees.forEach(t => {
      let marker = L.marker([t['geo_point_2d'][0], t['geo_point_2d'][1]]).addTo(mymap);
      marker.bindPopup(t['common_name']);
    });
}

// let tree1 = trees[0];
// console.log('Tree 1: ' + trees);
export default {
  data: () => {
    return {
      trees: trees
    }
  },
  mounted: function () {
  },
  name: 'Tmap',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#mapid {
  height: 100vh;
  width: 100%;
  z-index: 1;
}
</style>

