<template>
  <section class="content">
    <div class="error-page error404">
      <h2 class="headline text-blue m-0">404</h2>
      <div class="error-content ml-40">
        <h3><i class="fa fa-warning text-blue"></i> Oops! Page not found.</h3>
        <p>
          We could not find the page you were looking for.
          Meanwhile, you may <router-link :to="{ name: 'landing' }">return to landing page</router-link>.
        </p>
      </div>
    </div>
  </section>
</template>

<style scoped>
  .error404 {
    display: flex;
    justify-content: center;
  }

  .m-0 {
    margin: 0px;
  }

  .ml-40 {
    margin-left: 40px;
  }
</style>
