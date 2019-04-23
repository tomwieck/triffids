import http from '../utils/http'
import Vue from 'vue';

export const parkService = {
    parks,
    park,
    nearestParks,
    parkInfo
}

/**
 * return an array of parks found.
 *
 * empty if nothing found
 */
function parks(page = 1) {
    const url = `http://127.0.0.1:5000/api/v1/parks?page=${page}`;
    return http.get(url)
        .then((resp) => {
            return resp.data;
        }, (err) => {
            throw err;
        });
}

/**
 * return information about this park
 *
 * includes geometry, center, name and number of trees total/unique
 *
 * @param {string} parkId to lookup
 */
function park(parkId) {
    const url = `${Vue.config.API_URL}/parks/${parkId}`;
    return http.get(url)
        .then((resp) => {
            return resp.data;
        }, (err) => {
            throw err;
        });
}

/**
 * get a list of the nearest parks
 *
 * @param {number} page number for pagination
 * @param {string} lat latitude
 * @param {string} lng longitude
 * @param {number} rad within this radius, default 300m
 */
function nearestParks(page = 1, lat = 0, lng = 0, rad = 3000) {
    const url = `${Vue.config.API_URL}/parks?lat=${lat}&lng=${lng}&rad=${rad * page}`;
    return http.get(url)
        .then((resp) => {
            return resp.data
        }, (err) => {
            throw err;
        })
}

/**
 * return information about this park
 *
 * returns an HTML file from `data/parkinfo/`
 *
 * @param {string} parkId to lookup
 */
function parkInfo(parkId) {
    const url = `${Vue.config.API_URL}/parks/info/${parkId}`;
    return http.get(url)
        .then((resp) => {
            return resp.data
        }, (err) => {
            throw err;
        })
}
