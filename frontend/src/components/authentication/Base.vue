<template>
  <div class="login-box">
    <div class="login-logo">
      <a><b>Atenas Bank</b></a>
    </div>
    <div class="login-box-body">
      <p class="login-box-msg">Login to start your session</p>
      <form @submit.prevent="login()" method="post">
        <div class="form-group has-feedback is-empty">
          <input type="username" v-model="user.username" class="form-control" placeholder="Username" required="required">
          <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
        </div>
        <div class="form-group has-feedback is-empty">
          <input type="password" v-model="user.passwd" class="form-control" placeholder="Password" required="required">
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
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
    ...mapGetters('authentication', ['user'])
  },
  methods: {
    ...mapActions('authentication', ['login'])
  }
}
</script>
