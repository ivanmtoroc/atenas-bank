<template>
<!--
<section class="content">
  <div class="row">
    <div class="col-sm-12">
      <div class="box">
        <div class="box-body">
          <div class="row">
            <div class="col-sm-12">
              <h1>Operator</h1>
              <input @click="send('GEN')" class="btn btn-info" type="button" value="Next ticket"/>
              <input type="button" class="btn btn-info" value="Init attention"/>
              <input type="button" class="btn btn-info" value="Finish attention"/>
              <input type="text" placeholder="Service"/>
              <input :value="currentTicket.turn_number" type="text" placeholder="Ticket"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
-->
<div class="container-fluid">
  <section class="invoice">
    <div class="row">
      <div class="col-md-3">
        <div class="box box-default box-solid collapsed-box" style="width: 250px;">
          <div class="box-header with-border">
            <h3 class="box-title">General</h3>
            <div class="box-tools pull-right">
              <button type="button" class="btn btn-box-tool" data-widget="collapse" style="color: white;">
                <i class="fa fa-plus"></i>
                <div class="ripple-container"></div>
              </button>
            </div>
          </div>
          <div class="box-body">
            <li class="btn btn-info btn-block">General</li>
            <li class="btn btn-info btn-block">Imports and Exports</li>
            <li class="btn btn-info btn-block">Insurances</li>
            <li class="btn btn-info btn-block">Dollar Transactions</li>
            <li class="btn btn-info btn-block">VIP clients</li>
          </div>
        </div>
      </div>
      <div class="col-md-12"></div>
      <div class="col-md-4">
        <div class="box box-success">
          <div class="box-header with-border">
            <h3 class="box-title">Current ticket:</h3>
          </div>
          <div class="box-body">
            <div class="row">
              <div class="col-md-12" style="padding-left: 30px; padding-right: 30px;">
                <div class="small-box" style="margin-bottom: 0px;">
                  <div class="inner">
                    <h1 style="font-size: 30px; text-align: center; margin-top: 10px;">
                      G01 <i class="fa fa-fw fa-ticket pull-right"></i>
                    </h1>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <button type="button" class="btn btn-default"><i class="fa fa-fw fa-chevron-circle-right"></i> Start Service </button>
        <button type="button" class="btn btn-default"><i class="fa fa-fw fa-power-off"></i> Finish Service </button>
      </div>
      <div class="col-md-12">
        <button type="button" class="btn btn-danger pull-right">
          Postpone Ticket
        </button>
        <button type="button" class="btn btn-success pull-right" style="margin-right: 5px;">
          Next Ticket
        </button>
      </div>
    </div>
  </section>
</div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('tickets', ['currentTicket'])
  },
  methods: {
    ...mapMutations('tickets', ['initWSConection']),
    ...mapActions('tickets', ['send', 'retrieve'])
  },
  mounted () {
    this.initWSConection()
    this.retrieve()
  }
}
</script>

<style scoped>
.btn-default {
  border-color: black !important;
  border: 1px solid !important;
  padding-bottom: 20px;
  padding-top: 20px;
  font-size: 15px;
}

.btn-success {
  border-color: black !important;
  border: 1px solid !important;
  padding-bottom: 10px;
  padding-top: 10px;
  font-size: 15px;
}

.btn-danger {
  border-color: black !important;
  border: 1px solid !important;
  padding-bottom: 10px;
  padding-top: 10px;
  font-size: 15px;
}

.btn-info {
  color: black;
}

.box.box-solid.box-default>.box-header {
  color: white;
  background: #f44336;
  background-color: #f44336;
}
</style>
