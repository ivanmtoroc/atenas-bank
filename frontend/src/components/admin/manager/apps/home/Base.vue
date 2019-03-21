<template>
  <section class="content">
    <div class="row">
      <router-link :to="{ name: 'users' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="@/static/images/users.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Users</span>
            </div>
          </div>
        </div>
      </router-link>
      <router-link :to="{ name: 'offices' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="@/static/images/offices.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Branch Offices</span>
            </div>
          </div>
        </div>
      </router-link>
      <a href="">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="@/static/images/reports.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Reports</span>
            </div>
          </div>
        </div>
      </a>
      <router-link :to="{ name: 'clients' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="@/static/images/clients.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Clients</span>
            </div>
          </div>
        </div>
      </router-link>
      <router-link :to="{ name: 'ads' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="@/static/images/ads.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Ads and News</span>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </section>
</template>
