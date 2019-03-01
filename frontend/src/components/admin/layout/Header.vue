<template>
  <header class="main-header">
    <a class="logo">
      <span class="logo-mini"><strong>AB</strong></span>
      <span class="logo-lg">Atenas Bank</span>
    </a>
    <nav class="navbar navbar-static-top" role="navigation">
      <a class="sidebar-toggle" data-toggle="push-menu" role="button">
      </a>
      <div class="navbar-custom-menu">
        <ul class="nav navbar-nav">
          <li>
            <a>Username</a>
          </li>
          <li>
            <a @click="logout()" href=""><i class="fa fa-sign-out"></i> Logout</a>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions('authentication', ['logout'])
  }
}
</script>
