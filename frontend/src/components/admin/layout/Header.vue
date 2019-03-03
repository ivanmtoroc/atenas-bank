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
          <li class="dropdown user user-menu">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
              <img src="https://i.imgur.com/VvO9nVO.png" class="user-image" alt="User image">
              <span class="hidden-xs">{{ authUser.name }}</span>
              <div class="ripple-container"></div>
            </a>
            <ul class="dropdown-menu">
              <li class="user-header">
                <img src="https://i.imgur.com/VvO9nVO.png" class="img-circle" alt="User image">
                <p>
                  {{ authUser.name }} - {{ authUser.position === 'OP' ? 'Operator' : 'Manager' }}
                  <small>{{ authUser.username }}</small>
                  <small>{{ authUser.email }}</small>
                </p>
              </li>
              <li class="user-footer">
                <a @click="logout()" href="" class="btn btn-default">Logout</a>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('authentication', ['authUser'])
  },
  methods: {
    ...mapActions('authentication', ['logout'])
  }
}
</script>
