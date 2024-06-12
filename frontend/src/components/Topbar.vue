<template>
	<div
		v-if="user.isAuthenticated"
		class="flex justify-between w-screen h-16 bg-interface fixed sm:top-0 p-3"
	>
		<img src="/culturalink_logo.png" alt="Logo" class="h-full w-auto" />
		<div class="sm:flex w-10 h-full">
			<img
				src="/sample_img/mark.png"
				alt="Profile"
				class="rounded-full cursor-pointer"
			/>
		</div>
	</div>
</template>

<script>
import axios from "axios";
export default {
	data() {
		return {
			user: {
				isAuthenticated: false,
			},
		};
	},
	created() {
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
		});
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};

		client
			.get("api/user", { headers: headers })
			.then((res) => {
				console.log(res.data);
				this.user.isAuthenticated = true;
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
};
</script>

<style scoped></style>
