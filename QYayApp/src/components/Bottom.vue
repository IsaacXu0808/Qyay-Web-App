<template>
    <div class="fixed-bottom" style="text-align: center;">
        <div style="border-top: solid 2px; width: 80%; margin: auto;"></div>
        <p style="margin-top: 1%;"> @ 2024 Qyay! All rights reserved. </p>
        <a class="terms" @click="toTerms">Terms of Service</a>
        <a class="terms" @click="toTerms">Privacy Pllicy</a>
    </div>
</template>

<script>
    export default{
        methods:{
            toTerms(){
                this.$router.push('/terms')
            }
        }
    }
</script>

<style scoped>
.terms{
    margin-left: 5px;
    margin-right: 5px;
}
</style>