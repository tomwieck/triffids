import http from '../utils/http'
import Vue from 'vue';

export const parkService = {
    parks,
    park,
    nearestParks
}

/**
 * return an array of parks found.
 *
 * empty if nothing found
 */
function parks(page = 1) {
    const url = `${Vue.config.API_URL}/parks?page=${page}`;
    return http.get(url)
        .then((resp) => {
            return resp.data;
        }, (err) => {
            throw err;
        });
}

function park(parkId) {
    const url = `${Vue.config.API_URL}/parks/${parkId}`;
    return http.get(url)
        .then((resp) => {
            return resp.data[0];
        }, (err) => {
            throw err;
        });
}

function nearestParks(page = 1, lat = 0, lng = 0, rad = 1000) {
    const url = `${Vue.config.API_URL}/parks?lat=${lat}&lng=${lng}&rad=${rad}`;
    return http.get(url)
        .then((resp) => {
            return resp.data
        }, (err) => {
            throw err;
        })
}