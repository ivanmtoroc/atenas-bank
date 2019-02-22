import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  users: [],
  currentUser: {},
  newUser: {
    username: '',
    identification: '',
    first_name: '',
    last_name: '',
    email: '',
    is_active: true,
    phone: '',
    address: '',
    position: '',
    passwd: '',
    passwd_confirmation: ''
  },
  columns: [
    { label: 'Full name', field: 'name' },
    { label: 'Username', field: 'username' },
    { label: 'Identification', field: 'id' },
    { label: 'Email', field: 'email' },
    { label: 'Position', field: 'position' },
    { label: 'Status', field: 'status', type: 'boolean', thClass: 'text-center' },
    { label: 'Actions', field: 'actions' }
  ]
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
  currentUser: state => state.currentUser
}

const mutations = {
  setUsers (state, users) {
    state.users = users
  },
  setUser (state, user) {
    state.currentUser = user
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
  async deleteUser ({ commit }, identification) {
    await http.delete(`users/${identification}/`)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
