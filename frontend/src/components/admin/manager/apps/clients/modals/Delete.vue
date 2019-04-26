<template>
  <div id="delete" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>{{ client.is_active ? 'Deactivate' : 'Active' }} client</h3>
          </div>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-sm-12">
              <p>
                Are you sure to <strong>{{ client.is_active ? 'deactivate' : 'active' }}</strong>
                the client <strong>{{ client.first_name }} {{ client.last_name }}</strong>?
              </p>
            </div>
          </div>
          <div class="pull-right">
            <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
            <button data-dismiss="modal" @click="deleteClient(client.id)" type="button" :class="[ client.is_active ? 'btn-danger' : 'btn-success' ]" class="btn">
              {{ client.is_active ? 'Deactivate' : 'Active' }}
            </button>
          </div>
        </div>
        <div class="modal-footer"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    ...mapGetters('clients', ['client'])
  },
  methods: {
    ...mapActions('clients', ['deleteClient'])
  }
}
</script>
