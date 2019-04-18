import Vue from 'vue'
import Vuex from 'vuex'
import parks from './modules/parks'
import trees from './modules/trees'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    parks,
    trees
  },
  strict: debug,
})