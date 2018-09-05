<template>
      <div style="height:100%">
    
       <tab :line-width=2 active-color='#fc378c' v-model="index" style="padding-top: 0px;" 
        >
       <tab-item class="vux-center" :selected="demo2 === item.key" v-for="item in list2" @click="demo2 = item.key" :key="item.key">
       {{item.value}}</tab-item>
      </tab>
      <swiper v-model="index"  :show-dots="false">
        <swiper-item v-for="item in list2" :key="item.key" >
            <template v-for="good_item in list3">
                  <div  class="good_item">
                    <router-link :to="{
                      path:'/items',
                      query:{
                        goods_id:good_item.pk
                      }
                    }">
                              <div class="photo">
                                   <img  :src="'/getGoodsImage?goods_id='+good_item.pk" alt="">
                              </div>
                            <div class="dec">
                                <p class="title">{{good_item.fields.name}}</p>
                                <p class="content">{{good_item.fields.describe}}</p>
                                <span class="price">{{good_item.fields.price}}￥</span>
                            </div>
                    </router-link>

                  </div>
            </template>
        </swiper-item>
      </swiper>
      
      <navFix></navFix>
    </div>
</template>
<script>
import { Tab, TabItem, Sticky, Divider,  Swipeout,Swiper, SwiperItem,SwipeoutButton,SwipeoutItem,Panel } from 'vux'
import navFix from "../fix_nav"
const list = () => [{key:"1",value:'精选'}, {key:"2",value:'美食'}, {key:"3",value:'电影'}, {key:"4",value:'酒店'}, {key:"5",value:'外卖'}]

export default {
  components: {
    Tab,
    TabItem,
    Sticky,
    Divider,
    Swiper,
    SwiperItem,
    SwipeoutButton,
    Swipeout,
    navFix,
    Panel,
    SwipeoutItem
  },
  data () {
    return {
      disabled: false,
      index01: 0,
      list2: list(),
      demo2: '美食',
      list3: [],
      demo3: '收到的消息',
      list4: [],
      demo4: '即将上映',
      demoDisabled: 'A',
      index: 0,
      type: '1',
    }
  },
  watch: {
  index: function () {
      this.getGoodsByType(this.list2[this.index].key)
  }
}
  ,
  mounted: function () {
      this.getTypes()
        this.getGoodsByType(this.list2[this.index].key)
  },
  methods: {
    getTypes(){
      this.$http.get('http://localhost:8000/getGoodsTypes').then(response => {
        this.list2=this.querySetToArray(response.data)
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;

        }, response => {
            console.log("error");
        });
    },
    querySetToArray(obj){
      var newObj=[]
      for( var i=0;i<obj.length;i++){
        newObj.push(
        {
          key:obj[i].pk,
          value:obj[i].fields.name
        })
      }
      return newObj
    },
    getGoodsByType (index) {
      // this.$vux.loading.show({
      //   text: 'loading'
      // })
      // setTimeout(() => {
      //   this.$vux.loading.hide()
      //   this.index01 = index
      // }, 1000)
      this.$http.get('http://localhost:8000/getGoodsList?type_id='+index).then(response => {
             this.list3=response.data;
            // get body data
            // this.someData = response.body;

        }, response => {
            console.log("error");
        });
    }
  }
}
</script>

<style lang="less" scoped>
@import '~vux/src/styles/1px.less';
@import '~vux/src/styles/center.less';
.box {
  padding: 15px;
}
.active-6-1 {
  color: rgb(252, 55, 140) !important;
  border-color: rgb(252, 55, 140) !important;
}
.active-6-2 {
  color: #04be02 !important;
  border-color: #04be02 !important;
}
.active-6-3 {
  color: rgb(55, 174, 252) !important;
  border-color: rgb(55, 174, 252) !important;
}
.tab-swiper {
  background-color: #fff;
  height: 100px;
}
.demo-content {
  padding: 10px 10px;
}
.good_item .price,.title,.content{
    margin:0;
}
.good_item{
  display:inline-block;
  width:100%;
  text-decoration: none;
  background-color:white;
  margin-top:5px;
  height:17%;
}
.good_item a{
  width: 100%;
}
.good_item .photo img{
  width:100%;
  height:100%;
}
.good_item .dec{
  float:right;
  width:70%;
}
.good_item .title{

  font-size:15px;
  color:black;

}
.good_item .content{
  font-size:10px;
  color:gray;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  height: 30px;
}
.good_item .price{
  color:red;
}
.good_item .oporate{
  margin:0;
  font-size:10px;
  color:black;
  text-align:right;
  padding-right:20px;
}
.good_item button{
  margin:0;
}
.good_item a{
  display:inline-block;
  height:100%;
}
.good_item .photo{
  float:left;
  width:28%;
  height:100%;
}
.vux-slider > .vux-swiper > .vux-swiper-item{
    overflow: auto;

}
</style>
<style type="text/css">
  .vux-tab-wrap{
    height: 7%;
  }
  .vux-slider{
    height: 93%;

  }
#app{
  height:100%;
}
.vux-swiper{
  height:100%!important;
}
html,body {
  height: 100%;
  width: 100%;
  overflow-x: hidden;
}
</style>