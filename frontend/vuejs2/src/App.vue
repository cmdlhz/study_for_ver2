<template>
  <div>
    <show-blogs></show-blogs>
    <list-blogs></list-blogs>
  </div>
</template>

<script>
import showBlogs from './components/ShowBlogs.vue';
import listBlogs from './components/ListBlogs.vue';

export default {
  components:{
    'show-blogs': showBlogs,
    'list-blogs': listBlogs
  }
}
</script>

<style scoped>
body{
  margin: 0;
  font-family: 'Nunito SemiBold';
}
</style>
