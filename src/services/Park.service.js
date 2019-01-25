import http from '../utils/http'
import {
  config
} from '../utils/config'

export const parkService = {
  parks,
  park,
}

let page  = 1;

/**
 * return an array of parks found.
 *
 * empty if nothing found
 *
 * @param {string} site_code the code for the site
 */
function parks() {
  const url = `${config.localUrl}/parks?page=${page}`;
  return http.get(url)
    .then((resp) => {
      page++;
      return resp.data;
    }, (err) => {
      throw err;
    });
}

function park() {
  return {};
}
