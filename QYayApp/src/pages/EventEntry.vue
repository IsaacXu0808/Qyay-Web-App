<template>
    <div style="width: 800px; text-align: center; margin-top: 120px; margin-left: auto; margin-right: auto;" >
        <h1 style="font-weight: bold; font-size: 60px; margin-bottom: 20px;">{{ name }}</h1>
        <StateTag :start="start" :end="ended" style="font-size: 40px; margin-bottom: 20px; border-radius: 30px;"/>
        <h2 style="margin-bottom: 30px; font-style: oblique;">Organized by {{ uname }} </h2>
        <h3 style="margin-bottom: 30px;">{{ date }} {{ time }}</h3>
        <div style="width: 600px; margin-top: 50px; margin-bottom: 50px; font-size: 20px; margin-left: auto; margin-right: auto;">{{ discription }}</div>
        <h3>Invitation Code:</h3>
        <p style="font-weight: bold; font-size: 40px;"> {{ code }}</p>
        <div style="margin-bottom: 30px;">
            <button v-if="!start" @click="activeEvent" class="btn btn-primary" style="width: 280px; font-size: large;">Active the event</button>
            <button v-else-if="start && !ended" @click="toQuestions" class="btn btn-primary" style="width: 280px; font-size: large;">Enter the event</button>
            <button v-else-if="start && ended" disabled class="btn btn-primary" style="width: 280px; font-size: large;">Event has ended</button>
        </div>
        <div>
            <button @click="toCreate" class="btn btn-primary" style="width: 280px; font-size: large;">Go to my event list</button>
        </div>
    </div>
</template>

<script>
import StateTag from '@/components/StateTag.vue';
import axios from 'axios';
export default {
    components: {
        StateTag
    },
    data(){
        return {
            uid:"",
            uname:"",
            name:"",
            eid:"",
            discription:"",
            date:"",
            time:"",
            code:"",
            start:null,
            ended:null,
        }
    },

    methods:{
        toCreate(){
            this.$router.push('/create')
        },
        activeEvent(){
            axios.post('http://127.0.0.1:8000/activeEvent/', {
                    "event_id" : this.eid
                })
                .then(response => {
                    if (response.data.active_success) {
                        this.start = true
                        window.alert("The event is activated. Audience can enter and post questions.");
                    }
                    else {
                        window.alert("Failed to active the event. Please try again later.");
                    }
                })
                .catch(error => {
                    window.alert("Failed to active the event. Please try again later.");
                })
        },
        toQuestions(){
            this.$router.push({name: 'Questions', query: {"event_id": this.eid}})
        }
    },

    mounted() {
        this.uid = this.$route.query.uid;
        this.uname = this.$route.query.uname;
        this.eid = this.$route.query.event_id;
        this.name = this.$route.query.name;
        this.discription = this.$route.query.discription;
        this.date = this.$route.query.date;
        this.time = this.$route.query.time;
        this.code = this.$route.query.code;
        this.start = this.$route.query.start == "true";
        this.ended = this.$route.query.ended == "true";
    }
}
</script>