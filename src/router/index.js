import Vue from 'vue'
import Router from 'vue-router'
// import Hello from '@/components/Hello'
import ParkPage from '../components/ParkPage.vue'
import List from '../components/List.vue'

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Parks',
      component: List,
    },
    {
      path: '/park/:id',
      name: 'Park',
      component: ParkPage,
      props: (route) => ({ name: route.query.title })
    }
  ]
})