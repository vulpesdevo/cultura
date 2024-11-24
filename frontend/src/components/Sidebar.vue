<template>
	<div
		v-if="user.isAuthenticated"
		class="w-full sm:w-64 h-14 sm:min-h-screen bg-white dark:bg-dark-interface p-0 sm:p-2 fixed bottom-0 sm:bottom-auto z-40 shadow-lg"
	>
		<div class="hidden sm:flex flex-col items-center p-5">
			<img
				:src="
					isDark
						? '/ULTURALINK-DMLong.png'
						: '/culturalink_brand_logo.png'
				"
				alt="Logo"
				class="mr-3 sm:w-full sm:h-32"
			/>

			<div class="relative">
				<input
					type="search"
					:class="{ 'has-input': searchQuery }"
					placeholder="Search..."
					class="ml-auto pl-10 h-9 outline-none text-black dark:text-dark-prime dark:bg-dark-second-dark rounded-full shadow-md"
					v-model="searchQuery"
					@input="saveSearchQuery"
				/>
				<span
					class="material-icons-outlined absolute left-0 pl-3 pt-2 text-gray-700 dark:text-dark-prime"
					>search</span
				>
			</div>
		</div>
		<ul class="flex justify-evenly h-full sm:h-72 sm:block">
			<li
				:class="[
					'flex mb-0 sm:mb-4 justify-between',
					link.name === 'Itinerary'
						? 'order-0 sm:order-none'
						: 'order-2 sm:order-none',
				]"
				v-for="(link, index) in links"
				:key="index"
			>
				<router-link
					active-class="active"
					:to="link.path"
					class="flex flex-col sm:flex-row align-middle items-center text-prime dark:text-dark-second sm:dark:text-dark-prime sm:h-12 w-20 sm:w-full"
				>
					<span
						:class="{ active: $route.path === link.path }"
						class="left-border w-full h-[4px] sm:w-[4px] sm:h-full top-0 left-0 mr-0 mb-3 sm:mb-0 sm:mr-3 z-50"
					></span
					><span
						:class="{ active: $route.path === link.path }"
						class="side-icons material-icons-outlined sm:pr-3"
						>{{ link.label }}</span
					>
					<span class="hidden sm:flex font-montserrat">{{
						link.name
					}}</span
					><span
						v-if="link.name === 'Notification'"
						v-show="unreadCount > 0"
						class="absolute top-1 right-14 sm:relative sm:top-0 sm:right-0 inline-flex items-center justify-center px-2 py-1 ml-16 text-xs font-bold leading-none text-red-100 bg-red-600 rounded-full"
					>
						{{ unreadCount }}
					</span></router-link
				>
			</li>
		</ul>
		<div
			class="hidden sm:flex items-center absolute bottom-0 left-0 w-56 h-14 m-4 p-1 rounded-lg transition-all duration-500"
			@click.self="showPopup = false"
			v-show="user"
		>
			<img
				:src="user.profile"
				alt="Profile"
				class="rounded-full object-cover w-12 cursor-pointer"
				@click="togglePopup"
			/>
			<div class="flex flex-col font-montserrat pl-4 w-full font-medium">
				<p
					class="w-40 overflow-hidden whitespace-nowrap text-ellipsis text-prime dark:text-dark-prime"
				>
					{{ user.fullname }}
				</p>
				<small class="text-gray-600 dark:text-dark-second"
					>@{{ user.username }}</small
				>
			</div>
		</div>
		<div
			v-if="showPopup"
			class="hidden sm:flex bg-cl-purple text-prime dark:text-dark-prime dark:bg-dark-second absolute bottom-[4.5rem] left-20 rounded-lg p-4 w-36 h-40 transition-all duration-500 shadow-lg"
			@click.self="showPopup = false"
		>
			<ul class="">
				<div class="flex flex-col h-20 mb-2">
					<li>
						<router-link
							to="/profile"
							class="flex align-middle items-start pb-3"
							@click="showPopup = false"
							><span
								class="text-second dark:text-dark-prime material-icons-outlined pr-2"
								>account_circle</span
							>
							<p>Profile</p></router-link
						>
					</li>
					<li>
						<router-link
							to="/settings"
							class="flex align-middle items-start"
							@click="showPopup = false"
							><span
								class="text-second dark:text-dark-prime material-icons-outlined pr-2"
								>settings</span
							>
							<p>Settings</p></router-link
						>
					</li>
				</div>
				<li>
					<router-link
						to="/"
						class="flex align-middle items-start border-t border-gray-500 pt-2 w-full"
						@click="submitLogout"
						><span
							class="text-second dark:text-dark-prime material-icons-outlined pr-2"
							>logout</span
						>
						<p>Logout</p></router-link
					>
				</li>
			</ul>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useDark, useToggle } from "@vueuse/core";
import { useStore } from "vuex";

const router = useRouter();
const store = useStore();
const isDark = useDark();
const toggleDark = useToggle(isDark);

const showPopup = ref(false);
const isHovered = ref(false);
const searchQuery = ref("");
const searchResults = ref([]);
const unreadCount = ref(null);
const user = reactive({
	isAuthenticated: false,
	profile: null,
	username: null,
	fullname: null,
});
const links = [
	{ name: "Home", path: "/dashboard", label: "home" },
	{ name: "Notification", path: "/notifications", label: "notifications" },
	{ name: "Itinerary", path: "/itinerary", label: "explore" },
	{ name: "Trivia", path: "/trivia", label: "tips_and_updates" },
];

const client = axios.create({
	baseURL: "http://127.0.0.1:8000",
	withCredentials: true,
	timeout: 5000,
	xsrfCookieName: "csrftoken",
	xsrfHeaderName: "X-Csrftoken",
	headers: {
		"Content-Type": "application/json",
	},
});

const submitLogout1 = () => {
	client.post("/api/logout").then((res) => {
		console.log("Logged out user:", res.data);
	});
};

const fetchLikenotification = async () => {
	try {
		const response = await client.get("/api/like-notification-list");
		unreadCount.value = response.data.filter(
			(data) => !data.is_read
		).length;
	} catch (error) {
		console.log(error);
	}
};

const togglePopup = () => {
	showPopup.value = !showPopup.value;
};

const submitLogout = () => {
	const token = sessionStorage.getItem("TOKEN");
	const headers = {
		Authorization: `Token ${token}`,
		"Content-Type": "application/json",
	};
	client
		.post("http://127.0.0.1:8000/api/logout")
		.then((res) => {
			if (res.data.message === "You have not completed the survey yet.") {
				router.push({ name: "tamsurvey" }).then(() => {
					window.location.reload();
				});
			} else {
				localStorage.removeItem("token");
				localStorage.removeItem("username");
				window.scrollTo(0, 0);
				router.push({ name: "login" }).then(() => {
					window.location.reload();
				});
				console.log("User logged out", res);
			}
		})
		.catch((error) => {
			console.log(error);
		});
};

const reloadPage = () => {
	setTimeout(() => {
		router.go(0);
	}, 500);
};
const saveSearchQuery = (event) => {
	searchQuery.value = event.target.value;
};
watch(searchQuery, (newQuery) => {
	console.log(newQuery);
	store
		.dispatch("search", newQuery)
		.then((result) => {
			console.log("SEARCH RESULT :: ", result);

			if (searchQuery.value) {
				router.replace({
					name: "search-result",
					query: { q: searchQuery.value },
				});
			} else {
				router.push({
					name: "dashboard",
				});
			}
		})
		.catch((error) => {
			console.error(error);
		});
});

onMounted(() => {
	fetchLikenotification();
	setInterval(fetchLikenotification, 5000);

	const token = sessionStorage.getItem("TOKEN");
	client.defaults.headers.Authorization = `Token ${token}`;

	client
		.get("api/user", {})
		.then((res) => {
			user.username = res.data.user.username;
			user.fullname = res.data.profile[0].fullname;
			user.profile = res.data.profile[0].user_photo;
			user.isAuthenticated = true;
		})
		.catch((error) => {
			console.log("ERROR", error);
			user.isAuthenticated = false;
		});
});
</script>
<style scoped>
.has-input::-webkit-search-cancel-button {
	-webkit-appearance: none;
	height: 15px;
	width: 15px;
	border-radius: 50%;
	background-color: red; /* change the color here */
	cursor: pointer;
}

.has-input::-webkit-search-cancel-button:hover {
	background-color: #ccc; /* change the hover color here */
}
a {
	text-decoration: none;
}

.side-icons.active {
	color: #6a7fdb;
}

.left-border {
	transition: all 0.3s ease;
	border-radius: 15px;
	background: transparent;
}
.left-border.active {
	transition: all 0.3s ease;
	background: #6a7fdb;
}

input::placeholder {
	color: gray;
}
</style>
