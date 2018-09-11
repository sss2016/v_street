 <template>
    <div class="order">
          <div class="header">
              <div class="content">
                  订单编号:
                  <span >
                    {{orderNum}}
                  </span>
              </div>
          </div>
          <div class="body" @click="routerSwich">
            <div class="body-items">
                <span class="body-items-title">
                  订单状态：
                </span>
                  <span class="value" v-if="orderState==0">
                    等待接单
                </span>
                <span class="value" v-else-if="orderState==1">
                    等待发货
                </span>
                <span class="value" v-else-if="orderState==2">
                    已发货
                </span>
                <span class="value" v-else-if="orderState==3">
                    订单完成
                </span>
                <span class="value" v-else-if="orderState==4">
                    订单取消
                </span>
                <span class="value" v-else-if="orderState==5">
                    拒绝接单
                </span>
              </div>
              <div class="body-items">
                <span class="body-items-title">
                  客户姓名：
                </span>
                <span class="value">
                  {{userName}}
                </span>
              </div>
              <div class="body-items">
                <span class="body-items-title">
                  客户电话：
                </span>
                  <span class="value">
                  {{phone}}
                </span>
              </div>
              <div class="body-items">
                <span class="body-items-title">
                  客户备注：
                </span>
                  <span class="value">
                  {{ps}}
                </span>
              </div>
              <div class="body-items">
                <span class="body-items-title">
                  订单金额：
                </span>
                  <span class="value">
                  ￥{{money}}
                </span>
              </div>
               <div class="body-items" v-if="reason" style="color:green">
                <span class="body-items-title">
                  拒绝理由：
                </span>
                  <span class="value">
                  {{reason}}
                </span>
              </div>
          </div>
          <div class="footer">
              <div class="content" style="padding-top: 10px;" v-if="orderState==0">
                 <div class="button nobtn" @click="$emit('Deny',orderNum)">
                    拒绝接单
                  </div>
                  <div class="button yesbtn" @click="$emit('Agree',orderNum)">
                    立即接单
                  </div>
              </div>
              <div class="content" style="padding-top: 10px;" v-else-if="orderState==1">
                  <div class="button yesbtn" @click="$emit('Send',orderNum)">
                    发货
                  </div>
              </div>
               <div class="content" style="padding-top: 10px;" v-else-if="orderState==4">
                  <div class="button yesbtn" @click="$emit('Deleted',orderNum)">
                    删除
                  </div>
              </div>

             
          </div>

      </div>
 </template>
 <script type="text/javascript">
   export default{
    props:{
        orderNum:{
          default:null
        },
        phone:{
          default:false
        },
        ps:{
          default:""
        },
        userName:{
          default:null
        },
        orderState:{
          default:null
        },
        money:{
          default:null
        },
        link:{
          default:null
        },
        reason:{
          default:null
        }

    },
    data(){
      return {

      }
    },
    methods:{
      routerSwich(){
        this.$router.push(this.link)
      }
    }
   }
 </script>
 <style type="text/css">
   .order .header,.body,.footer{
  padding: 5px;
}
.order .footer{

}
.order .header .content{
  font-size: 20px;
  border-bottom: 1px dashed #eee;
}
.order .footer .content{
  border-top: 1px dashed #eee;
  text-align: right;
}

.order .content{
  padding-bottom: 5px;
}
.order .body .body-items{

}
.body-items .body-items-title{
  font-size: 16px;
  font-weight: 10px;
}
.value{
  color: gray;
}
.order .footer .button{
  /*width: 50px;*/
  height: 20px;
  
  display: inline-block;
  border-radius: 5px;
  text-align: center;
  
  padding:0 10px; 
  cursor: pointer;
}
.yesbtn{
  background-color: rgb(242,130,2);
  color: white;
}
.nobtn{
  background-color: #eee;
  color: black;
}
 .order{

    width: 100%;
    /*height: 20%;*/
    background-color: white;
    border-radius: 5px;
    margin-top: 10px;

  }
 </style>