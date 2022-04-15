<template>
  <div>
    <div class="deit">

      <div class="crumbs">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item><i class="el-icon-date"></i> 模拟数据</el-breadcrumb-item>
          <el-breadcrumb-item>模拟数据预览</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="container">
          <div class="left-group">
            <div class="cantainer">
              折线图模拟数据

              <el-table style="width: 100%;" :data="students.slice((currentPage-1)*pagesize,currentPage*pagesize)">
                <el-table-column type="index" width="30">
                </el-table-column>
                <el-table-column label="数据名称" prop="name" width="180">
                </el-table-column>
                <el-table-column label="折线图数据" prop="age" width="180">
                </el-table-column>

              </el-table>

            </div>
          </div>
          <div class="mid-group">

          </div>
          <div class="right-group">
            <div class="cantainer">
              饼图模拟数据

              <el-table style="width: 100%;" :data="students.slice((currentPage-1)*pagesize,currentPage*pagesize)">
                <el-table-column type="index">
                </el-table-column>

                <el-table-column label="数据名称" prop="name" width="180">
                </el-table-column>
                <el-table-column label="饼图数据" prop="bir" width="180">
                </el-table-column>

              </el-table>

            </div>

          </div>

        </div>
        <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[5, 10, 20, 40]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper" :total="students.length"> //这是显示总共有多少数据，
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      currentPage: 1, //初始页
      pagesize: 10,    //    每页的数据
      students: [],
    }
  },
  created () {
    this.handleUserList()
  },
  methods: {
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },
    handleUserList () {
      this.$http.get('http://49.235.47.70:9090/student/findAll').then((res) => {
        this.students = res.data.results
        console.log(this.students)
      })
    }
  }
}
</script>
<style scoped>
.container {
  width: 100%;
  display: flex;
  top: 100px;
  bottom: 100px;
}
.left-group,
.right-group {
  width: 600px;
  text-align: center;
}
.mid-group {
  flex: 1;
  text-align: center;
}
</style>