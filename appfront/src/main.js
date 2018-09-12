// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueI18n from 'vue-i18n'
import Vuetree from './components/vue-simple-tree'
import "font-awesome/css/font-awesome.min.css"
import $ from 'jquery'
import  { LoadingPlugin } from 'vux'
Vue.use(LoadingPlugin)

// 或者umd方式
// 引入构建的js文件
// Vue.use(vuxLoadingPlugin)
Vue.use(Vuetree);
Vue.use(VueI18n)
$.ajaxSetup({

dataType: "json",  
  beforeSend: function(xhr, settings){  
      var csrftoken = $('meta[name="csrf_token"]').attr('content') 
      xhr.setRequestHeader("X-CSRFToken", csrftoken);  
  },
})
Vue.http.headers.common['X-CSRFToken'] = $('meta[name="csrf_token"]').attr('content')

Vue.config.productionTip = false
    const i18n = new VueI18n({
        locale: "en-US",    // 语言标识
        messages: {
            'zh-CN': require('../common/lang/zh.js'),   // 中文语言包
            'en-US': require('../common/lang/en.js')    // 英文语言包
        }
    })
window.mycache={
  standards:null
}
new Vue({
  el: '#app',
  router,
  i18n,
  components: { App },
  template: '<App/>'
})