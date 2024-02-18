
<script>
    export default{
        data(){
            return {
                user_name: "",
                user_ID: "",
                logined: false,
                justReg: false,
                password: ""
            }
        },

        components:{
        },
        methods:{
            setUserName(data){
                this.user_name = data.uname
                this.user_ID = data.uid
                this.logined = true
            },
            setAutoLogin(data) {
                this.user_ID = data.uid
                this.password = data.pw
                this.justReg = true
            },
            homeButton() {
                this.$router.push('/')
                this.logined = false
                this.justReg = false
                this.user_name = ""
                this.user_ID = ""
                this.password = ""
            }
        }
    }
</script>

<template>
    <div class="home">
        <button id="home" class="btn btn-primary" @click="homeButton">Logout to Home</button>
    </div>
    <div>
        <router-view @logining="setUserName" 
                     @registered="setAutoLogin" 
                     :userName="user_name" 
                     :uID="user_ID"
                     :jReg="justReg"
                     :password="password"
                     :logined="logined">
        </router-view>
    </div>

    <Bottom/>
</template>

<style scoped>
    .home{
        margin-top: 10px;
        width: 150px;
        margin-left: auto;
    }
    #home{
        font-size: small;
    }
</style>