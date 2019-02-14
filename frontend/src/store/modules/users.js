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
  },
  columns: [
    {
      label: 'Name',
      field: 'name'
    },
    {
      label: 'Age',
      field: 'age',
      type: 'number',
      html: true
    },
    {
      label: 'Created On',
      field: 'createdAt',
      type: 'date',
      dateInputFormat: 'YYYY-MM-DD',
      dateOutputFormat: 'MMM Do YY'
    },
    {
      label: 'Percent',
      field: 'score',
      type: 'percentage'
    }
  ],
  rows: [
    {
      id: 1,
      name: 'John',
      age: '<p class="badge bg-green p-bg">Active</p>',
      createdAt: '201-10-31:9: 35 am',
      score: 0.03343
    }
  ]
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
