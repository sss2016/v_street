<template>
	<group>
	   <x-textarea  title="描述" :max="200"  name="username" placeholder="请输入商品描述" v-model="dec" @on-focus="onEvent('focus')" @on-blur="onEvent('blur')"></x-textarea >
	   <x-button type="primary" @click.native="complete">完成</x-button>
	</group>
</template>
<script type="text/javascript">
	import {Group,XTextarea,XButton} from 'vux'
	export default{
		data(){
			return {
				goods_id:this.$route.query.goods_id,
				dec:null
			}
		},
		mounted(){
			this.getTheGoodInfo()
		},
		methods:{
			 getTheGoodInfo(){
			      this.$http.get("getGoodsItem?goods_id="+this.goods_id)
			      .then(
			        response=>{
			          var the_item = response.data[0].fields
			          this.dec =  the_item.describe
			        },response=>{
			          console.log("error")
			        })
    		},
    		onEvent (event) {
      			console.log('on', event)
    		},
    		complete(){
    			this.$http.post("updateItem",{goods_id:this.goods_id,describe:this.dec})
			      .then(
			        response=>{
			          this.$router.replace({path:'items',query:{goods_id:this.goods_id}})
			        },response=>{
			          console.log("error")
			        })
    		}
		},
		components:{
			Group,XTextarea,XButton
		}

	}
</script>