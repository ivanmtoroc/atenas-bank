<template>
  <div>
    <h1>Esta es la vista de los tickets</h1>
    <input type="text" v-model="ticket">
  </div>
</template>

<script>
var ticketsWebSocket = new WebSocket(
  'ws://localhost:8000/ws/tickets/'
)

export default {
  data () {
    return {
      ticket: 'ticket'
    }
  },
  mounted () {
    var _this = this
    ticketsWebSocket.onmessage = function (e) {
      var data = JSON.parse(e.data)
      _this.ticket = data['ticket']
    }
  }
}
</script>
