<template>
  <div id="create" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Create user</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addUser()">
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.identification ? 'has-error' : '']">
                <label for="identification-create">Identification</label>
                <input id="identification-create" placeholder="Identification" v-model="user.identification" type="text" class="form-control" required="required">
                <p v-for="error in errors.identification" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.username ? 'has-error' : '']">
                <label for="username-create">Username</label>
                <input id="username-create" placeholder="Username" v-model="user.username" type="text" class="form-control" required="required">
                <p v-for="error in errors.username" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name-create">First name</label>
                <input id="first_name-create" placeholder="First name" v-model="user.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name-create">Last name</label>
                <input id="last_name-create" placeholder="Last name" v-model="user.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email-create">Email</label>
                <input id="email-create" placeholder="Email" v-model="user.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.position ? 'has-error' : '']">
                <label for="position-create">Position</label>
                <select id="position-create" v-model="user.position" class="form-control" required="required">
                  <option value="OP">Operator</option>
                  <option value="MG">Manager</option>
                </select>
                <p v-for="error in errors.position" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="address-create">Address</label>
                <input id="address-create" placeholder="Address" v-model="user.address" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="phone-create">Phone</label>
                <input id="phone-create" placeholder="Phone" v-model="user.phone" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.passwd ? 'has-error' : '']">
                <label for="passwd-create">Password</label>
                <input id="passwd-create" placeholder="Password" v-model="user.passwd" type="password" class="form-control" required="required">
                <p v-for="error in errors.passwd" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.passwd ? 'has-error' : '']">
                <label for="passwd_confirmation-create">Password confirmation</label>
                <input id="passwd_confirmation-create" placeholder="Password confirmation" v-model="user.passwd_confirmation" type="password" class="form-control" required="required">
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
    ...mapGetters('users', ['user', 'errors'])
  },
  methods: {
    ...mapActions('users', ['addUser'])
  }
}
</script>
