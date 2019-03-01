<template>
  <div id="create" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Create client</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addClient()">
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.identification ? 'has-error' : '']">
                <label for="identification-create">Identification</label>
                <input id="identification-create" placeholder="Identification" v-model="client.identification" type="text" class="form-control" required="required">
                <p v-for="error in errors.identification" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group checkbox">
                <label for="vip-create">
                <input id="vip-create" v-model="client.is_vip" type="checkbox"><span class="checkbox-material"><span class="check"></span></span>
              VIP</label>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name-create">First name</label>
                <input id="first_name-create" placeholder="First name" v-model="client.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name-create">Last name</label>
                <input id="last_name-create" placeholder="Last name" v-model="client.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email-create">Email</label>
                <input id="email-create" placeholder="Email" v-model="client.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group">
                <label for="address-create">Address</label>
                <input id="address-create" placeholder="Address" v-model="client.address" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="phone-create">Phone</label>
                <input id="phone-create" placeholder="Phone" v-model="client.phone" type="text" class="form-control" required="required">
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
    ...mapGetters('clients', ['client', 'errors'])
  },
  methods: {
    ...mapActions('clients', ['addClient'])
  }
}
</script>
