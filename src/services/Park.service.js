import http from '../utils/http'
import {
  config
} from '../utils/config'

export const parkService = {
  parks,
  park,
}


/**
 * return an array of parks found.
 *
 * empty if nothing found
 *
 * @param {string} site_code the code for the site
 */
function parks() {
  const url = `${config.localUrl}/allParkNames`;
  return http.get(url)
    .then((resp) => {
      return resp.data;
    }, (err) => {
      throw err;
    });
}

function park() {
  return {};
}
