<template> 
    <div id="main">
        <h1 style="text-align: center; font-weight: 900; font-size: 60px;">{{ event.ename }}</h1>
        <div id="ql">
            <h2 style="font-weight: bold; margin-bottom: 20px;">Question List</h2>
            <div class="list-group" id="scroll" v-if="questions.length">
                <a v-for="(item, index) in questions" 
                @click="setActive(index)" 
                :class="['list-group-item', 'list-group-item-action', {'active':index===active_que }]" 
                aria-current="true">
                <div class="d-flex w-100 justify-content-between">
                    <div style="display: flex;">
                        <h5 class="mb-3" style="margin-right: 0; font-weight: 900;">Question.{{ index + 1 }}</h5>
                        <!-- <StateTag :start="item.start" :end="item.ended" style="margin-left: 10px;"/> -->
                    </div>
                    <!-- <small>{{ item.edate }} {{ item.etime.substring(0, 5) }}</small> -->
                </div>
                <p class="mb-2">{{ item.content }}</p>
                <!-- <small>Invitation Code: </small>
                    <small style="font-weight: bold;">{{ item.ivcode }} </small> -->
                </a>
            </div>
            <p v-if="questions.length===0" class="form-label">There are no questions in this event.</p>
        </div>
        
        <div id="left">
            <div class="mb-3">
                <label class="form-label"></label>
                <h2 style="font-weight: bold; margin-bottom: 20px;">Submit a new question</h2>
                <textarea :disabled="logined" v-model="user_input" class="form-control" rows="10" :placeholder="logined? 'Only audience can submit questions':'Discribe your question...'"></textarea>
                <div class="form-text">
                    Your question must be 20-300 characters long.
                </div>
                <div class="form-text">
                    New questions are at the bottom.
                </div>
                <div v-if="sub_state===3" style="color: red; font-size: small;">Invalid length of the question: {{ user_input.length }}</div>
                <button class="btn btn-primary" id="subbtn" @click="submitQue" :disabled="logined">submit</button>
            </div>
            
            <div style="font-size: large; margin-bottom: 40px; margin-top: 30px;">
                <div >Sort the questions by (not implemenetd)</div>
                <select v-model="selected">
                    <option disabled value="">Please select one</option>
                    <option>Index</option>
                    <option>Vote</option>
                </select>
            </div>

            <button class="btn btn-primary" :disabled="!logined" @click="toCreate" v-if="logined"> Back to my event list</button>
            <button class="btn btn-danger" :disabled="!logined" @click="endEvent" v-if="logined" style="margin-left: 20px;"> Terminate this event</button>
        </div>

    </div>

</template>

<script>
import axios from 'axios';

    export default{
        data() {
            return {
                eid:"",
                event:null,
                questions:[],
                user_input:"",
                state:0,
                sub_state:0,
                active_que:null
            }
        },

        props:['logined'],

        methods:{
            submitQue(){
                if (this.user_input.length > 300 || this.user_input.length < 20) {
                    this.sub_state = 3;
                    return
                }
                axios.post('http://127.0.0.1:8000/submitQue/', {
                    "eid": this.eid,
                    "content": this.user_input})
                .then(response => {
                    if (response.data.submit_que) {
                        this.questions.push(response.data.new_que)
                        window.alert("You have submitted the question!")
                    }
                    else {
                        this.sub_state = 1;
                        window.alert("Submission falied!")
                    }

                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    window.alert("Submission falied!")
                    this.sub_state = 2;
                })
            },
            setActive(data){
                if (this.active_que == data) this.active_que = null
                else this.active_que = data
            },
            endEvent(){
                axios.post('http://127.0.0.1:8000/terminateEvent/', {
                    "event_id" : this.event.id
                })
                .then(response => {
                    console.log(response.data)
                    if (response.data.end_success) {
                        this.start = true
                        this.$router.push('/create')
                    }
                    else {
                        window.alert("Failed to end the event. Please try again later.");
                    }
                })
                .catch(error => {
                    window.alert("Failed to active the event. Please try again later.");
                })
            },
            toCreate(){
                this.$router.push('/create')
            },
        },

        created(){
            this.eid = this.$route.query.event_id;
            axios.post('http://127.0.0.1:8000/getEvent2/', {
                "eid": this.eid})
            .then(response => {
                this.state = response.data.found_event ? 1 : 2;
                this.event = response.data.event;
                console.log(this.event)
                if (response.data.found_event && !this.event.ended){
                    axios.post('http://127.0.0.1:8000/getQueList/', {
                        "eid": this.eid})
                    .then(response => {
                        this.state = response.data.get_que ? 1 : 5;
                        this.questions = response.data.questions;
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error);
                        this.state = 6;
                    })
                }
                else if (response.data.found_event) {
                    window.alert("This event has been terminated.")
                    this.state = 7
                }
                else {
                    window.alert("Unexpected error when fetching questions")
                    this.state = 8
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                window.alert("Unexpected error when fetching questions")
                this.state = 3;
            })
        },
    }
</script>

<style scoped>
    #main {
        width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }
    #ql {
        width: 700px; 
        float: left;
        margin-top: 60px;
    }
    #left{
        float: right;
        margin-top: 40px;
    }
    #scroll{
        height: 800px;
        overflow-y: auto;
        border: solid 2px rgb(175, 175, 175);
        border-radius: 10px;
    }
    #subbtn{
        margin-top: 15px;
        font-size: 15px;
        
    }
</style>