<template>
    <div>{{ this.hello }}</div>
</template>

<script>
import axios from 'axios'
export default {
    methods: {
        fetchHello() {
            axios.get('http://127.0.0.1:8000/hello_world/')
                .then(response => {
                    this.hello =  response.data.msg;
                })
                .catch(error => {
                    console.error('Error fetching data:', error)
                })
        }
    },
    data () {
        return {
            hello: "initial",
            msg: 'kkk',
        }
    },
    mounted() {
        this.fetchHello()
    }
}

</script>