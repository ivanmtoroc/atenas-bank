import axios from 'axios'
import router from '@/router'

var http = null

const updateHttp = (domain) => {
  http = axios.create({
    baseURL: `http://${domain === 'public' ? 'localhost' : `${domain}.localhost`}:8000`
  })
}

const TOKEN = 'super_secure_token'
const USER = 'super_user'
const TENANT = 'tenant'

const getUser = () => {
  if (!localStorage[USER]) {
    return { username: null, password: null }
  } else {
    return JSON.parse(localStorage[USER])
  }
}

const state = {
  token: localStorage.getItem(TOKEN),
  user: getUser(),
  errors: {},
  existsErrors: false
}

const getters = {
  logged: state => {
    // eslint-disable-next-line
    return !state.token ? false : true
  },
  authUser: state => {
    state.user.tenant = localStorage.getItem(TENANT)
    return state.user
  },
  errors: state => state.errors,
  token: state => state.token
}

const mutations = {
  setErrors (state, errors) {
    state.errors = errors.response.data
    state.existsErrors = true
  },
  cleanErrors (state) {
    state.errors = {}
    state.existsErrors = false
  },
  cleanData (state) {
    state.errors = {}
    state.existsErrors = false
    state.user = {
      id: null,
      identification: null,
      name: null,
      email: null,
      position: null,
      username: null,
      tenant: null
    }
  }
}

const actions = {
  async login ({ commit, state }) {
    commit('cleanErrors')
    updateHttp(state.user.tenant)
    const response = await http.post('users/login/', state.user)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      localStorage.setItem(TENANT, state.user.tenant)
      state.user = response.data.user
      localStorage.setItem(USER, JSON.stringify(state.user))
      state.token = response.data.token
      localStorage.setItem(TOKEN, state.token)
      commit('cleanErrors')
      router.push({ name: 'home' })
    }
  },
  logout ({ getters }) {
    router.push({ name: 'login' })
    state.token = null
    state.tenant = null
    localStorage.removeItem(TOKEN)
    localStorage.removeItem(USER)
    localStorage.removeItem(TENANT)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}
export { TOKEN }
