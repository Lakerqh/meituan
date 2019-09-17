<template>
    <div id="dataDetail">
        <div class="siteName">{{$route.query.siteName}}</div>
        <div class="echartBox">
            <div id="currentEchart" style="width:9rem; height:12rem"></div>
        </div>
    </div>
</template>
<script>
    import {
        Notify
    } from 'vant';
    export default {
        data() {
            return {

            }
        },
        mounted() {
            this.getData()
        },
        methods: {
            getData() {
                let params = {
                    stCode: this.$route.query.siteNo,
                }
                let url = this.$api.queryStationTempByPageDateil
                this.$http.post(url, params).then(res => {
                    if (res.data.code == 0) {
                        let list = res.data.result.list
                        this.renderEchart(list)
                    } else {
                        Notify(res.data.message);
                    }

                })
            },
            renderEchart(list) {
                let xdata = [];
                let ydata = [];
                list.forEach(item => {
                    xdata.push(item.tt)
                    ydata.push(item.Z)
                });
                var dom = document.getElementById('currentEchart')
                var myChart = this.echarts.init(dom)
                let option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross',
                            label: {
                                backgroundColor: '#6a7985'
                            }
                        }
                    },
                    legend: {
                        data: ['水位']
                    },
                    dataZoom: [{
                        type: 'inside',
                        start: 0,
                        end: 50
                    }, {
                        start: 0,
                        end: 50,
                        handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
                        handleSize: '80%',
                        handleStyle: {
                            color: '#fff',
                            shadowBlur: 3,
                            shadowColor: 'rgba(0, 0, 0, 0.6)',
                            shadowOffsetX: 2,
                            shadowOffsetY: 2
                        }
                    }],
                    xAxis: [{
                        type: 'category',
                        boundaryGap: false,
                        data: xdata
                    }],
                    yAxis: [{
                        type: 'value'
                    }],
                    series: [{
                        name: '水位',
                        type: 'line',
                        lineStyle: {
                            color: '#2c89f8'
                        },
                        areaStyle: {
                            color: '#2c89f8'
                        },
                        data: ydata
                    }]
                };
                // 绘制图表
                myChart.setOption(option)
            }
        }
    }

</script>
<style lang="scss" scoped>
    #dataDetail {
        height: 100%;
        padding: 10px;
        box-sizing: border-box;
        background: #f2f2f2;
        .siteName{
            height: 2rem;
            text-align: center;
            line-height: 2rem;
            font-size: 18px;
            background: #ffffff;
            border-radius: 10px;
            margin-bottom: 1px;
        }
        .echartBox {
            height: calc(100% - 2rem);
            background: #ffffff;
            border-radius: 10px;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }
    }

</style>
