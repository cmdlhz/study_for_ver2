import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueRouter from 'vue-router'
import Routes from './router'

Vue.prototype.$http = axios;
Vue.use(VueRouter);

const router = new VueRouter({
  routes : Routes  
});

Vue.config.productionTip = false
Vue.prototype.$http = axios;

export const bus = new Vue();

// Custom Directives
Vue.directive('theme', {
  bind(el,binding){
    if(binding.value=='wide'){
      el.style.maxWidth = '1200px';
    } else if(binding.value=='narrow'){
      el.style.maxWidth = '600px';
    }
    if(binding.arg =='column'){
      el.style.background = '#ddd';
      el.style.padding = '20px';
    }
  }
});

// Filters
// Vue.filter('to-uppercase', value => value.toUpperCase());
// Vue.filter('snippet', value => value.slice(0,100) + '...');

new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
