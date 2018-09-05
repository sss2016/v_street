<template>
	<div class="standars">	
	<group class="stan_list">
      		<vue-tree v-model="checkedIds" 
      		:tree-data="treeData" 
      		:options="options" 
      		@OnAdd="node_add" 
      		@OnEdit="node_edit"
      		@OnDelete="node_delete"
      		></vue-tree>
    </group>
    <div v-transfer-dom>
      <x-dialog v-model="show" class="dialog-demo mydiy" style="background-color: transparent;">
        <div class="img-box">
        	<x-input :placeholder="placeTitle" v-model="rootName"></x-input>
        </div>
        <div style="font-size:20px;">
	          <div @click="Allclear" style="float:left;color:white" >
	          	取消
	          </div>
	          <div style="float:right;color:white" @click="complete">
	          	完成
	          </div>
        </div>
      </x-dialog>

    </div>
    <flexbox>
        <flexbox-item>
          <x-button type="primary" @click.native="submitAlter">完成</x-button>
        </flexbox-item>
        <flexbox-item>
          <x-button type="default" @click.native="tree_add">添加</x-button>
        </flexbox-item>
      </flexbox>
	</div>


</template>
<style scoped lang="less">
	@import '~vux/src/styles/close';
		.weui-cells{
			position: relative;
			margin-top:0px; 
		}

</style>
<style type="text/css">
	.mydiy .weui-dialog{
		background-color: transparent!important;
	}
	.icon-green{
  		fill: green;
	}	
	.icon-red{
  		fill: red;
	}
	body,html,#app{
		height: 100%;
	}
	.weui-cells{
		margin: 0;
	}
	.stan_list{
		height: 92%;
		overflow: auto;
	}
	.standars div{
		margin: 0px;
		overflow: hidden;
	}
</style>
<style type="text/css" scoped>
	.standars p,.weui-cells,div{
		margin: 0;
		margin-top:0px!important; 
	}
	.standars{
		height: 100%;
		margin: 0;
		overflow: hidden;
	}
	
	.card-footer{
		text-align:right;
		padding-right:20px;
		border-top: 1px dashed #eee;
	}

  .weui-dialog{
    border-radius: 8px;
    padding-bottom: 8px;
    
  }
  .dialog-title {
    line-height: 30px;
    color: #666;
  }

  .vux-close {
    margin-top: 8px;
    margin-bottom: 8px;
  }
	.img-box{
	background-color: white;
	}
</style>
<script type="text/javascript">
	import { XDialog,TransferDomDirective as TransferDom } from 'vux'
	import { Cell,Card,Group,Checklist,XButton,Divider,XInput,Flexbox, FlexboxItem } from 'vux'
	import VueTree from '@components/vue-simple-tree/src/components/VueTree.vue'

export default {
  directives: {
    TransferDom
  },
  mounted () {
  	// if(this.$route.params.type){

  	// }
  	if (this.$route.params.treeData) {
  		this.treeData=this.$route.params.treeData
  	}
    setTimeout(() => {
      this.money = -1024
    }, 2000)
  },
  components: {
    Cell,
    Group,
    Checklist,
    XButton,
    Divider,
    VueTree,
    Card,
    XDialog,
    XInput,
    Flexbox,
    FlexboxItem
  },
  methods: {
    onClick (e) {
	window.event? window.event.cancelBubble = true : e.stopPropagation();

      console.log('on click')
    },
    change (val, label) {
      console.log('change', val, label)
    },

    tree_add(){
    	this.placeTitle="输入规格名称"
    	this.show=true;
    	this.operate_code=1
    },
    node_add(node){
    	this.show=true;
    	this.placeTitle="输入规格选项"
    	console.log(node)
    	this.operate_code=0
    	this.current_sel=this.treeData[node.the_id]
    },
    node_edit(){
    	console.log("编辑节点按钮")
    }
    ,
    node_delete(){
    	console.log("删除节点按钮")
    },
    complete(){
    	if (this.operate_code) {
    			    	this.treeData.push(
			    	{
			    		parent:-1,
			    		id:this.treeData.length,
			    		label:this.rootName,
			    		children:[]

			    	})
    	}else{
    		console.log(this.current_sel)
    			this.current_sel.children.push(
    				{
    					parent:this.current_sel.id,
    					id:this.current_sel.children.length,
    					label:this.rootName,
    					children:[]
    				}
    			)

    	}
    	this.Allclear()

    },
    submitAlter(){
      console.log(this.$route.params.type)
    	if (this.$route.params.type) {
    		this.$http.post('http://localhost:8000/updateItem',
    		{
    				"goods_id":this.$route.params.goods_id,
    				"standards":JSON.stringify(this.treeData)

    		}).then(response => {
             this.$router.replace({
		    		path:'items',
		    		query:{
		    			goods_id:this.$route.params.goods_id,
		    		}
    			})
        	}, response => {
            	console.log("error");
        	});
    	}else{
          window.mycache.standards=this.treeData
          console.log(this.treeData)
          this.$router.back(-1)
      }
    }
    ,
    Allclear(){
    	this.rootName=""
    	this.show=false;
    }
  },
  data () {
    return {
    	 rootName:null,
    	 show:false,
    	 placeTitle:"",
    	 operate_code:1,
    	 del:"checkbox",//hidden
    	 labelPosition: '',
    	 commonList: [ 'China', 'Japan', 'America' ],	
    	 current_sel:{},
    	 checklist001: [],
    	  checkedIds: [],
            // tree数据
          treeData: [],
            // 设置项
   options: {
    // String,节点显示字段
    itemName: 'label',
    
    // Boolean,是否显示添加子节点按钮
    addItem: true,
    
    // Boolean,是否显示选择框
    checkbox: false,
    
    // Array,初始化时选中id (v2.1以后不推荐使用，v3.0将废弃),替代方法见'#使用示例'章节
    checkedIds: [], 
    
    // Boolean,选中时是否展开节点
    checkedOpen: true,
    
    // Boolean,目录是否加粗显示
    folderBold: false,
    
    // String,展开按钮(默认依赖font-awesome)
    openClass: 'fa fa-plus-square text-info',
    // String,收缩按钮(默认依赖font-awesome)
    closeClass: 'fa fa-minus-square text-danger',
    
    // String,添加节点按钮(默认依赖font-awesome)
    addClass: 'fa fa-plus text-danger',
    
    // Boolean,是否显示编辑按钮
    showEdit: true,
    
    // Boolean,是否显示删除按钮
    showDelete: true,
    
    // String,编辑按钮(默认依赖font-awesome)
    editClass: 'fa fa-edit',
    
    // String,删除按钮(默认依赖font-awesome)
    deleteClass: 'fa fa-trash-o',
    
    // (v2.1新增) Boolean,获取复选项目是否包含目录,默认`true`,如果只获取叶子节点设置为`false`
    idsWithParent: true,
    
    // (v2.1新增) Number,初始化时展开层级,根节点为0,默认0
    depthOpen: 0
},
      list: [{
        label: 'Apple',
        value: '3.29'
      }, {
        label: 'Banana',
        value: '1.04'
      }, {
        label: 'Fish',
        value: '8.00'
      }],
      money: null,
      showContent001: false,
      showContent002: false,
      showContent003: false,
      showContent004: false
    }
  }
}
</script>