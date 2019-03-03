<template>
  <div id="create" class="modal fade" style="display: none;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">×</span>
          </button>
          <div class="modal-title">
            <h3>Create ad</h3>
          </div>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addAd()">
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="name-create">Name</label>
                <input id="name-create" placeholder="Name" v-model="ad.name" type="text" class="form-control" required="required">
              </div>
              <div class="col-md-6 form-group">
                <label for="description-create">Description</label>
                <input id="description-create" placeholder="Description" v-model="ad.description" type="text" class="form-control" required="required">
              </div>
            </div>
            <div class="row">
              <div class="col-md-6 form-group">
                <label for="image-create">Image</label>
                <input id="image-create" placeholder="Image" type="file"  @change="processFile($event)" class="form-control" >
              </div>
            </div>
            <div class="pull-right">
              <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
              <button type="submit" class="btn btn-success">Save</button>
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
    ...mapActions('ads', ['addAd']),
    processFile (event) {
      this.someData = event.target.files[0]
    }
  }
}
</script>
