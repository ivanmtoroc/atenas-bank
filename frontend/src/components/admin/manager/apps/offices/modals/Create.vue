<template>
  <div id="create" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Create office</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addOffice()">
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.name ? 'has-error' : '']">
                <label for="name-create">Name</label>
                <input id="name-create" placeholder="Name" v-model="office.name" type="text" class="form-control" required="required">
                <p v-for="error in errors.name" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.schema_name ? 'has-error' : '']">
                <label for="schema-name-create">Schema name</label>
                <input id="schema-name-create" placeholder="Schema name" v-model="office.schema_name" type="text" class="form-control" required="required">
                <p v-for="error in errors.schema_name" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="pull-right">
              <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
              <button type="submit" class="btn btn-success">Save</button>
            </div>
          </form>
        </div>
        <div class="modal-footer"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('offices', ['office', 'errors'])
  },
  methods: {
    ...mapActions('offices', ['addOffice'])
  }
}
</script>
