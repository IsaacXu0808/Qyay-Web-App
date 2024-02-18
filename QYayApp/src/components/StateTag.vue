<template>
    <div id="tag">
        <span class="badge text-bg-warning" v-if="!start">inactive</span>
        <span class="badge text-bg-success" v-else-if="start && !end">ongoing</span>
        <span class="badge text-bg-danger" v-else-if="end">terminated</span>
    </div>
</template>

<script>
export default{
    props:{
        start: Boolean,
        end: Boolean
    }
}
</script>

<style scoped>
    #tag {
        border: 1px black;
    }
</style>