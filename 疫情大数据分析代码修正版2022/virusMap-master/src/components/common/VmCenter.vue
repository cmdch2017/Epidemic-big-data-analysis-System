<template>
  <div id="vmcenter">
    <VmCenterTop :centerTop='centerTop'></VmCenterTop>
    <VmCenterContainer :foreignData='foreignData'></VmCenterContainer>
  </div>
</template>

<script>
import VmCenterTop from './VmCenterTop.vue'
import VmCenterContainer from './VmCenterContainer.vue'
export default {
  name: 'vmcenter',
  props: {
    centerTop: {},
    foreignData: {}
  },
  components: {
    VmCenterTop,
    VmCenterContainer
  },
}
</script>
<style scoped>
#vmcenter {
  /* height: 100px;
		background-color: #000088; */
  padding: 0 10px 15px;
}
</style>
