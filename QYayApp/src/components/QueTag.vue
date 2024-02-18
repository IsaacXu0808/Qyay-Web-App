<template>
    <div id="tag">
        <span class="badge text-bg-danger" v-if="!answered && logined">Mark as answered</span>
        <span class="badge text-bg-danger" v-else-if="!answered">To be answered</span>
        <span class="badge text-bg-success" v-else>Answered</span>
    </div>
</template>

<script>
export default{
    props:{
        answered:Boolean,
        logined:Boolean
    }
}
</script>

<style scoped>
    #tag {
        border: 1px black;
        user-select: none;
    }
</style>