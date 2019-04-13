<template>
  <div>
    <show-blogs></show-blogs>
  </div>
</template>

<script>
import showBlogs from './components/ShowBlogs.vue';

export default {
  components:{
    'show-blogs': showBlogs
  }
}
</script>

<style scoped>
body{
  margin: 0;
  font-family: 'Nunito SemiBold';
}
</style>
