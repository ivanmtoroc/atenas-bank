import axios from 'axios'

const state = {
  users: [],
  currentUser: {},
  newUser: {
    username: null,
    identification: null,
    fullname: null,
    email: null,
    is_active: true,
    position: 'Operator',
    phone: null,
    address: null,
    password1: null,
    password2: null
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
    const response = await axios.get('https://swapi.co/api/people/')
    commit('setUsers', response.data.results)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
