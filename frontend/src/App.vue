<template>
  <div id="app">
    <div class="wrapper">
      <header-component></header-component>
      <sidebar-component></sidebar-component>
      <div class="content-wrapper">
        <section class="content-header">
          <div class="list-inline">
            <li>
              <h1>
                Page title
              </h1>
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
    <div id="modal-create" class="modal fade modal-create" style="display: none;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">×</span>
            </button>
            <div class="modal-title">Modal create title</div>
          </div>
          <div class="modal-body">Modal create body</div>
          <div class="modal-footer"></div>
        </div>
      </div>
    </div>
    <div id="modal-read" class="modal fade modal-read" style="display: none;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">×</span>
            </button>
            <div class="modal-title">Modal read title</div>
          </div>
          <div class="modal-body">Modal read body</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
    <div id="modal-update" class="modal fade modal-update" style="display: none;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">×</span>
            </button>
            <div class="modal-title">Modal update title</div>
          </div>
          <div class="modal-body">Modal update body</div>
          <div class="modal-footer"></div>
        </div>
      </div>
    </div>
    <div id="modal-delete" class="modal fade modal-delete" style="display: none;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">
              <span aria-hidden="true">×</span>
            </button>
            <div class="modal-title">Modal delete title</div>
          </div>
          <div class="modal-body">Modal delete body</div>
          <div class="modal-footer"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue'
import SidebarComponent from '@/components/layout/SidebarComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue'

export default {
  name: 'App',
  components: {
    HeaderComponent,
    SidebarComponent,
    FooterComponent
  }
}
</script>
