<template>
  <div>
    <div class="cantainer">
      <h3>中国数据一览（最近更新日期）</h3>

      <el-table style=" width:1200px" stripe :data="worlds.slice((currentPage-1)*pagesize,currentPage*pagesize)">

        <el-table-column label="省份名称" prop="name" width="200">
        </el-table-column>
        <el-table-column label="最新确诊" prop="confirm" width="200">
        </el-table-column>
        <el-table-column label="累计确诊" prop="confirm_all" width="200">
        </el-table-column>
        <el-table-column label="累计死亡" prop="dead" width="200">
        </el-table-column>
        <el-table-column label="累计治愈" prop="heal" width="200">
        </el-table-column>
        <el-table-column label="更新日期" prop="last_update_time" width="200">
        </el-table-column>
      </el-table>
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[5, 10, 20, 40]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper" :total="worlds.length"> //这是显示总共有多少数据，
      </el-pagination>
    </div>

  </div>
</template>

<script>
export default {
  name: 'world',
  data: function () {
    return {
      currentPage: 1, //初始页
      pagesize: 10,    //    每页的数据
      worlds: []
    }
  },

  methods: {

    findAll () {
      this.$http.get('http://49.235.47.70:9090/china/findAllChina').then((res) => {
        this.worlds = res.data.results
      })
    },
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    }
  },
  created () {
    this.findAll()
  },
  watch: {// 用来监听
    $route: {
      handler (val, oldval) {
        // console.log(val)// 新路由信息

        if (val.path === '/world') {
          this.findAll
        }
      },
      // 深度观察监听
      deep: true
    }
  }
}
</script>
<style scoped>
</style>
