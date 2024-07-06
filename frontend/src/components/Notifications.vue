<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 py-5 4 ml-0 overflow-auto h-screen bg-field pt-20 sm:px-28 sm:ml-64 sm:pt-3"
	>
		<div class="flex w-full justify-between sm:w-3/4">
			<h1
				class="font-montserrat text-left text-prime font-semibold sm:text-3xl"
			>
				Notifications
			</h1>
			<div class="flex items-center">
				<a
					class="font-montserrat text-prime text-right sm:text-lg border border-l-0 border-y-0 border-r-prime pr-3 hover:underline cursor-pointer"
					>Mark all as read</a
				>
				<span class="text-prime material-icons-outlined pl-3"
					>settings</span
				>
			</div>
		</div>
		<div
			class="w-full mt-5 justify-between sm:mt-5 sm:w-3/4 cursor-pointer"
			v-for="(data, index) in like_notification"
			:key="index"
		>
			<div
				class="w-full mt-6 p-6 rounded-lg shadow-lg bg-interface sm:mt-5"
			>
				<div class="flex justify-between items-start sm:items-center">
					<div class="flex flex-col sm:flex-row">
						<h1
							class="font-montserrat text-start text-prime text-xs sm:text-lg pr-2"
						>
							@{{ data.liker }}
						</h1>
						<p
							class="font-bebas-neue overflow-hidden whitespace-nowrap text-ellipsis text-lg w-[17rem] sm:w-[30rem] text-prime sm:text-2xl"
						>
							Replied TO YOUR POST {{ data.post_title }}
						</p>
					</div>
					<small
						class="font-montserrat text-prime text-xs sm:text-lg"
						>{{
							new Date(data.created_at).toLocaleDateString()
						}}</small
					>
				</div>
				<p
					class="font-montserrat overflow-hidden whitespace-nowrap text-ellipsis sm:pl-4 sm:pt-2 text-sm w-[21rem] sm:w-full text-prime text-gray-500"
				>
					{{ data.post_content }}
				</p>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
export default {
	data() {
		return {
			like_notification: [],
		};
	},
	mounted() {
		this.fetchLikenotification();
		setInterval(this.fetchLikenotification, 5000);
	},
	created() {
		this.token = localStorage.getItem("token");
		this.client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				Authorization: `Token ${this.token}`,
				"Content-Type": "application/json",
			},
		});
	},
	methods: {
		async fetchLikenotification() {
			try {
				const response = await this.client.get(
					"/api/like-notification-list"
				);
				this.like_notification = response.data;
				console.log(this.like_notification);
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style></style>
