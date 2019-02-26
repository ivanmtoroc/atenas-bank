import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  users: [],
  currentUser: {
    username: '',
    identification: '',
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    address: '',
    position: ''
  },
  newUser: {
    username: '',
    identification: '',
    first_name: '',
    last_name: '',
    email: '',
    phone: '',
    address: '',
    position: 'OP',
    passwd: '',
    passwd_confirmation: ''
  },
  columns: [
    { label: 'Full name', field: 'name' },
    { label: 'Username', field: 'username' },
    { label: 'Identification', field: 'id' },
    { label: 'Email', field: 'email' },
    { label: 'Position', field: 'position' },
    { label: 'Status', field: 'status', type: 'boolean' },
    { label: 'Actions', field: 'actions' }
  ],
  errors: {},
  existsErrors: false
}

const getters = {
  users: state => state.users,
  columns: state => state.columns,
  rows: state => {
    var rows = []
    state.users.forEach(user => {
      rows.push({
        name: `${user['first_name']} ${user['last_name']}`,
        username: user['username'],
        id: user['identification'],
        email: user['email'],
        position: user['position'],
        status: user['is_active']
      })
    })
    return rows
  },
  currentUser: state => state.currentUser,
  newUser: state => state.newUser,
  errors: state => state.errors
}

const mutations = {
  setUsers (state, users) {
    state.users = users
  },
  setUser (state, user) {
    state.currentUser = user
  },
  closeModal (state, modalName) {
    // eslint-disable-next-line
    $(modalName).modal('hide')
  },
  cleanData (state) {
    state.errors = {}
    state.existsErrors = false
    state.newUser = {
      username: '',
      identification: '',
      first_name: '',
      last_name: '',
      email: '',
      phone: '',
      address: '',
      position: 'OP',
      passwd: '',
      passwd_confirmation: ''
    }
    state.currentUser = {
      username: '',
      identification: '',
      first_name: '',
      last_name: '',
      email: '',
      phone: '',
      address: '',
      position: ''
    }
  },
  setErrors (state, errors) {
    state.errors = errors.response.data
    state.existsErrors = true
  }
}

const actions = {
  async getUsers ({ commit }) {
    const response = await http.get('users/')
    commit('setUsers', response.data)
  },
  async getUser ({ commit }, identification) {
    const response = await http.get(`users/${identification}/`)
    commit('setUser', response.data)
  },
  async deleteUser ({ dispatch, commit }, identification) {
    await http.delete(`users/${identification}/`)
    await dispatch('getUsers')
  },
  async addUser ({ dispatch, commit, state }) {
    await http.post('users/', state.newUser)
      .catch(errors => {
        commit('setErrors', errors)
      })
    if (!state.existsErrors) {
      commit('closeModal', '#modal-create')
      await dispatch('getUsers')
      commit('cleanData')
    }
  },
  async updateUser ({ dispatch, commit, state }) {
    await http.put(`users/${state.currentUser.identification}/`, state.currentUser)
      .catch(errors => {
        commit('setErrors', errors)
      })
    if (!state.existsErrors) {
      commit('closeModal', '#modal-update')
      await dispatch('getUsers')
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
