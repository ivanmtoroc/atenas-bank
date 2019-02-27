import Vue from 'vue'
import Router from 'vue-router'

import admin from './modules/admin'
import landing from './modules/landing'
import authentication from './modules/authentication'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...landing },
    { ...authentication },
    { ...admin },
    { path: '*', redirect: '/' }
  ]
})
