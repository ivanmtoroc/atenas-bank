<template>
  <div class="col-lg-4 col-xs-6">
    <div class="small-box bg-green">
      <div class="inner">
        <p>{{ currentTicket.turn_number }}</p>
      </div>
      <div class="icon">
        <i class="fa fa-fw fa-ticket"></i>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('tickets', ['currentTicket']),
    ...mapGetters('authentication', ['authUser'])
  },
  methods: {
    ...mapMutations('tickets', ['initWSConection', 'setView']),
    ...mapActions('tickets', ['retrieve'])
  },
  mounted () {
    this.initWSConection(this.authUser.tenant)
    this.setView()
    this.retrieve()
  }
}
</script>

<style scoped>
.bg-hadder, .callout.callout-success, .alert-success, .label-success, .modal-success .modal-body {
  background-color: #d2d6d4 !important;
}

.box, .info-box, .small-box, .nav-tabs-custom, .callout {
  border-radius: 10px;
  height: 100px;
}

.btn {
  border:1px solid transparent;
  border-radius: 7px;
  border-color:#bdbdbd;
  padding: 15px;
  font-size: 18px;
  font-weight: bold;
}

.small-box h3 {
  font-size: 20px;
  font-weight: 100;
  margin: 0 0 0px 0;
  white-space: nowrap;
  padding: 0px;
}

.small-box p {
  text-align: center;
  font-size: 50px;
  font-weight: bold;
  padding: 0px;
}

.h4, h4 {
  font-size: 30px;
  margin: 0;
  text-align: center;
  color: white;
}

.box .box-header {
  padding: 15px;
  background-color: #d22828;
}
</style>
