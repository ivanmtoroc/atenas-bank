<template>
  <div class="wrapper">
    <header-component></header-component>
    <aside-component></aside-component>
    <div class="content-wrapper" style="min-height: 90vh;">
      <router-view/>
    </div>
    <footer-component></footer-component>
  </div>
</template>

<script>
import HeaderComponent from '@/components/admin/layout/Header'
import AsideComponent from '@/components/admin/layout/Aside'
import FooterComponent from '@/components/admin/layout/Footer'

export default {
  components: {
    HeaderComponent,
    AsideComponent,
    FooterComponent
  }
}
</script>

<style>
.action-btn {
  margin: 0px 3px;
}
</style>
