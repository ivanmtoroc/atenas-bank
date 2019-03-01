<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li class="active">
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i><span>Home</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'users' }">
            <i class="fa fa-users"></i><span>Users</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'offices' }">
            <i class="fa fa-institution"></i><span>Offices</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'clients' }">
            <i class="fa  fa-male"></i><span>Clients</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'ads' }">
            <i class="fa fa-camera"></i><span>Ads</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
</template>
