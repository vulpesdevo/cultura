<template>
	<div class="min-h-screen bg-gray-50 dark:bg-notif">
		<!-- Header -->
		<div class="sticky top-0 bg-white dark:bg-gray-800 shadow-sm z-10">
			<div class="max-w-3xl mx-auto px-4 py-4">
				<div class="flex items-center justify-between">
					<h1
						class="text-2xl font-semibold text-gray-900 dark:text-white"
					>
						Notifications
					</h1>
					<div class="flex items-center space-x-4">
						<button
							@click="markAllAsRead"
							class="text-sm text-blue-600 dark:text-blue-400 hover:underline"
						>
							Mark all as read
						</button>
						<button
							class="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full"
						>
							<Settings
								class="w-5 h-5 text-gray-600 dark:text-gray-400"
							/>
						</button>
					</div>
				</div>

				<!-- Filter Chips -->
				<div class="flex gap-2 mt-4 overflow-x-auto pb-2">
					<button
						v-for="filter in filters"
						:key="filter"
						@click="currentFilter = filter"
						class="px-4 py-1.5 rounded-full text-sm whitespace-nowrap transition-colors"
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
			<!-- Follow Notifications -->
			<div
				v-for="notification in filteredNotifications"
				:key="notification.id || notification._id"
				@click="handleNotificationClick(notification)"
				class="flex items-center space-x-4 p-4 rounded-lg bg-white dark:bg-dark-field shadow-sm hover:bg-gray-50 dark:hover:bg-gray-700 cursor-pointer transition"
				:class="{
					'bg-blue-50 dark:bg-blue-900/20': !notification.is_read,
				}"
			>
				<div
					v-if="notification.notif_type === 'follow'"
					class="flex-shrink-0"
				>
					<img
						:src="notification.user_data[0].user_photo"
						:alt="notification.user_data[0].fullname"
						class="w-12 h-12 rounded-full object-cover"
					/>
				</div>
				<div
					v-else
					class="w-12 h-12 rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center flex-shrink-0"
				>
					<Heart
						v-if="notification.notif_type === 'like'"
						class="w-6 h-6 text-red-500"
					/>
					<MessageCircle
						v-else-if="notification.notif_type === 'reply'"
						class="w-6 h-6 text-blue-500"
					/>
				</div>
				<div class="flex-1 min-w-0">
					<p class="text-sm text-gray-900 dark:text-white">
						<span class="font-medium">
							@{{
								notification.followed_by ||
								notification.audience
							}}
						</span>
						<span class="text-gray-600 dark:text-gray-300">
							{{ getNotificationText(notification) }}
						</span>
					</p>
					<template v-if="notification.notif_type !== 'follow'">
						<h3
							class="text-base font-medium text-gray-900 dark:text-white mt-1 truncate"
						>
							{{ notification.post_title }}
						</h3>
						<p
							class="text-sm text-gray-500 dark:text-gray-400 mt-1 truncate"
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
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { Settings, Heart, MessageCircle } from "lucide-vue-next";

const store = useStore();
const router = useRouter();

const filters = ["All", "Likes", "Follow"];
const currentFilter = ref("All");
const like_notification = ref([]);
const follow_notification_list = ref([]);

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

const formatDate = (dateString) => {
	const date = new Date(dateString);
	const now = new Date();
	const diffTime = Math.abs(now - date);
	const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

	if (diffDays === 1) return "Yesterday";
	if (diffDays < 7) return `${diffDays} days ago`;
	return date.toLocaleDateString("en-US", {
		month: "short",
		day: "numeric",
		year: date.getFullYear() !== now.getFullYear() ? "numeric" : undefined,
	});
};

const getNotificationText = (notification) => {
	switch (notification.notif_type) {
		case "follow":
			return " followed you";
		case "like":
			return " liked your post";
		case "reply":
			return " replied to your post";
		default:
			return " interacted with your content";
	}
};

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

const handleNotificationClick = async (notification) => {
	// console.log("NOTIF ", notification);

	await store.dispatch("updateNotificationReadStatus", {
		notificationType:
			notification.notif_type === "follow" ? "follow" : "like",
		notificationId: notification._id,
		isRead: true,
	});
	if (notification.notif_type === "follow") {
		view_user(notification.user_data);
	} else {
		view_post(notification.post_obj_id, notification._id);
	}
};

const view_post = (post_id_notif, notif_id) => {
	console.log("POST ID ", notif_id);
	router.push({
		name: "view-post",
		params: { post: post_id_notif },
		query: { n: notif_id },
	});
};

const view_user = (user_data) => {
	console.log("USER DATA ", user_data);

	router.push({
		name: "user-profile",
		params: {
			username: user_data[0].username,
		},
		query: {
			id: user_data[0].id,
		},
	});
};

const markAllAsRead = async () => {
	try {
		// await store.dispatch("markAllNotificationsAsRead");
		await fetchLikenotification();
		await fetchFollownotification();
	} catch (error) {
		console.log(error);
	}
};

onMounted(async () => {
	await fetchLikenotification();
	await fetchFollownotification();
});
onUnmounted(() => {
	const intervalId = setInterval(fetchLikenotification, 5000);
	clearInterval(intervalId);
});
</script>
