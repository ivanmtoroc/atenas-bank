<template>
  <div id="read" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Ad information</h3>
          </div>
        </div>
        <div class="modal-body">
          <ul>
            <li>
              <p><strong>Name:</strong> {{ ad.name }}.</p>
            </li>
            <li>
              <p><strong>Description:</strong> {{ ad.description }}.</p>
            </li>
            <li>
              <p><strong>Image:</strong></p>
              <img :src="ad.image" alt="Ad image" width="auto" height="200">
            </li>
            <li>
              <p><strong>Status:</strong> {{ ad.is_active ? 'Active' : 'Inactive' }}.</p>
            </li>
          </ul>
          <div class="pull-right">
            <button type="button" class="btn btn-info" data-dismiss="modal">Close</button>
          </div>
        </div>
        <div class="modal-footer"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('ads', ['ad'])
  }
}
</script>
