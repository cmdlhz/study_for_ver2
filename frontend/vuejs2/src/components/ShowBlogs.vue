<template>
  <div v-theme:column="'narrow'" id="show-blogs">
    <h1>All Blog Articles</h1>
    <input type="text" v-model="search" placeholder="SEARCH Blogs :)">
    <div v-for="blog in filteredBlogs" :key="blog.id" class="single-blog">
      <h2 v-rainbow>{{ blog.title | to-uppercase }}</h2>
      <article>{{ blog.body | snippet }}</article>
    </div>
  </div>
</template>

<script>

export default {
  data(){
    return{
      blogs: [],
      search: ''
    }
  },
  methods:{

  },
  created(){
    const axios = require('axios');
    axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(response => {
      console.log(response);
      this.blogs = response.data.slice(0,10);
    });
  },
  computed:{
    filteredBlogs: function(){
      return this.blogs.filter(blog => {
        return blog.title.match(this.search) || blog.body.match(this.search);
      });
    }
  }
}
</script>

<style scoped>
#show-blogs{
  max-width: 800px;
  margin: 0 auto;
}
.single-blog{
  padding: 20px;
  margin: 20px 0;
  box-sizing: border-box;
  background: #eee;
}
</style>
