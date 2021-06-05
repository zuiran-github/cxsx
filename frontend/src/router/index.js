import Vue from 'vue'
import Router from 'vue-router'
// 引用页面模板->供路由使用
import index from '../pages/index.vue'
import ticketSearch from '../pages/ticketSearch.vue'
import fooddiscounts from '../pages/fooddiscounts.vue'
import ticketinfos from '../pages/ticketinfos.vue'
import ticketinfos2 from '../pages/ticketinfos2.vue'
import schedule from '../pages/schedule.vue'
import discount from '../pages/discount.vue'
import tickets from '../pages/tickets.vue'
import tickets2 from '../pages/tickets2.vue'
import hotels from '../pages/hotels.vue'
import foods from '../pages/foods.vue'
import try1 from '../pages/try.vue'
import showPath from '../pages/showPath.vue'
import blank from '../pages/blank.vue'
import scenicSearch from '../pages/scenicSearch.vue'
import food from '../components/food.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: try1
    },
    {
      path: '/ticket',
      name: 'ticketSearch',
      component: ticketSearch
    },
    {
      path: '/hotel',
      name: 'hotelSearch',
      component: scenicSearch
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
      path: '/discount/discounts',
      name: 'fooddiscount',
      component: fooddiscounts
    },
    {
      path: '/discount/scenictickets',
      name: 'scenictickets',
      component: ticketinfos
    },
    {
      path: '/discount/food',
      name: 'foods',
      component: foods
    },
    {
      path: '/discount/scenicticket',
      name: 'scenicticket',
      component: ticketinfos2
    },
    {
      path: '/ticket/ticketResult',
      name: 'tickets',
      component: tickets
    },
    {
      path: '/ticket/ticketResults',
      name: 'tickets2',
      component: tickets2
    },
    {
      path: '/hotel/hotelResult',
      name: 'hotels',
      component: hotels
    },
    {
      path: '/hotel/hotelResult/path',
      name: 'path',
      component: showPath
    },
    {
      path: '/stry',
      name: 'strys',
      component:food,
    },
    {
      path: '/blank',
      name: 'blank',
      component: blank
    },
  ]
})
