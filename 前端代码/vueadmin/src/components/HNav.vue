<template>
    <div id="hnav">
        <div v-for="(item,index) in List" :key="index" @click="selectNav(item.path,index)">
            <img :src="item.srcin" v-if="i == index">
            <img :src="item.srcout" v-else>
            <p>{{item.name}}</p>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                i:0,
                List:[
                    {
                        name:'积水信息',
                        srcin:'./../../static/img/currentdata/sssj_xz@2x.png',
                        srcout:'./../../static/img/currentdata/sssj_wxz@2x.png',
                        path:'/home/currentdata'
                    },
                    {
                        name:'预警信息',
                        srcin:'./../../static/img/currentdata/lssj_xz@2x.png',
                        srcout:'./../../static/img/currentdata/lssj_wxz@2x.png',
                        path:'/home/historydata'
                    },
                    {
                        name:'报警信息',
                        srcin:'./../../static/img/currentdata/lssj_xz@2x.png',
                        srcout:'./../../static/img/currentdata/lssj_wxz@2x.png',
                        path:'/home/warning'
                    },
                ]
            }
        },
        methods: {
            selectNav(path,index) {
               this.i = index
               this.$router.push({
                   path:path
               })
            },
        }
    }

</script>
<style lang="scss" scoped>
    #hnav {
        height: 1.4rem;
        background: #ffffff;
        display: flex;
        align-items: center;
        
        div{
            text-align: center;
            flex-grow: 1;
            box-sizing: border-box;
            font-size: 12px;
            color: #666666;
            img{
                width: 0.6rem;
                height: 0.6rem;
            }
        }

    }

</style>
