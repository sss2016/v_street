<template>
    
    <tabbar>
      <tabbar-item  link="/notDail" badge="2">
        <img slot="icon" src="../assets/订单.png">
        <span slot="label">未处理</span>
      </tabbar-item>
      <tabbar-item show-dot>
        <img slot="icon" src="../assets/完成.png">
        <span slot="label">已处理</span>
      </tabbar-item>
      <tabbar-item   link="/" selected>
        <img slot="icon" src="../assets/我的.png">
        <span slot="label" >我的</span>
      </tabbar-item>
      <tabbar-item>
        <img slot="icon" src="../assets/设置.png">
        <span slot="label">设置</span>
      </tabbar-item>
    </tabbar>
</template>

<script>

import { Tabbar, TabbarItem, Group, Cell } from 'vux'

export default {
  components: {
    Tabbar,
    TabbarItem,
    Group,
    Cell,
  }
}
</script>
<style type="text/css">
	.weui-tabbar__item{
		text-decoration: none;
	}
	.weui-tabbar{
		left: 0;
	}

</style>