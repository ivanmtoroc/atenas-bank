<template>
  <section class="content">
    <div class="row">
      <router-link :to="{ name: 'users' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="https://i.imgur.com/ccwBmTp.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Employees</span>
            </div>
          </div>
        </div>
      </router-link>
      <router-link :to="{ name: 'offices' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="https://i.imgur.com/VvO9nVO.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Branch Offices</span>
            </div>
          </div>
        </div>
      </router-link>
      <a href="">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="https://i.imgur.com/rfqWoEf.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Reports</span>
            </div>
          </div>
        </div>
      </a>
      <router-link :to="{ name: 'clients' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="https://i.imgur.com/B1IaFOY.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Customers</span>
            </div>
          </div>
        </div>
      </router-link>
      <router-link :to="{ name: 'ads' }">
        <div class="col-md-3 col-sm-6 col-xs-12">
          <div class="info-box">
            <span class="info-box-icon"><img src="https://i.imgur.com/tXDCY5N.png" ></span>
            <div class="info-box-content">
              <span class="info-box-number">Ads And News</span>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </section>
</template>
