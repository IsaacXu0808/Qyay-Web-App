<template>
  <h3>if惰性条件渲染，切换开销更高</h3>
  <div v-if='flag'>{{ msg }}</div>
  <div v-else>Not {{ msg }}</div> 
  <div v-if="type==='A'">{{ msg1 }}</div>
  <div v-else-if="type==='B'">{{ msg2 }}</div>
  <div v-else-if="type==='C'">{{ msg3 }}</div>
  <div v-else-if="type==='D'">{{ msg4 }}</div>

  <h3>show条件渲染，初次开销更高</h3>
  <div v-show='flag === false'>{{ msg }}</div>
</template>

<script>

export default {
    data(){
        return {
            flag: true,
            type: 'B',
            msg: "SEE?",
            msg1: "A",
            msg2: "B",
            msg3: "C",
            msg4: "D"
        }
    }
}

</script>