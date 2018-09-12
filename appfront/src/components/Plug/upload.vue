<template>
		<div class="upload" @click="select_img" :style="'background-image:url('+image_path+')'" >
			<img src="../../assets/相机.png" >
			<form>
				<input type="file" name="" id="upload"  accept="image/*"  @change="handleInputChange">
			</form>
		</div>

</template>
<style type="text/css" scoped>
	.upload{
		display: flex;
		height: 200px;
		width: 100%;
		background: green no-repeat;
		background-size: 100% 100%;
		justify-content:center;
		align-items:center;
	}
	.upload img{
		width: 60px;
		height: 50px;
		position: relative;
	}
	.upload input[type='file']{
		display: none;
	}
</style>
<script type="text/javascript">
const imgFile = {};
import $ from 'jquery'
		export default{
			props:{
				path:{
					default:""
				},
				isAutoUpload:{
					default:false
				},
				uploadUrl:{
					default:""
				}

			},
			data(){
				return {
					the_formData:new FormData(),
					image_path:this.path,
				}
			},
			
			methods:{
				getObjectURL:function (file){
				  var url = null;
				  if(window.createObjectURL != undefined){
				    url = window.createObjectURL(file);//basic
				  }else if(window.URL != undefined){
				    url = window.URL.createObjectURL(file);
				  }else if(window.webkitURL != undefined){
				    url = window.webkitURL.createObjectURL(file);
				  }

				  return url;
				},
				select_img:function (argument) {
					var uploadPlug=document.getElementById('upload')
					uploadPlug.click()
				},
				 handleInputChange:function (event) {
				    // 获取当前选中的文件
				    this.$emit("imageChange")
				    const file = event.target.files[0];
				    const imgMasSize = 1024 * 1024 * 10; // 10MB
				    this.image_path=this.getObjectURL(file)
				    // 检查文件类型
				    if(['jpeg', 'png', 'gif', 'jpg'].indexOf(file.type.split("/")[1]) < 0){
				        // 自定义报错方式
				        // Toast.error("文件类型仅支持 jpeg/png/gif！", 2000, undefined, false);
				        return;
				    }

				    // 文件大小限制
				    if(file.size > imgMasSize ) {
				        // 文件大小自定义限制
				        // Toast.error("文件大小不能超过10MB！", 2000, undefined, false);
				        return;
				    }

				    // 判断是否是ios
				    if(!!window.navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)){
				        // iOS
				        this.transformFileToFormData(file);
				        return;
				    }
				    // 图片压缩之旅
				    this.transformFileToDataUrl(file);
				},
				// 将File append进 FormData
				transformFileToFormData:function(file) {
				    var formData = new FormData();
				    // 自定义formData中的内容
				    // type

				    formData.append('type', file.type);
				    // size
				    formData.append('size', file.size || "image/jpeg");
				    // name
				    formData.append('name', file.name);
				    // lastModifiedDate
				    formData.append('lastModifiedDate', file.lastModifiedDate);
				    // append 文件
				    formData.append('file', file);

				    // 上传图片
					this.the_formData=formData
					// console.log(formData)
				    if (this.isAutoUpload)				    	
				    	this.uploadImg(formData);
				},
				// 将file转成dataUrl
				transformFileToDataUrl:function (file) {
				    const imgCompassMaxSize = 200 * 1024; // 超过 200k 就压缩
				    // 存储文件相关信息
				    imgFile.type = file.type || 'image/jpeg'; // 部分安卓出现获取不到type的情况
				    imgFile.size = file.size;
				    imgFile.name = file.name;
				    imgFile.lastModifiedDate = file.lastModifiedDate;

				    // 封装好的函数
				    const reader = new FileReader();
				    var this_=this
				    // file转dataUrl是个异步函数，要将代码写在回调里
				    reader.onload = function(e) {
				        const result = e.target.result;

				        if(result.length < imgCompassMaxSize) {
				            this_.compress(result, this_.processData, false );    // 图片不压缩
				        } else {
				            this_.compress(result, this_.processData);            // 图片压缩
				        }
				    };

				    reader.readAsDataURL(file);
				},
				// 使用canvas绘制图片并压缩
				compress:function (dataURL, callback, shouldCompress = true) {
				    const img = new window.Image();

				    img.src = dataURL;

				    img.onload = function () {
				        const canvas = document.createElement('canvas');
				        const ctx = canvas.getContext('2d');

				        canvas.width = img.width;
				        canvas.height = img.height;

				        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

				        let compressedDataUrl;

				        if(shouldCompress){
				            compressedDataUrl = canvas.toDataURL(imgFile.type, 0.2);
				        } else {
				            compressedDataUrl = canvas.toDataURL(imgFile.type, 1);
				        }

				        callback(compressedDataUrl);
				    }
				},

				processData:function (dataURL) {

				    // 这里使用二进制方式处理dataUrl
				    const binaryString = window.atob(dataURL.split(',')[1]);
				    const arrayBuffer = new ArrayBuffer(binaryString.length);
				    const intArray = new Uint8Array(arrayBuffer);

				    for (let i = 0, j = binaryString.length; i < j; i++) {
				        intArray[i] = binaryString.charCodeAt(i);
				    }

				    const data = [intArray];

				    let blob;

				    try {
				        blob = new Blob(data, { type: imgFile.type });
				    } catch (error) {
				        window.BlobBuilder = window.BlobBuilder ||
				            window.WebKitBlobBuilder ||
				            window.MozBlobBuilder ||
				            window.MSBlobBuilder;
				        if (error.name === 'TypeError' && window.BlobBuilder){
				            const builder = new BlobBuilder();
				            builder.append(arrayBuffer);
				            blob = builder.getBlob(imgFile.type);
				        } else {
				            // Toast.error("版本过低，不支持上传图片", 2000, undefined, false);
				            throw new Error('版本过低，不支持上传图片');
				        }
				    }

				    // blob 转file
				    const fileOfBlob = new File([blob], imgFile.name);
				    const formData = new FormData();

				    // type
				    formData.append('type', imgFile.type);
				    // size
				    formData.append('size', fileOfBlob.size);
				    // name
				    formData.append('name', imgFile.name);
				    // lastModifiedDate
				    formData.append('lastModifiedDate', imgFile.lastModifiedDate);
				    // append 文件
				    formData.append('file', fileOfBlob);
				    this.the_formData=formData

				    if (this.isAutoUpload)
				    	this.uploadImg(formData);
				},

				// 上传图片
				uploadImg:function(formData,args) {
				    // const xhr = new XMLHttpRequest();
				    // // 进度监听
				    // xhr.upload.addEventListener('progress', (e)=>{console.log(e.loaded / e.total)}, false);
				    // // 加载监听
				    // // xhr.addEventListener('load', ()=>{console.log("加载中");}, false);
				    // // 错误监听
				    // xhr.addEventListener('error', ()=>{Toast.error("上传失败！", 2000, undefined, false);}, false);
				    // xhr.onreadystatechange = function () {
				    //             console.log(123)

				    //     if (xhr.readyState === 4) {
				    //         const result = JSON.parse(xhr.responseText);
				    //         if (xhr.status === 200) {
				    //             // 上传成功

				    //         } else {
				    //             // 上传失败
				    //         }
				    //     }
				    // };

				    for (var key in args){
    					this.the_formData.append(key,args[key]);
    					console.log(key+"--"+args[key])
					}
				    this.the_formData.append("csrfmiddlewaretoken",$('meta[name="csrf_token"]').attr('content'))
				    // console.log(this.the_formData.get('csrfmiddlewaretoken'))
				   this.$http.post('https://www.ktsweb.cn/'+this.uploadUrl,this.the_formData).then(response => {
				   	console.log(response)
				   		this.$emit("success",response)
            		// get body data
            		// this.someData = response.body;

        			}, response => {
        				this.$emit("error",response)
							console.log("error");
        			});
				}
			}
		}

</script>