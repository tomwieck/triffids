import Vue from 'vue'
import Vuex from 'vuex'
import state from './state'
import actions from './actions'
import mutations from './mutations'
import getters from './getters'

import boostrapDataPlugin from '../services/bootstrap-park-data'


Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  state: state,
  actions,
  mutations,
  getters,
  plugins: [
  	boostrapDataPlugin,
  ],
  strict: debug,
})
