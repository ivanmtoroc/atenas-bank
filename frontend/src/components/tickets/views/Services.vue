<template>
  <div class="col-md-4">
    <div class="box box-primary">
      <div class="box-header">
        <h3>Atenas Bank</h3>
        <h4>Request your ticket</h4>
      </div>
      <div class="box-body">
        <div class="form-group has-feedback is-empty">
          <label for="tenant">Tenant</label>
          <select id="tenant" v-model="ticket.tenant" class="form-control" required>
            <option v-for="office in tenantOffices" :value="office.schema_name">
              {{ office.name }}
            </option>
          </select>
          <span class="glyphicon glyphicon-home form-control-feedback"></span>
        </div>
        <router-link @click.native="setService('GEN')" :to="{ name: 'identification' }" type="button" class="btn btn-block btn-default">
          General
        </router-link>
        <router-link @click.native="setService('IAE')" :to="{ name: 'identification' }" type="button" class="btn btn-block btn-default">
          Imports and exports
        </router-link>
        <router-link @click.native="setService('INS')" :to="{ name: 'identification' }" type="button" class="btn btn-block btn-default">
          Insurances
        </router-link>
        <router-link @click.native="setService('DOT')" :to="{ name: 'identification' }" type="button" class="btn btn-block btn-default">
          Dollar transactions
        </router-link>
        <router-link @click.native="setService('VIP')" :to="{ name: 'identification' }" type="button" class="btn btn-block btn-default">
          VIP clients
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapGetters('tickets', ['ticket']),
    ...mapGetters('offices', ['tenantOffices'])
  },
  methods: {
    ...mapActions('offices', ['getOffices']),
    ...mapMutations('tickets', ['setService', 'cleanData'])
  },
  mounted () {
    this.cleanData()
    this.getOffices()
  }
}
</script>

<style scoped>
.btn {
  border: 1px solid transparent;
  border-radius: 7px;
  border-color: #bdbdbd;
  padding: 20px;
  font-size: 18px;
  font-weight: bold;
}

.h3, h3 {
  font-size: 40px;
  font-weight: bold;
  margin: 0;
  text-align: center;
  color: white;
}

.h4, h4 {
  font-size: 30px;
  margin: 0;
  text-align: center;
  color: white;
}

.box .box-header {
  padding: 19px;
  background-color: #d22828;
}
</style>
