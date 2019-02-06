<template>
  <div>
    <tr v-for="(user, index) in users" :key="index" role="row" class="odd">
      <td class="sorting_1">{{ user.first_name }} {{ user.last_name }}</td>
      <td>{{ user.username }}</td>
      <td>{{ user.identification }}</td>
      <td>{{ user.email }}</td>
      <td>{{ user.position }}</td>
      <td class="text-center">
        <p v-if="user.is_active" class="badge bg-green p-bg">Active</p>
        <p v-else class="badge bg-red p-bg">Inactive</p>
      </td>
      <td class="text-center">
        <div class="input-group-btn">
          <button type="button" class="btn btn-default btn-sm dropdown-toggle" data-toggle="dropdown">Actions <span class="fa fa-caret-down"></span></button>
          <ul class="dropdown-menu">
            <li>
              <a @click="getUser(user.cedula)" href="#modal-delete" class="btn btn-sm" :class="[user.is_active ? 'btn-danger' : 'btn-success']" data-toggle="modal" data-target="#modal-delete">
                <span v-if="user.is_active"><i class="fa fa-user-times"></i> Deactivate</span>
                <span v-else><i class="fa fa-user-plus"></i> Activate</span>
              </a>
            </li>
            <li>
              <a @click="getUser(user.cedula)" href="#modal-update" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#modal-update">
                <i class="fa fa-edit"></i> Update
              </a>
            </li>
            <li>
              <a @click="readUser(user.cedula)" href="#modal-read" class="btn btn-info btn-sm" data-toggle="modal" data-target="#modal-read">
                <i class="fa fa-info-circle"></i> Information
              </a>
            </li>
          </ul>
        </div>
      </td>
    </tr>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('users', ['users'])
  }
}
</script>
