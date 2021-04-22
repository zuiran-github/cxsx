import Vue from 'vue'
import Router from 'vue-router'
// 引用页面模板->供路由使用
import index from '../pages/index.vue'
import ticketSearch from '../pages/ticketSearch.vue'
import hotelSearch from '../pages/hotelSearch.vue'
import schedule from '../pages/schedule.vue'
import discount from '../pages/discount.vue'
import tickets from '../pages/tickets.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/ticket',
      name: 'ticketSearch',
      component: ticketSearch
    },
    {
      path: '/hotel',
      name: 'hotelSearch',
      component: hotelSearch
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: schedule
    },
    {
      path: '/discount',
      name: 'discount',
      component: discount
    },
    {
      path: '/ticket/ticketResult',
      name: 'tickets',
      component: tickets
    }
  ]
})
