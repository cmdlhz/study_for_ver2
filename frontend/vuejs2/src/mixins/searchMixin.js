export default{
  computed:{
    filteredBlogs: function(){
      return this.blogs.filter(blog => {
        return blog.title.match(this.search) || blog.body.match(this.search);
      });
    }
  }
}