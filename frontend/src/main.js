import { createApp } from "vue";
import App from "./App.vue";
import router from "./routes";
import axios from "axios";
// import "../output.css";//

const app = createApp(App);

axios.defaults.baseURL = "http://127.0.0.1:8000";
app.use(router, axios);

app.mount("#app");
