<template>
  <div class="col-lg-4 col-xs-6">
    <div class="small-box">
      <div class="inner">
        <p>Your ticket:</p>
        <h3>{{ currentTicket.turn_number }}</h3>
      </div>
      <div class="icon">
        <i class="fa fa-fw fa-ticket"></i>
      </div>
    </div>
    <router-link :to="{ name: 'tickets' }" type="button" class="btn btn-block btn-default" style= "background-color: #d22828; color: white;">
      <i class="fa fa-fw fa-arrow-left"></i> Back
    </router-link>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('tickets', ['currentTicket'])
  }
}
</script>
