<template>
  <div>
    <h1>Home</h1>
    <input @click="send()" type="button" value="Next ticket"/>
  </div>
</template>

<script>
var ticketsWebSocket = new WebSocket(
  'ws://localhost:8000/ws/tickets/'
)

export default {
  methods: {
    send () {
      ticketsWebSocket.send(JSON.stringify({ 'trash': 'hadder' }))
    }
  }
}
</script>
