<template>
    <!-- Main content -->
    <section class="content">
      <!-- Info boxes -->
      <div class="row">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="'./images/employees.png'" ></span>

            <div class="info-box-content">
              <span class="info-box-number">EMPLOYEES</span>
            </div>
            <!-- /.info-box-content -->
          </div>
          <!-- /.info-box -->
        </div>
        <!-- /.col -->
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="public/static/images/employees.png" ></span>

            <div class="info-box-content">

              <span class="info-box-number">BRANCH OFFICES</span>
            </div>
            <!-- /.info-box-content -->
          </div>
          <!-- /.info-box -->
        </div>
        <!-- /.col -->

        <!-- fix for small devices only -->
        <div class="clearfix visible-sm-block"></div>

        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="public/static/images/employees.png" ></span>

            <div class="info-box-content">
              <span class="info-box-number">REPORTS</span>
            </div>
            <!-- /.info-box-content -->
          </div>
          <!-- /.info-box -->
        </div>
        <!-- /.col -->
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="public/static/images/employees.png" ></span>

            <div class="info-box-content">
              <span class="info-box-number">CUSTOMERS</span>
            </div>
            <!-- /.info-box-content -->
          </div>
          <!-- /.info-box -->
        </div>
        <!-- /.col -->

        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="public/static/images/employees.png" ></span>

            <div class="info-box-content">

              <span class="info-box-number">ADS AND NEWS</span>
            </div>
            <!-- /.info-box-content -->
          </div>
          <!-- /.info-box -->
        </div>
        <!-- /.col -->

      </div>

    </section>
</template>
<script>

export default {
  data () {
    return {
      publicPath: process.env.BASE_URL
    }
  }
}

</script>
