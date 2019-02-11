import http from '../utils/http'
import Vue from 'vue';

export const treeService = {
    trees,
    tree,
}

/**
 * return an array of records for the trees found.
 *
 * empty if nothing found
 *
 * @param {string} site_code the code for the site
 */
function trees(site_code) {
    const url = `${Vue.config.API_URL}/trees/${site_code}`;

    Vue.$log.info('Tree.service: loading trees: ', url)
    return http.get(url)
        .then((resp) => {
            return resp.data
        }, (err) => {
            throw err;
        });
}

function tree(treeId) {
    const url = `${Vue.config.API_URL}/tree/${treeId}`;

    return http.get(url)
        .then((resp) => {
            return resp.data
        }, (err) => {
            throw err;
        });
}