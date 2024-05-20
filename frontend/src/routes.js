import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [{ path: "/", component: Login, name: "login" }],
});

export default router;
