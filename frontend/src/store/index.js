import Vue from 'vue'
import Vuex from 'vuex'

import users from './modules/users'
import offices from './modules/offices'
import clients from './modules/clients'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    offices,
    clients
  }
})
