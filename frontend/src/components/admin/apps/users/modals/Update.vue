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
                <label for="identification2">Identification</label>
                <input id="identification2" placeholder="Identification" v-model="currentUser.identification" type="text" class="form-control" required="required" readonly>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.username ? 'has-error' : '']">
                <label for="username2">Username</label>
                <input id="username2" placeholder="Username" v-model="currentUser.username" type="text" class="form-control" required="required">
                <p v-for="error in errors.username" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="first_name2">First name</label>
                <input id="first_name2" placeholder="First name" v-model="currentUser.first_name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="last_name2">Last name</label>
                <input id="last_name2" placeholder="Last name" v-model="currentUser.last_name" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group" :class="[ errors.email ? 'has-error' : '']">
                <label for="email2">Email</label>
                <input id="email2" placeholder="Email" v-model="currentUser.email" type="text" class="form-control" required="required">
                <p v-for="error in errors.email" class="text-red">{{ error }}</p>
              </div>
              <div class="col-md-6 form-group" :class="[ errors.position ? 'has-error' : '']">
                <label>Position</label>
                <select v-model="currentUser.position" class="form-control" required="required">
                  <option>OP</option>
                  <option>MG</option>
                </select>
                <p v-for="error in errors.position" class="text-red">{{ error }}</p>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="address2">Address</label>
                <input id="address2" placeholder="Address" v-model="currentUser.address" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="phone2">Phone</label>
                <input id="phone2" placeholder="Phone" v-model="currentUser.phone" type="text" class="form-control" required="required">
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
    ...mapGetters('users', ['currentUser', 'errors'])
  },
  methods: {
    ...mapActions('users', ['updateUser'])
  }
}
</script>
