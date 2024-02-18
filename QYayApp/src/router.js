import { createRouter, createMemoryHistory } from "vue-router"
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import Create from './pages/Create.vue'
import EventInfo from './pages/EventInfo.vue'
import Join from './pages/Join.vue'
import Terms from './pages/Terms.vue'
import EventEntry from './pages/EventEntry.vue'
import Quesitons from './pages/Questions.vue'
const router = createRouter({
    history:createMemoryHistory(),
    routes:[
        {
            path:"/",
            component: Home
        },
        {
            path:"/login",
            component: Login
        },
        {
            path:"/register",
            component: Register
        },
        {
            path:"/create",
            component: Create
        },
        {
            path:"/eventInfo",
            component: EventInfo
        },
        {
            path:"/join",
            component: Join
        },
        {
            path:"/terms",
            component: Terms
        },
        {
            path:"/evententry",
            component: EventEntry,
            name: 'EventEntry'
        },
        {
            path:"/questions",
            component: Quesitons,
            name: 'Questions'
        },
    ]
});

export default router;