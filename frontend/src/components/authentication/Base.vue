<template>
  <div class="login-box">
    <div class="login-logo">
      <router-link :to="{ name: 'landing' }">
        <b>Atenas Bank</b>
      </router-link>
    </div>
    <div class="login-box-body">
      <p class="login-box-msg">Login to start your session</p>
      <form @submit.prevent="login()" method="post">
        <div v-for="error in errors.non_field_errors" class="alert alert-danger alert-dismissible">
          <h4><i class="icon fa fa-ban"></i> Alert!</h4>
          <p>{{ error }}</p>
        </div>
        <div class="form-group has-feedback is-empty">
          <input type="username" v-model="authUser.username" class="form-control" placeholder="Username" required>
          <span class="glyphicon glyphicon-user form-control-feedback"></span>
          <p v-for="error in errors.username" class="text-red">{{ error }}</p>
        </div>
        <div class="form-group has-feedback is-empty">
          <input type="password" v-model="authUser.password" class="form-control" placeholder="Password" required>
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
          <p v-for="error in errors.password" class="text-red">{{ error }}</p>
        </div>
        <div class="form-group has-feedback is-empty">
          <label for="tenant">Tenant</label>
          <select id="tenant" v-model="authUser.tenant" class="form-control" required>
            <option v-for="office in offices" :value="office.schema_name">
              {{ office.name }}
            </option>
          </select>
          <span class="glyphicon glyphicon-home form-control-feedback"></span>
        </div>
        <div class="row">
          <div class="col-xs-offset-7 col-xs-5">
            <button type="submit" class="btn btn-primary btn-raised btn-block btn-flat">Login</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('authentication', ['authUser', 'errors']),
    ...mapGetters('offices', ['offices'])
  },
  methods: {
    ...mapActions('offices', ['getOffices']),
    ...mapActions('authentication', ['login'])
  },
  mounted () {
    this.getOffices()
  }
}
</script>

<style>
body {
  background-image: url('~@/static/images/background.jpg');
  background-size: cover;
}
</style>
