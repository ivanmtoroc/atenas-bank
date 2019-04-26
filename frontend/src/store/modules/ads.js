import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8000'
})

const state = {
  ads: [],
  ad: {},
  errors: {},
  existsErrors: false,
  formData: new FormData()
}

const getters = {
  ad: state => state.ad,
  errors: state => state.errors,
  ads: state => {
    var ads = []
    state.ads.forEach(ad => {
      ads.push({
        id: ad['id'],
        name: ad['name'],
        description: ad['description'],
        image: ad['image'],
        status: ad['is_active']
      })
    })
    return ads
  },
  formData: state => state.formData
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
      name: null,
      description: null,
      image: null,
      is_active: true
    }
  },
  buildRequest (state, file) {
    state.formData.append('image', file)
    state.formData.append('name', state.ad.name)
    state.formData.append('description', state.ad.description)
  }
}

const actions = {
  async getAds ({ state, getters }) {
    const response = await http.get('ads/')
    state.ads = response.data
  },
  async getAd ({ commit, state, getters }, id) {
    commit('cleanData')
    const response = await http.get(`ads/${id}/`)
    state.ad = response.data
  },
  async deleteAd ({ dispatch, getters }, id) {
    await http.delete(`ads/${id}/`)
    await dispatch('getAds')
  },
  async addAd ({ dispatch, commit, state, getters }, file) {
    commit('cleanErrors')
    commit('buildRequest', file)
    await http.post('ads/', state.formData)
      .catch(errors => commit('setErrors', errors))
    if (!state.existsErrors) {
      await dispatch('getAds')
      commit('closeModal', '#create')
      commit('cleanData')
    }
  },
  async updateAd ({ dispatch, commit, state, getters }, file) {
    commit('cleanErrors')
    commit('buildRequest', file)
    await http.put(`ads/${state.ad.id}/`, state.formData)
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
