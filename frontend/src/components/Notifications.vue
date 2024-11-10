<template>
	<div
		class="flex flex-col items-center align-middle px-5 py-5 4 ml-0 overflow-auto h-screen bg-field dark:bg-dark-notif sm:px-28 sm:pt-3"
	>
		<div class="flex w-full mb-4 justify-between sm:w-3/4">
			<h1
				class="font-montserrat text-left text-prime dark:text-dark-prime font-semibold sm:text-3xl"
			>
				Notifications
			</h1>
			<div class="flex items-center">
				<a
					class="font-montserrat text-prime dark:text-dark-prime text-right sm:text-lg border border-l-0 border-y-0 border-r-prime pr-3 hover:underline cursor-pointer"
					>Mark all as read</a
				>
				<span
					class="text-prime dark:text-dark-second material-icons-outlined pl-3"
					>settings</span
				>
			</div>
		</div>
		<div
			class="w-full justify-between sm:mt-2 sm:w-3/4 cursor-pointer"
			v-for="(data, index) in follow_notification_list"
			:key="index"
			@click="view_user(follow_notification_list[index].user_data)"
		>
			<div
				class="w-full mt-1 p-3 sm:p-5 rounded-lg shadow-lg sm:mt-2"
				:class="!data.is_read ? 'bg-interface' : 'bg-zinc-400'"
			>
				@{{ data.followed_by }} followed you
			</div>
		</div>
		<div
			class="w-full justify-between sm:mt-2 sm:w-3/4 cursor-pointer"
			v-for="(data, index) in like_notification"
			:key="index"
			@click="view_post(data.post_obj_id, data._id)"
		>
			<div
				class="w-full mt-1 p-3 sm:p-5 rounded-lg shadow-lg sm:mt-2"
				:class="!data.is_read ? 'bg-interface' : 'bg-zinc-400'"
			>
				<div class="flex justify-between items-start sm:items-center">
					<div class="flex flex-col sm:flex-row">
						<h1
							class="font-montserrat flex items-center text-start text-prime text-xs sm:text-[16px] pr-2"
						>
							@{{ data.audience }}
							{{
								data.notif_type === "like"
									? "liked your post"
									: "replied to your post"
							}}:
						</h1>
						<p
							class="font-bebas-neue flex items-center pb-0 overflow-hidden whitespace-nowrap text-ellipsis text-lg w-[17rem] sm:w-[20rem] text-start text-prime sm:text-[20px]"
						>
							{{ data.post_title }}
						</p>
					</div>
					<small
						class="font-montserrat text-prime text-xs sm:text-[15px]"
						>{{
							new Date(data.created_at).toLocaleDateString()
						}}</small
					>
				</div>
				<p
					class="font-montserrat overflow-hidden whitespace-nowrap text-ellipsis sm:pl-4 sm:pt-2 text-sm w-[21rem] sm:w-full text-prime"
				>
					{{ data.post_content }}
				</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const store = useStore();
const router = useRouter();

const like_notification = ref([]);
const unreadCount = ref(null);
const follow_notification_list = ref([]);

const fetchLikenotification = async () => {
	try {
		await store.dispatch("fetchLikeNotifications");
		like_notification.value = store.getters.getLikeNotifications;
		unreadCount.value = like_notification.value.filter(
			(data) => !data.is_read
		).length;
	} catch (error) {
		console.log(error);
	}
};

const fetchFollownotification = async () => {
	try {
		await store.dispatch("fetchFollowNotifications");
		follow_notification_list.value = store.getters.getFollowNotifications;
		unreadCount.value = follow_notification_list.value.filter(
			(data) => !data.is_read
		).length;
		console.log("FOLLOW", follow_notification_list.value);
	} catch (error) {
		console.log(error);
	}
};

const view_post = (post_id_notif, notif_id) => {
	router.push({
		name: "view-post",
		params: { post_id_notif, notif_id },
	});
};

const view_user = (user_data) => {
	console.log("FGFGF", user_data[0]);
	router.push({
		name: "user-profile",
		params: {
			username: user_data[0].username,
			user: JSON.stringify(user_data[0]),
		},
	});
};

onMounted(async () => {
	await fetchLikenotification();
	await fetchFollownotification();
	const intervalId = setInterval(fetchLikenotification, 5000);
	onUnmounted(() => {
		clearInterval(intervalId);
	});
});
</script>

<style></style>
