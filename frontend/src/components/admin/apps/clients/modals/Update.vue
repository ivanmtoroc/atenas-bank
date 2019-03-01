<template>
  <div id="update" class="modal fade update" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Update client</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="updateClient()">
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="identification-update">Identification</label>
                <input id="identification-update" placeholder="Identification" v-model="client.identification" type="text" class="form-control" required="required" readonly>
              </div>
              <div class="col-md-6 form-group checkbox">
                <label for="vip-create">
                <input id="vip-create" v-model="client.is_vip" type="checkbox"><span class="checkbox-material"><span class="check"></span></span>
              VIP</label>
            </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name-update">First name</label>
                <input id="first_name-update" placeholder="First name" v-model="client.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name-update">Last name</label>
                <input id="last_name-update" placeholder="Last name" v-model="client.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email-update">Email</label>
                <input id="email-update" placeholder="Email" v-model="client.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group">
                <label for="address-update">Address</label>
                <input id="address-update" placeholder="Address" v-model="client.address" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="phone-update">Phone</label>
                <input id="phone-update" placeholder="Phone" v-model="client.phone" type="text" class="form-control" required="required">
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
    ...mapGetters('clients', ['client', 'errors'])
  },
  methods: {
    ...mapActions('clients', ['updateClient'])
  }
}
</script>
