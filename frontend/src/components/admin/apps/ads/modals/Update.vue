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
          <form @submit.prevent="updateAd(file)">
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <label for="identification-update">Id</label>
                  <input id="identification-update" placeholder="Id" v-model="ad.id" type="text" class="form-control" required="required" readonly>
                </div>
                <div class="form-group">
                  <label for="name-update">Name</label>
                  <input id="name-update" placeholder="Name" v-model="ad.name" type="text" class="form-control" required="required">
                </div>
                <div class="form-group">
                  <label for="description-update">Description</label>
                  <input id="description-update" placeholder="Description" v-model="ad.description" type="text" class="form-control" required="required">
                </div>
              </div>
              <div class="col-md-6">
                <div class="custom-file">
                  <input type="file" ref="file" class="custom-file-input" id="image-create" @change="handleFileUpload()">
                </div>
                <div class="form-group center">
                  <img :src="ad.image" alt="Ad image" width="auto" height="200">
                </div>
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
  data () {
    return {
      file: ''
    }
  },
  computed: {
    ...mapGetters('ads', ['ad', 'errors'])
  },
  methods: {
    ...mapActions('ads', ['updateAd']),
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    }
  }
}
</script>
