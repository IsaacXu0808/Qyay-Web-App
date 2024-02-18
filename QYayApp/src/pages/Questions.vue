<template> 
    <div id="main">
        <h1 style="text-align: center; font-weight: 900; font-size: 60px;">{{ event_name }}</h1>
        <div id="ql">
            <h2 style="font-weight: bold; margin-bottom: 20px;">Question List</h2>
            <div class="list-group" id="scroll" v-if="questions.length">
                <a v-for="(item, index) in (order === 'Question ID'? questions : sorted_ques)" 
                :class="['list-group-item', 'list-group-item-action', {'active':index===active_que }]" 
                aria-current="true" v-show="!(ignore && item.answered)">
                    <div class="d-flex w-100 justify-content-between">
                        <div style="display: flex;">
                            <h5 class="mb-3" style="margin-right: 0; font-weight: 900;">Question ID. {{ item.id }}</h5>
                            <QueTag :answered="item.answered" :logined="logined" style="margin-left: 20px;" @click="ansQue(item.id)"/>
                        </div>
                        <div style="font-size: 20px;">
                            <i :class="voted.includes(item.id) || logined ? 'bi bi-hand-thumbs-up-fill':'bi bi-hand-thumbs-up'" style="color: rgb(255, 157, 0);" @click="upvote(item.id, index)"></i>
                            <small  ref="voteCount" style="user-select: none;">{{ " " + item.vote }}</small>
                        </div>
                    </div>
                    <p class="mb-2">{{ item.content }}</p>
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
            

            <div class="sort-options" style="font-size: large; margin-bottom: 40px; margin-top: 30px;">
                <div>Sort the questions by</div>
                <select v-model="order" class="form-select" aria-label="Default select example">
                    <option disabled>Please select a mode</option>
                    <option>Question ID</option>
                    <option>Number of votes</option>
                </select>
            </div>

            <div class="form-check" style="font-size: large; margin-bottom: 30px;">
                <input class="form-check-input" type="checkbox" id="flexCheckDefault" v-model="ignore">
                <label class="form-check-label" for="flexCheckDefault">
                    Ignore answered questions
                </label>
            </div>


            <button class="btn btn-primary" @click="toCreate" v-if="logined"> Back to my event list</button>
            <button class="btn btn-danger"  @click="endEvent" v-if="logined" style="margin-left: 20px;"> Terminate this event</button>
        </div>
    </div>


</template>

<script>
import axios from 'axios';
import 'bootstrap-icons/font/bootstrap-icons.css';
import QueTag from '@/components/QueTag.vue';

    export default{
        data() {
            return {
                eid:"",
                event:null,
                event_name:null,
                questions:[],
                user_input:"",
                state:0,
                sub_state:0,
                active_que:null,
                voted:[],
                order:"Question ID",
                ignore:false,
                refreshItv: null
            }
        },

        props:['logined'],
        components:{
            QueTag,
        },  

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
            getQues() {
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
            },

            upvote(id, idx) {
                if (this.voted.includes(id)) return;
                if (this.logined) return;
                axios.post('http://127.0.0.1:8000/voteQue/', {
                    "qid": id})
                .then(response => {
                    if (response.data.vote_success) {
                        this.voted.push(id);
                        this.getQues();
                    }
                    else {
                        window.alert("Failed to submit your vote. Please reenter the event and try agian.")
                    }
                })
                .catch(error => {
                    window.alert("Failed to submit your vote. Please re-enter the event and try agian.")
                })
                
            },
            ansQue(id) {
                if (!this.logined) return;
                if (this.voted.includes(id)) return;
                axios.post('http://127.0.0.1:8000/ansQue/', {
                    "qid": id})
                .then(response => {
                    if (response.data.ans_success) {
                        this.getQues();
                    }
                    else {
                        window.alert("Failed to mark an answered question. Please reenter the event and try agian.")
                    }
                })
                .catch(error => {
                    window.alert("Failed to mark an answered question. Please reenter the event and try agian.")
                })
                
            },

            endEvent(){
                axios.post('http://127.0.0.1:8000/terminateEvent/', {
                    "event_id" : this.event.id
                })
                .then(response => {
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

            getEvent() {
                axios.post('http://127.0.0.1:8000/getEvent2/', {
                "eid": this.eid})
                .then(response => {
                    this.state = response.data.found_event ? 1 : 2;
                    this.event = response.data.event;
                    this.event_name = response.data.event.ename;
                    if (response.data.found_event && !this.event.ended){
                        this.getQues()
                    }
                    else if (response.data.found_event && this.event.ended) {
                        window.alert("This event has been terminated.")
                        this.state = 7
                        this.$router.push('/')
                    }
                    else {
                        window.alert("Unexpected error when fetching questions")
                        this.state = 8
                    }
                })
            },

            toCreate(){
                this.$router.push('/create')
            },
        },

        created(){
            this.eid = this.$route.query.event_id;
            this.getEvent()
        },

        mounted() {
            this.refreshItv = setInterval(() => {
                this.getEvent();
            }, 1500);
        },

        beforeUnmount() {
            clearInterval(this.refreshItv);
        },

        computed:{
            sorted_ques() {
                if (this.questions.length == 0) return [];
                return this.questions.slice().sort((a, b) => (b.vote - a.vote));
            },
            ques() {
                if (this.questions.length == 0) return [];
                return this.questions.slice().sort((a, b) => (a.id - b.id));
            } 
        }
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
    .sort-options select:focus {
        outline: none;
        box-shadow: 0 0 5px rgba(85, 85, 85, 0.5);
    }


</style>