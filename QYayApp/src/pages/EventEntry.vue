<template>
    <div style="width: 800px; text-align: center; margin-top: 80px; margin-left: auto; margin-right: auto;" >
        <h1 style="font-weight: bold; font-size: 100px; margin-bottom: 30px;">{{ name }}</h1>
        <h2 style="margin-bottom: 30px; font-style: oblique;">Organized by {{ uname }} </h2>
        <h3 style="margin-bottom: 30px;">{{ date }} {{ time }}</h3>
        <p style="width: 600px; margin-left: auto; margin-right: auto;">{{ discription }}</p>
        <h3>Invitation Code:</h3>
        <p style="font-weight: bold; font-size: 40px;"> {{ code }}</p>
        <div style="margin-bottom: 30px;">
            <button @click="toEventInfo" class="btn btn-primary" style="width: 250px; font-size: large;">Start the event</button>
        </div>
        <div>
            <button @click="toCreate" class="btn btn-primary" style="width: 250px; font-size: large;">Go to my event list</button>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            uid:"",
            uname:"",
            name:"",
            discription:"",
            date:"",
            time:"",
            code:"",
        }
    },

    methods:{
        toCreate(){
            this.$router.push('/create')
        }
    },

    mounted() {
        this.uid = this.$route.query.uid;
        this.uname = this.$route.query.uname;
        this.name = this.$route.query.name;
        this.discription = this.$route.query.discription;
        this.date = this.$route.query.date;
        this.time = this.$route.query.time;
        this.code = this.$route.query.code;
    }
}
</script>