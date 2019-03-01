import Vue from 'vue'
import Vuex from 'vuex'

import users from './modules/users'
import authentication from './modules/authentication'
import offices from './modules/offices'
import clients from './modules/clients'
import ads from './modules/ads'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    authentication,
    offices,
    clients,
    ads
  }
})
