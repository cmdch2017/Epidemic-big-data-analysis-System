<template>
  <div id="vmleft">
    <VmPanel>
      <div slot='panelcontent'>
        <h2>新增确诊TOP10</h2>
        <div class="chart topteninfected"></div>
      </div>
    </VmPanel>
    <VmPanel>
      <div slot='panelcontent'>
        <h2>境外输入病情top10省份</h2>
        <div class="chart infectedstates"></div>
      </div>
    </VmPanel>
    <VmPanel>
      <div slot='panelcontent'>
        <h2>世界每周新增治愈和死亡人数</h2>
        <div class="chart infectedstatesPie"></div>
      </div>
    </VmPanel>
  </div>
</template>

<script>
import VmPanel from './VmPanel.vue'

import {
  addChart,
} from '../../commonfun/charts.js'

export default {
  name: 'vmleft',
  props: {
    option1: {},
    option3: {},
    option5: {}
  },
  components: {
    VmPanel
  },
  watch: {
    option1() {
      let topteninfected = document.querySelector('.topteninfected');
      addChart(topteninfected, this.option1);
    },
    option3() {
      let infectedstates = document.querySelector('.infectedstates');
      addChart(infectedstates, this.option3);
    },
    option5() {
      let infectedstatesPie = document.querySelector('.infectedstatesPie');
      addChart(infectedstatesPie, this.option5);
    },
  }
}
</script>
<style scoped>
</style>
