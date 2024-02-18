<template>
    <div style="text-align: center;">
        <h1>Terms of Service</h1> no content
        <h1>Provacy Policy</h1> no content
        <div>
            <button @click="toHome"  class="btn btn-primary" style="width: 140px; font-size: large;">Home Page</button>
        </div>
    </div>

</template>

<script>
    export default{
        methods:{
            toHome(){
                this.$router.push("/")
            }
        }
    }
</script>