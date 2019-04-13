<template>
  <div id="app">
    <app-header></app-header>
    <router-view></router-view>
  </div>
</template>

<script>
import addBlog from './components/AddBlog.vue';	
import showBlogs from './components/ShowBlogs.vue';
import listBlogs from './components/ListBlogs.vue';
import header from './components/Header.vue';

export default {	
  components:{
    'add-blogs': addBlog,
    'show-blogs': showBlogs,	    
    'list-blogs': listBlogs,
    'app-header': header
  }	  
}	
</script>	


<style scoped>
body{
  margin: 0;
  font-family: 'Nunito SemiBold';
}
</style>
