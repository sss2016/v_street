<template>
  <div class="area">
  <div class="show">
    <template v-for="item in newOrders">
      
        <order :orderNum="item.fields.ordernum"
          :phone="item.fields.tel"
          :ps="'多点兰尼加'"
          :userName="item.fields.user_name"
          :orderState="item.fields.state"
          :money="item.fields.total"
          v-on:Deny="onDeny"
          v-on:Agree="onAgree"

     >
     </order>
    </template>
           <load-more :show-loading="false" :tip="$t('暂无数据')"  v-if="newOrders.length<1" background-color="#fbf9fe"></load-more>

    <!-- <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list" :footer-buttons="buttons1"></form-preview>
    <br>
    <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list" :footer-buttons="buttons2" name="demo"></form-preview>
    <br>
    <form-preview :header-label="$t('付款金额')" header-value="¥2400.00" :body-items="list"></form-preview> -->
  </div>
     <confirm v-model="DenyShow"
      show-input
      ref="confirm5"
      title="请输入拒接理由"
      @on-confirm="DenyOrder"
      >
      </confirm>
      <confirm v-model="show"
      title="提示"
      @on-confirm="AgreeOrder"
      >
        <p style="text-align:center;">确定要接单吗？</p>
      </confirm>
      <toast v-model="showPositionValue" type="text" :time="800" is-show-mask text="接单成功" ></toast>

  <myTabbar :selectTab="1" :notDail="newOrders.length"></myTabbar>
  </div>
</template>
<script>
    
import { FormPreview ,LoadMore,Toast,Confirm} from 'vux'
import myTabbar from '../myTabbar'
import order from '../Plug/order.vue'

export default {
  components: {
    FormPreview,
    myTabbar,
    order,
    LoadMore,
    Toast,
    Confirm
  },
  data () {
    return {
        newOrders:[],
      showPositionValue:false,
      show:false,
      DenyShow:false,
      curSelOrderNum:null
    }
  },
  mounted(){
    this.getNewOrders()
  },
  methods:{
    onDeny(num){
        this.curSelOrderNum=num
        this.DenyShow=true
    },
    onAgree(num){
        this.curSelOrderNum=num
        this.show=true
    }
    ,
    DenyOrder(reason){
     var _ordernum=this.curSelOrderNum
     var _state = 5
      this.$http.get('https://www.ktsweb.cn/denyOrder?ordernum='+_ordernum+"&state="+_state+'&reason='+reason).then(response => {
            console.log(response)
        }, response => {
            console.log("error");
        });
      // this.orderStateTo()
    },
    AgreeOrder(){
      this.orderStateTo(this.curSelOrderNum,1)
      this.showPositionValue=true;
    },
    getNewOrders(){
      this.$http.get('https://www.ktsweb.cn/getMyOrderByType?type=0').then(response => {
        // this.list2=this.querySetToArray(response.data.json)
        // this.shop_id = response.data.shop_id
             // this.list3=response.data;
            // get body data
            // this.someData = response.body;
            this.newOrders=response.body
            console.log(response)

        }, response => {
            console.log("error");
        });
    }
    ,
    orderStateTo(_ordernum,_state){
      // console.log(ordernum,state)
      this.$http.get('https://www.ktsweb.cn/alterOrderState?ordernum='+_ordernum+"&state="+_state).then(response => {
            console.log(response)
        }, response => {
            console.log("error");
        });
    },
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
  height: 88%;
  overflow-y: auto;
}

</style>