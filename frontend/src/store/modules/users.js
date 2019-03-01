import axios from 'axios'
import { TOKEN } from './authentication'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  users: [],
  user: {},
  errors: {},
  existsErrors: false
}

const getters = {
  user: state => state.user,
  errors: state => state.errors,
  users: state => {
    var users = []
    state.users.forEach(user => {
      users.push({
        id: user['identification'],
        name: `${user['first_name']} ${user['last_name']}`,
        username: user['username'],
        email: user['email'],
        position: user['position'] === 'OP' ? 'Operator' : 'Manager',
        status: user['is_active']
      })
    })
    return users
  }
}

const mutations = {
  dataTable (state) {
    // eslint-disable-next-line
    $(function () { $('#table').DataTable() })
  },
  closeModal (state, modalName) {
    // eslint-disable-next-line
    $(modalName).modal('hide')
  },
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
      username: null,
      identification: null,
      first_name: null,
      last_name: null,
      email: null,
      is_active: true,
      phone: null,
      address: null,
      position: null,
      passwd: null,
      passwd_confirmation: null
    }
  }
}

const actions = {
  async getUsers ({ state }) {
    const headers = { Authorization: 'Token ' + localStorage[TOKEN] }
    const response = await http.get('users/', { headers })
    state.users = response.data
  },
  async getUser ({ commit, state }, id) {
    commit('cleanData')
    const headers = { Authorization: 'Token ' + localStorage[TOKEN] }
    const response = await http.get(`users/${id}/`, { headers })
    state.user = response.data
  },
  async deleteUser ({ dispatch }, id) {
    const headers = { Authorization: 'Token ' + localStorage[TOKEN] }
    await http.delete(`users/${id}/`, { headers })
    await dispatch('getUsers')
  },
  async addUser ({ dispatch, commit, state }) {
    commit('cleanErrors')
    const headers = { Authorization: 'Token ' + localStorage[TOKEN] }
    await http.post('users/', { headers }, state.user)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getUsers')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateUser ({ dispatch, commit, state }) {
    commit('cleanErrors')
    const headers = { Authorization: 'Token ' + localStorage[TOKEN] }
    await http.put(`users/${state.user.identification}/`, { headers }, state.user)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getUsers')
      commit('closeModal', '#update')
      commit('cleanData')
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
