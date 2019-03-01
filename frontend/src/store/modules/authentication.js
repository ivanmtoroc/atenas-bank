import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const TOKEN = 'super_secure_token'

const state = {
  token: localStorage[TOKEN],
  user: { username: null, passwd: null },
  errors: {},
  existsErrors: false
}

const getters = {
  logged: state => {
    // eslint-disable-next-line
    return !state.token ? false : true
  },
  user: state => state.user
}

const mutations = {
  setToken (state, data) {
    state.token = data.access_token
    state.user = data.user
    localStorage[TOKEN] = data.access_token
  },
  resetToken (state) {
    state.token = null
    state.user = { username: null, passwd: null }
    localStorage[TOKEN] = null
  },
  setErrors (state, errors) {
    state.errors = errors.response.data
    state.existsErrors = true
  }
}

const actions = {
  async login ({ commit, state }) {
    const response = await http.post('users/login/', state.user)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      commit('setToken', response.data)
    }
  },
  logout ({ commit }) {
    commit('resetToken')
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
