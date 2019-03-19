<template>
  <div>
    <ads></ads>
    <router-view/>
  </div>
</template>

<script>
import Ads from '@/components/tickets/layout/Ads'

export default {
  components: {
    Ads
  }
}
</script>
