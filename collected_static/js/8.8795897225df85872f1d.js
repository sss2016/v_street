webpackJsonp([8],{riqQ:function(e,t,r){"use strict";var a=r("7+S+"),i={name:"form-preview",props:["headerLabel","headerValue","bodyItems","footerButtons","name"],methods:{onButtonClick:function(e,t){e&&e(this.name),t&&Object(a.b)(t,this.$router)}}},s={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"vux-form-preview weui-form-preview"},[r("div",{staticClass:"weui-form-preview__hd"},[r("label",{staticClass:"weui-form-preview__label",domProps:{innerHTML:e._s(e.headerLabel)}}),e._v(" "),r("em",{staticClass:"weui-form-preview__value",domProps:{innerHTML:e._s(e.headerValue||"&nbsp;")}})]),e._v(" "),r("div",{staticClass:"weui-form-preview__bd"},e._l(e.bodyItems,function(t){return r("div",{staticClass:"weui-form-preview__item"},[r("label",{staticClass:"weui-form-preview__label"},[e._v(e._s(t.label))]),e._v(" "),r("span",{staticClass:"weui-form-preview__value"},[e._v(e._s(t.value))])])})),e._v(" "),r("div",{staticClass:"weui-form-preview__ft"},e._l(e.footerButtons,function(t){return r("a",{staticClass:"weui-form-preview__btn",class:{"weui-form-preview__btn_default":"default"===t.style,"weui-form-preview__btn_primary":"primary"===t.style},attrs:{href:"javascript:"},on:{click:function(r){e.onButtonClick(t.onButtonClick,t.link)}}},[e._v(e._s(t.text))])}))])},staticRenderFns:[]};var l=r("C7Lr")(i,s,!1,function(e){r("tWtk")},null,null);t.a=l.exports},tWtk:function(e,t){},zZcw:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=r("riqQ"),i=r("4pOY"),s=(a.a,i.a,{components:{FormPreview:a.a,myTabbar:i.a},data:function(){return{list:[{label:"商品",value:"电动打蛋机"},{label:"标题标题",value:"名字名字名字"},{label:"标题标题",value:"很长很长的名字很长很长的名字很长很长的名字很长很长的名字很长很长的名字"}],buttons1:[{style:"default",text:"辅助操作"},{style:"primary",text:this.$t("跳转到首页"),link:"/"}],buttons2:[{style:"primary",text:this.$t("点击事件"),onButtonClick:function(e){alert("clicking "+e)}}]}}}),l={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"area"},[r("div",[r("form-preview",{attrs:{"header-label":e.$t("付款金额"),"header-value":"¥2400.00","body-items":e.list,"footer-buttons":e.buttons1}}),e._v(" "),r("br"),e._v(" "),r("form-preview",{attrs:{"header-label":e.$t("付款金额"),"header-value":"¥2400.00","body-items":e.list,"footer-buttons":e.buttons2,name:"demo"}}),e._v(" "),r("br"),e._v(" "),r("form-preview",{attrs:{"header-label":e.$t("付款金额"),"header-value":"¥2400.00","body-items":e.list}})],1),e._v(" "),r("myTabbar",{attrs:{selectTab:1}})],1)},staticRenderFns:[]},n=r("C7Lr")(s,l,!1,null,null,null);t.default=n.exports}});
//# sourceMappingURL=8.8795897225df85872f1d.js.map