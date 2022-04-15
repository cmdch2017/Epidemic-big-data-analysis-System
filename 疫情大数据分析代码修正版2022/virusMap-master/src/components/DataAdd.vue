<template>
  <div>
    <h2>项目主要流程</h2>
    <form action="">
      <input type="button" @click="save1To2" value="1、爬取数据信息，经过数据清洗后保存为csv文件">

    </form>
    <p>
      <input type="button" @click="saveStudentInfo" v-if="clickShowHDFS" value="2、上传至hdfs，并将文件保存入数据库">

    <div class="cantainer" v-if="clickShowTodayInformation">
      <img src="../assets/image/hdfs.jpg" />

      <h3>中国今日Top榜</h3>

      <el-table style=" width:1200px" stripe :data="worlds.slice((currentPage-1)*pagesize,currentPage*pagesize)">

        <el-table-column label="省份名称" prop="name" width="240">
        </el-table-column>
        <el-table-column label="最新确诊" prop="confirm" width="240">
        </el-table-column>
        <el-table-column label="累计确诊" prop="confirm_all" width="240">
        </el-table-column>
        <el-table-column label="累计死亡" prop="dead" width="240">
        </el-table-column>
        <el-table-column label="累计治愈" prop="heal" width="240">
        </el-table-column>

      </el-table>
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[5, 10, 20, 40]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper" :total="worlds.length"> //这是显示总共有多少数据，
      </el-pagination>
    </div>
  </div>

</template>

<script>
export default {
  name: 'DataAdd',
  data () {
    return {
      currentPage: 1, //初始页
      pagesize: 10,    //    每页的数据
      worlds: [],
      flag: '1',
      clickShowHDFS: false,
      clickShowTodayInformation: false

    }
  },
  methods: {
    save1To2 () {
      this.clickShowHDFS = true
    },
    saveStudentInfo () {
      this.clickShowTodayInformation = true
      // 发送axios请求
      this.$http.post('http://49.235.47.70:9090/china/DataAdd', this.flag).then(res => {
        this.worlds = res.data.results

      })
    },
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    }
  }
}
</script>
<style scoped>
</style>
