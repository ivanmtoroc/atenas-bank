<template>
  <div id="update" class="modal fade update" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Update ad</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="updateAds()">
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="identification-update">ID</label>
                <input id="identification-update" placeholder="ID" v-model="ad.id" type="text" class="form-control" required="required" readonly>
              </div>
              <div class="col-md-6 form-group">
                <label for="description-update">Description</label>
                <input id="description-update" placeholder="Description" v-model="ad.description" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="image-update">Image</label>
                <input id="image-update" placeholder="Image" v-model="ad.image" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="pull-right">
              <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
              <button type="submit" class="btn btn-primary">Update</button>
            </div>
          </form>
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
    ...mapGetters('ads', ['ad', 'errors'])
  },
  methods: {
    ...mapActions('ads', ['updateAds'])
  }
}
</script>
