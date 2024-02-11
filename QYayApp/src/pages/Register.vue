<template>
    <div style="margin-left: auto; margin-right: auto; margin-top: 50px; width: 600px;">
        <legend style="text-align: center; font-size: 40px; font-weight: bold;">
            Register for an account
        </legend>
    
        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 30px;">User ID</label>
            <input class="form-control" placeholder="Enter your user ID" v-model="userID"/>
            <div class="form-text">
                Your User ID must be 8-20 characters long
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 20px;">User Name</label>
            <input class="form-control" placeholder="Enter your user name" v-model="userName"/>
            <div class="form-text">
                Your User Name must be 3-14 characters long
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 20px;">Password</label>
            <input type="password" class="form-control" placeholder="Enter your password" v-model="password"/>
            <div class="form-text">
                Your password must be 8-20 characters long
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label" style="text-align: left; margin-top: 20px;">Confirm Password</label>
            <input type="password" class="form-control" placeholder="Repeat your password" v-model="password2"/>
        </div>

        <div style="color: red; font-size: smaller; font-weight: bold;">
            <div v-if="state===1">Invalid length of User ID</div>
            <div v-else-if="state===2">Invalid length of User Name</div>
            <div v-else-if="state===3">Invalid length of User Name</div>
            <div v-else-if="state===4">Passwords do not match</div>
            <div v-else-if="state===5">The User ID is registered, please use another one</div>
            <div v-else-if="state===6">Unexpected error, please try later</div>
        </div>

        <div class="form-check" style="margin-top: 30px;">
            <input class="form-check-input" type="checkbox" v-model="isChecked">
            <label class="form-check-label" for="flexCheckDefault">
                I agree to 
                <a class="terms" @click="toTerms">Terms of Service</a> and
                <a class="terms" @click="toTerms">Privacy Pllicy</a>.
            </label>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <button :disabled="!isChecked" class="btn btn-primary" style="width: 120px; font-size: large;" @click="tryReg">Register</button>
        </div>

        <div class=mb-3 style="text-align: center; margin-top: 100px;">
            <h2 class="title" style="margin-bottom: 30px;"> Already have an account?</h2>
            <button @click="toLogin"  class="btn btn-primary" style="width: 120px; font-size: large;">Login</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    
    export default{
        data(){
            return {
                userID:"",
                userName:"",
                password:"",
                password2:"",
                state: 0, // 1 uid; 2 uname; 3 pw; 4 unmatched; 5 dup ID,
                isChecked: false
            }
        },
        methods:{
            tryReg(){
                // local check
                if (this.userID.length < 8 || this.userID.length > 20) {
                    this.state = 1
                    this.userID = ""
                }
                else if (this.userName.length < 3 || this.userID.Name > 14) {
                    this.state = 2
                    this.userName = ""
                }
                else if (this.password.length < 8 || this.password.Name > 20) {
                    this.state = 3
                    this.password = ""
                }
                else if (this.password != this.password2) {
                    this.state = 4
                    this.password = ""
                    this.password2 = ""
                }
                else {
                    this.state = 0
                    axios.post('http://127.0.0.1:8000/register/', {
                        "uid": this.userID,
                        "uname": this.userName,
                        "pw":  this.password
                    })
                    .then(response => {
                        console.log(response.data)
                        if (!response.data.Reg_success) {
                            this.state = 5
                            this.userID = ""
                        }
                        else {
                            this.state = 0
                            this.$emit("registered", {uid: this.userID, pw: this.password})
                            this.$router.push('/login')
                        }
                    })
                    .catch(error => {
                        this.satte = 6
                        console.error('Error fetching data:', error)
                    })
                }
            },
            toLogin(){
                this.$router.push('/login')
            },
            toTerms(){
                window.alert("{{Content of terms}}");
            }
        },
    }
</script>