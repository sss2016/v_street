<template>
  <div class="area">
  	 <search
  	 v-model="search"
  	 @on-submit="findOrders"
      ref="search"></search>
  <div class="show">
    <template v-for="item in searchData">
      
        <order :orderNum="item.fields.ordernum"
          :phone="item.fields.tel"
          :ps="'多点兰尼加'"
          :userName="item.fields.user_name"
          :orderState="item.fields.state"
          :money="item.fields.total"
          v-on:Deny="DenyOrder"
          v-on:Agree="AgreeOrder"

     >
     </order>
    </template>
           <load-more :show-loading="false" :tip="$t('暂无数据')"  v-if="searchData.length<1" background-color="#fbf9fe"></load-more>

    <!-- <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list" :footer-buttons="buttons1"></form-preview>
    <br>
    <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list" :footer-buttons="buttons2" name="demo"></form-preview>
    <br>
    <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list"></form-preview> -->
  </div>
  </div>
</template>
<script>
import {LoadMore,Search} from 'vux'
import order from '../Plug/order.vue'

export default {
  components: {
    order,
    Search,
    LoadMore
  },
  data () {
    return {
        searchData:[],
        search:null
    }
  },
  mounted(){
    // this.getNewOrders()
  },
  methods:{
    DenyOrder(num){
      this.orderStateTo(num,4)
    },
    AgreeOrder(num){
      this.orderStateTo(num,1)
    },
    findOrders(data){
    	 console.log(data);
      this.$http.get('http://localhost:8000/findOrders?rule='+this.search).then(response => {
        // this.list2=this.querySetToArray(response.data.json)
        // this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            this.searchData=response.body
            console.log(response)

        }, response => {
            console.log("error");
        });
    }
    ,
    orderStateTo(_ordernum,_state){
      // console.log(ordernum,state)
      this.$http.get('http://localhost:8000/alterOrderState?ordernum='+_ordernum+"&state="+_state).then(response => {
        // this.list2=this.querySetToArray(response.data.json)
        // this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            // this.newOrders=response.body
            console.log(response)

        }, response => {
            console.log("error");
        });
    }
  }
}
</script>
<style type="text/css">
  .order{

    width: 100%;
    /*height: 20%;*/
    background-color: white;
    border-radius: 5px;
    margin-top: 10px;

  }
  #app,.area,html,body{
    height: 100%;
  }
.show{
  height: 100%;
  overflow-y: auto;
}

</style>