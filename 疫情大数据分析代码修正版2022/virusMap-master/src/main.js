// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import JsonExcel from 'vue-json-excel'
import FileSaver from 'file-saver'
import XLSX from 'xlsx'
import echarts from 'echarts';

Vue.prototype.$echart = echarts

Vue.prototype.$FileSaver = FileSaver // 设置全局
Vue.prototype.$XLSX = XLSX // 设置全局
Vue.component('downloadExcel', JsonExcel)
Vue.prototype.$http = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  // store,
  router,
  render: h => h(App)
}).$mount("#app")