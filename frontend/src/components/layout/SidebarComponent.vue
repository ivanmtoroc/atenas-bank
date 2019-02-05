<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li class="active">
          <router-link :to="{ name: 'dashboard' }">
            <i class="fa fa-bank"></i><span>Dashboard</span>
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'users' }">
            <i class="fa fa-users"></i><span>Users</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
</template>
