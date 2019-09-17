<template>
    <div id="pageone" class="animated slideInRight">
        <div class="swiperBox">
            <van-swipe :autoplay="3000" indicator-color="white">
                <van-swipe-item v-for="(item,index) in picList" :key="index"><img :src="item.src"></van-swipe-item>
            </van-swipe>
        </div>
        <div class="content">
            <div class="box">
                <div class="title">
                    <h1>站点名称</h1>
                    <p>
                        <span>襄阳站点</span>
                    </p>
                </div>
                <div class="boxSection">
                    <div class="dateName">
                        <div>
                            <p>
                                <img src="./../../../static/img/currentdata/sw_icon@2x.png">
                                <span>积水量</span>
                            </p>
                            <p>
                                <span class="math">adfasdf</span>
                                <span>m</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
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
                picList: [{
                        src: './../../../static/img/currentdata/pic1.jpg'
                    },
                    {
                        src: './../../../static/img/currentdata/pic2.jpg'
                    },
                    {
                        src: './../../../static/img/currentdata/pic3.jpg'
                    },
                    {
                        src: './../../../static/img/currentdata/pic4.jpg'
                    },
                ]
            }
        },
        mounted() {

        },
        methods: {

        }
    }

</script>
<style lang="scss" scoped>
    #pageone {
        height: 100%;

        .swiperBox {
            height: 5rem;

            img {
                width: 10rem;
                height: 5rem;
            }
        }

        .content {
            height: calc(100% - 5rem);
            padding: 10px 10px 0 10px;
            box-sizing: border-box;
            overflow: auto;

            .box {
                background: #ffffff;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 10px;

                .title {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    border-bottom: 1px solid #f2f2f2;
                    padding-bottom: 10px;

                    h1 {
                        font-size: 16px;
                        color: #333333;
                        font-weight: bold;
                        width: 6rem;
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;
                    }

                    p {
                        display: flex;
                        align-items: center;

                        span {
                            display: inline-block;
                            // background: #df5136;
                            // color: #ffffff;
                            font-size: 16px;
                            padding: 0.01rem 0.2rem;
                            border-radius: 20px;
                            margin-right: 10px;
                        }

                        .nomal {
                            background: #3fca71 !important;
                        }

                        img {
                            width: 0.48rem;
                            height: 0.48rem;
                        }
                    }
                }

                .boxSection {
                    display: flex;
                    margin-top: 10px;

                    .dateName {
                        width: 100%;
                        box-sizing: border-box;

                        >div {
                            display: flex;
                            justify-content: space-between;
                            padding: 5px 0;
                            padding-right: 0.5rem;

                            p {
                                display: flex;
                                align-items: center;

                                img {
                                    width: 0.56rem;
                                    height: 0.56rem;
                                    margin-right: 10px;
                                }

                                span {
                                    color: #666666;
                                    font-size: 14px;
                                }

                                .math {
                                    color: #333333;
                                    font-size: 16px;
                                    margin-right: 10px;
                                }
                            }
                        }
                    }
                }
            }
        }

    }

</style>
