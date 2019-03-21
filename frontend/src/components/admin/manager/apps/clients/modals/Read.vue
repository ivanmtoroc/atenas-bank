<template>
  <div id="read" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Client information</h3>
          </div>
        </div>
        <div class="modal-body">
          <ul>
            <li>
              <p><strong>Identification:</strong> {{ client.identification }}.</p>
            </li>
            <li>
              <p><strong>Full name:</strong> {{ client.first_name }} {{ client.last_name }}.</p>
            </li>
            <li>
              <p><strong>Email:</strong> {{ client.email }}.</p>
            </li>
            <li>
              <p><strong>Phone:</strong> {{ client.phone }}.</p>
            </li>
            <li>
              <p><strong>Address:</strong> {{ client.address }}.</p>
            </li>
            <li>
              <p><strong>Status:</strong> {{ client.is_active ? 'Active' : 'Inactive' }}.</p>
            </li>
            <li>
              <p><strong>VIP:</strong> {{ client.is_vip ? 'Yes' : 'No' }}.</p>
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
    ...mapGetters('clients', ['client'])
  }
}
</script>
