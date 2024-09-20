import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
import Sidebar from "./components/Sidebar.vue";
import Dashboard from "./components/Dashboard.vue";
import Notification from "./components/Notifications.vue";
import Profile from "./components/Profile.vue";
import ItineraryHome from "./components/ItineraryHome.vue";
import CreateItinerary from "./components/CreateItinerary.vue";
import Settings from "./components/Settings.vue";
import ViewItinerary from "./components/ViewItinerary.vue";
import PostViewing from "./components/PostViewing.vue";
import ViewSearchResult from "./components/ViewSearchResult.vue";
import PublicViewProfile from "./components/PublicViewProfile.vue";
import Test from "./components/Test.vue";
import Otp from "./components/Otp.vue";
import Report from "./components/Report.vue";
import TamSurvey from "./components/TamSurvey.vue";
import Trivia from "./components/Trivia.vue";
import EditPost from "./components/EditPost.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/", component: Login, name: "login" },
		{ path: "/dashboard", component: Dashboard, name: "dashboard" },
		{ path: "/otp", name: "otp", component: Otp },
		{ path: "/report", name: "report", component: Report },
		{
			path: "/edit-post/:post",
			name: "editpost",
			component: EditPost,
		},
		{
			path: "/notifications",
			component: Notification,
			name: "notifications",
		},
		{
			path: "/trivia",
			component: Trivia,
			name: "trivia",
		},
		{
			path: "/tamsurvey",
			component: TamSurvey,
			name: "tamsurvey",
		},
		{
			path: "/itinerary",
			component: ItineraryHome,
			name: "itinerary",
		},
		{
			path: "/create-itinerary",
			component: CreateItinerary,
			name: "create-itinerary",
		},
		{
			path: "/view-itinerary",
			component: ViewItinerary,
			name: "view-itinerary",
		},
		{
			path: "/view-post",
			component: PostViewing,
			name: "view-post",
		},
		{
			path: "/search-result/",
			component: ViewSearchResult,
			name: "search-result",
		},
		{ path: "/profile", component: Profile, name: "profile" },
		{ path: "/test", component: Test, name: "test" },
		{
			path: "/user-profile/:username/:user",
			component: PublicViewProfile,
			name: "user-profile",
		},
		{
			path: "/settings",
			component: Settings,
			name: "settings",
		},
	],
});
router.beforeEach((to, from, next) => {
	// Check if the user is logged in before accessing protected routes
	const token = localStorage.getItem("token");

	if (to.name !== "login" && to.name !== "otp" && !token) {
		// If the route is not the login page, home page, and the user is not logged in,
		// redirect to the login page
		next({ name: "login" });
	} else {
		// If the user is logged in or accessing the login page or home page, proceed to the next route
		next();
	}
	if (to.name === "login" || to.name === "otp") {
		window.scrollTo(0, 0);
	}
});
export default router;
