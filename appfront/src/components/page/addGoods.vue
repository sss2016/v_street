<template>
  <div>
    <upload :path="'../../assets/ic_empty_event.png'" 
    ref="upload" 
    :isAutoUpload="false" :uploadUrl="'addGoods'" 
    @success="wancheng"
    @imageChange="hadSelImg=true"
    >
    </upload>
    <group class="myform">
      <x-input title="名称" name="username" placeholder="请输入商品名称" v-model="formData.goods_name" ></x-input>

      <x-input  title="价格" name="username" placeholder="请输入商品价格" v-model="formData.goods_price" ></x-input>

      <cell title="规格"  is-link :link="{
            name: 'standards', 
            params: {        
                type: 0,
                goods_id:null,
                treeData:formData.guige
            }
          }">
          已设置
        {{formData.guige?Object.keys(formData.guige).length:"0"}}
        个规格
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
      <x-textarea title="描述" placeholder="请填写详细信息" :show-counter="false" :rows="3" v-model="formData.dec"></x-textarea>

    </group>
          <div class="picker-buttons">
       <x-button type="primary" @click.native="submit_goods" :disabled="uping">完成</x-button>
     </div>
    <div v-transfer-dom>
      <loading :show="uping" text=""></loading>
    </div>

  </div>
</template>
<style type="text/css">
  .myform p{
    margin: 0;
  }
</style>
<script>
import $ from 'jquery'
import { PopupPicker,XInput,XButton } from 'vux'
import { Group,Cell, XTextarea,CellBox } from 'vux'
import { Loading } from 'vux'
import { TransferDomDirective as TransferDom } from 'vux'
import upload from '../Plug/upload.vue'
export default {
  directives: {
    TransferDom
  },
  data(){
    return {
      show2:false,
      date: '',
      title1: '类型',
      list1: [],
      value1: [],
      formData:{
        csrfmiddlewaretoken:"",
        type_id: null,
        goods_name:null,
        goods_price:null,
        dec:null,
        guige:null
      },
      hadSelImg:false,
      uping:false
    }
  },
  components: {
    Group,
    Cell,
    CellBox,
    upload,
    XTextarea,
    PopupPicker,
    XInput,
    XButton,
    Loading
  },
  mounted(){

    this.getTypes()
  },
   activated () {
    if (window.mycache.standards) {
      this.formData.guige=window.mycache.standards
    }
    console.log(window.mycache.standards)

  },
  methods:{
    changes(value){
      console.log(value)
    },
    getTypes(){
      this.$http.get('https://www.ktsweb.cn/getGoodsTypes').then(response => {
        this.list1=[this.querySetToArray(response.data.json)]
        // console.log(this.list1)
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
    submit_goods:function() {
    var reg = /(^[1-9]([0-9]+)?(\.[0-9]{1,2})?$)|(^(0){1}$)|(^[0-9]\.[0-9]([0-9])?$)/;
      if (!this.hadSelImg) {
          alert("请上传一张商品图片")
        return
      }
      if (this.formData.goods_name==null||this.formData.goods_name.replace("",' ').length<1) {
          alert("请输入商品名称")
        return
      }
      if (this.formData.goods_price==null||this.formData.goods_price.replace("",' ').length<1) {
          alert("请输入商品价格")
        return
      }
      if (!reg.test(this.formData.goods_price)) {
          alert("价格格式不正确")
            return
      }
      if (this.formData.dec==null&&this.formData.dec.replace("",' ').length<1) {
          alert("请输入商品描述")
        return
      }
      this.formData.type_id=this.value1[0]

      var senData = this.obj_copy(this.formData)
      senData.guige = JSON.stringify(senData.guige)
      // this.showLoading()
      this.uping=true
      this.$refs.upload.uploadImg(null,senData)
    },
    wancheng(){
      this.uping=false
      this.$router.push({
        　　name:"goods"

      }
      )
    },
    obj_copy(old){
      var newobj ={}
        for(var key in old ){
          newobj[key]=old[key]
        }
        return newobj
    }


  }
}
</script>
<style scoped>
.picker-buttons {
  margin: 0 15px;
}
</style>