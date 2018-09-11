<template>
      <div style="height:100%">
    
       <tab :line-width=2 active-color='#fc378c' v-model="index" style="padding-top: 0px;" 
        >
       <tab-item class="vux-center" :selected="demo2 === item.key" v-for="item in list2" @click="demo2 = item.key" :key="item.key">
       {{item.value}}</tab-item>
      </tab>
      <swiper v-model="index"  :show-dots="false">
        <swiper-item v-for="item in list2" :key="item.key" >
    <scroller height="-46" lock-x scrollbar-y :use-pullup="true" :pullup-config="pullupConfig2"  ref="scroller" @on-pullup-loading="load2" v-model="scrolleStatus">
              <div >
                  <div  class="good_item" v-for="good_item in list3">
                    <router-link :to="{
                      path:'/items',
                      query:{
                        goods_id:good_item.pk
                      }
                    }">
                              <div class="photo">
                                   <img  :src="'/getGoodsImage?goods_image='+shop_id+'_'+good_item.pk" alt="">
                              </div>
                            <div class="dec">
                                <p class="title">{{good_item.fields.name}}</p>
                                <p class="content">{{good_item.fields.describe}}</p>
                                <span class="price">{{good_item.fields.price}}￥</span>
                            </div>
                    </router-link>

                </div>
            <!--    <load-more tip="loading" v-if="page<=pageTotal"></load-more>
               <load-more   v-else :show-loading="false" tip="没有更多" background-color="#fbf9fe"></load-more> -->
               <load-more  v-if="list3.length<1" :show-loading="false" :tip="$t('暂无数据')" background-color="#fbf9fe"></load-more>
            </div>
          </scroller>
            
        </swiper-item>
      </swiper>
      
      <navFix></navFix>
    </div>
</template>
<script>
import { Tab, TabItem,Scroller,Swipeout,Swiper, SwiperItem,SwipeoutButton,SwipeoutItem,Panel,LoadMore } from 'vux'
import navFix from "../fix_nav"
export default {
  components: {
    Tab,
    TabItem,
    Swiper,
    SwiperItem,
    SwipeoutButton,
    Swipeout,
    navFix,
    Panel,
    SwipeoutItem,
    LoadMore,
    Scroller
  },
  data () {
    return {
      disabled: false,
      index01: 0,
      list2:  [],
      demo2: '美食',
      list3: [],
      list4: [],
      demoDisabled: 'A',
      index: 0,
      type: '1',
      page:1,
      pageTotal:2,
      shop_id:null,
      pullupConfig2: {
        content: '上拉加载更多',
        downContent: '松开进行加载',
        upContent: '上拉加载更多',
        loadingContent: '加载中...'
      },
      scrolleStatus:{pullupStatus:'default'}
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

  },
  methods: {
    load2 () {
      let _this = this
      // console.log(_this.$refs.scroller[0].donePullup())
      setTimeout(() => {
          _this.ToBottom()
        setTimeout(() => {
          _this.$refs.scroller[0].donePullup()
        }, 100)
        if (_this.page == _this.pageTotal) { // unload plugin
          setTimeout(() => {
            _this.$refs.scroller[0].disablePullup()
          }, 100)
        }
      }, 2000)
      //       // var _this=this
      this.$nextTick(() => {
        _this.$refs.scroller[0].reset()
      })
    },
    getTypes(){
      this.$http.get('https://www.ktsweb.cn/getGoodsTypes').then(response => {
        this.list2=this.querySetToArray(response.data.json)
        this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
        this.getGoodsByType(this.list2[this.index].key)
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
      if (newObj.length<1) {
        newObj.push({
          key:-1,
          value:"暂无任何分类"
        })
      }
      return newObj
    },
    ToBottom(){
    this.getGoodsByType(this.list2[this.index].key)
    },
    getGoodsByType (index) {
      this.$vux.loading.show({
        text: 'loading'
      })
      // setTimeout(() => {
      //   this.$vux.loading.hide()
      //   this.index01 = index
      // }, 1000)
      this.$http.get('https://www.ktsweb.cn/getGoodsList?type_id='+index+'&size='+8+'&page='+this.page).then(response => {
        // https://www.ktsweb.cn
          var result = JSON.parse(response.data.data);
          this.pageTotal=response.data.pages
          for (var i = 0; i < result.length; i++) {
            this.list3.push(result[i])
          }
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            this.page++;
            this.$vux.loading.hide()
            if (_this.page >= _this.pageTotal) {
              this.$refs.scroller[0].disablePullup()
            }
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