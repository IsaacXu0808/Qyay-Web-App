// import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Bottom from './components/Bottom.vue'
const app = createApp(App)
app.component("Bottom", Bottom)
app.use(router)
app.mount('#app')
