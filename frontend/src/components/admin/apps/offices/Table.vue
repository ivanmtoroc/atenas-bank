<template>
      <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Offices
          <a @click="cleanData()" href="#create" class="btn btn-primary btn-raised" data-toggle="modal" data-target="#create">
            + New Office
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">
            <span>Home</span>
          </router-link>
        </li>
        <li class="active">Offices</li>
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
                        <th class="sorting_asc" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Code</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Name</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Employees</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Status</th>
                        <th class="sorting" tabindex="0" aria-controls="table" rowspan="1" colspan="1">Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="office in offices" role="row" class="odd">
                        <td>{{ office.code }}</td>
                        <td>{{ office.name }}</td>
                        <td>{{ office.employees }}</td>
                        <td class="text-center">
                          <p v-if="office.status" class="badge bg-green p-bg">Active</p>
                          <p v-else class="badge bg-red p-bg">Inactive</p>
                        </td>
                        <td class="text-center">
                          <a @click="getOffice(office.code)" href="#delete" class="btn.btn-app btn-sm action-btn" :class="[office.status ? 'btn-danger' : 'btn-success']" data-toggle="modal" data-target="#delete">
                            <i v-if="office.status" class="fa fa-user-times"></i>
                            <i v-else class="fa fa-user-plus"></i>
                          </a>
                          <a @click="getOffice(office.code)" href="#update" class="btn.btn-app btn-primary btn-sm action-btn" data-toggle="modal" data-target="#update">
                            <i class="fa fa-edit"></i>
                          </a>
                          <a @click="getOffice(office.code)" href="#read" class="btn.btn-app btn-info btn-sm action-btn" data-toggle="modal" data-target="#read">
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
    ...mapGetters('offices', ['offices'])
  },
  methods: {
    ...mapActions('offices', ['getOffices', 'getOffice']),
    ...mapMutations('offices', ['cleanData', 'dataTable'])
  },
  beforeMount () {
    this.getOffices()
  },
  beforeUpdate () {
    this.dataTable()
  }
}
</script>
