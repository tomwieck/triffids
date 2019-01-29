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
function parks(page = 1) {
  const url = `${config.localUrl}/parks?page=${page}`;
  return http.get(url)
    .then((resp) => {
      return resp.data;
    }, (err) => {
      throw err;
    });
}

function park(parkId) {
  const url = `${config.localUrl}/parks/${parkId}`;
  return http.get(url)
    .then((resp) => {
      return resp.data[0];
    }, (err) => {
      throw err;
    });
}