
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
            // HelloWorld
        },
        methods:{
            setUserName(data){
                console.log("Success login")
                this.user_name = data.uname
                this.user_ID = data.uid
                this.logined = true
                console.log(this.user_ID)
            },
            setAutoLogin(data) {
                this.user_ID = data.uid
                this.password = data.pw
                this.justReg = true
                console.log(this.user_ID)
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
    <!-- <HelloWorld/> -->
    <!-- <Home/> -->
    <div class="home">
        <button id="home" class="btn btn-primary" @click="homeButton">Logout to Home</button>
    </div>
    <!-- <router-link to="/">Home</router-link>
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/create">Create</router-link> |
    <router-link to="/eventInfo">EventInfo</router-link> |
    <router-link to="/join">Join</router-link> |
    <router-link to="/eventEntry">EventEntry</router-link>  -->
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