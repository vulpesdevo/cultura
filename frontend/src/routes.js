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
router.beforeEach((to, from, next) => {
	// Check if the user is logged in before accessing protected routes
	const token = localStorage.getItem("token");
	
	if (to.name !== "login" && !token) {
		// If the route is not the login page, home page, and the user is not logged in,
		// redirect to the login page
		next({ name: "login" });
	} else {
		// If the user is logged in or accessing the login page or home page, proceed to the next route
		next();
	}
	if (to.name === "login") {
		window.scrollTo(0, 0);
	}
});
export default router;
