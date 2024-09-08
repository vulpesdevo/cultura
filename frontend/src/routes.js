import { createRouter, createWebHistory } from "vue-router";

const Login = () => import("./components/Login.vue");
const Sidebar = () => import("./components/Sidebar.vue");
const Dashboard = () => import("./components/Dashboard.vue");
const Notification = () => import("./components/Notifications.vue");
const Profile = () => import("./components/Profile.vue");
const ItineraryHome = () => import("./components/ItineraryHome.vue");
const CreateItinerary = () => import("./components/CreateItinerary.vue");
const Settings = () => import("./components/Settings.vue");
const ViewItinerary = () => import("./components/ViewItinerary.vue");
const PostViewing = () => import("./components/PostViewing.vue");
const ViewSearchResult = () => import("./components/ViewSearchResult.vue");
const PublicViewProfile = () => import("./components/PublicViewProfile.vue");
const Test = () => import("./components/Test.vue");

const routes = [
	{ path: "/login", name: "login", component: Login },
	{ path: "/sidebar", name: "sidebar", component: Sidebar },
	{ path: "/dashboard", name: "dashboard", component: Dashboard },
	{ path: "/notifications", name: "notifications", component: Notification },
	{ path: "/profile", name: "profile", component: Profile },
	{
		path: "/itinerary",
		name: "itinerary",
		component: ItineraryHome,
	},
	{
		path: "/create-itinerary",
		name: "create-itinerary",
		component: CreateItinerary,
	},
	{ path: "/settings", name: "settings", component: Settings },
	{
		path: "/view-itinerary",
		name: "view-itinerary",
		component: ViewItinerary,
	},
	{ path: "/post-viewing", name: "post-viewing", component: PostViewing },
	{
		path: "/search-result",
		name: "search-result",
		component: ViewSearchResult,
	},
	{
		path: "/user-profile",
		name: "user-profile",
		component: PublicViewProfile,
	},
	{ path: "/test", name: "test", component: Test },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
	scrollBehavior(to, from, savedPosition) {
		if (savedPosition) {
			return savedPosition;
		} else if (to.hash) {
			return { selector: to.hash };
		} else {
			return { top: 0 };
		}
	},
});

router.beforeEach((to, from, next) => {
	// Check if the user is logged in before accessing protected routes
	const token = localStorage.getItem("token");

	if (to.name !== "login" && !token) {
		// If the route is not the login page and the user is not logged in,
		// redirect to the login page
		next({ name: "login" });
	} else {
		// If the user is logged in or accessing the login page, proceed to the next route
		next();
	}
});

export default router;
