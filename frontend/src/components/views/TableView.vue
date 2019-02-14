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
                <vue-good-table
                  :columns="columns"
                  :rows="rows"
                  :line-numbers="true"
                  :search-options="{ enabled: true }"
                  :pagination-options="{ enabled: true }" />
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
import { VueGoodTable } from 'vue-good-table'

import 'vue-good-table/dist/vue-good-table.css'

export default {
  components: {
    VueGoodTable
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
