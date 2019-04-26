import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  offices: [],
  office: {},
  errors: {},
  existsErrors: false
}

const getters = {
  office: state => state.office,
  errors: state => state.errors,
  offices: state => {
    var offices = []
    state.offices.forEach(office => {
      offices.push({
        id: office['id'],
        name: office['name'],
        schema_name: office['schema_name'],
        status: office['is_active']
      })
    })
    return offices
  },
  tenantOffices: state => {
    var offices = []
    state.offices.forEach(office => {
      if (office['schema_name'] !== 'public') {
        offices.push({
          id: office['id'],
          name: office['name'],
          schema_name: office['schema_name'],
          status: office['is_active']
        })
      }
    })
    return offices
  },
  headers: (state, getters, rootGetters) => {
    return { headers: { Authorization: 'Token ' + rootGetters.authentication.token } }
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
    state.office = {
      id: null,
      name: null,
      schema_name: null,
      is_active: true
    }
  }
}

const actions = {
  async getOffices ({ commit, state, getters }) {
    const response = await http.get('offices/')
    state.offices = response.data
  },
  async getOffice ({ commit, state, getters }, id) {
    commit('cleanData')
    const response = await http.get(`offices/${id}/`, getters.headers)
    state.office = response.data
  },
  async deleteOffice ({ dispatch, getters }, id) {
    await http.delete(`offices/${id}/`, getters.headers)
    await dispatch('getOffices')
  },
  async addOffice ({ dispatch, commit, state, getters }) {
    commit('cleanErrors')
    await http.post('offices/', state.office, getters.headers)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getOffices')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateOffice ({ dispatch, commit, state, getters }) {
    commit('cleanErrors')
    await http.put(`offices/${state.office.id}/`, state.office, getters.headers)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getOffices')
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
