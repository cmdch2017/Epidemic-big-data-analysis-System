<template>

  <div>

    <div class="container">
      <div class="left-group"></div>
      <div class="mid-group">
        香港近日新增疫情折线图
      </div>
      <div class="right-group"></div>
    </div>

    <div style="width: 100%;height: 300px;border:0px solid rgb(180,180,180)" id="main" />
    <div class="container">
      <div class="left-group"></div>
      <div class="mid-group">
        香港近日累计新增疫情折线图
      </div>
      <div class="right-group"></div>
    </div>
    <div style="width: 100%;height: 300px;border:0px solid rgb(180,180,180)" id="main2" />
    <div class="container">
      <div class="left-group"></div>
      <div class="mid-group">
        香港近日累计治愈折线图
      </div>
      <div class="right-group"></div>
    </div>
    <div style="width: 100%;height: 300px;border:0px solid rgb(180,180,180)" id="main3" />
    <div class="container">
      <div class="left-group"></div>
      <div class="mid-group">
        香港近日累计死亡折线图
      </div>
      <div class="right-group"></div>
    </div>
    <div style="width: 100%;height: 300px;border:0px solid rgb(180,180,180)" id="main4" />

  </div>

</template>
<script>
export default {
  async mounted () {
    await this.handleUserList()
    let lineChart = this.$echart.init(document.getElementById('main'))
    lineChart.setOption(this.option)
    let lineChart2 = this.$echart.init(document.getElementById('main2'))
    lineChart2.setOption(this.option2)
    let lineChart3 = this.$echart.init(document.getElementById('main3'))
    lineChart3.setOption(this.option3)
    let lineChart4 = this.$echart.init(document.getElementById('main4'))
    lineChart4.setOption(this.option4)
  },
  data () {
    return {
      students: [],
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

      },
      option2: {
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

      },
      option3: {
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

      },
      option4: {
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

      await this.$http.get('http://49.235.47.70:9090/china/findXianggang').then((res) => {

        this.students = res.data.results
        var newArray = new Array()
        var newArray2 = new Array()
        var newArray3 = new Array()
        var newArray4 = new Array()

        var newArrayName = new Array()

        var i;
        for (i = 0; i < this.students.length; i++) {
          const answer = parseInt(this.students[i].confirm)
          newArray[i] = answer;
          const confirm_all = parseInt(this.students[i].confirm_all)
          newArray2[i] = confirm_all
          const heal = parseInt(this.students[i].heal)
          newArray3[i] = heal
          const dead = parseInt(this.students[i].dead)
          newArray4[i] = dead
          newArrayName[i] = this.students[i].last_update_time
        }
        this.option.series[0].data = newArray
        this.option2.series[0].data = newArray2
        this.option3.series[0].data = newArray3
        this.option4.series[0].data = newArray4

        this.option.xAxis.data = newArrayName
        this.option2.xAxis.data = newArrayName
        this.option3.xAxis.data = newArrayName
        this.option4.xAxis.data = newArrayName



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