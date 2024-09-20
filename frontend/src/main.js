import { createApp } from "vue";
import App from "./App.vue";
import router from "./routes";
import axios from "axios";
import store from "./store";
// import "../output.css";//
import "/node_modules/@material-tailwind/html/scripts/collapse.js";

const app = createApp(App);

axios.defaults.baseURL = "http://127.0.0.1:8000";
app.use(router);
app.use(store);
app.use(axios);
// app.use(store);
app.mount("#app");
