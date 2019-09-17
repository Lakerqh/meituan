<template>
    <div id="home">
        <div class="section">
            <router-view></router-view>
        </div>
        <h-nav></h-nav>
    </div>
</template>
<script>
import HNav from '@/components/HNav'
    export default {
        data() {
            return {

            }
        },
        mounted(){
        },
        methods: {
           
        },
        components:{
           HNav
        }
    }

</script>
<style lang="scss" scoped>
    #home {
        height: 100%;
        .section{
            height: calc(100% - 1.4rem);
            background: #f2f2f2;
            overflow: auto;
        }
    }

</style>
