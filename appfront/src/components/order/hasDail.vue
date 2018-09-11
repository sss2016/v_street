<template>
  <div class="area">
  <tab>
    <tab-item selected @on-item-click="onItemClick">未发货</tab-item>
    <tab-item @on-item-click="onItemClick">已发货</tab-item>
    <tab-item @on-item-click="onItemClick">全部订单</tab-item>
  </tab>
  <div class="topSearchBtn" @click="searchShow"
  ></div>
  <div class="content">
    <template v-for="item in Orders">
      
        <order :orderNum="item.fields.ordernum"
          :phone="item.fields.tel"
          :ps="'多点兰尼加'"
          :userName="item.fields.user_name"
          :orderState="item.fields.state"
          :money="item.fields.total"
          v-on:Send="Send"
          v-on:Deleted="Deleted"
          :reason="item.fields.reason"
     >
     </order>
    </template>
      <load-more :show-loading="false" :tip="$t('暂无数据')"  v-if="Orders.length<1" background-color="#fbf9fe"></load-more>
  </div>

  <myTabbar :selectTab="2"></myTabbar>
  </div>
</template>
<script>
import myTabbar from '../myTabbar'
import { Tab, TabItem,LoadMore,Toast} from 'vux'
import order from '../Plug/order.vue'
export default {
  components: {
    myTabbar,
    Tab,
    TabItem,
    order,
    LoadMore,
  },
   mounted(){
    this.getNewOrders(1)
  },
  data () {
    return {
      content:[],
      results: [],
      value: 'test',
      Orders:[],
    }
  },
  methods:{
    onItemClick (index) {
      // this.index=index
      if (index==0) {
          this.getNewOrders(1)
      }else if(index==1){
          this.getNewOrders(2)
      }else{
          this.getNewOrders(-1)
      }
    },
    Send(num){
      this.orderStateTo(num,2)
    },
    Deleted(num){
      // this.orderStateTo(num,2)
    },
     setFocus () {
      this.$refs.search.setFocus()
    },
    resultClick (item) {
      window.alert('you click the result item: ' + JSON.stringify(item))
    },
    getResult (val) {
      console.log('on-change', val)
      this.results = val ? getResult(this.value) : []
    },
    onSubmit () {
      this.$refs.search.setBlur()
      this.$vux.toast.show({
        type: 'text',
        position: 'top',
        text: 'on submit'
      })
    },
    onFocus () {
      console.log('on focus')
    },
    onCancel () {
      console.log('on cancel')
      this.searchShow=false
    },
    searchShow(){
      this.$router.push({
        path:'orderSearch'
      })
    },
    orderStateTo(_ordernum,_state){
      this.$http.get('https://www.ktsweb.cn/alterOrderState?ordernum='+_ordernum+"&state="+_state)
      .then(response => {
        console.log(response)
        // this.list2=this.querySetToArray(response.data.json)
        // this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            // this.Orders=response.body
            // console.log(response)

        }, response => {
            console.log("error");
        });
    }
    ,
    getNewOrders(type){
      this.$http.get('https://www.ktsweb.cn/getMyOrderByType?type='+type).then(response => {
        // this.list2=this.querySetToArray(response.data.json)
        // this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            this.Orders=response.body
            // console.log(this.newOrders)

        }, response => {
            console.log("error");
        });
    }


  }
}
function getResult (val) {
  let rs = []
  for (let i = 0; i < 20; i++) {
    rs.push({
      title: `${val} result: ${i + 1} `,
      other: i
    })
  }
  return rs
}
</script>
<style type="text/css">
  #app,.area,html,body{
    height: 100%;
  }
  .content{
    height: 82%;
    overflow: auto;
  }
  .topSearchBtn{
    display: inline-block;
    width: 30px;
    height: 30px;
    position: fixed;
    bottom: 20%;
    right: 10%;
    background: url("../../assets/搜索.png");
    background-size: 100% 100%;

  }
  .vux-tab-wrap{
    height: 0;
  }
</style>