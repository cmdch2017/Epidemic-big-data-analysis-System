<template>
  <div>

    <el-drawer title="表格页面"
               :before-close="handleClose"
               :visible.sync="dialog"
               direction="rtl"
               custom-class="demo-drawer"
               ref="drawer">
      <div class="demo-drawer__content">
        <el-form :model="form">
          <el-form-item label="用户名"
                        :label-width="formLabelWidth">
            <input v-model="student.name"
                   type="text">
          </el-form-item>
          <el-form-item label="年龄"
                        :label-width="formLabelWidth">
            <input v-model="student.age"
                   type="text">
          </el-form-item>
          <el-form-item label="生日"
                        :label-width="formLabelWidth">
            <input v-model="student.bir"
                   type="text">
          </el-form-item>

        </el-form>
        <div class="demo-drawer__footer">
          <el-button @click="cancelForm">取 消</el-button>
          <el-button type="primary"
                     @click="editStudentInfo">确 定</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
    };
  },
  methods: {
    handleClose(done) {
      this.$parent.findAll()
    },
    cancelForm() {
      this.loading = false;
      this.dialog = false;
      clearTimeout(this.timer);
    },
    findOne() {
      this.$http.get('http://localhost:9090/student/findOne?id=' + this.student.id).then(res => {
        console.log(res.data)
        this.student = res.data
      })
    },
    editStudentInfo() {
      this.$http.post('http://localhost:9090/student/update', this.student).then(res => {
        console.log(res)
        if (res.data.success) {
          this.$parent.findAll()
          this.$router.push('/student')
        }
      })
    }
  },
  created() {
    console.log("获取行号" + this.$route.query.id)
    this.student.id = this.$route.query.id
    this.findOne()
  },
  components: {

  }
}
</script>