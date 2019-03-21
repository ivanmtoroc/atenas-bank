import axios from 'axios'
import router from '@/router'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const TOKEN = 'super_secure_token'
const USER = 'super_user'

const getUser = () => {
  if (!localStorage[USER]) {
    return { username: null, passwd: null }
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
  // eslint-disable-next-line
  authUser: state => state.user,
  position: state => state.user.position,
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
      nombre: null,
      email: null,
      id: null,
      posicion: null,
      username: null
    }
  }
}

const actions = {
  async login ({ commit, state }) {
    commit('cleanErrors')
    const response = await http.post('users/login/', state.user)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      state.user = response.data.user
      localStorage.setItem(USER, JSON.stringify(state.user))
      state.token = response.data.token
      localStorage.setItem(TOKEN, state.token)
      commit('cleanErrors')
      router.push({ name: 'home' })
    }
  },
  logout ({ getters }) {
    if (getters.logged) {
      router.push({ name: 'landing' })
    } else {
      router.push({ name: 'authentication' })
    }
    state.token = null
    localStorage.removeItem(TOKEN)
    localStorage.removeItem(USER)
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
