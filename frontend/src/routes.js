import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import Sidebar from "./components/Sidebar.vue";
import Dashboard from "./components/Dashboard.vue"
const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", component: Login, name: "login" },
		{ path: "/dashboard", component: Dashboard, name: "dashboard" },
	],
});

export default router;
