import axios from 'axios';
import qs from 'qs';
import router from './../router/index'


// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 添加headers到post请求中
    config.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
    // let token = localStorage.getItem('token');
    // if (token != null) {
    //     config.headers['token'] = token;
    // }
    // 在发送请求之前做些什么
    return config;
}, function (error) {
    return Promise.reject(error);
});

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    return Promise.reject(error);
});


export default {
    get(url) {
        return new Promise((resolve, reject) => {
            axios.get(url).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    delete(url, params) {
        return new Promise((resolve, reject) => {
            axios.delete(url, params).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    post(url, params = {}) {
        return new Promise((resolve, reject) => {
            axios.post(url, qs.stringify(params)).then(function (data) {
                resolve(data);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    put(url, params) {
        return new Promise((resolve, reject) => {
            axios.put(url, params).then(function (data) {
                resolve(data);
            }).catch((error) => {
                reject(error)
            })
        })
    },
}
