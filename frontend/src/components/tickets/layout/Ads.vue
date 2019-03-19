<template>
  <div class="col-md-8">
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div v-for="(ad, index) in ads" :class="[index === 0 ? 'active' : '']" class="item">
          <img :src="ad.image" alt="Ad">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('ads', ['ads'])
  },
  methods: {
    ...mapActions('ads', ['getAds'])
  },
  mounted () {
    this.getAds()
  }
}
</script>
