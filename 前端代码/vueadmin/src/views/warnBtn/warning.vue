<template>
    <div id="pageone" class="animated slideInRight">
        <div class="box">
            <div>
                <van-button type="info">信息按钮</van-button>
            </div>
            <div>
                <van-button type="warning">警告按钮</van-button>
            </div>
            <div>
                <van-button type="danger">危险按钮</van-button>
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

        .box {
            height: 100%;
            background: #ffffff;
            overflow: auto;
            >div{
                text-align: center;
                padding: 1rem;
            }
        }
    }

</style>
