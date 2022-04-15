import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui';
import Table from '../components/Table'


Vue.use(Router)

Vue.use(ElementUI)

export default new Router({
  routes: [{
    path: '/',
    redirect: '/Home'
  }, {
    path: '/EpidemicMap',
    name: 'EpidemicMap',
    component: () => import('../components/EpidemicMap')
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home
  }, {
    path: '/Table',
    name: 'Table',
    component: Table
  },
  {
    path: '/world',
    name: 'world',
    component: () => import('../components/World')
  },
  {
    path: '/china',
    name: 'china',
    component: () => import('../components/China')
  }, {
    path: '/shanghai',
    name: 'shanghai',
    component: () => import('../components/Shanghai')
  }, {
    path: '/Time',
    component: () => import('../components/Time'),
  }, {
    path: '/PersonalInfo',
    name: 'PersonalInfo',
    component: () => import('../components/PersonalInfo')
  }, {
    path: '/Message',
    name: 'Message',
    component: () => import('../components/Message')
  },
  {
    path: '/student',
    name: 'student',
    component: () => import('../components/Student'),
    children: [{
      path: 'add',
      name: 'add',
      component: () => import('../components/StudentAdd')
    }, {
      path: 'edit',
      name: 'edit',
      component: () => import('../components/StudentEdit')
    }]
  }, {
    path: '/exercise1',
    name: 'exercise1',
    component: () => import('../components/Exercise1')
  },
  {
    path: '/Element',
    name: 'Element',
    component: () => import('../components/Element')
  }, {
    path: '/DataAdd',
    name: 'DataAdd',
    component: () => import('../components/DataAdd')
  },

  ]
})
