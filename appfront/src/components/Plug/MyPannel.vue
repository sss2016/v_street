<template>
  <div class="myPanel">
    	<div class="header">
    		<slot name="header"></slot>
    		{{title}}
    	</div>
    	<div class="content">
    		<slot name="content" v-if="!keyValue"></slot>
    		<template v-else-if="!rows" v-for="item in keyValue">
    				<div class="item" >
    					<span class="key">{{item.key}}</span>
    					<span class="value">{{item.value}}</span>
    				</div>
    		</template>
    		<template v-for="it in rows">
    			<div class="item" :key="it">
    					<slot :name="it"></slot>
    			</div>
    		</template>
    		
    	</div>
    	<div class="footer">
    		<slot name="footer"></slot>
    	</div>
  </div>
</template>
<script>

export default {
  components: {
    
  },
  props:{
  	//设置rows后keyvalue不可用n
  		soltTitle:null,
  		title:{
  			default:null
  		},

        keyValue:{
          default:null
        },
        rows:{
        	default:null
        }
  },
  methods: {
    
  },
  data () {
    return {
      
    }
  }
}
</script>
<style type="text/css" scoped>
	.myPanel{
		background-color: white;
	}	
	.myPanel .header{
		padding: 10px;
		font-family:"Times New Roman", Times, serif;
		font-size: 17px;
		font-weight: bold;
		border-bottom: 1px solid #eee;
	}
	.myPanel .content .item{
		padding: 10px 0;
		overflow: hidden;
		border-bottom: 1px solid #eee;
		margin: 0 10px;
	}
	.footer{
		padding: 10px;
	}
	.myPanel .content .item .key{
		display: inline-block;
		width: 20%;
		float: left;
	}
	.myPanel .content .item .value{
		color: gray;
		float: left;
		width: 70%;

	}

	.myPanel{
		margin-top: 10px;
		border-radius: 5px;
	}
</style>