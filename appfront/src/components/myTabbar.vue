 <template>
     <tabbar slot="bottom" >
    <tabbar-item  link="/notDail" badge="2" index="1" :selected="selectTab==1">
      <img slot="icon" src="../assets/订单.png">
      <span slot="label">未处理</span>
    </tabbar-item>
    <tabbar-item show-dot link="hasDail" index="2" :selected="selectTab==2">
      <img slot="icon" src="../assets/完成.png">
      <span slot="label">已处理</span>
    </tabbar-item>
    <tabbar-item   link="/" index="3" :selected="selectTab==3">
      <img slot="icon" src="../assets/我的.png">
      <span slot="label" >我的</span>
    </tabbar-item>
    <tabbar-item index="4" :selected="selectTab==4"> 
      <img slot="icon" src="../assets/设置.png">
      <span slot="label">设置</span>
    </tabbar-item>
  </tabbar> 


 </template>
 <script type="text/javascript">
   
   import {Tabbar,TabbarItem } from 'vux'
export default {
  components:{
    Tabbar,
    TabbarItem
  },
    name: 'myTabbar',
    props:{
      selectTab:{
         default: 1
      }
    },

  }
 </script>
<style scoped>

html, body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
  text-decoration: 
}
.area{
    height: 88.5%;
    display: inline-block;
    overflow: auto;
    position: absolute;
}
.weui-tabbar a{
      height: 11.5%;
      text-decoration: none;
}
</style>