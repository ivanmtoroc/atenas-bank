import Vue from 'vue'
import Vuex from 'vuex'

import users from './modules/users'
import authentication from './modules/authentication'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    users,
    authentication
  }
})
