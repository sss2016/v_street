<template>
    <div class="area">
      <div class="myhead">
        <div class="myhead-left">
            <span>今日营业统计</span>
        </div>
        <div class="myhead-right">
            <span>单击查看详情</span>
        </div>
        <div style="clear:both;"></div>
      </div>
      <div class="card-demo-flex card-demo-content01 Statistics">
        <div class="vux-1px-r">
          <span> 1130</span>
          <br/>
          余额
        </div>
        <div >
          <span>15</span>
          <br/>
          订单数
        </div>
      </div>
      <card>
        <div slot="content" class="card-demo-flex card-demo-content01">
          <div class="vux-1px-r">
            余额<span>15</span>
          </div>
          <div >
            订单数
          </div>
      </div>
    </card>
    <div class="menu">
      <grid :cols="3" :show-lr-borders="false">
            <grid-item label="店铺信息" link="/shopInfo">
              <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
          </grid-item>
        
         <grid-item label="商品管理" link="/goods">
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
        <grid-item label="品类管理" link="/typeManage">
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
                 <grid-item label="商品评价" >
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
                 <grid-item label="店铺信息" >
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
                 <grid-item label="店铺信息" >
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
      </grid>
        <divider>我是有底线的</divider>
    </div>

<myTabbar :selectTab="3"></myTabbar>
    </div>


</template>
<script>

import myTabbar from '../myTabbar'

import { Divider, Card,Grid, GridItem } from 'vux'

export default {
  components: {
    Card,
    Divider,
    Grid,
    GridItem,
    myTabbar
  }

}
    console.log(1)

</script>

<style scoped lang="less">
@import '~vux/src/styles/1px.less';

.card-demo-flex {
  display: flex;
  background-color: white;
}
.card-demo-content01 {
  padding: 10px 0;
}
.card-padding {
  padding: 15px;
}
.card-demo-flex > div {
  flex: 1;
  text-align: center;
  font-size: 15px;
}
.Statistics span {
  color: #f74c31;
  font-size:20px;
}
body{
    background-color: #eee;

}
.myhead-left{
  float:left;
  padding-left:25px;
}
.myhead-right{
  float:right;
  padding-right:25px;
}
.myhead{
  padding:5px;
  background-color: white;

}
.menu{
  margin-top:20px;
  background-color: white;
}
.weui-panel{
  margin-top:0px;
}
</style>