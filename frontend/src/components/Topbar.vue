<template>
	<div
		v-if="user.isAuthenticated"
		class="flex justify-between w-screen h-16 bg-interface fixed sm:top-0 p-3 z-20"
	>
		<img src="/culturalink_logo.png" alt="Logo" class="h-full w-auto" />
		<div class="sm:flex w-10 h-full" @click.self="showPopup = false">
			<img
				src="/sample_img/mark.png"
				alt="Profile"
				class="rounded-full cursor-pointer"
				@click="togglePopup"
			/>
		</div>
		<div
			v-if="showPopup"
			class=" sm:flex bg-cl-purple text-prime absolute top-16 right-5 rounded-lg p-4 w-36 h-40 transition-all duration-500 shadow-lg bg-interface"
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
								class="text-second material-icons-outlined pr-2"
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
								class="text-second material-icons-outlined pr-2"
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
						><span class="text-second material-icons-outlined pr-2"
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
export default {
	data() {
		return {
			showPopup: false,
			user: {
				isAuthenticated: true,
			},
		};
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
			axios
				.post("http://127.0.0.1:8000/api/logout", { headers: headers })
				.then((res) => {
					this.user.isAuthenticated = false;

					localStorage.removeItem("token");
					localStorage.removeItem("username");
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
