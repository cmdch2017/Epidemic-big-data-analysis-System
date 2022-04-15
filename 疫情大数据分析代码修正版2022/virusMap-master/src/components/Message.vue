<template>
  <div>
    <h2>疫情数据追溯415——南丁格尔玫瑰图</h2>
    <div style="width: 100%;height: 500px;border:0px solid rgb(180,180,180)" id="coxcomb" />
    <div style="height: 100px" />
    <h2>云南一周天气——折线图</h2>
    <div style="width: 100%;height: 500px;border:0px solid rgb(180,180,180)" id="weather" />
    <div style="height: 100px" />

    <h2>云南新增追溯——组合图</h2>
    <div style="width: 100%;height: 500px;border:0px solid rgb(180,180,180)" id="mixed" />
    <TipsNews />
    <div style="height: 100px" />

    <YunnanNews />

  </div>
</template>
<script>
import TipsNews from '@/components/news/TipsNews'
import YunnanNews from '@/components/news/YunnanNews'
export default {
  mounted () {
    //绘制南丁格尔玫瑰图
    let pieChart = this.$echart.init(document.getElementById('coxcomb'))
    pieChart.setOption(this.optionCoxcomb)
    //绘制天气图
    let weatherChart = this.$echart.init(document.getElementById("weather"));
    weatherChart.setOption(this.optionWeather);
    //绘制组合图
    let mixedChart = this.$echart.init(document.getElementById("mixed"));
    mixedChart.setOption(this.option);

  },
  components: {
    YunnanNews,
    TipsNews
  },
  data () {
    return {
      option: {
        backgroundColor: '#0f375f',
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['line', 'bar'],
          textStyle: {
            color: '#ccc'
          }
        },
        xAxis: {
          data: ['2021-03-24', '2021-03-25', '2021-03-26', '2021-03-27', '2021-03-28', '2021-03-29', '2021-03-30', '2021-03-31', '2021-04-01', '2021-04-02', '2021-04-03', '2021-04-04', '2021-04-05', '2021-04-06', '2021-04-07', '2021-04-08', '2021-04-09', '2021-04-10', '2021-04-11', '2021-04-12', '2021-04-13', '2021-04-14', '2021-04-15'],
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        yAxis: {
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        series: [{
          name: '气温',
          type: 'line',
          smooth: true,
          showAllSymbol: true,
          symbol: 'emptyCircle',
          symbolSize: 15,
          data: [25, 26, 26, 26, 26, 27, 25, 25, 26, 26, 26, 25, 22, 16, 22, 22, 24, 25, 25, 26, 27, 26, 26]
        }, {
          name: '新增人数',
          type: 'bar',
          barWidth: 10,
          itemStyle: {
            barBorderRadius: 5,
            color: new this.$echart.graphic.LinearGradient(
              0, 0, 0, 1,
              [
                { offset: 0, color: '#14c8d4' },
                { offset: 1, color: '#43eec6' }
              ]
            )
          },
          data: [
            { value: 1 },
            { value: 0 },
            { value: 0 },
            { value: 0 },
            { value: 0 },
            { value: 0 },
            { value: 0 },
            { value: 0 },
            { value: 6 },
            { value: 6 },
            { value: 4 },
            { value: 8 },
            { value: 10 },
            { value: 15 },
            { value: 15 },
            { value: 2 },
            { value: 11 },
            { value: 8 },
            { value: 1 },
            { value: 0 },
            { value: 2 },
            { value: 1 },
            { value: 1 }
          ],
        }, {
          name: '气温',
          type: 'bar',
          barGap: '-100%',
          barWidth: 10,
          itemStyle: {
            color: new this.$echart.graphic.LinearGradient(
              0, 0, 0, 1,
              [
                { offset: 0, color: 'rgba(20,200,212,0.5)' },
                { offset: 0.2, color: 'rgba(20,200,212,0.2)' },
                { offset: 1, color: 'rgba(20,200,212,0)' }
              ]
            )
          },
          z: -12,
          data: [25, 26, 26, 26, 26, 27, 25, 25, 26, 26, 26, 25, 22, 16, 22, 22, 24, 25, 25, 26, 27, 26, 26]
        }, {
          name: '气温',
          type: 'pictorialBar',
          symbol: 'rect',
          itemStyle: {
            color: '#0f375f'
          },
          symbolRepeat: true,
          symbolSize: [12, 4],
          symbolMargin: 1,
          z: -10,
          data: [25, 26, 26, 26, 26, 27, 25, 25, 26, 26, 26, 25, 22, 16, 22, 22, 24, 25, 25, 26, 27, 26, 26]
        }]
      },
      optionWeather: {
        backgroundColor: 'rgba(252,173,54,0.1)',
        //图表标题
        title: {
          left: 20,
          top: 10, //进行标题位置的微调，top:10 距离顶端10px
          x: 'left', //标题的水平位置；left-左（默认）；right-右
          y: 'top', //垂直位置：bottom-将标题置于表底；center-中间；top-上
          //                    borderColor:'#999999', //标题边框的颜色
          //                    borderWidth:2, //标题边框的宽度，默认是0-无边框

          //修改标题字体
          //                    textStyle:{
          //                        fontSize:20,
          //                        color:'cornflowerblue',
          //                    },
          //注意：title一定要在text之前
          text: '上周气温'
          //                    subtext: '虚构天气' //小标题
        },

        //图例组件
        //默认位置是中间
        //大部分属性都和title类似
        legend: {
          //                    x:'center',
          //                    y:'bottom',
          //                    orient:'vertical' //布局方式，默认是水平布局；vertical-垂直布局
        },

        //提示框
        tooltip: {
          backgroundColor: "cornflowerblue" //设置背景色
        },

        //工具箱
        toolbox: {
          //                    padding:35,   //内边距
          right: 25,
          top: 10,
          show: true,
          //结构-样式图
          feature: {
            //mark是辅助线开关
            mark: {
              // show: true
            },
            //数据可视化标签
            dataView: {
              //                            show:true,
              readOnly: false //可修改数据
            },
            saveAsImage: {}, //下载标签
            magicType: { type: ['line', 'bar'] } //可更换图表样式标签
          }
        },

        //视觉映射组件
        visualMap: {
          right: 2,
          bottom: 10,
          //有几个花括号就代表分成几个区域显示
          pieces: [{
            gt: 0, lte: 10, color: "#096"
          },
          {
            gt: 10, lte: 20, color: "#ffde33"
          },
          {
            gt: 20, lte: 30, color: "#ff9933"
          }]
        },

        //图表位置
        grid: { x: 50, y: 50, x2: 100, y2: 50 },

        xAxis: [{
          data: ['4月1日', '4月2日', '4月3日', '4月4日', '4月5日', '4月6日', '4月7日']

        }],
        yAxis: {},
        //图标核心内容
        series: [{
          name: '最高气温',
          type: 'line',
          color: 'green',
          markLine: { data: [{ type: 'average', name: '平均值' }] },
          markPoint: { data: [{ type: 'max', name: '最大值' }, { type: 'min', name: '最小值' }] },
          data: [26, 26, 26, 25, 22, 16, 22]
        },
        {
          name: '最低气温',
          type: 'line',
          color: 'blue',
          markLine: { data: [{ type: 'average', name: '平均值' }] },
          markPoint: { data: [{ type: 'max', name: '最大值' }, { type: 'min', name: '最小值' }] },
          data: [15, 15, 14, 14, 12, 10, 12]
        }]
      },
      optionCoxcomb: {
        title: {
          text: '2021年4月15日现有确诊——累计确诊对比',
          // subtext: '纯属虚构',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          top: 'bottom'
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        series: [{
          name: '现有确诊人数',
          type: 'pie',
          radius: [50, 150],
          center: ['25%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 8
          },
          data: [
            { value: 85, name: '云南' },
            { value: 55, name: '上海' },
            { value: 44, name: '广东' },
            { value: 27, name: '台湾' },
            { value: 25, name: '福建' },
            { value: 16, name: '四川' },
            { value: 13, name: '陕西' },
            { value: 10, name: '北京' }
          ]
        },
        {
          name: '累计确诊人数',
          type: 'pie',
          radius: [50, 150],
          center: ['75%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 8
          },
          emphasis: {
            label: {
              show: true
            }
          },
          data: [
            { value: 2308, name: '广东' },
            { value: 1934, name: '上海' },
            { value: 1057, name: '北京' },
            { value: 1027, name: '台湾' },
            { value: 578, name: '陕西' },
            { value: 959, name: '四川' },
            { value: 582, name: '福建' },
            { value: 325, name: '云南' },
          ]
        }

        ]
      },

    }
  },
}
</script>
 <style type="text/css" scoped>
#weather {
  width: 600px;
  height: 400px;
  border: 1px solid red;
}
</style>
