import Vue from 'vue'
import {
  treeTypes
} from '../utils/TreeTypes'

export const treePhotoService = {
  getPhotoFor
}

const trees = treeTypes();

function getPhotoFor(name) {
  // Vue.$log.info('getPhotoFor: ', trees[name]);
  if (trees[name]) {
    return require(`../assets/trees/photos/${trees[name]['photo']}.jpg`);
  } else {
    return require('../assets/trees/photos/default.jpg');
  }
}