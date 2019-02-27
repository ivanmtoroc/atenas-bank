<template>
  <div id="read" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>User information</h3>
          </div>
        </div>
        <div class="modal-body">
          <ul>
            <li>
              <p><strong>Username:</strong> {{ user.username }}.</p>
            </li>
            <li>
              <p><strong>Identification:</strong> {{ user.identification }}.</p>
            </li>
            <li>
              <p><strong>Full name:</strong> {{ user.first_name }} {{ user.last_name }}.</p>
            </li>
            <li>
              <p><strong>Status:</strong> {{ user.is_active ? 'Active' : 'Inactive' }}.</p>
            </li>
            <li>
              <p><strong>Phone:</strong> {{ user.phone }}.</p>
            </li>
            <li>
              <p><strong>Address:</strong> {{ user.address }}.</p>
            </li>
            <li>
              <p><strong>Position:</strong> {{ user.position === 'OP' ? 'Operator' : 'Manager' }}.</p>
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
    ...mapGetters('users', ['user'])
  }
}
</script>
