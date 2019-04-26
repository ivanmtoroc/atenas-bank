<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul v-if="authUser.position === 'MG'" class="sidebar-menu" data-widget="tree">
        <li @click="setApp('home')" :class="[app === 'home' ? 'active' : '']">
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i><span>Home</span>
          </router-link>
        </li>
        <li @click="setApp('users')" :class="[app === 'users' ? 'active' : '']">
          <router-link :to="{ name: 'users' }">
            <i class="fa fa-users"></i><span>Users</span>
          </router-link>
        </li>
        <li v-if="authUser.tenant === 'public'" @click="setApp('offices')" :class="[app === 'offices' ? 'active' : '']">
          <router-link :to="{ name: 'offices' }">
            <i class="fa fa-institution"></i><span>Offices</span>
          </router-link>
        </li>
        <li v-if="authUser.tenant === 'public'" @click="setApp('clients')" :class="[app === 'clients' ? 'active' : '']">
          <router-link :to="{ name: 'clients' }">
            <i class="fa  fa-male"></i><span>Clients</span>
          </router-link>
        </li>
        <li v-if="authUser.tenant === 'public'" @click="setApp('ads')" :class="[app === 'ads' ? 'active' : '']">
          <router-link :to="{ name: 'ads' }">
            <i class="fa fa-camera"></i><span>Ads</span>
          </router-link>
        </li>
      </ul>
      <ul v-else class="sidebar-menu" data-widget="tree">
        <li class="active">
          <router-link :to="{ name: 'operator' }">
            <i class="fa fa-home"></i><span>Dashboard</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      app: null
    }
  },
  computed: {
    ...mapGetters('authentication', ['authUser'])
  },
  methods: {
    setApp (app) {
      this.app = app
    }
  },
  mounted () {
    this.setApp(this.$route.matched[1].name)
  }
}
</script>
