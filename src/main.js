import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueLogger from 'vuejs-logger'

Vue.config.productionTip = false

const isProduction = process.env.NODE_ENV === 'production'

// -- setup VueLogger
const options = {
  isEnabled: true,
  logLevel: isProduction ? 'error' : 'debug',
  stringifyArguments: false,
  showLogLevel: true,
  showMethodName: true,
  separator: '|',
  showConsoleColors: true
};
Vue.use(VueLogger, options);
// -- end setup


new Vue({
    render: h => h(App),
    router
}).$mount('#app')
