<template>
    <div style="width: 600px; margin-left: auto; margin-right: auto;">
        <h1>Create an Event</h1>

        <div class="mb-3">
            <label  class="form-label">Event Name</label>
            <input v-model="eName" type="text" class="form-control" placeholder="Name your event...">
            <div class="form-text">
                Your Event Name must be 5-30 characters long
            </div>
        </div>

        <div class="mb-3">
            <label class="form-label">Event Discription</label>
            <textarea v-model="eDscr" class="form-control" rows="3" placeholder="Discribe your event..."></textarea>
            <div class="form-text">
                Your Event Discription must be 1-200 characters long
            </div>
        </div>
        
        <div class="input-group mb-3">
            <div style="width: 300px; text-align: left;">
                <label class="form-label">Event Date</label>
                <input v-model="eDate" class="form-control" ref="datePicker" style="width: 80%;"/>
            </div>
    
            <div style="width: 240px; text-align: left; margin-left: 60px;">
                <label class="form-label">Event Time</label>
                <input v-model="eTime" class="form-control" ref="timePicker" style="width: 100%;"/>
            </div>
        </div>

        <div style="color: red; font-size: smaller;">
            <div v-if="errState===1">Invalid length of event name</div>
            <div v-else-if="errState===2">Invalid length of event discription</div>
            <div v-else-if="errState===3">Unexpected error, please try later</div>
            <div v-else-if="errState===4">Please login to create and event</div>
        </div>
        <div id="btn">
            <button type="button" class="btn btn-primary" @click="createEvent" style="margin-right: 20px;">Create</button>
            <button type="button" class="btn btn-secondary" @click="toCreate" style="margin-left: 20px;">Cancel</button>
        </div>

    </div>

</template>

<script>
    import flatpicker from 'flatpickr';
    import 'flatpickr/dist/flatpickr.min.css';
    import axios from 'axios';
    export default{
        data(){
            return {
                eName:"",
                eDscr:"",
                eTime:"",
                eDate:"",
                errState: 0 // 1 name; 2 discription; other
            }
        },
        props:{
            userName: String,
            uID: String,
            logined: Boolean
        },
        methods:{
            createEvent(){
                if (!this.logined) {this.errState = 4}
                else if (this.eName.length > 50 || this.eName.length < 5) this.errState = 1;
                else if (this.eDscr.length > 200 || this.eDscr.length < 1) this.errState = 2;
                else {
                    axios.post('http://127.0.0.1:8000/createEvent/', {
                        "uid": this.uID,
                        "uname": this.userName,
                        "name": this.eName,
                        "discription": this.eDscr,
                        "date": this.eDate,
                        "time": this.eTime
                    })
                    .then(response => {
                        console.log(response.data)
                        if (!response.data.create_success) {
                            this.errState = 3
                        }
                        else {
                            this.$router.push({name: 'EventEntry', query: {"event_id": response.data.eid,
                                                                           "uid": this.uID,
                                                                           "uname": this.userName,
                                                                           "name": this.eName,
                                                                           "discription": this.eDscr,
                                                                           "date": this.eDate,
                                                                           "time": this.eTime,
                                                                           "code": response.data.ivcode}
                            })
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching data:', error)
                        this.errState = 3
                    })
                }
            },
            toCreate(){
                this.$router.push('/create')
            },
        },
        mounted() {
            flatpickr(this.$refs.datePicker, {
                enableTime: false,
                dateFormat: 'Y-m-d',
            });

            flatpickr(this.$refs.timePicker, {
                noCalendar: true,
                enableTime: true,
                dateFormat: 'H:i',
                time_24hr: true
            });
        }
    }
</script>

<style scoped>
    h1{
        font-weight: bold;
        margin-top: 100px;
        margin-bottom: 60px
    }
    .mb-3{
        font-size: large;
        font-weight: bold;
    }
    .form-text{
        font-size: small;
        font-weight: 500;
        margin-bottom: 50px;
    }
    .form-label{
        font-size: 20px;
    }

    #btn{
        margin-top: 60px;
        text-align: center;
    }
    .btn{
        width: 120px;
        font-size: large;
        font-weight: bold;
    }
</style>