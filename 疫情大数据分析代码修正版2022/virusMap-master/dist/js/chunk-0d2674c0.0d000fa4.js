(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0d2674c0"],{"55e3":function(t,e,a){t.exports=a.p+"img/hdfs.e1f1a16b.jpg"},b85d:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("h2",[t._v("项目主要流程")]),n("form",{attrs:{action:""}},[n("input",{attrs:{type:"button",value:"1、爬取数据信息，经过数据清洗后保存为csv文件"},on:{click:t.save1To2}})]),n("p",[t.clickShowHDFS?n("input",{attrs:{type:"button",value:"2、上传至hdfs，并将文件保存入数据库"},on:{click:t.saveStudentInfo}}):t._e()]),t.clickShowTodayInformation?n("div",{staticClass:"cantainer"},[n("img",{attrs:{src:a("55e3")}}),n("h3",[t._v("中国今日Top榜")]),n("el-table",{staticStyle:{width:"1200px"},attrs:{stripe:"",data:t.worlds.slice((t.currentPage-1)*t.pagesize,t.currentPage*t.pagesize)}},[n("el-table-column",{attrs:{label:"省份名称",prop:"name",width:"240"}}),n("el-table-column",{attrs:{label:"最新确诊",prop:"confirm",width:"240"}}),n("el-table-column",{attrs:{label:"累计确诊",prop:"confirm_all",width:"240"}}),n("el-table-column",{attrs:{label:"累计死亡",prop:"dead",width:"240"}}),n("el-table-column",{attrs:{label:"累计治愈",prop:"heal",width:"240"}})],1),n("el-pagination",{attrs:{"current-page":t.currentPage,"page-sizes":[5,10,20,40],"page-size":t.pagesize,layout:"total, sizes, prev, pager, next, jumper",total:t.worlds.length},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}},[t._v(" //这是显示总共有多少数据， ")])],1):t._e()])},l=[],i={name:"DataAdd",data:function(){return{currentPage:1,pagesize:10,worlds:[],flag:"1",clickShowHDFS:!1,clickShowTodayInformation:!1}},methods:{save1To2:function(){this.clickShowHDFS=!0},saveStudentInfo:function(){var t=this;this.clickShowTodayInformation=!0,this.$http.post("http://49.235.47.70:9090/china/DataAdd",this.flag).then((function(e){t.worlds=e.data.results}))},handleSizeChange:function(t){this.pagesize=t},handleCurrentChange:function(t){this.currentPage=t}}},o=i,r=a("2877"),s=Object(r["a"])(o,n,l,!1,null,"7fba2aac",null);e["default"]=s.exports}}]);
//# sourceMappingURL=chunk-0d2674c0.0d000fa4.js.map