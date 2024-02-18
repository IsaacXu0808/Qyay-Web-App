<template>
    <div style="margin-left: auto; margin-right: auto; margin-top: 200px; width: 600px;">
        <legend style="text-align: center; font-size: 40px; font-weight: bold;">
            Login to create an event
        </legend>
    
        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 50px;">User ID</label>
            <input class="form-control" placeholder="Enter your user ID" v-model="userID"/>
        </div>
        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 20px;">Password</label>
            <input type="password" class="form-control" placeholder="Enter your password" v-model="passWord"/>
        </div>

        <div style="color: red; font-size: smaller;">
            <div v-if="state===1">User ID not found</div>
            <div v-else-if="state===2">Invalid Password</div>
            <div v-else-if="state===3">Uexpected error</div>
        </div>

        <div style="text-align: center; margin-top: 60px;">
            <button class="btn btn-primary" style="width: 120px; font-size: large;" @click="tryLogin">Login</button>
        </div>

        <div class=mb-3 style="text-align: center; margin-top: 50px;">
            <h2 class="title" style="margin-bottom: 30px;"> Do not have an account?</h2>
            <button @click="toRegister"  class="btn btn-primary" style="width: 120px; font-size: large;">Register</button>
        </div>
    </div>
    
</template>

<script>
    import axios from 'axios';
    export default{
        
        data(){
            return {
                userID:"",
                passWord:"",
                state: 0 // 0 primary; 1 user not found; 2 invalid password
            }
        },
        props: {
            jReg: Boolean,
            uID: String,
            password: String
        },
        emits: ['logining'],
        methods:{
            tryLogin(){
                axios.post('http://127.0.0.1:8000/login/', {
                    "uid": this.userID,
                    "pw":  this.passWord
                })
                .then(response => {
                    if (!response.data.findUser) {
                        this.state = 1
                    }
                    else if (!response.data.match) {
                        this.state = 2
                    }
                    else {
                        this.$emit("logining", {uname: response.data.uName, uid: this.userID})
                        this.$router.push('/create')
                        this.state = 3
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error)
                })
            },
            toRegister(){
                this.$router.push('/register')
            }
        },
        mounted () {
            if (this.jReg) {
                this.userID = this.uID
                this.passWord = this.password
            }
        }
    }
</script>