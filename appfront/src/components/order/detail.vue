<template>
  <div>
  		<MyPannel :title="'订单信息'" :keyValue="orderInfo">
  			
  		</MyPannel>
  		<MyPannel :title="'配送信息'" :keyValue="driverInfo">
  			
  		</MyPannel>
  		<MyPannel :title="'服务清单'" :rows="3">
  			<template v-for="i in 3">
  				<div :slot="i" class="imgItem">
  						<div class="headImg">
  							<img src="http://placeholder.qiniudn.com/60x60/3cc51f/ffffff">
  						</div>
  						<div class="textarea">
  							qq
  						</div>

  				</div>
  			</template>
  			<div slot="footer">
  				<div>总价100</div>
  			</div>
  		</MyPannel>
  		
  </div>
</template>
<script>
import MyPannel from '../Plug/MyPannel.vue'
export default {
  components: {
    MyPannel
  },
  methods: {
    
  },
  data () {
    return {
      orderInfo:[
      {
      	key:"订单号",
      	value:"2018445456"
      },
      {
      	key:"订单状态",
      	value:"已发货"
      },
      {
      	key:"创建时间",
      	value:"2018-06-03"
      }
      ],
      driverInfo:[
      	{
      		key:"配送地址",
      		value:"大苏打阿瑟东撒的</br>撒的撒的撒的撒啊撒"
      	}

      ]
    }
  }
}
</script>
<style type="text/css">
	.headImg{
		display: inline-block;
		width: 50px;
		height: 50px;
		float: left;
		background-color: black;
	}
	.textarea{
		display: inline-block;
		width: 77%;
		/*height: 100%;*/
		float: right;
		background-color: red;
	}
	.imgItem{
		overflow: hidden;
	}
	.headImg img{
		height: 100%;
		width: 100%;
	}
</style>