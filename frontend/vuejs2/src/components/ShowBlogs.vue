<template>
  <div v-theme:column="'narrow'" id="show-blogs">
    <h1>All Blog Articles</h1>
    <input type="text" v-model="search" placeholder="SEARCH Blogs :)">
    <div v-for="blog in filteredBlogs" :key="blog.id" class="single-blog">
      <router-link :to="'/blog/' + blog.id">
        <h2 v-rainbow>{{ blog.title | toUppercase }}</h2>
      </router-link>
      <article>{{ blog.content | snippet }}</article>
    </div>
  </div>
</template>

<script>
import searchMixin from "../mixins/searchMixin";

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
    axios.get('https://nn-vuejs2-playlist.firebaseio.com/posts.json')
    .then(response => {
      return response.data;
    }).then(response => {
      let blogsArray = [];
      for(let key in response){
        response[key].id = key;
        blogsArray.push(response[key]);
      }
      this.blogs = blogsArray;
    })
  },
  computed:{
    
  },
  filters: {
    toUppercase: value => value.toUpperCase(),
    snippet: value => value.slice(0,100) + '...'
  },
  directives: {
    rainbow: {
      bind(el){
        el.style.color = '#' + Math.random().toString().slice(2,8);
      }
    }
  },
  mixins: [searchMixin]
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
