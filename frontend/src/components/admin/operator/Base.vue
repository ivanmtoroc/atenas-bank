<template>
  <div class="container-fluid">
    <section class="invoice">
      <div class="row">
        <div class="col-md-3">
          <div class="form-group has-feedback is-empty">
            <label for="tenant">Service</label>
            <select id="tenant" class="form-control" required>
              <option @click="setService('GEN')">General</option>
              <option @click="setService('IAE')">Imports and Exports</option>
              <option @click="setService('INS')">Insurances</option>
              <option @click="setService('DOT')">Dollar Transactions</option>
              <option @click="setService('VIP')">VIP clients</option>
            </select>
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
                        #{{ currentTicket.turn_number }}
                      </h1>
                      User: {{ currentTicket.user }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <button @click="initAttention(currentTicket.id)" :class="[1, 3].includes(operatorState) ? 'disabled' : ''" type="button" class="btn btn-default"><i class="fa fa-fw fa-chevron-circle-right"></i> Start Service </button>
          <button @click="finishAttention(currentTicket.id)" :class="[1, 2].includes(operatorState) ? 'disabled' : ''" type="button" class="btn btn-default"><i class="fa fa-fw fa-power-off"></i> Finish Service </button>
        </div>
        <div class="col-md-12">
          <button @click="defer(currentTicket.id)" type="button" :class="[1, 3].includes(operatorState) ? 'disabled' : ''" class="btn btn-danger pull-right">
            Postpone Ticket
          </button>
          <button @click="send(service)" :class="[2, 3].includes(operatorState) ? 'disabled' : ''" type="button" class="btn btn-success pull-right" style="margin-right: 5px;">
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
    ...mapGetters('tickets', ['currentTicket']),
    ...mapGetters('operator', ['service', 'operatorState']),
    ...mapGetters('authentication', ['authUser'])
  },
  methods: {
    ...mapMutations('tickets', ['initWSConection', 'cleanTicket']),
    ...mapMutations('operator', ['updateHttp', 'setService', 'setState']),
    ...mapActions('tickets', ['send', 'retrieve']),
    ...mapActions('operator', ['initAttention', 'finishAttention', 'defer'])
  },
  watch: {
    currentTicket: function (newTicket, oldTicket) {
      if (newTicket.turn_number !== '') {
        this.setState(2)
      }
    },
    operatorState: function (newState, oldState) {
      if (newState === 1) {
        this.cleanTicket()
      }
    }
  },
  filters: {
    showService: value => {
      switch (value) {
        case 'GEN':
          return 'General'
        case 'IAE':
          return 'Imports and exports'
        case 'INS':
          return 'Insurances'
        case 'DOT':
          return 'Dollar transactions'
        case 'VIP':
          return 'VIP'
        default:
          return 'General'
      }
    }
  },
  mounted () {
    this.updateHttp(this.authUser.tenant)
    this.initWSConection(this.authUser.tenant)
    this.retrieve()
    this.setService('GEN')
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
