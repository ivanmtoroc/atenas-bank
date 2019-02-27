<template>
  <div id="read" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Information</h3>
          </div>
        </div>
        <div class="modal-body">
          <ul>
            <li>
              <p><strong>Username:</strong> {{ currentUser.username }}.</p>
            </li>
            <li>
              <p><strong>Identification:</strong> {{ currentUser.identification }}.</p>
            </li>
            <li>
              <p><strong>Full name:</strong> {{ currentUser.first_name }} {{ currentUser.last_name }}.</p>
            </li>
            <li>
              <p><strong>Status:</strong> {{ currentUser.is_active }}.</p>
            </li>
            <li>
              <p><strong>Phone:</strong> {{ currentUser.phone }}.</p>
            </li>
            <li>
              <p><strong>Address:</strong> {{ currentUser.address }}.</p>
            </li>
            <li>
              <p><strong>Position:</strong> {{ currentUser.position }}.</p>
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
    ...mapGetters('users', ['currentUser'])
  }
}
</script>
