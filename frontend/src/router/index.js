import Vue from 'vue'
import Router from 'vue-router'

import LandingPage from '@/components/bases/LandingPage'
import LoginBase from '@/components/bases/LoginBase'

import dashboardRouters from './dashboard-routes.js'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage
    },
    {
      path: '/login',
      name: 'login',
      component: LoginBase
    },
    { ...dashboardRouters },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
