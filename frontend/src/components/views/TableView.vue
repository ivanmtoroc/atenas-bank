<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="box">
        <div class="box-body">
          <div class="row">
            <div class="col-sm-12">
              <a href="#modal-create" class="btn bg-olive margin" data-toggle="modal" data-target="#modal-create">Create user</a>
              <table id="table" class="table table-bordered table-striped dataTable" role="grid">
                <vue-good-table
                :columns="columns"
                :rows="rows"
                :line-numbers="true"
                :search-options="{ enabled: true }"
                :pagination-options="{ enabled: true }">
                <template slot="table-row" slot-scope="props">
                  <span v-if="props.column.field == 'status'">
                    <p v-if="props.row.status" class="badge bg-green p-bg">Active</p>
                    <p v-else class="badge bg-red p-bg">Inactive</p>
                  </span>
                  <span v-else-if="props.column.field == 'actions'">
                    <a @click="getUser(props.row.id)" href="#modal-delete" class="btn.btn-app btn-sm btns" :class="[props.row.status ? 'btn-danger' : 'btn-success']" data-toggle="modal" data-target="#modal-delete">
                      <span v-if="props.row.status">
                        <i class="fa fa-user-times"></i>
                      </span>
                      <span v-else>
                        <i class="fa fa-user-plus"></i>
                      </span>
                    </a>
                    <a href="#modal-update" class="btn.btn-app btn-primary btn-sm btns" data-toggle="modal" data-target="#modal-update">
                      <i class="fa fa-edit"></i>
                    </a>
                    <a @click="getUser(props.row.id)" href="#modal-read" class="btn.btn-app btn-info btn-sm btns" data-toggle="modal" data-target="#modal-read">
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
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { VueGoodTable } from 'vue-good-table'

import 'vue-good-table/dist/vue-good-table.css'

export default {
  components: {
    VueGoodTable
  },
  computed: {
    ...mapGetters('users', ['columns', 'rows'])
  },
  methods: {
    ...mapActions('users', ['getUsers', 'getUser'])
  },
  mounted () {
    this.getUsers()
  }
}
</script>

<style>
.btns {
  margin: 0px 3px;
}
</style>
