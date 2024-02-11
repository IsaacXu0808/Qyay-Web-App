<template>
    <div style="width: 800px; margin-left: auto; margin-right: auto;">
        <h2 id="title">Join an Event</h2>
        <h3 id="subtt">Enter the six-digit invitation code to join the event.</h3>
        <div id="codeInput">
            <CodeContainer @ivcode="searchEvent" @backspace="initialize"></CodeContainer>
        </div>

        <div v-if="state==3" class="err_msg">
            An unexpected error occurs. Please try again later.
        </div>

        <div v-else-if="state==2" class="err_msg">No event found. Please note that the invitation code is case-sensitive.</div>

        <div v-else-if="state==1" style="width: 700px; margin-left: auto; margin-right: auto;">
            <div style="text-align: center; margin-bottom: 30px; font-size: 30px; font-weight: 300;">
                Event found:
            </div>
            <div class="list-group">
                <a v-for="(item) in [event]" 
                    :class="['list-group-item', 'list-group-item-action']" 
                    aria-current="true">
                    <div class="d-flex w-100 justify-content-between">
                        <div style="display: flex;">
                            <h5 class="mb-3" style="margin-right: 0; font-weight: 900;">{{ item.ename }}</h5>
                            <StateTag :start="item.start" :end="item.ended" style="margin-left: 10px;"/>
                        </div>
                        <small>{{ item.edate }} {{ item.etime.substring(0, 5) }}</small>
                    </div>
                    <p class="mb-2">{{ item.ediscription }}</p>
                    <small>Organized by: </small>
                    <small style="font-weight: bold;">{{ item.uname }} </small>
                </a>
            </div>

            <div style="margin-top: 30px; margin-bottom: 30px; text-align: center;">
                <button :disabled="!event.start || event.ended" 
                        class="btn btn-primary"
                        @click="toQuestions"
                        style="width: 120px; font-size: 20px;"
                        >Join</button>
            </div>
            <div class="err_msg">
                <div v-if="!event.start">Please wait for the organizer to start the event.</div>
                <div v-else-if="event.ended">This event has ended.</div>
            </div>
        </div>
        
    </div>
</template>

<script>
    import axios from "axios"
    import CodeContainer from "../components/CodeContainer.vue"
    import StateTag from "@/components/StateTag.vue"
    export default{
        components: {
            CodeContainer,
            StateTag
        },
        data(){
            return {
                state: 0, // 0 primitive / 1 found / 2 not found / 3 error 
                event: null,
            }
        },
        methods:{
            searchEvent(code){
                axios.post('http://127.0.0.1:8000/getEvent/', {
                    "ivcode": code
                })
                .then(response => {
                    this.state = response.data.found_event ? 1 : 2;
                    this.event = response.data.event;
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    this.state = 3;
                })
            },
            initialize(){
                this.state = 0;
            },
            toQuestions(){
                this.$router.push({name: 'Questions', query: {"event_id": this.event.id}})
            }
        },
    }
</script>

<style scoped>
    #title{
        text-align: center;
        margin-top: 200px;
        font-weight: bold;
        font-size: 60px;
    }
    #subtt{
        text-align: center;
        margin-top: 100px;
        font-weight: 300;
        font-size: 30px;
    }
    #codeInput{
        text-align: center;
        margin-top: 60px;
        margin-bottom: 60px;
    }
    .err_msg{
        text-align: center;
        color: red;
    }

</style>