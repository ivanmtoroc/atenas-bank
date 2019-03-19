<template>
  <div class="col-md-4">
    <div class="box box-primary">
      <div class="box-header">
        <h3>Atenas Bank</h3>
        <h4>Request your ticket</h4>
      </div>
      <div class="box-body">
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
import { mapMutations } from 'vuex'

export default {
  methods: {
    ...mapMutations('tickets', ['setService', 'cleanData'])
  },
  mounted () {
    this.cleanData()
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
