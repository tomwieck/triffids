import http from '../utils/http'
import {
  config
} from '../utils/config'
import Vue from 'vue';

export const treeService = {
  count,
  unique,
  trees,
  tree,
}

// const ODBUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&rows=1000&facet=feature_type_name&facet=common_name`;
// const localUrl = `http://localhost:4242/server/getTrees/?siteCode="VICTPA"&lat=0&long=0`;

// https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DDURDDO&rows=0

/**
 * get the count of trees for this park.
 *
 * this will return 0 if the site_code is not found
 *
 * @param {string} site_code the code for the site
 * @return number the count of trees found
 */
function count(site_code) {
  return http.get(`${config.ODBTreesUrl}&q=site_code%3D${site_code}&rows=0`)
    .then((resp) => {
      return resp.data.nhits;
    }, (err) => {
      throw err;
    });
}

/**
 * get the count of tree species for this park.
 *
 * this is based on the Latin Code of the trees.
 * this will return 0 if the site_code is not found
 *
 * @param {string} site_code the code for the site
 * @return number the count of tree species found
 */
function unique(site_code) {
  return http.get(`${config.ODBTreesUrl}&q=site_code%3D${site_code}&rows=0&facet=latin_code`)
    .then((resp) => {
      return resp.data.facet_groups[0].facets.length;
    }, (err) => {
      throw err;
    });
}

/**
 * return an array of records for the trees found.
 *
 * empty if nothing found
 *
 * @param {string} site_code the code for the site
 */
function trees(site_code) {
  // Vue.$log.info('Tree.service: loading trees: ', trees)
  const url = `${config.ODBTreesUrl}&q=site_code%3D${site_code}&rows=1000&facet=feature_type_name&facet=common_name`;
  Vue.$log.info('Tree.service: loading trees: ', url)
  return http.get(url)
    .then((resp) => {
      const trees = resp.data.records.map((item) => {
        return item.fields;
      })
      return trees;
    }, (err) => {
      throw err;
    });
}

function tree() {
  return {};
}