import L from 'leaflet'
import {
  treeTypes
} from '../utils/TreeTypes'

export const treeIconService = {
  getIconFor
}

// base type for the tree icons, this size is an estimate for now.
var TreeIcon = L.Icon.extend({
  options: {
    iconSize: [24, 24],
    shadowSize: [24, 24],
    iconAnchor: [20, 12],
    shadowAnchor: [0, 0],
    popupAnchor: [-8, -14],
    className: 'treeicon'
  }
})

const trees = treeTypes();

function getIconFor(name) {
  if (trees[name]) {
    return new TreeIcon({
      iconUrl: require(`../assets/trees/icons/${trees[name]["icon"]}.svg`)
    });
  } else {
    return new TreeIcon({
      iconUrl: require('../assets/trees/icons/generic.svg')
    });
  }
}

// attribution for icons:
// <div>Icons made by <a href="https://www.flaticon.com/authors/simpleicon" title="SimpleIcon">SimpleIcon</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
//