import { createRouter, createWebHistory } from "vue-router";
import Login from "./components/Login.vue";
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
import store from "./store";
import DefaultLayout from "./components/DefaultLayout.vue";
import ReportsView from "./components/admin/ReportsView.vue";
import CulturaUserAdminView from "./components/admin/CulturaUserAdminView.vue";
import NotFound from "./components/NotFound.vue";
import LandingPage from "./components/LandingPage.vue";

const routes = [
	{
		path: "/",
		redirect: "/dashboard",
		component: DefaultLayout,
		meta: { requiresAuth: true },
		children: [
			{ path: "/dashboard", component: Dashboard, name: "dashboard" },
			{ path: "/report", name: "report", component: Report },
			{ path: "/edit-post/:post", name: "editpost", component: EditPost },
			{
				path: "/notifications",
				component: Notification,
				name: "notifications",
			},
			{ path: "/trivia", component: Trivia, name: "trivia" },
			{ path: "/tamsurvey", component: TamSurvey, name: "tamsurvey" },
			{ path: "/itinerary", component: ItineraryHome, name: "itinerary" },
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
				path: "/view-post/:post",
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
				path: "/user-profile/:username",
				component: PublicViewProfile,
				name: "user-profile",
			},
			{ path: "/settings", component: Settings, name: "settings" },
			{
				path: "/rp",
				component: ReportsView,
				name: "rp",
				meta: { requiresAdmin: true },
			},
			{
				path: "/cu",
				component: CulturaUserAdminView,
				name: "cu",
				meta: { requiresAdmin: true },
			},
		],
	},
	{
		path: "/",
		name: "landing-page",
		component: LandingPage,
		meta: { isGuest: true },
	},
	{
		path: "/login",
		name: "login",
		component: Login,
		meta: { isGuest: true },
	},
	{
		path: "/otp",
		name: "otp",
		component: Otp,
		beforeEnter: (to, from, next) => {
			if (store.getters.hasOtp) {
				next();
			} else {
				next({ name: "login" });
			}
		},
	},
	{ path: "/:pathMatch(.*)*", name: "NotFound", component: NotFound },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

router.beforeEach(async (to, from, next) => {
	if (!store.state.user.token) {
		try {
			await store.dispatch("fetchUserData");
		} catch (error) {
			console.error("Error fetching user data:", error);
		}
	}

	if (to.meta.requiresAuth && !store.state.user.token) {
		next({ name: "login" });
	} else if (store.state.user.token && to.meta.isGuest) {
		await store.dispatch("fetchUserData");
		next({ name: "dashboard" });
	} else {
		next();
	}

	if (to.name === "login" || to.name === "otp") {
		window.scrollTo(0, 0);
	}
});

export default router;
