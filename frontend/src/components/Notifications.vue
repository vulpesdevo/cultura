<template>
	<div class="min-h-screen bg-gray-100 dark:bg-notif">
		<!-- Header -->
		<div class="sticky top-0 bg-white dark:bg-gray-800 shadow-sm z-10">
			<div class="max-w-3xl mx-auto px-4 py-4">
				<div class="flex items-center justify-between">
					<h1
						class="text-xl sm:text-2xl font-semibold text-gray-900 dark:text-white"
					>
						Notifications
					</h1>
					<router-link
						:to="{ name: 'settings' }"
						class="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
					>
						<CogIcon
							class="w-5 h-5 text-gray-600 dark:text-gray-400"
						/>
					</router-link>
				</div>

				<!-- Filter Chips -->
				<div class="flex gap-2 mt-4 overflow-x-auto pb-2">
					<button
						v-for="filter in filters"
						:key="filter"
						@click="currentFilter = filter"
						class="px-3 py-1 rounded-full text-xs sm:text-sm whitespace-nowrap transition-colors"
						:class="
							currentFilter === filter
								? 'bg-blue-600 text-white'
								: 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
						"
					>
						{{ filter }}
					</button>
				</div>
			</div>
		</div>

		<!-- Notifications List -->
		<div class="max-w-3xl mx-auto px-4 py-6 space-y-4">
			<div
				v-for="notification in displayedNotifications"
				:key="notification.id || notification._id"
				@click="handleNotificationClick(notification)"
				class="flex items-center space-x-4 p-4 rounded-lg shadow-sm cursor-pointer transition"
				:class="getNotificationClass(notification)"
			>
				<div
					class="w-10 h-10 sm:w-12 sm:h-12 rounded-full flex items-center justify-center flex-shrink-0"
				>
					<HeartIcon
						v-if="notification.notif_type === 'like'"
						class="w-5 h-5 sm:w-6 sm:h-6 text-red-500"
					/>
					<ChatBubbleLeftIcon
						v-else-if="notification.notif_type === 'commented'"
						class="w-5 h-5 sm:w-6 sm:h-6 text-blue-500"
					/>
					<ExclamationTriangleIcon
						v-else-if="notification.notif_type === 'warn'"
						class="w-5 h-5 sm:w-6 sm:h-6 text-yellow-500"
					/>
					<NoSymbolIcon
						v-else-if="notification.notif_type === 'reported'"
						class="w-5 h-5 sm:w-6 sm:h-6 text-red-500"
					/>
					<UserIcon
						v-else-if="notification.notif_type === 'follow'"
						class="w-5 h-5 sm:w-6 sm:h-6 text-blue-500"
					/>
				</div>
				<div class="flex-1 min-w-0">
					<p
						class="text-xs sm:text-sm"
						:class="getTextClass(notification)"
					>
						<span
							v-if="
								notification.followed_by ||
								notification.audience
							"
							class="font-medium"
						>
							@{{
								notification.followed_by ||
								notification.audience
							}}
						</span>
						<span>
							{{ getNotificationText(notification) }}
						</span>
					</p>
					<template v-if="notification.notif_type !== 'follow'">
						<h3
							class="text-sm sm:text-base font-medium mt-1 truncate"
							:class="getTextClass(notification)"
						>
							{{ notification.post_title }}
						</h3>
						<p
							class="text-xs sm:text-sm mt-1 truncate"
							:class="getSubtextClass(notification)"
						>
							{{ notification.post_content }}
						</p>
					</template>
					<p class="text-xs text-gray-500 dark:text-gray-400 mt-2">
						{{ formatDate(notification.created_at) }}
					</p>
				</div>
				<div
					v-if="!notification.is_read"
					class="w-2 h-2 bg-blue-600 rounded-full flex-shrink-0"
				></div>
			</div>

			<!-- Show More Button -->
			<div v-if="hasMoreNotifications" class="text-center mt-4">
				<button
					@click="loadMoreNotifications"
					class="px-4 py-2 text-xs bg-second text-white rounded-md hover:bg-blue-400 transition-colors"
				>
					Show More
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import {
	CogIcon,
	ExclamationTriangleIcon,
	NoSymbolIcon,
	UserIcon,
} from "@heroicons/vue/24/outline";
import { ChatBubbleLeftIcon, HeartIcon } from "@heroicons/vue/24/solid";
import axiosClient from "../axios";
import moment from "moment";
import { io } from "socket.io-client";

const store = useStore();
const router = useRouter();

const filters = ["All", "Likes", "Follow"];
const currentFilter = ref("All");
const like_notification = ref([]);
const follow_notification_list = ref([]);
// const socket = ref(null);

const filteredNotifications = computed(() => {
	const allNotifications = [
		...follow_notification_list.value,
		...like_notification.value,
	];
	switch (currentFilter.value) {
		case "Likes":
			return like_notification.value.filter(
				(n) => n.notif_type === "like"
			);
		case "Follow":
			return follow_notification_list.value;
		default:
			return allNotifications;
	}
});

// const setupWebSocket = () => {
// 	socket.value = io("http://your-backend-url"); // Replace with your actual backend URL

// 	socket.value.on("newNotification", (notification) => {
// 		if (notification.notif_type === "like") {
// 			like_notification.value.unshift(notification);
// 		} else if (notification.notif_type === "follow") {
// 			follow_notification_list.value.unshift(notification);
// 		} else {
// 			// Handle other notification types
// 			console.log("New notification received:", notification);
// 		}
// 	});

// 	socket.value.on("connect", () => {
// 		console.log("Connected to WebSocket for notifications");
// 	});

// 	socket.value.on("disconnect", () => {
// 		console.log("Disconnected from WebSocket for notifications");
// 	});
// };

const fetchLikenotification = async () => {
	try {
		await store.dispatch("fetchLikeNotifications");
		like_notification.value = store.getters.getLikeNotifications;
		console.log("LIKE NOTIF ", like_notification.value);
	} catch (error) {
		console.log(error);
	}
};

const fetchFollownotification = async () => {
	try {
		await store.dispatch("fetchFollowNotifications");
		follow_notification_list.value = store.getters.getFollowNotifications;
	} catch (error) {
		console.log(error);
	}
};

const formatDate = (dateString) => {
	return moment(dateString).fromNow();
};

const getNotificationClass = (notification) => {
	const baseClasses =
		"bg-white dark:bg-dark-field hover:bg-gray-50 dark:hover:bg-gray-700";
	if (!notification.is_read) {
		return `${baseClasses} bg-blue-50 dark:bg-blue-900/20`;
	}
	if (notification.notif_type === "warn") {
		return `${baseClasses} bg-yellow-50 dark:bg-yellow-900/20`;
	}
	if (notification.notif_type === "reported") {
		return `${baseClasses} bg-red-50 dark:bg-red-900/20`;
	}
	return baseClasses;
};

const getTextClass = (notification) => {
	if (notification.notif_type === "warn") {
		return "text-yellow-800 dark:text-yellow-200";
	}
	if (notification.notif_type === "reported") {
		return "text-red-800 dark:text-red-200";
	}
	return "text-gray-900 dark:text-white";
};

const getSubtextClass = (notification) => {
	if (notification.notif_type === "warn") {
		return "text-yellow-600 dark:text-yellow-300";
	}
	if (notification.notif_type === "reported") {
		return "text-red-600 dark:text-red-300";
	}
	return "text-gray-500 dark:text-gray-400";
};

const getNotificationText = (notification) => {
	switch (notification.notif_type) {
		case "follow":
			return " followed you";
		case "like":
			return " liked your post";
		case "reply":
			return " replied to your post";
		case "warn":
			return " Your post has received a warning";
		case "reported":
			return " Your post has been banned";
		default:
			return " interacted with your content";
	}
};

const displayedNotifications = computed(() => {
	return filteredNotifications.value;
});

const hasMoreNotifications = ref(false);

const loadMoreNotifications = () => {
	// Implement your logic to load more notifications here
	console.log("Load More Notifications Clicked");
	hasMoreNotifications.value = false; // Set to false after loading
};

const handleNotificationClick = async (notification) => {
	// Update the notification's read status
	await store.dispatch("updateNotificationReadStatus", {
		notificationType:
			notification.notif_type === "follow" ? "follow" : "like",
		notificationId: notification._id,
		isRead: true,
	});

	// Set the notification as read locally
	notification.is_read = true;

	// Navigate based on notification type
	if (notification.notif_type === "follow") {
		router.push({
			name: "user-profile",
			params: {
				username: notification.user_data[0].username,
			},
			query: {
				id: notification.user_data[0].id,
			},
		});
	} else {
		// For all other notification types (like, comment, warn, reported)
		router.push({
			name: "view-post",
			params: { post: notification.post_obj_id },
			query: { n: notification._id },
		});
	}

	console.log("Notification Clicked:", notification);
};

onMounted(async () => {
	await fetchLikenotification();
	await fetchFollownotification();
	setupWebSocket();
});

// onUnmounted(() => {
// 	if (socket.value) {
// 		socket.value.disconnect();
// 	}
// });
</script>
