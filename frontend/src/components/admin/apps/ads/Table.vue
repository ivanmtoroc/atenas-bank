<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Ads
          <a @click="cleanData()" href="#create" class="btn btn-primary btn-raised" data-toggle="modal" data-target="#create">
            + New ads
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">
            <span>Home</span>
          </router-link>
        </li>
        <li class="active">Ads</li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <div class="row">
                <div class="col-sm-12">
                  <table id="table" class="table table-bordered table-striped dataTable" role="grid">
                    <thead>
                      <tr role="row">
                        <th class="sorting_asc" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Name</th>
                        <th class="sorting_asc" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Description</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Status</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="ad in ads" role="row" class="odd">
                        <td>{{ ad.name }}</td>
                        <td>{{ ad.description }}</td>
                        <td class="text-center">
                          <p v-if="ad.status" class="badge bg-green p-bg">Active</p>
                          <p v-else class="badge bg-red p-bg">Inactive</p>
                        </td>
                        <td class="text-center">
                          <a @click="getAd(ad.id)" href="#delete" class="btn.btn-app btn-sm action-btn" :class="[ad.status ? 'btn-danger' : 'btn-success']" data-toggle="modal" data-target="#delete">
                            <i v-if="ad.status" class="fa fa-user-times"></i>
                            <i v-else class="fa fa-user-plus"></i>
                          </a>
                          <a @click="getAd(ad.id)" href="#update" class="btn.btn-app btn-primary btn-sm action-btn" data-toggle="modal" data-target="#update">
                            <i class="fa fa-edit"></i>
                          </a>
                          <a @click="getAd(ad.id)" href="#read" class="btn.btn-app btn-info btn-sm action-btn" data-toggle="modal" data-target="#read">
                            <i class="fa fa-info-circle"></i>
                          </a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <create></create>
    <delete></delete>
    <read></read>
    <update></update>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import Create from './modals/Create'
import Delete from './modals/Delete'
import Read from './modals/Read'
import Update from './modals/Update'

export default {
  components: {
    Create,
    Delete,
    Read,
    Update
  },
  computed: {
    ...mapGetters('ads', ['ads'])
  },
  methods: {
    ...mapActions('ads', ['getAds', 'getAd']),
    ...mapMutations('ads', ['cleanData', 'dataTable'])
  },
  beforeMount () {
    this.getAds()
  },
  beforeUpdate () {
    this.dataTable()
  }
}
</script>
