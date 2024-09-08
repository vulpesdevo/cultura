<template>
	<div
		v-if="user.isAuthenticated"
		v-show="user"
		class="flex justify-between w-screen h-16 bg-interface dark:bg-dark-interface fixed sm:top-0 p-3 z-50"
	>
		<img
			:src="isDark ? '/logo1Light.png' : '/culturalink_logo.png'"
			alt="Logo"
			class="h-full w-auto"
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
		<div class="sm:flex w-10 h-full" @click.self="showPopup = false">
			<img
				:src="user.profile"
				alt="Profile"
				class="rounded-full cursor-pointer"
				@click="togglePopup"
			/>
		</div>

		<div
			v-if="showPopup"
			class="sm:flex bg-cl-purple text-prime absolute top-16 right-5 rounded-lg p-4 w-36 h-40 transition-all duration-500 shadow-lg bg-interface dark:bg-dark-second dark:text-dark-prime"
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
						to="/login"
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

<script>
import axios from "axios";
import router from "../routes";
import { useDark, useToggle } from "@vueuse/core";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
export default {
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		return { isDark, toggleDark };
	},
	data() {
		return {
			searchQuery: "",
			searchResults: [],
			showPopup: false,
			user: {
				isAuthenticated: true,
				profile: null,
			},
		};
	},
	watch: {
		searchQuery(newQuery) {
			console.log(newQuery);
			this.client
				.get("api/search/", {
					params: {
						title: newQuery,
					},
				})
				.then((response) => {
					this.searchResults = response.data;
					let result = response.data;
					console.log("SEARCH RESULT :: ", result);

					if (this.searchQuery) {
						this.$router.replace({
							name: "search-result",
							params: { result: JSON.stringify(result) },
						});
					} else {
						this.$router.push({
							name: "dashboard",
						});
					}
				})
				.catch((error) => {
					console.error(error);
				});
		},
	},
	methods: {
		togglePopup() {
			this.showPopup = !this.showPopup;
		},
		submitLogout() {
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			this.client
				.post("http://127.0.0.1:8000/api/logout")
				.then((res) => {
					this.user.isAuthenticated = false;

					localStorage.removeItem("token");

					window.scrollTo(0, 0);
					router.push({ name: "login" }).then(() => {
						window.location.reload();
					});
					console.log("User logged out");
				})
				.catch((error) => {
					console.log(error);
				});
		},
		// Method to reload the page
		reloadPage() {
			setTimeout(() => {
				this.$router.go(0);
			}, 500);
		},
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

		this.client
			.get("api/user")
			.then((res) => {
				// console.log(res.data);
				this.user.isAuthenticated = true;
				this.user.profile = res.data.profile[0].user_photo;
				console.log("Profile Sidebar", res.data);
			})
			.catch((error) => {
				console.log("ERROR", error);
				this.user.isAuthenticated = false;
			});
	},
};
</script>

<style scoped></style>
