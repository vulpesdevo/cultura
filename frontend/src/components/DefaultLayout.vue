<template>
	<div
		class="flex flex-col sm:flex-row min-h-screen w-screen bg-white dark:bg-dark-interface transition-colors duration-300"
	>
		<!-- Topbar (mobile only) -->
		<div
			class="sm:hidden flex justify-between items-center w-full h-16 bg-interface dark:bg-dark-interface fixed top-0 p-3 z-50 shadow-lg shadow-bg-interface"
		>
			<img
				:src="isDark ? '/logo1Light.png' : '/culturalink_logo.png'"
				alt="Logo"
				class="h-full w-auto"
			/>
			<div class="relative w-3/4">
				<input
					type="text"
					:class="{ 'has-input': searchQuery }"
					placeholder="Search..."
					class="w-full pl-10 h-9 outline-none text-black dark:text-dark-prime dark:bg-dark-second-dark rounded-full shadow-md"
					v-model="searchQuery"
				/>
				<span
					class="material-icons-outlined absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-700 dark:text-dark-prime"
					>search</span
				>
			</div>
			<div class="flex items-center">
				<img
					:src="user.profile.user_photo"
					alt="Profile"
					class="w-10 h-10 rounded-full cursor-pointer"
					@click="togglePopup"
				/>
			</div>
		</div>

		<!-- Sidebar (desktop) / Bottom Navigation (mobile) -->
		<aside
			class="fixed flex flex-col sm:relative bottom-0 sm:bottom-auto left-0 right-0 sm:left-auto sm:right-auto w-full sm:w-64 bg-white dark:bg-dark-interface sm:min-h-screen z-40"
		>
			<div class="hidden sm:flex flex-col items-center px-5">
				<img
					:src="
						isDark
							? '/ULTURALINK-DMLong.png'
							: '/culturalink_brand_logo.png'
					"
					alt="Logo"
					class="w-full h-32"
				/>
				<div class="relative w-full mb-4">
					<input
						type="search"
						:class="{ 'has-input': searchQuery }"
						placeholder="Search..."
						class="w-full pl-10 h-9 outline-none text-gray-700 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 rounded-full shadow-sm"
						v-model="searchQuery"
					/>
					<MagnifyingGlassIcon
						class="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400"
					/>
				</div>
			</div>
			<nav
				class="flex sm:flex-col justify-around sm:justify-start sm:space-y-3 px-4 font-montserrat"
			>
				<router-link
					v-for="link in links"
					:key="link.path"
					:to="link.path"
					class="flex flex-col sm:flex-row items-center px-3 py-4 sm:py-1 text-sm relative group"
					:class="[
						$route.path === link.path
							? 'text-second '
							: 'text-gray-700 dark:text-gray-300 hover:text-second dark:hover:text-second',
					]"
				>
					<div
						class="absolute sm:left-0 sm:top-0 sm:bottom-0 sm:w-1 w-full sm:h-auto h-1 top-0 left-0 rounded-full transition-all duration-300"
						:class="[
							$route.path === link.path
								? 'bg-second'
								: 'bg-transparent group-hover:bg-blue-200 dark:group-hover:bg-second',
						]"
					></div>
					<component
						:is="link.icon"
						class="w-6 h-6 sm:mr-3 mt-1 sm:mb-0"
						:class="{
							'text-second': $route.path === link.path,
						}"
					/>
					<span
						class="text-xs sm:text-sm font-medium text-center sm:flex hidden"
						>{{ link.name }}</span
					>
					<span
						v-if="link.name === 'Notifications' && unreadCount > 0"
						class="absolute right-2 top-1 text-xs bg-red-500 text-white rounded-full px-2 py-[.20rem]"
					>
						{{ unreadCount }}
					</span>
				</router-link>
			</nav>
			<div class="hidden sm:flex items-center px-4 mt-auto mb-4">
				<img
					:src="user.profile?.user_photo"
					alt="Profile"
					class="w-10 h-10 rounded-full mr-3"
				/>
				<div class="flex-1">
					<p
						class="text-sm font-medium text-gray-700 dark:text-gray-200 truncate"
					>
						{{ user.profile.fullname }}
					</p>
					<p
						class="text-xs text-gray-500 dark:text-gray-400 truncate"
					>
						@{{ user.username }}
					</p>
				</div>
				<button @click="togglePopup">
					<ChevronUpIcon
						class="w-5 h-5 text-gray-500 dark:text-gray-400"
					/>
				</button>
			</div>
		</aside>

		<!-- Main content -->
		<main
			class="flex-1 pt-16 sm:pt-0 pb-14 sm:pb-0 overflow-x-hidden overflow-y-auto w-full bg-gray-100 dark:bg-gray-900"
		>
			<router-view></router-view>
		</main>

		<!-- Bottom navigation (mobile only) -->

		<!-- User popup menu -->
		<Transition name="fade">
			<div
				v-if="showPopup"
				class="fixed inset-0 z-50"
				@click="closePopup"
			>
				<div
					class="fixed top-16 sm:top-auto sm:bottom-16 sm:left-32 right-4 bg-interface dark:bg-gray-800 rounded-lg p-4 w-48 shadow"
					@click.stop
				>
					<ul class="space-y-2">
						<li>
							<router-link
								to="/profile"
								class="flex items-center text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 p-2 rounded-md"
								@click="closePopup"
							>
								<UserCircleIcon class="w-5 h-5 mr-3" />
								<span>Profile</span>
							</router-link>
						</li>
						<li>
							<router-link
								to="/settings"
								class="flex items-center text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 p-2 rounded-md"
								@click="closePopup"
							>
								<Cog6ToothIcon class="w-5 h-5 mr-3" />
								<span>Settings</span>
							</router-link>
						</li>
						<li
							class="border-t border-gray-200 dark:border-gray-700 pt-2"
						>
							<button
								@click="submitLogout"
								class="flex items-center w-full text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 p-2 rounded-md"
							>
								<ArrowRightOnRectangleIcon
									class="w-5 h-5 mr-3"
								/>
								<span>Logout</span>
							</button>
						</li>
					</ul>
				</div>
			</div>
		</Transition>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, watchEffect } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useDark, useToggle } from "@vueuse/core";
import axiosClient from "../axios";
import {
	HomeIcon,
	BellIcon,
	MapIcon,
	AcademicCapIcon,
	UserCircleIcon,
	Cog6ToothIcon,
	ArrowRightOnRectangleIcon,
	MagnifyingGlassIcon,
	ChevronUpIcon,
} from "@heroicons/vue/24/outline";

const store = useStore();
const router = useRouter();
const isDark = useDark();
const showPopup = ref(false);
const searchQuery = ref("");
const searchResults = ref([]);
const unreadCount = ref(0);
const user = ref({ profile: { user_photo: "" } });
const links = ref([
	{ name: "Home", path: "/dashboard", icon: HomeIcon },
	{ name: "Notifications", path: "/notifications", icon: BellIcon },
	{ name: "Itineraries", path: "/itinerary", icon: MapIcon },
	{ name: "Trivia", path: "/trivia", icon: AcademicCapIcon },
]);

onMounted(async () => {
	try {
		const userData = await store.dispatch("fetchUserData");
		user.value = userData.user;
		user.value.profile = userData.profile;
		console.log("data HAHAHA", user.value.profile.is_admin);
	} catch (error) {
		console.error("Error fetching user data:", error);
	}
});

onUnmounted(() => {
	document.removeEventListener("click", closePopup);
});

const togglePopup = () => {
	showPopup.value = !showPopup.value;
};
const closePopup = () => {
	showPopup.value = false;
};

watch(() => router.currentRoute.value, closePopup);
watch(searchQuery, (newQuery) => {
	console.log(newQuery);
	store
		.dispatch("search", newQuery)
		.then((response) => {
			searchResults.value = response;
			console.log("SEARCH RESULT :: ", response);

			if (searchQuery.value) {
				router.replace({
					name: "search-result",
					query: { q: JSON.stringify(response) },
				});
			} else {
				router.go(-1);
			}
		})
		.catch((error) => {
			console.error(error);
		});
});
const lastFetchTime = ref(Date.now());
const fetchNotification = async () => {
	try {
		await store.dispatch("fetchLikeNotifications");
		await store.dispatch("fetchFollowNotifications");

		unreadCount.value = store.getters.getTotalUnreadNotificationsCount; // Assuming you have a getter for unread count
		console.log("unreadCount", unreadCount.value);
	} catch (error) {
		console.error("Error fetching notifications:", error);
	}
};

const submitLogout = async () => {
	try {
		await store.dispatch("logout");
		router.push({ name: "login" });
	} catch (error) {
		router.push({ name: "tamsurvey" });

		console.error("Error during logout:", error);
	}
};
// Watch the lastFetchTime property
watch(lastFetchTime, () => {
	fetchNotification(); // Call fetchNotification whenever lastFetchTime changes
});

// Example of updating lastFetchTime periodically
setInterval(() => {
	lastFetchTime.value = Date.now(); // Update the timestamp to trigger the watcher
}, 6000); // Fetch notifications every minute
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
	opacity: 0;
}

@media (max-width: 640px) {
	.has-input::-webkit-search-cancel-button {
		-webkit-appearance: none;
		height: 15px;
		width: 15px;
		border-radius: 50%;
		background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23999'%3E%3Cpath d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'/%3E%3C/svg%3E")
			no-repeat center;
		background-size: 12px;
		cursor: pointer;
	}
}
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
You
