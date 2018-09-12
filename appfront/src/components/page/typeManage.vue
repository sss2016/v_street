
<template>
	<div class="tabbar-out">
		<div class="checklist">
			 <checklist  
			 ref="clist"
			 :disabled="edit" 
			 :class="edit?'buts':''"  
			 required 
			 :options="commonList" 
			 v-model="checklist001" 
			 @on-change="change"></checklist>
		</div>
	   
	    <div class="mytabbar">
	    	<span @click="inputshow=true" v-if="edit">添加</span>
	    	<span  v-if="!edit" style="color:#eee">添加</span>
	    	<span v-if="!delete_disable" style="color:red" @click="downdelete=true">删除</span>
	    	<span v-if="!edit&&delete_disable" style="color:#eee">删除</span>
	        <span @click="Edit" v-if="edit">编辑</span>
	        <span @click="complete" v-if="cp_show">完成</span>
	    </div>
	 <div v-transfer-dom>
      <confirm v-model="inputshow"
      @on-confirm="addType"
      show-input
      title="请输入类别名称">
      </confirm>
    </div>
    <div v-transfer-dom>
      <confirm v-model="downdelete"
      @on-confirm="deleteType"
      title="操作提示">
      <p style="color:red">确定咩？</p>
      </confirm>
    </div>
      <toast  v-model="repeatTip" :time="1000" type="cancel">类别重复</toast>

	</div>
</template>
<script>
import { Group, CellBox, Checklist, Cell, Divider, Confirm,XButton,TransferDomDirective as TransferDom,Toast } from 'vux'
import _ from 'lodash'
import $ from 'jquery'
export default {
  mounted () {
    
    this.getGoodsTypes()
  },
   directives: {
    TransferDom
  },
  components: {
    Group,
    Checklist,
    Cell,
    Divider,
    XButton,
    Toast,
    CellBox,
    Confirm
  },
  methods: {
    change (val, label) {
     this.fullValues=this.$refs.clist.getFullValue()
      this.delete_disable=label.length<1?true:false
    },
    Edit(){
      this.edit=false
      this.cp_show=true
    },
    complete(){
      this.checklist001=[]
      this.edit=true
      this.cp_show=false
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
    	return newObj
    },
    getGoodsTypes(){
	    this.$http.get('https://www.ktsweb.cn/getGoodsTypes').then(
	     respones=>{
	     	// console.log(respones.data).
	     	this.commonList=this.querySetToArray(respones.data.json)
	    },respones=>{
	    	console.log('error')
	    })
    }
    ,
    addType(value){
      var formData = new FormData();
      formData.append('name', value);
      // formData.append("csrfmiddlewaretoken",$('meta[name="csrf_token"]').attr('content'))
	    this.$http.post('https://www.ktsweb.cn/addType',formData).then(
	     respones=>{
        if (respones.body.state==0) {
          this.getGoodsTypes()
        }else{
          this.repeatTip=true
        }
	    },respones=>{
	    	console.log('error')
	    })
    },
    deleteType(){
	    this.$http.post('https://www.ktsweb.cn/deleteType',
	    		{type_id:this.checklist001}
	    ).then(
	     respones=>{
	     	for (var i = this.commonList.length - 1; i >= 0; i--) {
	     		if(this.checklist001.indexOf(this.commonList[i].key)>-1){
	     			console.log(i)
	     			    this.commonList.splice(i, 1);
	     		}
	     	}
	     	this.checklist001=[]
	    },respones=>{
	    	console.log('error')
	    })
    }
  },
  data () {
    return {
      fullValues: [],
      error: '',
      commonList: [{key:"1",value:"中国"},{key:'2',value:"日本"}],
      checklist001:  [],
      checklist0011: [],
      asyncList: [],
      asyncListValue: [],
      radioValue: ['China'],
      edit:true,
      cp_show:false,
      delete_disable:true,
      inputshow:false,
      downdelete:false,
      repeatTip:false
    }
  }
}
</script>

<style scoped>
.error {
  padding-left: 15px;
  line-height: 28px;
  color: #888;
  font-size: 12px;
}
.mytabbar span{
	margin: 0 5px;
}
</style>
<style type="text/css">
.weui-cell p{
	margin: 0;
}
.buts label>.weui-cell__hd{
	display: none;
}

.mytabbar{
	width: 100%;
	height: 8%;
	background-color: white;
	display: flex;
    align-items:center;
    justify-content: space-between;
    font-size: 20px;
    border-top: 1px solid #eee;
}
html,body,#app{
height: 100%;
}
.tabbar-out .checklist{
height: 92%;
overflow: auto;
}
.tabbar-out{
overflow: hidden;

height: 100%;
}

</style>