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
                <label for="identification">Identification</label>
                <input id="identification" placeholder="Identification" v-model="newUser.identification" type="text" class="form-control" required="required">
                <p v-for="error in errors.identification" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.username ? 'has-error' : '']">
                <label for="username">Username</label>
                <input id="username" placeholder="Username" v-model="newUser.username" type="text" class="form-control" required="required">
                <p v-for="error in errors.username" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name">First name</label>
                <input id="first_name" placeholder="First name" v-model="newUser.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name">Last name</label>
                <input id="last_name" placeholder="Last name" v-model="newUser.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email">Email</label>
                <input id="email" placeholder="Email" v-model="newUser.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.position ? 'has-error' : '']">
                <label for="position">Position</label>
                <select id="position" v-model="newUser.position" class="form-control" required="required">
                  <option>OP</option>
                  <option>MG</option>
                </select>
                <p v-for="error in errors.position" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="address">Address</label>
                <input id="address" placeholder="Address" v-model="newUser.address" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="phone">Phone</label>
                <input id="phone" placeholder="Phone" v-model="newUser.phone" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.passwd ? 'has-error' : '']">
                <label for="passwd">Password</label>
                <input id="passwd" placeholder="Password" v-model="newUser.passwd" type="password" class="form-control" required="required">
                <p v-for="error in errors.passwd" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.passwd ? 'has-error' : '']">
                <label for="passwd_confirmation">Password confirmation</label>
                <input id="passwd_confirmation" placeholder="Password confirmation" v-model="newUser.passwd_confirmation" type="password" class="form-control" required="required">
                <p v-for="error in errors.passwd" class="text-red">{{ error }}</p>
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
    ...mapGetters('users', ['newUser', 'errors'])
  },
  methods: {
    ...mapActions('users', ['addUser'])
  }
}
</script>
