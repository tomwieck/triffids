import L from 'leaflet'

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

// name of icon file only here, then we can switch folder, filetype easily.
const treeTypes = {
  'Lime': 'lime',
  'Hawthorn': 'hawthorn',
  'Horse Chestnut': 'chestnut',
  'Beech': 'beech',
  'Ash': 'ash',
  'Sycamore': 'sycamore',
  'Oak': 'oak',
  'Silver Birch': 'silverbirch',
  'Elder': 'elder',
  'Holly': 'holly',
  'Maple': 'maple',
}

function getIconFor(name) {
  if (treeTypes[name]) {
    return new TreeIcon({ iconUrl: require(`../assets/trees/${treeTypes[name]}.svg`) });
  } else {
    return new TreeIcon({ iconUrl: require('../assets/trees/generic.svg') });
  }
}

// attribution for icons:
// <div>Icons made by <a href="https://www.flaticon.com/authors/simpleicon" title="SimpleIcon">SimpleIcon</a> from <a href="https://www.flaticon.com/" 		    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 		    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
//
