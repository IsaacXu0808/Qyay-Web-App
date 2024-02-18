<template>
    <div style="width: 1200px; margin-left: auto; margin-right: auto;">
        <div style="text-align: center;">
            <h1 style="margin-top: 100px; margin-bottom: 60px; font-size: 60px; font-weight: bold;">Welcome, {{userName}}!</h1>
            <button @click="toEventInfo" class="btn btn-primary" style="width: 200px; font-size: large;">Create an event</button>
        </div>
        
        <div style="width: 800px; margin-left: auto; margin-right: auto; margin-top: 80px;">
            <h2 style="font-weight: bold; margin-bottom: 20px;">Your Event List</h2>

            <div class="list-group" id="scroll" v-if="eventList.length">
                <a v-for="(item, index) in eventList" 
                @click="setActive(index)" 
                :class="['list-group-item', 'list-group-item-action', {'active':index===active_event }]" 
                aria-current="true">
                    <div class="d-flex w-100 justify-content-between">
                        <div style="display: flex;">
                            <h5 class="mb-3" style="margin-right: 0; font-weight: 900;">{{ item.ename }}</h5>
                            <StateTag :start="item.start" :end="item.ended" style="margin-left: 10px;"/>
                        </div>
                    <small>{{ item.edate }} {{ item.etime.substring(0, 5) }}</small>
                    </div>
                    <p class="mb-2">{{ item.ediscription }}</p>
                    <small>Invitation Code: </small>
                    <small style="font-weight: bold;">{{ item.ivcode }} </small>
                </a>
            </div>
            <p v-if="eventList.length===0" class="form-label">You have not created any events.</p>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <button :disabled="active_event===null" @click="toEntry" class="btn btn-primary" style="width: 200px; font-size: large;">Enter this event</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import StateTag from '@/components/StateTag.vue';

    function sort_helper(n) {
        if (n == 1) return 0;
        if (n == 2) return 2;
        if (n == 0) return 1;
    }

    export default{
        data(){
            return {
                eventList: [],
                active_event: null,
                errState: 0
            }
        },
        methods:{
            toEventInfo(){
                this.$router.push('/eventInfo')
            },
            setActive(data){
                if (this.active_event == data) this.active_event = null
                else this.active_event = data
            },
            toEntry(){
                this.$router.push({name: 'EventEntry', 
                                   query: {"uid": this.uID,
                                            "uname": this.userName,
                                            "event_id": this.eventList[this.active_event].id,
                                            "name": this.eventList[this.active_event].ename,
                                            "discription": this.eventList[this.active_event].ediscription,
                                            "date": this.eventList[this.active_event].edate,
                                            "time": this.eventList[this.active_event].etime,
                                            "code": this.eventList[this.active_event].ivcode,
                                            "start": this.eventList[this.active_event].start,
                                            "ended": this.eventList[this.active_event].ended}
                })
            }
        },
        props:{
            userName:String,
            uID:String
        },
        created () {
            axios.post('http://127.0.0.1:8000/getEventList/', {
                        "uid": this.uID,
                    })
            .then(response => {
                if (response.data.get_event_success) {
                    this.eventList = response.data.event_list;
                    this.eventList.sort((a, b) => (sort_helper(a.ended + a.start) - sort_helper(b.ended + b.start)))
                }
                else window.alert("Failed to load fetch your events. Please retry later.");
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                window.alert("Failed to load fetch your events. Please retry later.");
            })
        },
        components:{
            StateTag,
        }
    }
</script>

<style scoped>
#scroll{
        height: 600px;
        overflow-y: auto;
        overflow-x: hidden;
        border: solid 2px rgb(175, 175, 175);
        border-radius: 10px;
    }
</style>