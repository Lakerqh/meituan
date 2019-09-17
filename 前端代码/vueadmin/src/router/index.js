import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/home'
import Login from '@/views/login'
import Currentdata from '@/views/currentdata/currentdata'
import DataDetail from '@/views/currentdata/dataDetail'
import Historydata from '@/views/historydata/historydata'
import Warning from '@/views/warnBtn/warning'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path:'/',
            redirect:'/login'
        },
        {
            path:'/login',
            name:'Login',
            component: Login,
            meta: {
                title: '登录'
            }
        },{
        path: '/home',
        name: 'Home',
        component: Home,
        children: [{
                path: 'currentdata',
                name: 'Currentdata',
                component: Currentdata,
                meta: {
                    title: '积水信息'
                }
            },
            {
                path: 'historydata',
                name: 'Historydata',
                component: Historydata,
                meta: {
                    title: '预警信息'
                }
            },
            {
                path: 'warning',
                name: 'Warning',
                component: Warning,
                meta: {
                    title: '报警信息'
                }
            },
        ]
    },
    {
        path:'/dataDetail',
        name: 'DataDetail',
        component: DataDetail,
        meta: {
            title: '站点图表信息'
        }
    }
    ]
})
