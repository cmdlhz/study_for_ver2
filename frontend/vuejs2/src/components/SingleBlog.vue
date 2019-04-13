<template>
  <div id="single-blog">
    <h1>{{ blog.title }}</h1>
    <article>{{ blog.content }}</article>
    <p>Author: {{ blog.author }}</p>
    <ul>
      <li v-for="category in blog.categories" :key="category.id">{{ category }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data(){
    return{
      id: this.$route.params.id,
      blog: {}
    }
  },
  created(){
    const axios = require('axios');
    axios.get('https://nn-vuejs2-playlist.firebaseio.com/posts/' + this.id + '.json')
    .then(response => {
      return response.data;
    }).then(response => {
      this.blog = response;
    });
  }
}
</script>

<style scoped>
#single-blog{
  max-width: 960px;
  margin: 0 auto;
}
</style>
