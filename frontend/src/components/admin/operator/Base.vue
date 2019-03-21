<template>
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
