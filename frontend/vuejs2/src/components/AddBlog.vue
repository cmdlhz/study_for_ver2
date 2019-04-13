<template>
  <div id="add-blog">
    <h2>Add a New Blog Post</h2>
    <form v-if="!submitted">
      <label>Blog Title:</label>
      <input type="text" v-model.lazy="blog.title" required>
      <label>Blog Content:</label>
      <textarea v-model.lazy="blog.content" cols="30" rows="10"></textarea>
      <div id="checkboxes">
        <label>STEP 1</label>
        <input type="checkbox" value="STEP 1" v-model="blog.categories">
        <label>STEP 2</label>
        <input type="checkbox" value="STEP 2" v-model="blog.categories">
        <label>STEP 3</label>
        <input type="checkbox" value="STEP 3" v-model="blog.categories">
        <label>STEP 4</label>
        <input type="checkbox" value="STEP 4" v-model="blog.categories">
      </div>
      <label>Author: </label>
      <select v-model="blog.author">
        <option v-for="author in authors" :key="author.id">{{ author }}</option>
      </select>
      <button @click.prevent="post">Add Blog</button>
    </form>
    <div v-if="submitted">
      <h3>Thanks for adding your post! :)</h3>
    </div>
    <div id="preview">
      <h3>PREVIEW</h3>
      <p>Blog Title: {{ blog.title }}</p>
      <p>Blog Content: </p>
      <p>{{ blog.content }}</p>
      <p>Blog Categories: </p>
      <ul>
        <li v-for="category in blog.categories" :key="category.id">{{ category }}</li>
      </ul>
      <p>Author: {{ blog.author }}</p>
    </div>
  </div>
</template>

<script>
export default {
  components:{
    'add-blog': addBlog,
    'show-blogs': showBlogs
  },
  data(){
    return{
      blog: {
        title: "",
        content: "",
        author: "",
        categories: []
      },
      authors: ['Jane', 'Kate', 'Sam'],
      submitted: false
    }
  },
  methods:{
    post: function(){
      const axios = require('axios');
      axios.post('https://jsonplaceholder.typicode.com/posts', {
        title: this.blog.title,
        body: this.blog.content,
        userID: 1
      }).then(response => {
        console.log(response);
        this.submitted = true;
      });
    }
  }
}
</script>

<style scoped>
#add-blog *{
  box-sizing: border-box;
}
#add-blog{
  margin: 20px auto;
  max-width: 500px;
}
label{
  display: block;
  margin: 20px 0 10px;
}
input[type="text"], textarea{
  display: block;
  width: 100%;
  padding: 8px;
}
#preview{
  padding: 10px 20px;
  border: 1px dotted #ccc;
  margin: 30px 0;
}
h3{
  margin-top: 10px;
}
#checkboxes input{
  display: inline-block;
  margin-right: 10px;
}
#checkboxes label{
  display: inline-block;
}
</style>