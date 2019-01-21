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

/**
 * return details of this park
 * 
 * using opendata url for now as the local server is not working yet...
 * https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=parks-and-greens-spaces&q=site_code%3DSTPACHSO
 *
 * @param {string} pcode the site_code for the park
 */
function park(pcode) {
  // const url = `${config.localUrl}/getPark/${pcode}`;
  const url = `https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=parks-and-greens-spaces&q=site_code=${pcode}`;
  return http.get(url)
    .then((resp) => {
      return resp.data;
    }, (err) => {
      throw err;
    });
}