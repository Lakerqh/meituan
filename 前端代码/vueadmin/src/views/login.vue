<template>
    <div id="login">
        <div class="box">
            <input type="text" v-model="name">
            <input type="text" v-model="message">
            <div>
                <span @click="login">提交</span>
                <span @click="delete_note">删除</span>{{id}}
                <span @click="updatenote">修改</span>{{id}}
            </div>
        </div>
        <div>
            <p v-for="(item,index) in list" :key="index" @click="selectnote(item.id)">{{item.name}}:{{item.message}}</p>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                name: '',
                message: '',
                list: [],
                id:''
            }
        },
        mounted() {
            this.getlist()
        },
        methods: {
            login() {
                let params = {
                    name: this.name,
                    message: this.message
                }
                this.$http.post('/api/add', params).then(res => {
                    this.getlist()
                })
            },
            getlist() {
                this.$http.get('/api/list').then(res => {
                    this.list = res.data.result
                })
            },
            selectnote(id){
                this.id = id
            },
            delete_note() {
                let params = {
                    id: this.id,
                }
                this.$http.post('/api/deletenote',params).then(res => {
                    this.getlist()
                })
            },
            updatenote(){
                let params = {
                    id: this.id,
                    name:'zhoujielun',
                    message:'china person'
                }
                this.$http.post('/api/updatenote',params).then(res => {
                    this.getlist()
                })
            }
        }
    }

</script>
<style lang="scss">
    #login {
        height: 100%;
        
    }

</style>
