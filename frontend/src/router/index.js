import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'

import admin from './modules/admin'
import landing from './modules/landing'
import authentication from './modules/authentication'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...landing },
    { ...authentication },
    { ...admin },
    { path: '*', redirect: '/' }
  ]
})

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  switch (to.name) {
    case 'authentication':
      if (logged) {
        next({ name: 'home' })
      } else {
        next()
      }
      break
    case 'home':
    case 'users':
    case 'offices':
    case 'clients':
    case 'ads':
      if (!logged) {
        next({ name: 'authentication' })
      } else {
        next()
      }
      break
    default:
      next()
  }
})

export default router
