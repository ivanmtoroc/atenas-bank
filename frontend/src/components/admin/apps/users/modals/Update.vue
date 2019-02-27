<template>
  <div id="update" class="modal fade update" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Update user</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="updateUser()">
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="identification-update">Identification</label>
                <input id="identification-update" placeholder="Identification" v-model="user.identification" type="text" class="form-control" required="required" readonly>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.username ? 'has-error' : '']">
                <label for="username-update">Username</label>
                <input id="username-update" placeholder="Username" v-model="user.username" type="text" class="form-control" required="required">
                <p v-for="error in errors.username" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name-update">First name</label>
                <input id="first_name-update" placeholder="First name" v-model="user.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name-update">Last name</label>
                <input id="last_name-update" placeholder="Last name" v-model="user.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email-update">Email</label>
                <input id="email-update" placeholder="Email" v-model="user.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.position ? 'has-error' : '']">
                <label for="position-update">Position</label>
                <select id="position-update" v-model="user.position" class="form-control" required="required">
                  <option value="OP">Operator</option>
                  <option value="MG">Manager</option>
                </select>
                <p v-for="error in errors.position" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="address-update">Address</label>
                <input id="address-update" placeholder="Address" v-model="user.address" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="phone-update">Phone</label>
                <input id="phone-update" placeholder="Phone" v-model="user.phone" type="text" class="form-control" required="required">
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
    ...mapGetters('users', ['user', 'errors'])
  },
  methods: {
    ...mapActions('users', ['updateUser'])
  }
}
</script>
