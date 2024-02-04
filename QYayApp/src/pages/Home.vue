<template>
    <div class="mid">
        <div>
            <h1 class="title head">Welcome to Qyay!</h1>
        </div>

        <div>
            <div class="choice" style="width: 330px; float: left; text-align: center; margin-left: 270px;">
                <h2 class="title">Join an event?</h2>
                <button @click="toJoin"  class="btn btn-primary">Join</button>
            </div>

            <div class="choice" style="width: 330px; float: right; text-align: center; margin-right: 270px;">
                <h2 class="title">Create an event?</h2>
                <button @click="toLogin" class="btn btn-primary">Login</button>
            </div>
        </div>

        <div class="choice">
            <h2 class="title"> Do not have an account?</h2>
            <button @click="toRegister"  class="btn btn-primary">Register</button>
        </div>
        
        
    </div>
    
</template>

<script>
    export default{
        data(){
            return {

            }
        },
        methods:{
            toLogin(){
                this.$router.push('/login')
            },
            toRegister(){
                this.$router.push('/register')
            },
            toJoin(){
                this.$router.push('/join')
            },
        },
    }
</script>

<style scoped>
.mid{
    text-align: center;
    width: 1200px;
    margin-right: auto;
    margin-left: auto;
}

.title{
    font-weight: bolder;
}

.head{
    font-size: 60px;
    margin-top: 250px;
    margin-bottom: 150px;
}
button{
    width: 160px;
    font-size: 18px;
}

.choice{
    margin-bottom: 100px;
}

h2{
    margin-bottom: 20px;
}

</style>