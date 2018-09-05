<template>
  <div>
    <upload :path="'/getGoodsImage?goods_id='+($route.query?$route.query.goods_id:$route.params.goods_id)" :isAutoUpload="true">
    </upload>
    <group class="myform">
      <cell title="商品名称"  is-link :link="{name:'alterName',query:{goods_id:this.goods_id}}">
        {{name}}
      </cell>
      <cell title="商品价格"  is-link :link="{name:'alterPrice',query:{goods_id:this.goods_id}}">
        {{price}}
      </cell>
      <cell title="规格"  is-link :link="{
        name:'standards',
        params: {        
                type: 1,
                goods_id:this.goods_id,
                treeData:guige
            }

      }">
        已设置{{guige.length}}个规格
      </cell>
       <popup-picker 
     :title="title1" 
     :data="list1" 
      v-model="value1" 
      show-name
      :columns="1"
      placeholder="please select"
      @on-change="changes"
      ></popup-picker>
      </cell>
      <cell title="描述"  is-link v-model="dec" :link="{name:'alterDec',query:{goods_id:this.goods_id}}">
      </cell>
    </group>
    <div class="picker-buttons">
      <x-button type="warn" @click.native="downdelete=true">删除该商品</x-button>
    </div>
    <div v-transfer-dom>
      <confirm v-model="downdelete"
      @on-confirm="deleteGoods"
      title="操作提示">
      <p style="color:red">确定咩？</p>
      </confirm>
    </div>
    <loading :show="deling" text="删除中"></loading>
  </div>
</template>
<style type="text/css">
  .myform p{
    margin: 0;
  }
</style>
<script>
import { Group, Cell, XTextarea,XButton,CellBox,PopupPicker,Confirm,TransferDomDirective as TransferDom,Loading  } from 'vux'
import upload from './Plug/upload.vue'
export default {
  directives: {
    TransferDom
  },
  data(){
    return {
      guige:[],
      name:"",
      price:"",
      type:"",
      dec:"",
      goods_id:null,
      title1: '类型',
      list1: [],
      value1: [],
      downdelete:false,
      deling:false
    }
  },
  mounted(){
    this.goods_id=this.$route.query.goods_id
    this.getTheGoodInfo()
    this.getTypes()
  },
  methods:{
    getTheGoodInfo(){
      this.$http.get("getGoodsItem?goods_id="+this.goods_id)
      .then(
        response=>{
          console.log(response.data)
          var the_item = response.data[0].fields
          this.guige = JSON.parse(the_item.standards)
          this.name =  the_item.name
          this.price = the_item.price
          this.dec   = the_item.describe
          this.value1.push(the_item.type)
          console.log(the_item.type)
        },response=>{

          console.log("error")
        })
    },
    changes(value){
      console.log(value)
        this.$http.post('http://localhost:8000/updateItem',
        {
            "goods_id":this.goods_id,
            "type":this.value1[0]

        }).then(response => {
             console.log("sucess")
          }, response => {
              console.log("error");
          });    
    },
    getTypes(){
      this.$http.get('http://localhost:8000/getGoodsTypes').then(response => {
        this.list1=[this.querySetToArray(response.data)]
        console.log(this.list1)
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
          value:obj[i].pk,
          name:obj[i].fields.name
        })
      }
      return newObj
    },
    deleteGoods(){
      this.deling=true
      this.$http.get('http://localhost:8000/deleteGoods?goods_id='+this.goods_id).then(
        response => {
          this.deling=false
          this.$router.replace({path:"goods"})
        }, 
        response => {
            console.log("error");
        }
      );
    }

  },
  components: {
    Group,
    Cell,
    CellBox,
    upload,
    XTextarea
    ,XButton,
    PopupPicker,
    Confirm,
    Loading

  }
}
</script>