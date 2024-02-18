<template>
    <div id="main">
        <p style="margin-top: 1%;"> @ 2024 Qyay! All rights reserved. </p>
        <a class="terms" @click="toTerms">Terms of Service</a>
        <a class="terms" @click="toTerms">Privacy Pllicy</a>
    </div>
</template>

<script>
    export default{
        methods:{
            toTerms(){
                window.alert("{{content of terms}}")
            }
        }
    }
</script>

<style scoped>
.terms{
    margin-left: 5px;
    margin-right: 5px;
}
#main{
    position: fixed;
    bottom: 0;
    border-top: solid 2px; 
    width: 80%;
    margin-left: 10%;
    margin-right: 10%;
    text-align: center;
}
</style>