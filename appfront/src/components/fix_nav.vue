<template>


<nav class="cd-stretchy-nav">
    <a class="cd-nav-trigger" href="javascript:void(0);" @click=trigger()>
      <span aria-hidden="true"></span>
    </a>
    <ul class="cd-stretchy-nav-ul">
      <router-link to="/addGoods"><li><span></span></li></router-link>
      <router-link to="/user/index"><li><span></span></li></router-link>
      <router-link to="/shopping/cart"><li><span></span></li></router-link>
    </ul>

    <span aria-hidden="true" class="stretchy-nav-bg"></span>
  </nav>
</template>
<style lang="less" scoped>
li{
  list-style: none;
}
.cd-stretchy-nav {
  position: fixed;
  z-index: 2;
  bottom: 0.42rem;
  right: 2px;
}
.cd-stretchy-nav .stretchy-nav-bg {
  position: absolute;
  z-index: 1;
  bottom: 0;
  right: 0;
  width: 40px;
  height: 40px;
  border-radius: 30px;
  background: rgba(255, 0, 23,.8);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  -webkit-transition: height 0.2s, box-shadow 0.2s;
  transition: height 0.2s, box-shadow 0.2s;
}
.cd-stretchy-nav.nav-is-visible .stretchy-nav-bg {
  height: 100%;
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.2);
}

.cd-nav-trigger {
  position: absolute;
  z-index: 3;
  bottom: 0;
  right: 0;
  height: 40px;
  width: 40px;
  border-radius: 50%;
  overflow: hidden;
  white-space: nowrap;
  color: transparent;
}
.cd-nav-trigger span, .cd-nav-trigger span::after, .cd-nav-trigger span::before {
  position: absolute;
  width: 16px;
  height: 2px;
  background-color: #ffffff;
}
.cd-nav-trigger span {
  left: 50%;
  top: 50%;
  bottom: auto;
  right: auto;
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
  -webkit-transition: background-color 0.2s;
  transition: background-color 0.2s;
}
.cd-nav-trigger span::after, .cd-nav-trigger span::before {
  content: '';
  top: 0;
  left: 0;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  -webkit-transition: -webkit-transform 0.2s;
  transition: transform 0.2s;
}
.cd-nav-trigger span::before {
  -webkit-transform: translateY(-6px);
  transform: translateY(-6px);
}
.cd-nav-trigger span::after {
  -webkit-transform: translateY(6px);
  transform: translateY(6px);
}
.nav-is-visible .cd-nav-trigger span {
  background-color: transparent;
}
.nav-is-visible .cd-nav-trigger span::before {
  -webkit-transform: rotate(-45deg);
  transform: rotate(-45deg);
}
.nav-is-visible .cd-nav-trigger span::after {
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
}

.cd-stretchy-nav ul {
  position: relative;
  z-index: 2;
  padding-bottom: 35px;
  visibility: hidden;
  -webkit-transition: visibility 0.3s;
  transition: visibility 0.3s;
  text-align: right;
}
.cd-stretchy-nav ul span {
  position: relative;
  display: block;
  width: 40px;
  height: 40px;
  line-height: 40px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.4rem;
  -webkit-transition: color 0.2s;
  transition: color 0.2s;
}
.cd-stretchy-nav ul span::after {
  content: '';
  position: absolute;
  height: 22px;
  width: 22px;
  left: 0;
  right: 0;
  margin: auto;
  top: 50%;
  -webkit-transform: translateY(-50%) scale(0);
  transform: translateY(-50%) scale(0);
}
.cd-stretchy-nav ul a{
  display:block;
  position:relative;
  z-index:2;
}

.cd-stretchy-nav.nav-is-visible ul {
  visibility: visible;
}
.cd-stretchy-nav.nav-is-visible ul span::after {
  -webkit-transform: translateY(-50%) scale(1);
  transform: translateY(-50%) scale(1);
  -webkit-animation: scaleIn 0.15s backwards;
  animation: scaleIn 0.15s backwards;
  -webkit-transition: opacity 0.2s;
  transition: opacity 0.2s;
}

.cd-stretchy-nav.nav-is-visible ul a:first-of-type li span::after{
  -webkit-animation-delay: 0.05s;
  animation-delay: 0.05s;
  background: url(../assets/icon/icon_home.png) no-repeat center;
  background-size: contain;
}
.cd-stretchy-nav.nav-is-visible ul a:nth-of-type(2) li span::after{
  -webkit-animation-delay: 0.1s;
  animation-delay: 0.1s;
  background: url(../assets/icon/icon_index.png) no-repeat center;
  background-size: contain;
}
.cd-stretchy-nav.nav-is-visible ul a:nth-of-type(3) li span::after{
  -webkit-animation-delay: 0.15s;
  animation-delay: 0.15s;
  background: url(../assets/icon/icon_car.png) no-repeat center;
  background-size: contain;
}
</style>
<script type="text/javascript">
export default {
    methods:{
      trigger(){
        var stretchyNavs = document.getElementsByClassName("cd-stretchy-nav")[0];
        var time;
        if(stretchyNavs.className.indexOf("nav-is-visible")<0){
          stretchyNavs.className = "cd-stretchy-nav nav-is-visible"
          clearTimeout(time)
          document.getElementsByClassName("cd-stretchy-nav-ul")[0].style.display = "block"
        }else{
          stretchyNavs.className = "cd-stretchy-nav"
          time=setTimeout(function(){
            document.getElementsByClassName("cd-stretchy-nav-ul")[0].style.display = "none"
          },200)
        }
      },
      wxConfig:function(){

      },
    }
}
      
</script>


