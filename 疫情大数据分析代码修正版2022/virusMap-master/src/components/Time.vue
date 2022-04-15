<template>

  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item><i class="el-icon-date"></i> 模拟数据</el-breadcrumb-item>
      <el-breadcrumb-item>模拟数据展示</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="container">
      <div class="left-group"></div>
      <div class="mid-group">
        <el-input type="textarea" autosize placeholder="请输入标题：上海市浦东新区每月累计新增疫情数" v-model="textarea1">
        </el-input>
      </div>
      <div class="right-group"></div>
    </div>

    <div style="width: 75%;height: 280px;border:0px solid rgb(180,180,180)" id="main" />
    <div style="width: 75%;height: 280px;border:0px solid rgb(180,180,180)" id="main2" />

  </div>

</template>
<script>
export default {
  async mounted () {
    await this.handleUserList()
    let lineChart = this.$echart.init(document.getElementById('main'))
    lineChart.setOption(this.option)
    let pieChart = this.$echart.init(document.getElementById('main2'))
    pieChart.setOption(this.optionpie)
  },
  data () {
    return {
      optionpie: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      },
      textarea1: '',
      students: [],
      newStudents: [],
      option: {
        xAxis: {
          type: 'category',
          data: []
        },
        yAxis: {
          type: 'value'
        },
        series:
          [{
            data: [],
            type: 'line',
            smooth: true
          }]

      }
    }
  },
  created () {
  },
  methods: {
    async handleUserList () {

      await this.$http.get('http://49.235.47.70:9090/student/findAll').then((res) => {

        this.students = res.data.results
        var newArray = new Array()
        var newArrayName = new Array()
        var i;
        for (i = 0; i < this.students.length; i++) {
          const answer = parseInt(this.students[i].age)
          newArray[i] = answer;
          newArrayName[i] = this.students[i].name
        }
        this.option.series[0].data = newArray
        this.option.xAxis.data = newArrayName
        this.optionpie.series[0].data = newArray
        this.optionpie.xAxis.data = newArrayName

      }
      )


    }
  },
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
  width: 500px;
  text-align: center;
}
.mid-group {
  flex: 1;
  text-align: center;
}
</style>