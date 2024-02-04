<template>
    <h1>Join</h1>
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
            }
        },
    }
</script>