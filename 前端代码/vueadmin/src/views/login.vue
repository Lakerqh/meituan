<template>
    <div id="login">
        <div class="box">
            <h3>QH个人Python项目系统</h3>
            <el-input placeholder="请输入账号" v-model="username">
                <template slot="prepend">账号</template>
            </el-input>
            <!-- <el-input placeholder="请输入密码" v-model="password">
                <template slot="prepend">密码</template>
            </el-input> -->
            <el-input type="password" autocomplete="off" v-model="password">
                <template slot="prepend">密码</template>
            </el-input>
            <el-button type="primary" @click="onSubmit">登录</el-button>
            <el-button>注册</el-button>
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
        }
    }

</script>
<style lang="scss" scoped>
    #login {
        height: 100%;
        background: url('./../../static/img/login/login.png') no-repeat;
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        justify-content: space-around;

        .box {
            width: 30%;
            height: 35%;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
            padding: 0 50px;
            box-sizing: border-box;

            h3 {
                color: #365a7a;
                text-align: center;
                margin: 30px 0 20px 0;
            }

            .el-input-group {
                margin: 20px 0;
            }
            .el-button--primary{
                width: 30%
            }
        }
    }

</style>
