<template>
  <div v-theme:column="'narrow'" id="show-blogs">
    <h1>All Blog Articles</h1>
    <div v-for="blog in blogs" :key="blog.id" class="single-blog">
      <h2 v-rainbow>{{ blog.title | to-uppercase }}</h2>
      <article>{{ blog.body | snippet }}</article>
    </div>
  </div>
</template>

<script>

export default {
  data(){
    return{
      blogs: []
    }
  },
  methods:{

  },
  created(){
    const axios = require('axios');
    axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(response => {
      console.log(response);
      this.blogs = response.data.slice(0,3);
    })
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
