<template>
  <div>
    <group  label-width="5.5em" label-margin-right="2em" label-align="justify">
      <cell   is-link> <span slot="title">
          店铺名称
      </span> title="店铺名称"</cell>
      <cell title="店主" ></cell>
      <cell title="店铺类型" ></cell>
      <cell title="到期时间" ></cell>
       <cell title="热度" ></cell>
       <cell title="成交数" ></cell>
       
    </group>
    <br>
  </div>
</template>
<style type="text/css">
 .weui-cell p { white-space:nowrap;margin: 0; }


</style>
<script>
  import { GroupTitle, Group, Cell, XInput, Selector, PopupPicker, Datetime, XNumber, ChinaAddressData, XAddress, XTextarea, XSwitch } from 'vux'

  export default {
    components: {
      Group,
      GroupTitle,
      Cell,
      XInput,
      Selector,
      PopupPicker,
      XAddress,
      Datetime,
      XNumber,
      XTextarea,
      XSwitch
    },
    data () {
      return {
        addressData: ChinaAddressData,
        addressValue: ['广东省', '深圳市', '南山区'],
        value1: '张三',
        value2: '工艺技术',
        value3: '',
        value7: '',
        value8: '',
        value4: '',
        time1: '2017-06-01',
        value5: ['A'],
        value6: [],
        list: [['A', 'B', 'C']],
        numberValue: 0
      }
    }
  }
</script>