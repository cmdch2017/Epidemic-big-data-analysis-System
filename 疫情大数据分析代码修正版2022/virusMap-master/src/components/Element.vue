
<template>
  <div>
    <h2>国内外疫情数据Top榜单</h2>
    <!--导出表格数据-->
    <div id="stock-concentration-analysis-table">
      疫情数据分析表
      <el-row :gutter="20">
        <div class="text-right">
          <el-col :span="12">
            <el-button type="primary" size="mini" @click="deriveExcel('table2')">
              导出
            </el-button>
          </el-col>
        </div>
        <div class="text-right">
          <el-col :span="12">
            <el-button type="primary" size="mini" @click="deriveExcel('table')">
              导出
            </el-button>
          </el-col>
        </div>
      </el-row>
      <!--中间空格部分-->
      <el-row style="height: 10px" />
      <el-row :gutter="20">
        <!--leftTable-->
        <el-col :span="12">
          <el-table v-if="showTableFlag" id="table2" :data="tableData2" lazy border style="width: 640px">
            <el-table-column prop="col1" label="集中度指标" style="width: 40%" />
            <el-table-column prop="col2" label="指标结果" style="width: 60%" />
          </el-table>
        </el-col>
        <!--rightTable-->
        <el-col :span="12">
          <el-table v-if="showTableFlag" id="table" :data="tableData" lazy border style="width: 100%">
            <el-table-column prop="col1" label="集中度指标" style="width: 40%" />
            <el-table-column prop="col2" label="指标结果" style="width: 60%" />
          </el-table>
        </el-col>
      </el-row>
    </div>

  </div>
</template>
<script>
import XLSXS from 'xlsx-style'
export default {
  data () {
    return {
      ExcelFlag: true,
      showTableFlag: true,

      tableData: [{
        col1: '新冠累计最多国家',
        col2: '美国'
      }, {
        col1: '新冠累计最多国家比例(%)',
        col2: '22.2222'
      }, {
        col1: '新冠累计最多三个国家',
        col2: '美国，印度，巴西'
      }, {
        col1: '新冠累计最多三个国家比例(%)',
        col2: '37.1651'
      }],
      tableData2: [
        {
          col1: '新冠国内累计最多省',
          col2: '湖北'
        }, {
          col1: '新冠国内累计最多城市比例(%)',
          col2: '65.6653'
        },
        {
          col1: '新冠国内累计最多三个省',
          col2: '湖北，香港，广东'
        }, {
          col1: '新冠国内累计最多三个省比例(%)',
          col2: '79.3229'
        }
      ]
    }
  }, methods: {
    deriveExcel (table) {
      if (!this.showTableFlag) return
      let dom = document.getElementById(table)
      if (this.ExcelFlag) {
        let a = document.querySelectorAll('.has-gutter .gutter')
        a[0].parentElement.removeChild(a[0])
        a[1].parentElement.removeChild(a[1])
        this.ExcelFlag = false
      }

      let workbook = this.$XLSX.utils.table_to_book(dom, { sheet: '分组表' }); //需要在table上定义一个id
      try {
        this.setExlStyle(workbook['Sheets']['分组表'])
        //仅在报表有合并时使用
        // this.addRangeBorder(workbook['Sheets']['分组表']['!merges'], workbook['Sheets']['分组表'])
        var ws = XLSXS.write(workbook, {
          type: "buffer"
        })
        this.$FileSaver.saveAs(
          new Blob([ws], { type: "application/octet-stream" }),
          `疫情数据Top表.xlsx`
        );

        this.$message({
          type: 'success',
          message: '导出成功,注意查收系统下载文件'
        })
      } catch (e) {
        this.$message({
          type: 'success',
          message: '导出失败,失败信息:' + e
        })
      }
    },
    setExlStyle (data) {
      let borderAll = {  //单元格外侧框线
        top: {
          style: 'thin',
        },
        bottom: {
          style: 'thin'
        },
        left: {
          style: 'thin'
        },
        right: {
          style: 'thin'
        }
      };
      data['!cols'] = [];
      for (let key in data) {
        if (data[key] instanceof Object) {
          data[key].s = {
            border: borderAll,
            alignment: {
              horizontal: 'center',   //水平居中对齐
              vertical: 'center'
            },
            font: {
              sz: 11
            },
            bold: true,
            numFmt: 0
          }
          data['!cols'].push({ wpx: 200 });
        }
      }
      return data;
    },
    addRangeBorder (range, ws) {
      let arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
      range.forEach(item => {
        let startRowNumber = Number(item.s.c),
          endRowNumber = Number(item.e.c);

        for (let i = startRowNumber + 1; i <= endRowNumber; i++) {
          ws[arr[i] + (Number(item.e.r) + 1)] = { s: { border: { top: { style: 'thin' }, left: { style: 'thin' }, bottom: { style: 'thin' }, right: { style: 'thin' } } } };
        }
        //手动补上标题栏的高度

      })
      return ws;

    }


  },
}
</script>