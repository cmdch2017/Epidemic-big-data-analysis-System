<template>
  <div>
    <h1>学生更新信息</h1>
    <form action="">
      用户名：<input v-model="student.name" type="text"><br>
      年龄：<input v-model="student.age" type="text"><br>
      生日：<input v-model="student.bir" type="text"><br>
      <input type="button" @click="editStudentInfo" value="更新学生信息">
    </form>
  </div>

</template>

<script>
export default {
  name: 'StudentEdit',
  data () {
    return {
      student: {
        id: ''
      }
    }
  },
  methods: {
    findOne () {
      this.$http.get('http://49.235.47.70:9090/student/findOne?id=' + this.student.id).then(res => {
        console.log(res.data)
        this.student = res.data
      })
    },
    editStudentInfo () {
      this.$http.post('http://49.235.47.70:9090/student/update', this.student).then(res => {
        console.log(res)
        if (res.data.success) {
          this.$parent.findAll()
          this.$router.push('/student')
        }
      })
    }

  },
  created () {
    console.log("获取行号" + this.$route.query.id)
    this.student.id = this.$route.query.id
    this.findOne()
  },
  components: {

  }
}
</script>
<style scoped>
</style>
