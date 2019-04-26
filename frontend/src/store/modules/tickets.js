import axios from 'axios'
import router from '@/router'

var http = null

const updateHttp = (domain) => {
  http = axios.create({
    baseURL: `http://${domain}.localhost:8000`
  })
}

var WS = null

const updateWS = (domain) => {
  WS = `ws://localhost:8000/${domain}`
}

const state = {
  ticket: {
    tenant: null
  },
  identification: '',
  webSocket: null,
  currentTicket: {
    turn_number: '',
    user: ''
  },
  listView: false
}

const getters = {
  identification: state => state.identification,
  ticket: state => state.ticket,
  currentTicket: state => state.currentTicket
}

const mutations = {
  initWSConection (state, tenant) {
    updateWS(tenant)
    state.webSocket = new WebSocket(WS)
  },
  cleanData (state) {
    state.ticket = {}
    state.identification = ''
  },
  cleanTicket (state) {
    state.currentTicket = {
      turn_number: '',
      user: ''
    }
  },
  setView (state) {
    state.listView = true
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
  async getTicket ({ state, getters }) {
    updateHttp(state.ticket.tenant)
    state.ticket.user = state.identification
    const response = await http.post('tickets/', state.ticket)
    state.currentTicket = response.data
    router.push({ name: 'ticket' })
  },
  send ({ state, rootGetters }, service) {
    state.webSocket.send(JSON.stringify({
      'service': service,
      'operator': rootGetters['authentication/authUser']['id'],
      'tenant': rootGetters['authentication/authUser']['tenant']
    }))
  },
  retrieve ({ state, rootGetters }) {
    state.webSocket.onmessage = (response) => {
      const data = JSON.parse(response.data)
      if (data['operator'] === rootGetters['authentication/authUser']['id'] || state.listView) {
        if (data['status']) {
          state.currentTicket = data['ticket']
        } else {
          state.currentTicket = {
            turn_number: '',
            user: ''
          }
        }
      }
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
