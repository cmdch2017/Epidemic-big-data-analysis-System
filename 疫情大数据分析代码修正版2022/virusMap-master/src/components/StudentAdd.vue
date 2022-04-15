<template>
  <div>
    <h2>模拟数据添加信息</h2>
    <form action="">
      名 称：<input v-model="student.name" type="text"><br>
      说 明：<input v-model="student.age" type="text"><br>
      数 值：<input v-model="student.bir" type="text"><br>
      <input type="button" @click="saveStudentInfo" value="添加模拟数据信息">
    </form>
  </div>

</template>

<script>
export default {
  name: 'StudentAdd',
  data () {
    return {
      student: {}
    }
  },
  methods: {
    saveStudentInfo () {
      // 发送axios请求
      console.log(this.student)
      this.$http.post('http://49.235.47.70:9090/student/add', this.student).then(res => {
        console.log(res)
        if (res.data.success) {
          this.$parent.findAll()
          this.$router.push('/student')
        }
      })
    }
  }
}
</script>
<style scoped>
</style>
