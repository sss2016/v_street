<template>
    <div class="area">
      <group style="overflow:hidden" class="shopInfo">
        <cell-box is-link>
        <div class="headImg">
            <img src="https://ss0.baidu.com/73F1bjeh1BF3odCf/it/u=926886369,3147214923&fm=85&s=F13B30D68C44BD4F12AA18930300D089">

        </div>
        <div class="headInfo">
            <div>
                  dasada
            </div>
            <div>
                dasdasd
            </div>
        </div>
        </cell-box>
    </group>
   
      <div class="myhead">
        <div class="myhead-left">
            <span>营业统计</span>
        </div>
        <div class="myhead-right">
            <span>单击查看详情</span>
        </div>
        <div style="clear:both;"></div>
      </div>
      <div class="card-demo-flex card-demo-content01 Statistics">
        <div class="vux-1px-r">
          <span> {{orderCount}}</span>
          <br/>
          累计余额
        </div>
        <div >
          <span>{{money}}</span>
          <br/>
          订单数
        </div>
      </div>
      <group style="overflow:hidden">
        <cell-box is-link>
        <div class="notify">
            <img src="../../assets/通知.png">
        </div>
        <div class="msgInfo">
             <ul class="msg">
               <li>dsds</li>
                <li>dasda</li>
             </ul>
        </div>      
        </cell-box>
    </group>
    <div class="menu">
      <grid :cols="3" :show-lr-borders="false">
            <grid-item label="店铺信息" link="/shopInfo">
              <img slot="icon" class="grid-center" src="../../assets/店铺.png">
          </grid-item>
        
         <grid-item label="商品管理" link="/goods">
          <img slot="icon" class="grid-center" src="../../assets/购物袋.png">
        </grid-item>
        <grid-item label="品类管理" link="/typeManage">
          <img slot="icon" class="grid-center" src="../../assets/分类.png">
        </grid-item>
                 <grid-item label="商品评价" >
          <img slot="icon" class="grid-center" src="../../assets/消息.png">
        </grid-item>
                 <grid-item label="店铺信息" >
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
                 <grid-item label="店铺信息" >
          <img slot="icon" class="grid-center" src="../../assets/grid_icon.png">
        </grid-item>
      </grid>
    </div>
        <divider>我是有底线的</divider>
<myTabbar :selectTab="3"></myTabbar>
    </div>


</template>
<script>

import myTabbar from '../myTabbar'

import { Divider, Card,Grid, GridItem,CellBox,Group  } from 'vux'

export default {
  components: {
    Card,
    Divider,
    Grid,
    GridItem,
    myTabbar,
    CellBox ,
    Group
  },
  mounted(){
    this.getMyCount()
  },
  methods:{
    getMyCount(){
      this.$http.get('https://www.ktsweb.cn/getMyCount').then(response => {
            console.log(response)
            this.orderCount = response.body.num
            this.money = response.body.Alltotal
        }, response => {

        });
    }
  },
  data(){
    return {
      orderCount:0,
      money:0
    }
  }

}

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
.notify img{
      width: 40px;
    height: 45px;
}
.msg{
  margin:0;
}
.headInfo{
  padding-left:20px;
}
</style>
<style type="text/css">
  
  .weui-grid__label span{
    display:inline-block;
  }
  .headImg{
    height: 65px;
    width: 65px;
    border: 3px solid black;
  }
  .headImg img{
    width: 100%;
    height: 100%;
  }
  .area .shopInfo .weui-cells{
  margin-top:0px;
}
</style>