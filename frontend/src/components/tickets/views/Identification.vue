<template>
  <div class="col-md-4">
    <div class="box box-primary">
      <div class="box-header">
        <h3>Atenas Bank</h3>
        <h4>Request your ticket</h4>
      </div>
      <div class="box-body">
        <input v-model="identification" type="text" class="form-control" placeholder="Identification">
        <div class="col-md-6 col-md-offset-1">
          <ul id="keyboard">
            <li class="letter" @click="change('1')">1</li>
            <li class="letter" @click="change('2')">2</li>
            <li class="letter" @click="change('3')">3</li>
            <li class="letter clearl" @click="change('4')">4</li>
            <li class="letter" @click="change('5')">5</li>
            <li class="letter" @click="change('6')">6</li>
            <li class="letter clearl" @click="change('7')">7</li>
            <li class="letter " @click="change('8')">8</li>
            <li class="letter" @click="change('9')">9</li>
            <li class="letter clearl" @click="change('0')">0</li>
            <li class="delete lastitem" @click="change('DEL')">DELETE</li>
          </ul>
        </div>
        <div class="col-md-4">
          <button @click="getTicket()" type="button" class="btn btn-block btn-default" style="background-color: #00a65a; color: white;">
            Get ticket
          </button>
          <router-link :to="{ name: 'tickets' }" type="button" class="btn btn-block btn-default" style= "background-color: #d22828; color: white;">
            <i class="fa fa-fw fa-arrow-left"></i> Back
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('tickets', ['identification'])
  },
  methods: {
    ...mapMutations('tickets', ['change']),
    ...mapActions('tickets', ['getTicket'])
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

body {
  font: 71%/1.5 Verdana, Sans-Serif;
  background: #eee;
}

#container {
  margin: 100px auto;
  width: 760px;
}

#keyboard {
  margin: 0;
  padding: 0;
  list-style: none;
}

#keyboard li {
  float: left;
  margin: 0 5px 5px 0;
  width: 60px;
  height: 60px;
  font-size: 24px;
  line-height: 60px;
  text-align: center;
  background: #fff;
  border: 1px solid #f9f9f9;
  border-radius: 5px;
}

.capslock, .tab, .left-shift, .clearl, .switch {
  clear: left;
}

#keyboard .tab, #keyboard .delete {
  width: 123px;
}

#keyboard .capslock {
  width: 80px;
}

#keyboard .return {
  width: 90px;
}

#keyboard .left-shift{
  width: 70px;
}

#keyboard .switch {
  width: 90px;
}

#keyboard .rightright-shift {
  width: 109px;
}

.lastitem {
  margin-right: 0;
}

.uppercase {
  text-transform: uppercase;
}

#keyboard .space {
  float: left;
  width: 556px;
}

#keyboard .switch, #keyboard .space, #keyboard .return{
  font-size: 16px;
}

.on {
  display: none;
}

#keyboard li:hover {
  position: relative;
  top: 1px;
  left: 1px;
  border-color: #e5e5e5;
  cursor: pointer;
}

.form-control {
  font-size: 20px;
}

.form-group {
  margin-left: 40px;
  margin-right: 40px;
}

input {
  text-align:center;
}

.skin-red .form-group.is-focused .form-control {
  background-image: linear-gradient(#d22828, #d22828), linear-gradient(#d22828, #d22828);
}

.skin-red .form-control, .skin-red .form-group .form-control {
  background-image: linear-gradient(#d22828, #d22828),linear-gradient(#d22828, #d22828);
}

.btn {
  border:1px solid transparent;
  border-radius: 7px;
  border-color:#bdbdbd;
  padding: 20px;
  font-size: 18px;
  font-weight: bold;
}

box-body {
  width:80%;
  margin-left:auto;
  margin-right:auto;
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
