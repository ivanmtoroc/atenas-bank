import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  ticket: {},
  identification: ''
}

const getters = {
  ticket: state => state.ticket,
  identification: state => state.identification
}

const mutations = {
  cleanData (state) {
    state.ticket = {}
    state.identification = ''
  },
  setService (state, service) {
    state.ticket.service = service
  },
  change (state, value) {
    if (value === 'DEL') {
      state.identification = state.identification.slice(0, -1)
    } else if (state.identification.length < 10) {
      state.identification += value
    }
  }
}

const actions = {
  async getTicket ({ state }) {
    state.ticket.identification = state.identification
    await http.post('tickets/', state.ticket)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
