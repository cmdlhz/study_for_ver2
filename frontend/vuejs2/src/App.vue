<template>
  <div>
    <keep-alive>
      <component :is="component"></component>
    </keep-alive>
    <button @click="component = 'form-one'">Show Form 1</button>
    <button @click="component = 'form-two'">Show Form 2</button>
  </div>
</template>

<script>
import formOne from './components/FormOne.vue';
import formTwo from './components/FormTwo.vue';

export default {
  components:{
    'form-one': formOne,
    'form-two': formTwo
  },
  data(){
    return{
      component: 'form-one'
    }
  },
  methods:{

  }
}
</script>

<style scoped>

</style>
