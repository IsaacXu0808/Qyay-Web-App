
<template>
    <div :class="msg" :id = "dynamicID">Test</div>
    <button :disabled="isButDis">Login</button>
    <div v-bind="Attr">123</div>
</template>

<script>

export default {
    data() {
        return{
            msg:"active",
            dynamicID: "id1",
            isButDis: false,
            Attr:{class:"active", id:"id1"}
        }
    }
}

</script>