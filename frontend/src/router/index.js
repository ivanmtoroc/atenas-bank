import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'

import admin from './modules/admin'
import landing from './modules/landing'
import authentication from './modules/authentication'
import tickets from './modules/tickets'

import error404 from '@/components/errors/404'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...landing },
    { ...authentication },
    { ...admin },
    { ...tickets },
    {
      path: '*',
      component: error404
    }
  ]
})

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  const authUser = store.getters['authentication/authUser']
  switch (to.name) {
    case 'login':
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
        next({ name: 'login' })
      } else if (authUser.position === 'OP') {
        next({ name: 'operator' })
      } else if (authUser.tenant === 'public') {
        next()
      } else if (to.name === 'home' || to.name === 'users') {
        next()
      } else {
        next({ name: 'home' })
      }
      break
    case 'operator':
      if (authUser.position === 'MG') {
        next({ name: 'home' })
      } else {
        next()
      }
      break
    default:
      next()
  }
})

export default router
