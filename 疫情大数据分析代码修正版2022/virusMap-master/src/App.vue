
<template>
  <div id="app">

    <el-container style="height: 738px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-active="this.$route.path" router mode="vertical" :default-openeds="['1','2']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>数据展示</template>
            <el-menu-item-group>

              <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
                {{ item.navItem }}
              </el-menu-item>

            </el-menu-item-group>

          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-message"></i>模拟数据</template>
            <el-menu-item-group>

              <el-menu-item v-for="(item,i) in navList2" :key="i" :index="item.name">
                {{ item.navItem }}
              </el-menu-item>

            </el-menu-item-group>

          </el-submenu>
          <el-submenu index="3"> <template slot="title"><i class="el-icon-message"></i>显示大屏</template>
            <el-menu-item>
              <router-link to="/EpidemicMap" @click="fun">疫情大屏</router-link>
            </el-menu-item>
          </el-submenu>
        </el-menu>
        <!--弟弟模式，使用文字超链接-->
        <!-- <el-menu :default-openeds="['1','2']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">
                <router-link to="/Table">表单</router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/Time">时间</router-link>
              </el-menu-item>
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>导航二</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu> -->
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>个人信息</el-dropdown-item>
              <el-dropdown-item>账号信息管理</el-dropdown-item>
              <el-dropdown-item>关于我们</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>Admin</span>
        </el-header>

        <el-main>
          <router-view />
        </el-main>
        <el-footer>

          版权所有 © {{ new Date().getFullYear() }} 陕西科技大学 刘舒同

          未经许可不得复制、转载或摘编，违者必究!

        </el-footer>

      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      navList: [
        { name: '/DataAdd', navItem: '数据爬取及结果演示' }
        ,
        { name: '/exercise1', navItem: '疫情新闻' },
        { name: '/shanghai', navItem: '香港疫情' },
        { name: '/Message', navItem: '云南疫情追溯' },
        { name: '/world', navItem: '世界数据一览' },
        { name: '/china', navItem: '中国数据一览' },
        { name: "/Element", navItem: '疫情数据导出' },
        { name: '/Table', navItem: '预测分析' },
      ],
      navList2: [
        { name: '/Time', navItem: '模拟数据展示' },

        // { name: '/PersonalInfo', navItem: '模拟数据预览' },

        { name: '/student', navItem: '模拟数据编辑' },

      ]
    }
  },
  methods: {
    fun () {

    }
  },
}
</script>

<style>
/* .router-link-active {
  text-decoration: none;
} */

.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
}

.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}
</style>
