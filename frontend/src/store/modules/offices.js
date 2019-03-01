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
        code: office['code'],
        name: office['name'],
        employees: office['employees'],
        status: office['is_active']
      })
    })
    return offices
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
      code: null,
      name: null,
      employees: null,
      is_active: true
    }
  }
}

const actions = {
  async getOffices ({ state }) {
    const response = await http.get('offices/')
    state.offices = response.data
  },
  async getOffice ({ commit, state }, id) {
    commit('cleanData')
    const response = await http.get(`offices/${id}/`)
    state.office = response.data
  },
  async deleteOffice ({ dispatch }, id) {
    await http.delete(`offices/${id}/`)
    await dispatch('getOffices')
  },
  async addOffice ({ dispatch, commit, state }) {
    commit('cleanErrors')
    await http.post('offices/', state.office)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getOffices')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateOffice ({ dispatch, commit, state }) {
    commit('cleanErrors')
    await http.put(`offices/${state.office.code}/`, state.office)
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
