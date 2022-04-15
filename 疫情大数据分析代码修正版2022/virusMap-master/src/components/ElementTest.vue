<template>
  <div>

    <el-table :data="tableData"
              style="width: 100%">
      <el-table-column label="行业结构">
        <el-table-column prop="col11"
                         label="行业集中度 "
                         width="120">
        </el-table-column>
        <el-table-column prop="col12"
                         label="最大持仓行业"
                         width="120">
        </el-table-column>
        <el-table-column prop="col13"
                         label="最大持仓行业占比"
                         width="120">
        </el-table-column>
        <el-table-column prop="col14"
                         label="前三大持仓行业"
                         width="120">
        </el-table-column>
        <el-table-column prop="col15"
                         label="前三大持仓行业占比"
                         width="120">
        </el-table-column>
      </el-table-column>
      <el-table-column label="个股集中度">
        <el-table-column prop="col21"
                         label="前三大个股/个券"
                         width="300">
        </el-table-column>
        <el-table-column prop="col22"
                         label="前三大个股/个券占比"
                         width="120">
        </el-table-column>
        <el-table-column prop="col23"
                         label="前五大个股/个券"
                         width="300">
        </el-table-column>
        <el-table-column prop="col24"
                         label="前五大个股/个券占比"
                         width="120">
        </el-table-column>
      </el-table-column>
    </el-table>

    <el-button type="mini"
               @click="handleDownload()">下载</el-button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tableData: [{
        col11: '10%',
        col12: '医药生物',
        col13: '1.5618%',
        col14: '医药生物,食品饮料,化工',
        col15: '4.16%',
        col21: '安琪酵母,中国平安,通威股份',
        col22: '1.98%',
        col23: '安琪酵母,中国平安,通威股份,九州药业,万华化学',
        col24: '3.01%',
      }]
    }
  },
  methods: {
    handleDownload() {
      // 未完成
      let thiz = this
      let loading = thiz.$loading({
        lock: true,
        text: '下载中，请稍候...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      })


      // encodeURIComponent解决中文乱码
      let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(this.tableData[0].col11)
      // 通过创建a标签实现
      let link = document.createElement('a')
      link.href = uri
      // 对下载的文件命名
      link.download = "analysisTable" + '.csv'
      document.body.appendChild(link)
      // link.click()
      document.body.removeChild(link)
      loading.close()
    }
  }
}
</script>
<style scoped>
</style>
