<template>
  <group>
     <x-input title="价格" name="username" placeholder="请输入商品价格" v-model="price" ></x-input>
     <x-button type="primary" @click.native="complete">完成</x-button>
  </group>
</template>
<script type="text/javascript">
  import {Group,XInput,XButton } from 'vux'
  export default{
    data(){
      return {
        goods_id:this.$route.query.goods_id,
        price:null
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
                this.price =  the_item.price
              },response=>{
                console.log("error")
              })
        },
        onEvent (event) {
            console.log('on', event)
        },
        complete(){
          this.$http.post("updateItem",{goods_id:this.goods_id,price:this.price})
            .then(
              response=>{
                this.$router.replace({path:'items',query:{goods_id:this.goods_id}})
              },response=>{
                console.log("error")
              })
        }
    },
    components:{
      Group,XInput,XButton
    }

  }

</script>