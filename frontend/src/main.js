// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './mock.js';
import axios from 'axios';
import "@/assets/fonts/font1.css";
import VideoBg from 'vue-videobg';
import BaiduMap from 'vue-baidu-map';
import {VueJsonp} from 'vue-jsonp';

Vue.use(VueJsonp);

Vue.use(BaiduMap, {
  ak: 'umawrZEEKAx20cCK1NHsRLmLYwmgpURB'    //这个地方是官方提供的ak密钥
});

Vue.component('video-bg', VideoBg);


// console.log(VueJsonp.install)

//require('.mock');

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App,VideoBg },
  template: '<App/>'
}).$mount('#app')
