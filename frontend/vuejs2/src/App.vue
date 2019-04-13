<template>
  <div>
    <form-helper>
      <div slot="form-header">
        <h3>This is the title</h3>
        <p>Info of the form</p>
      </div>
      <div slot="form-fields">
        <input type="text" placeholder="name" required>
        <input type="password" placeholder="password" required>
      </div>
      <div slot="form-controls">
        <button @click="handleSubmit">SUBMIT</button>
      </div>
    </form-helper>
  </div>
</template>

<script>
import formHelper from './components/FormHelper.vue';

export default {
  components:{
    'form-helper': formHelper
  },
  data(){
    return{
      title: "I'm a dynamic title."
    }
  },
  methods:{

  }
}
</script>

<style scoped>
h1{
  color: purple;
}
</style>
