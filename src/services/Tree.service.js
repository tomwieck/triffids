import http from '../utils/http'
import {
  config
} from '../utils/config'

export const treeService = {
  trees,
  tree,
}

// const ODBUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&rows=1000&facet=feature_type_name&facet=common_name`;
// const localUrl = `http://localhost:4242/server/getTrees/?siteCode="VICTPA"&lat=0&long=0`;

// https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DDURDDO&rows=0

/**
 * return an array of records for the trees found.
 *
 * empty if nothing found
 *
 * @param {string} site_code the code for the site
 */
function trees(site_code) {
  // Vue.$log.info('Tree.service: loading trees: ', trees)
  // const url = `${config.ODBTreesUrl}&q=site_code%3D${site_code}&rows=1000&facet=feature_type_name&facet=common_name`;
  const url = `${config.localUrl}/trees/${site_code}`;

  return http.get(url)
    .then((resp) => {
      return resp.data
    }, (err) => {
      throw err;
    });
}

function tree(treeId) {
  const url = `${config.localUrl}/tree/${treeId}`;

  return http.get(url)
    .then((resp) => {
      return resp.data
    }, (err) => {
      throw err;
    });
}