<template>
    <div>
        <div id="mapid"></div>
        <h1>Map</h1>
    </div>
</template>

<script>
const lat = 51.44080;
const lng = -2.58889;
const testUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&facet=feature_type_name&facet=common_name`;
let trees = axios.get(testUrl)
  .then((resp) => {
      const l = resp.data.records.map((item, idx) => {
        return item.fields.geo_point_2d;
      })
    console.log(l);
  });
// let tree1 = trees[0];
// console.log('Tree 1: ' + trees);
export default {
  data: () => {
    return {
      trees: trees
    }
  },
  mounted: function () {
    const mymap = L.map('mapid').setView([lat, lng], 16);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiamFsYWxza2kiLCJhIjoiY2pvd3d3bm40MXcxczNrbzlyazB2ZDVobyJ9.wV99nDE6dCfGjMUrEIjgFQ'
    }).addTo(mymap);
    var marker = L.marker([51.44246819415003, -2.58468603740490]).addTo(mymap);
    marker.bindPopup("Hi, I'm a Scots Pine tree!").openPopup();
    marker = L.marker([51.43851539948433, -2.5838943269219232]).addTo(mymap);
    marker.bindPopup("Hi, I'm an Aspen tree!");
    marker = L.marker([51.439150727525785, -2.5870542824523888]).addTo(mymap);
    marker.bindPopup("Hi, I'm a Hollybush tree!");
    marker = L.marker([51.439650474460116, -2.588689907775596]).addTo(mymap);
    marker.bindPopup("Hi, I'm an Oak tree!");
  },
  name: 'Tmap',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
tmap {
  width: 100%;
  left: 0;
  top: 0;
}
#mapid {
  height: 400px;
  width: 600px;
}
</style>

