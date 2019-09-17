<template>
    <div id="historyData" class="animated slideInRight">
        12
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
           
        },
        methods: {
           
        }
    }

</script>
<style lang="scss" scoped>
    #historyData {
        height: 100%;

        .siteName {
            display: flex;
            align-items: center;
            height: 1.4rem;
            background: #ffffff;

            .site {
                width: 8rem;
                display: flex;
                align-items: center;
                padding: 0 10px;

                img {
                    width: 0.5rem;
                    height: 0.5rem;
                    margin-right: 10px;
                }

                h2 {
                    width: 6rem;
                    overflow: hidden;
                    white-space: nowrap;
                    text-overflow: ellipsis;
                    font-size: 15px;
                    color: #333333;
                    font-weight: bold;
                    background: #f7f8fa;
                    border-radius: 15px;
                    padding: 5px 10px;
                }
            }

            .type {
                width: 2rem;
                display: flex;
                align-items: center;

                img {
                    width: 0.6rem;
                    height: 0.6rem;
                    margin-left: 5px;
                }

                h2 {
                    font-size: 14px;
                    color: #333333;
                }
            }
        }

        .datebox {
            height: 1.4rem;
            background: #ffffff;
            display: flex;
            align-items: center;

            .stdate,
            .eddate {
                width: 4.5rem;
                display: flex;
                align-items: center;
                padding: 0 5px;

                img {
                    width: 0.53rem;
                    height: 0.53rem;
                    margin-right: 6px;
                }

                span {
                    color: #333333;
                    width: 3.5rem;
                    font-size: 12px;
                    height: 0.5rem;
                    line-height: 0.5rem;
                    background: #f7f8fa;
                    border-radius: 15px;
                    padding: 5px 0px;
                    text-align: center;
                    white-space: nowrap;
                    overflow: hidden;
                }
            }

            .search {
                width: 1rem;
                display: flex;
                align-items: center;

                img {
                    width: 0.6rem;
                    height: 0.6rem;
                    border: 1px solid #cccccc;
                    border-radius: 0.6rem;
                }
            }
        }

        .content {
            height: calc(100% - 2.8rem);
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
                            background: #df5136;
                            color: #ffffff;
                            font-size: 14px;
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

                    .date {
                        width: 30%;
                        box-sizing: border-box;
                        display: flex;
                        align-items: center;

                        .month {
                            font-size: 15px;
                            color: #333;
                            font-weight: bold;
                        }

                        .time {
                            font-size: 13px;
                            color: #999999;
                        }
                    }

                    .dateName {
                        width: 70%;
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

            .echartBox {
                height: calc(100% - 10px);
                background: #ffffff;
                border-radius: 10px;
                display: flex;
                justify-content: space-around;
                align-items: center;
            }
        }
    }

</style>
