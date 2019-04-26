import axios from 'axios'

var http = null

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
        id: user['id'],
        identification: user['identification'],
        name: `${user['first_name']} ${user['last_name']}`,
        username: user['username'],
        email: user['email'],
        position: user['position'] === 'OP' ? 'Operator' : 'Manager',
        status: user['is_active']
      })
    })
    return users
  },
  headers: (state, getters, rootGetters) => {
    return { headers: { Authorization: 'Token ' + rootGetters.authentication.token } }
  },
  tenant: (state, getters, rootGetters) => {
    return rootGetters.authentication.user.tenant
  }
}

const mutations = {
  updateTable () {
    // eslint-disable-next-line
    $('#table').DataTable().draw()
  },
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
      id: null,
      username: null,
      identification: null,
      first_name: null,
      last_name: null,
      email: null,
      is_active: true,
      phone: null,
      address: null,
      position: null,
      password: null,
      password_confirmation: null,
      tenant: null
    }
  },
  updateHttp: (state, domain) => {
    http = axios.create({
      baseURL: `http://${domain === 'public' ? 'localhost' : `${domain}.localhost`}:8000`
    })
  }
}

const actions = {
  async getUsers ({ state, commit, getters }) {
    const response = await http.get('users/', getters.headers)
    state.users = response.data
  },
  async getUser ({ commit, state, getters }, id) {
    commit('cleanData')
    const response = await http.get(`users/${id}/`, getters.headers)
    state.user = response.data
  },
  async deleteUser ({ dispatch, getters }, id) {
    await http.delete(`users/${id}/`, getters.headers)
    await dispatch('getUsers')
  },
  async addUser ({ dispatch, commit, state, getters }) {
    commit('cleanErrors')
    if (getters.tenant === 'public' && state.user.tenant !== 'public') {
      commit('updateHttp', state.user.tenant)
    }
    await http.post('users/', state.user, getters.headers)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getUsers')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateUser ({ dispatch, commit, state, getters }) {
    commit('cleanErrors')
    await http.put(`users/${state.user.id}/`, state.user, getters.headers)
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
