<template>
  <div id="delete" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>{{ user.is_active ? 'Deactivate' : 'Active' }} user</h3>
          </div>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-sm-12">
              <p>
                Are you sure to <strong>{{ user.is_active ? 'deactivate' : 'active' }}</strong>
                the user <strong>{{ user.first_name }} {{ user.last_name }}</strong>?
              </p>
            </div>
          </div>
          <div class="pull-right">
            <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
            <button data-dismiss="modal" @click="deleteUser(user.id)" type="button" :class="[ user.is_active ? 'btn-danger' : 'btn-success' ]" class="btn">
              {{ user.is_active ? 'Deactivate' : 'Active' }}
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
    ...mapGetters('users', ['user'])
  },
  methods: {
    ...mapActions('users', ['deleteUser'])
  }
}
</script>
