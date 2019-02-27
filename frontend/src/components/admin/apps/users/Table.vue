<template>
  <div>
    <section class="content-header">
      <div class="list-inline"><h1>Users</h1></div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'admin' }">
            <span>Home</span>
          </router-link>
        </li>
        <li class="active">Users</li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <div class="row">
                <div class="col-sm-12">
                  <a @click="cleanData()" href="#create" class="btn bg-olive" data-toggle="modal" data-target="#create">Create new user</a>
                  <table id="table" class="table table-bordered table-striped dataTable" role="grid">
                    <vue-good-table :columns="columns" :rows="rows" :line-numbers="true" :search-options="{ enabled: true }" :pagination-options="{ enabled: true }">
                      <template slot="table-row" slot-scope="props">
                        <span v-if="props.column.field == 'status'">
                          <p v-if="props.row.status" class="badge bg-green p-bg">Active</p>
                          <p v-else class="badge bg-red p-bg">Inactive</p>
                        </span>
                        <span v-else-if="props.column.field == 'actions'">
                          <a @click="getUser(props.row.id)" href="#delete" class="btn.btn-app btn-sm action-btn" :class="[props.row.status ? 'btn-danger' : 'btn-success']" data-toggle="modal" data-target="#delete">
                            <i v-if="props.row.status" class="fa fa-user-times"></i>
                            <i v-else class="fa fa-user-plus"></i>
                          </a>
                          <a @click="getUser(props.row.id)" href="#update" class="btn.btn-app btn-primary btn-sm action-btn" data-toggle="modal" data-target="#update">
                            <i class="fa fa-edit"></i>
                          </a>
                          <a @click="getUser(props.row.id)" href="#read" class="btn.btn-app btn-info btn-sm action-btn" data-toggle="modal" data-target="#read">
                            <i class="fa fa-info-circle"></i>
                          </a>
                        </span>
                        <span v-else>
                          {{ props.formattedRow[props.column.field] }}
                        </span>
                      </template>
                    </vue-good-table>
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
import { VueGoodTable } from 'vue-good-table'
import Create from './modals/Create'
import Delete from './modals/Delete'
import Read from './modals/Read'
import Update from './modals/Update'

import 'vue-good-table/dist/vue-good-table.css'

export default {
  components: {
    VueGoodTable,
    Create,
    Delete,
    Read,
    Update
  },
  computed: {
    ...mapGetters('users', ['columns', 'rows'])
  },
  methods: {
    ...mapActions('users', ['getUsers', 'getUser']),
    ...mapMutations('users', ['cleanData'])
  },
  mounted () {
    this.getUsers()
  }
}
</script>
