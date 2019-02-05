import Vue from 'vue'
import Router from 'vue-router'

import DashboardBase from '@/bases/DashboardBase.vue'
import LoginBase from '@/bases/LoginBase.vue'
import Error404 from '@/bases/Error404.vue'

// import HomeView from '@/views/HomeView.vue'
import TableView from '@/views/TableView.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '*',
      name: '404',
      component: Error404
    },
    {
      path: '/login',
      name: 'login',
      component: LoginBase
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardBase,
      children: [
        {
          path: 'users',
          name: 'users',
          component: TableView
        }
      ]
    }
  ]
})
