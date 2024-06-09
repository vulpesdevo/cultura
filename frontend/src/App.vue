<template>
	<main class="h-full select-none flex ">
		<Sidebar v-if="user.isAuthenticated"  />
		<router-view class="overflow-auto"></router-view>
	</main>
</template>
<script>
import Login from "./components/Login.vue";
import Sidebar from "./components/Sidebar.vue";

import axios from "axios";

import { ref } from "vue";
export default {
	components: {
		Sidebar,
	},
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
			.get("api/user", {})
			.then((res) => {
				console.log(res.data);
				user.isAuthenticated = true;
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
};
</script>
<style>
:root {
	--text-color-a: #ffff;
	--text-color-b: #b8a3e9;
	--text-color-c: #2c4760;

	--bg-main-color: #2c4760;
	--bg-secondary-color: #2d313d;

	--purple: #564787;

	--dark-bg-theme: #1e1e1e;
}

.text-purple-light {
	color: var(--text-color-b);
}
.dark-bg-color {
	background: var(--dark-bg-theme);
}

.cultura-text,
.buttons,
.text-bebas {
	font-family: "Bebas Neue";
}

.slc,
input,
.text-mont {
	font-family: "Montserrat";
}
input::placeholder {
	color:#1A193F;
}
</style>
