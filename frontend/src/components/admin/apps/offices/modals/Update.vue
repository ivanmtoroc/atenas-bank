<template>
  <div id="update" class="modal fade update" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Update Office</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="updateOffice()">
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="code-update">Code</label>
                <input id="code-update" placeholder="Code" v-model="office.code" type="text" class="form-control" required="required" readonly>
              </div>
              <div class="col-md-6 form-group">
                <label for="name-update">Name</label>
                <input id="name-update" placeholder="Name" v-model="office.name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="employees-update">Employees</label>
                <input id="employees-update" placeholder="Employees" v-model="office.employees" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="pull-right">
              <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
              <button type="submit" class="btn btn-primary">Update</button>
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
    ...mapActions('offices', ['updateOffice'])
  }
}
</script>
