import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import Sidebar from "./components/Sidebar.vue";
const router = createRouter({
	history: createWebHistory(),
	routes: [{ path: "/", component: Login, name: "sidebar" }],
});

export default router;
