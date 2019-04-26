import axios from 'axios'

var http = null

const state = {
  service: '',
  operatorState: 1
}

const getters = {
  service: state => state.service,
  operatorState: state => state.operatorState
}

const mutations = {
  setService (state, service) {
    state.service = service
  },
  setState (state, newState) {
    state.operatorState = newState
  },
  updateHttp (state, domain) {
    http = axios.create({
      baseURL: `http://${domain === 'public' ? 'localhost' : `${domain}.localhost`}:8000`
    })
  }
}

const actions = {
  async initAttention ({ commit, state }, id) {
    await http.get(`tickets/${id}/init_attention`)
    commit('setState', 3)
  },
  async finishAttention ({ commit, state }, id) {
    await http.get(`tickets/${id}/finish_attention`)
    commit('setState', 1)
  },
  async defer ({ commit, state }, id) {
    await http.get(`tickets/${id}/defer`)
    commit('setState', 1)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
