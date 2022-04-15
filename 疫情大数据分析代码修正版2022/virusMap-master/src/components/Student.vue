<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item><i class="el-icon-date"></i> 模拟数据</el-breadcrumb-item>
      <el-breadcrumb-item>模拟数据编辑</el-breadcrumb-item>
    </el-breadcrumb>
    <h1>模拟数据模块</h1>
    说明：可在此模块修改x轴与y轴数据
    <p>
    <table id="table1" border="1">
      <tr>
        <td>编号</td>
        <td>x轴数据名称</td>
        <td>y轴模拟数据</td>
        <td>特殊说明</td>
        <td>操作</td>

      </tr>
      <tr v-for="student in students" :key=student.id>
        <td>{{student.id}}</td>
        <td>{{student.name}}</td>
        <td>{{student.age}}</td>
        <td>{{student.bir}}</td>
        <td>
          <el-button type="primary" icon="el-icon-edit" circle @click="delRow(student.id)">删除

            <!-- <a :href="'#/student/page?id='+student.id">修改</a> -->
          </el-button>
          <el-button type="primary" icon="el-icon-edit" circle @click="fun(student.id)">修改

            <!-- <a :href="'#/student/page?id='+student.id">修改</a> -->
          </el-button>
        </td>
      </tr>
    </table>

    <a href="#/student/add">添加</a>

    <router-view></router-view>
    <!-- <router-view></router-view> -->
    <div v-if="flag">
      <el-drawer title="表格页面" :before-close="handleClose" :visible.sync="dialog" direction="rtl" custom-class="demo-drawer" ref="drawer">
        <div class="demo-drawer__content">
          <el-form :model="form">
            <el-form-item label="数据名称" :label-width="formLabelWidth">
              <input v-model="student.name" type="text">
            </el-form-item>
            <el-form-item label="y轴数值" :label-width="formLabelWidth">
              <input v-model="student.age" type="text">
            </el-form-item>
            <el-form-item label="特殊说明" :label-width="formLabelWidth">
              <input v-model="student.bir" type="text">
            </el-form-item>

          </el-form>
          <div class="demo-drawer__footer">
            <el-button @click="cancelForm">取 消</el-button>
            <el-button type="primary" @click="editStudentInfo">确 定</el-button>
          </div>
        </div>
      </el-drawer>
    </div>
  </div>
</template>

<script>
import Page from './Page'
export default {
  name: 'student',
  data: function () {
    return {
      students: [
        // { id: 1, name: 'zhangsan', age: 23, bir: '2021-03-18' },
        // { id: 2, name: 'xiaohei', age: 24, bir: '2021-01-18' }
      ],
      flag: false,
      table: false,
      dialog: true,
      loading: false,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      formLabelWidth: '80px',
      timer: null,
      student: {
        id: ''
      }
    }
  },
  components: {
    Page
  },
  methods: {
    fun (id) {
      this.findOne(id)
      this.flag = true
    },
    findAll () {
      this.$http.get('http://49.235.47.70:9090/student/findAll?page=1&rows=4').then((res) => {
        this.students = res.data.results
      })
    },
    delRow (id) {
      this.$http.get('http://49.235.47.70:9090/student/delete?id=' + id).then(res => {
        console.log(res)
        if (res.data.success) {
          alert(res.data.msg + ',确认要删除该条信息吗')
          this.findAll()// 查询所有学生信息
        }
      })
    },
    handleClose (done) {
      this.$parent.findAll()
    },
    cancelForm () {
      this.flag = false
      clearTimeout(this.timer);
    },
    findOne (id) {
      this.$http.get('http://49.235.47.70:9090/student/findOne?id=' + id).then(res => {
        console.log(res.data)
        this.student = res.data
      })
    },
    editStudentInfo () {
      this.$http.post('http://49.235.47.70:9090/student/update', this.student).then(res => {
        console.log(res)
        if (res.data.success) {
          this.findAll()
          this.flag = false
        }
      })
    }
  },
  created () {
    this.findAll()
  },
  watch: {// 用来监听
    $route: {
      handler (val, oldval) {
        // console.log(val)// 新路由信息

        if (val.path === '/student') {
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
#table1 {
  margin: auto;
  width: 50%;
  border: 10px rgb(193, 209, 212);
}
</style>
