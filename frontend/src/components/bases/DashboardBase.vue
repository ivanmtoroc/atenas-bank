<template>
  <div>
    <div class="wrapper">
      <header-component></header-component>
      <sidebar-component></sidebar-component>
      <div class="content-wrapper">
        <section class="content-header">
          <div class="list-inline">
            <li>
              <h1>Users</h1>
            </li>
          </div>
          <ol class="breadcrumb"></ol>
        </section>
        <section class="content">
          <router-view/>
        </section>
      </div>
      <footer-component></footer-component>
    </div>
    <modal-create></modal-create>
    <modal-read></modal-read>
    <modal-update></modal-update>
    <modal-delete></modal-delete>
  </div>
</template>

<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue'
import SidebarComponent from '@/components/layout/SidebarComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue'

import ModalDelete from '@/components/modals/ModalDelete.vue'
import ModalRead from '@/components/modals/ModalRead.vue'
import ModalCreate from '@/components/modals/ModalCreate.vue'
import ModalUpdate from '@/components/modals/ModalUpdate.vue'

export default {
  components: {
    HeaderComponent,
    SidebarComponent,
    FooterComponent,
    ModalDelete,
    ModalRead,
    ModalCreate,
    ModalUpdate
  }
}
</script>
