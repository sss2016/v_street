import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(VueResource);
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name:'index',
      component:resolve=>require(['@/components/mycontrolTab/index.vue'] , resolve),//懒加载
       meta: {
        title: '我的'
      }
    },
    {
      path:'/notDail',
      name:'notDail',
      component:resolve=>require(['@/components/order/notDail.vue'] , resolve),//懒加载
       meta: {
        title: 'notDail'
      }
    },
    {
      path:'/hasDail',
      name:'hasDail',
      component:resolve=>require(['@/components/order/hasDail.vue'] , resolve),//懒加载
       meta: {
        title: 'hasDail'
      }
    },
     {
      path:'/shopInfo',
      name:'shopInfo',
      component:resolve=>require(['@/components/page/shopInfo.vue'] , resolve),//懒加载
       meta: {
        title: 'shopInfo'
      }
    },
      {
      path:'/goods',
      name:'goods',
      component:resolve=>require(['@/components/page/goods.vue'] , resolve),//懒加载
       meta: {
        title: 'goods'
      }
    },
     {
      path:'/items',
      name:'items',
      component:resolve=>require(['@/components/items.vue'] , resolve),//懒加载
       meta: {
        title: 'items',
        keepAlive: false // 需要被缓存

      }
    },
    {
      path:'/upload',
      name:'upload',
      component:resolve=>require(['@/components/Plug/upload.vue'] , resolve),//懒加载
       meta: {
        title: 'upload'
      }
    },
    {
      path:'/addGoods',
      name:'addGoods',
      component:resolve=>require(['@/components/page/addGoods.vue'] , resolve),//懒加载
      meta: {
          keepAlive: true // 需要被缓存
      }
    },
    {
      path:'/standards',
      name:'standards',
      component:resolve=>require(['@/components/alterPage/standards.vue'] , resolve),//懒加载
       meta: {
        title: 'standards'
      }
    },
    {
      path:'/typeManage',
      name:'typeManage',
      component:resolve=>require(['@/components/page/typeManage.vue'] , resolve),//懒加载
       meta: {
        title: 'standards'
      }
    },
    {
      path:'/alterDec',
      name:'alterDec',
      component:resolve=>require(['@/components/alterPage/alterDec.vue'] , resolve),//懒加载
       meta: {
        title: 'alterPage'
      }
    },
    {
      path:'/alterName',
      name:'alterName',
      component:resolve=>require(['@/components/alterPage/alterName.vue'] , resolve),//懒加载
       meta: {
        title: 'alterName'
      }
    },
    {
      path:'/alterPrice',
      name:'alterPrice',
      component:resolve=>require(['@/components/alterPage/alterPrice.vue'] , resolve),//懒加载
       meta: {
        title: 'alterPrice'
      }
    },

  ]
})
