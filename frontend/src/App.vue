<template>
	<main class="select-none sm:flex">
		<Topbar class="sm:hidden" />
		<Sidebar />
		<router-view class=""></router-view>
	</main>
</template>
<script>
import Sidebar from "./components/Sidebar.vue";
import Topbar from "./components/Topbar.vue";
import axios from "axios";
import { useDark, useToggle } from "@vueuse/core";
import { ref } from "vue";
export default {
	components: {
		Sidebar,
		Topbar,
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		return { isDark, toggleDark };
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
			.get("api/user", { headers: headers })
			.then((res) => {
				console.log(res.data);
				this.user.isAuthenticated = true;
			})
			.catch((error) => {
				console.log("ERROR", error);
				this.user.isAuthenticated = false;
			});
	},
	methods: {},
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

::-webkit-scrollbar {
	display: none;
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
	color: #9b9bb4;
}
.dark input::placeholder {
	color: #d1d1da;
}
</style>
