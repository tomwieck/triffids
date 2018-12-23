import http from '../utils/http'
import { config } from '../utils/config'
import Vue from 'vue';

export const treeService = {
  trees,
  tree,
}

// const ODBUrl = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=trees&q=site_code%3DVICTPA&rows=1000&facet=feature_type_name&facet=common_name`;
// const localUrl = `http://localhost:4242/server/getTrees/?siteCode="VICTPA"&lat=0&long=0`;

function loadTrees() {
  Vue.$log.info('Tree.service: loading trees: ', trees)
  return http.get(config.ODBUrl)
    .then((resp) => {
      const trees = resp.data.records.map((item) => {
        return item.fields;
      })
      return trees;
    }, (err) => {
      throw err;
    });
}

function trees() {
  return loadTrees();
}

function tree() {
  return {};
}