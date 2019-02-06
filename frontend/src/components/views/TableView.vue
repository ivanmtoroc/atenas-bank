<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="box">
        <div class="box-header">
          <h3 class="box-title">Table title</h3>
        </div>
        <div class="box-body">
          <div class="row">
            <div class="col-sm-12">
              <table id="table" class="table table-bordered table-striped dataTable" role="grid">
                <thead>
                  <table-columns></table-columns>
                </thead>
                <tbody>
                  <table-rows></table-rows>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import TableColumns from '@/components/views/TableColumns.vue'
import TableRows from '@/components/views/TableRows.vue'

export default {
  components: {
    TableColumns,
    TableRows
  },
  computed: {
    ...mapState('users', ['users'])
  },
  methods: {
    ...mapActions('users', ['getUsers'])
  },
  mounted () {
    this.getUsers()
  }
}
</script>
