import Vue from 'vue'
import App from './App.vue'
// import Ninjas from './components/Ninjas.vue'

Vue.config.productionTip = false

// Vue.component('ninjas', Ninjas);
export const bus = new Vue();

new Vue({
  render: h => h(App),
}).$mount('#app')
