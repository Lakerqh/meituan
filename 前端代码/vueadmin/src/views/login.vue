<template>
    <div id="login">
        <div class="box">
            <input type="text" v-model="username">
            <input type="text" v-model="password">
            <div>
                <span @click="login">登录</span>
                <span @click="register">注册</span>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                username: '',
                password: '',
            }
        },
        mounted() {
            // this.register()
        },
        methods: {
            login() {
                let params = {
                    username: this.username,
                    password: this.password
                }
                this.$http.post('/api/login', params).then(res => {

                })
            },
            register() {
                let params = {
                    username: this.username,
                    password: this.password
                }
                this.$http.post('/api/register', params).then(res => {

                })
            }
        }
    }

</script>
<style lang="scss">
    #login {
        height: 100%;
        padding-top: 250px;
        box-sizing: border-box;

        .box {
            width: 500px;
            height: 350px;
            margin: 0 auto;
        }
    }

</style>
