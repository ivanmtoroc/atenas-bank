import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  ads: [],
  ad: {},
  errors: {},
  existsErrors: false
}

const getters = {
  ad: state => state.ad,
  errors: state => state.errors,
  ads: state => {
    var ads = []
    state.ads.forEach(ad => {
      ads.push({
        id: ad['id'],
        description: ad['description'],
        image: ad['image'],
        status: ad['is_active']
      })
    })
    return ads
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
    state.ad = {
      id: null,
      description: null,
      image: null,
      is_active: true
    }
  }
}

const actions = {
  async getAds ({ state }) {
    const response = await http.get('ads/')
    state.ads = response.data
  },
  async getAd ({ commit, state }, id) {
    commit('cleanData')
    const response = await http.get(`ads/${id}/`)
    state.ad = response.data
  },
  async deleteAd ({ dispatch }, id) {
    await http.delete(`ads/${id}/`)
    await dispatch('getAds')
  },
  async addAd ({ dispatch, commit, state }) {
    commit('cleanErrors')
    await http.post('ads/', state.ad)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getAds')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateAd ({ dispatch, commit, state }) {
    commit('cleanErrors')
    await http.put(`ads/${state.ad.identification}/`, state.ad)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getAds')
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
