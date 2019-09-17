// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vant from 'vant'
import 'vant/lib/index.css'
import animate from 'animate.css'
import VueWechatTitle from 'vue-wechat-title'
import Echarts from 'echarts'
import api from './api/api'
import http from './api/index'

Vue.use(Echarts)
Vue.use(Vant)
Vue.use(VueWechatTitle);

Vue.prototype.echarts = Echarts
Vue.prototype.$api = api
Vue.prototype.$http = http

/*
 * 这段代码解决重复跳转到相同路由控制台报错的问题
 */
import Router from 'vue-router'
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
    if (to.meta.title) {
        window.document.title = to.meta.title
        next()
    }
})

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: {
        App
    },
    template: '<App/>'
})
