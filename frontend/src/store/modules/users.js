import axios from 'axios'

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
  }
}

const mutations = {
  setUsers (state, users) {
    state.users = users
  }
}

const actions = {
  async getUsers ({ commit }) {
    this.loading = true
    const response = await axios.get('http://localhost:8000/users/')
    commit('setUsers', response.data)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
