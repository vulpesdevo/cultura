<template>
	<section
		class="bg-interface h-screen w-screen flex flex-col justify-center items-center sm:flex-row p-0 sm:p-20"
	>
		<div
			class="logo-container sm:w-1/2  flex justify-center items-center align-middle pt-10 sm:pt-1"
		>
			<img
				class="h-56 sm:w-screen sm:h-auto"
				src="/culturalink_logo.png"
				alt="cultura-logo"
			/>
		</div>
		<div
			class="flex flex-col justify-center items-center  sm:w-1/2 align-middle text-center "
		>
			<h3
				class="sm:pl-0 flex text-center text-prime text-2xl  sm:text-5xl mb-3 w-auto"
			>
				Share. Learn. Connect.
			</h3>
			<h1
				class="font-bebas-neue text-6xl text-prime text-center mb-6 tracking-widest sm:text-9xl"
			>
				Culturalink
			</h1>
			<form
				class="flex flex-col justify-center align-middle items-center m-12 mx-10"
				@submit.prevent="submitLogin"
			>
				<input
					type="text"
					placeholder="Username"
					name="lusername"
					v-model="username"
					class="pl-5 bg-field rounded-full mb-4 w-80 sm:w-96 h-14"
				/>
				<input
					type="password"
					name="lpassword"
					v-model="password"
					placeholder="Password"
					class="pl-5 bg-field rounded-full mb-2 w-80 sm:w-96 h-14"
				/>
				<a href="" class="text-center text-second mb-10"
					>Forgot passsword?</a
				>
				<input
					type="submit"
					value="Log in"
					class="font-bebas-neue text-3xl bg-second text-interface p-2 rounded-full w-52 h-14 mb-6 hover:bg-second-light"
				/>

				<span class="flex"
					><p class="text-black">Don't have an account?</p>
					<a
						href=""
						class="pl-3 text-second"
						@click.prevent="showModal = true"
						>Sign Up Now!</a
					></span
				>
			</form>
		</div>
		<div
			class="fixed z-50 inset-0 overflow-y-auto "
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
		>
			<div
				class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0 w-screen"
			>
				<div
					class="fixed inset-0  bg-black bg-opacity-70 transition-opacity w-full"
					aria-hidden="true"
				></div>
				<span
					class="hidden sm:inline-block sm:align-middle sm:h-screen"
					aria-hidden="true"
					>&#8203;</span
				>
				<div
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/2"
				>
					<button
						class="absolute top-0 right-0 m-2 text-prime text-2xl"
						@click="showModal = false"
					>
						&times;
					</button>
					<div
						class="bg-interface px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<h3
							class="font-bebas-neue text-5xl pt-5 sm:text-7xl leading-6 font-medium text-prime"
							id="modal-title"
						>
							SIGN UP
						</h3>
						<p
							class="font-montserrat text-prime pt-2 pb-5 text-lg sm:text-2xl"
						>
							Create your account
						</p>
						<form class="mt-2" @submit.prevent="submitRegistration">
							<div class="flex flex-wrap">
								<div class="w-full md:w-1/2 px-3">
									<input
										type="text"
										placeholder="Username"
										name="rusername"
										v-model="rusername"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
									<input
										type="email"
										placeholder="Email"
										name="email"
										v-model="email"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
									<input
										type="text"
										placeholder="Name"
										name="name"
										v-model="rname"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
								</div>
								<div class="w-full md:w-1/2 px-3">
									<input
										type="text"
										placeholder="Country"
										name="country"
										v-model="rcountry"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
									<input
										type="password"
										placeholder="Password"
										name="rpassword"
										v-model="rpassword"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
									<input
										type="password"
										placeholder="Re-enter Password"
										name="repassword"
										v-model="repassword"
										class="mt-2 pl-5 w-full rounded-full h-14 bg-field"
									/>
								</div>
							</div>

							<div
								class="flex flex-col items-center align-middle text-center"
							>
								<p
									class="py-5 text-white font-montserrat text-xs"
								>
									By signing up, you agree to the Terms of
									Service and Privacy Policy, including Cookie
									Use.
								</p>
								<input
									type="submit"
									value="SIGN UP"
									class="font-bebas-neue text-interface text-3xl bg-second p-2 rounded-full w-52 h-14 mb-6 hover:bg-second-light"
								/>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>
<script>
import axios from "axios";

import { ref } from "vue";
import router from "../routes";
// import emailjs from "emailjs-com";
export default {
	name: "register-login",
	data() {
		return {
			// showLoginModal: null,
			// loginSuccess: null,
			object: null,
			showModal: false,
			// // Data property for showing/hiding the OTP modal
			// showOtpModal: false,
		};
	},
	setup() {
		const email = ref("");
		const rname = ref("");
		const rcountry = ref("");
		const rusername = ref("");
		const rpassword = ref("");
		const repassword = ref("");

		const username = ref("");
		const password = ref("");

		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const submitRegistration = () => {
			if (rpassword.value == repassword.value) {
				client
					.post("/api/registration", {
						email: email.value,
						fullname: rname.value,
						country: rcountry.value,
						username: rusername.value,
						password: rpassword.value,
					})
					.then((response) => {
						client
							.post("/api/login", {
								username: rusername.value,
								password: rpassword.value,
							})
							.then((response) => {
								const token = response.data.token; // Replace with your token
								localStorage.setItem("token", token);
								localStorage.setItem(
									"username",
									response.data.user.username
								);
								document.cookie =
									"name=value; SameSite=Lax; Secure";
								console.log("logged in!");
								window.scrollTo(0, 0);
								router.push({ name: "dashboard" }).then(() => {window.location.reload(); });
							});
					})
					.catch((error) => {
						console.log("ERROR: ", error);
						// showRegisterModal.value = true;
						// registerSuccess.value = false;
					});
				// otp_val.value = Math.floor(Math.random() * 900000) + 100000;

				// emailjs
				// 	.send(
				// 		"service_d5qxdx5",
				// 		"template_oqirukd",
				// 		{
				// 			to_email: email.value,
				// 			to_name: `${first_name.value}_${last_name.value}`,
				// 			message: `Your OTP is: ${otp_val.value}`,
				// 		},
				// 		"q4h4FsnDFS63Vb78i"
				// 	)
				// 	.then((message) => {
				// 		if (message.text === "OK") {
				// 			alert("OTP sent to your email " + email.value);
				// 			showOtpModal.value = true;
				// 		}
				// 	});
			}
		};

		const submitLogin = () => {
			//console.log(email.value, password.value);
			client
				.post("/api/login", {
					username: username.value,
					password: password.value,
				})
				.then((response) => {
					console.log("Login successful:", response.data);
					// Redirect to home page
					const token = response.data.token; // Replace with your token
					localStorage.setItem("token", token);
					localStorage.setItem(
						"username",
						response.data.user.username
					);
					window.scrollTo(0, 0);
					
					
					router.push({ name: "dashboard" }).then(() => {window.location.reload(); });
					// 	// After navigating to the "home" route, reload the page
					// 	const client = axios.create({
					// 		baseURL: "http://127.0.0.1:8000",
					// 	});
					// 	const token = localStorage.getItem("token");
					// 	const headers = {
					// 		Authorization: `Token ${token}`,
					// 		"Content-Type": "application/json",
					// 	};

					// 	client
					// 		.get("api/profile/", { headers: headers })
					// 		.then((res) => {
					// 			console.log(res.data);
					// 		})
					// 		.catch((error) => {
					// 			console.log("ERROR", error);
					// 		});
					// });
				})
				.catch((error) => {});
		};

		const submitLogout = () => {
			client.post("/api/logout").then((res) => {
				console.log("Logged out user:", res.data);
			});
		};

		// Watch for changes in currentUser
		// const updateFormBtn = () => {
		// 	registrationToggle.value = !registrationToggle.value;
		// };
		// const closeModal = () => {
		// 	showLoginModal.value = false;
		// 	showRegisterModal.value = false;
		// };

		return {
			//login
			username,
			password,

			//registration
			email,
			rcountry,
			rname,
			rusername,
			rpassword,
			repassword,
			//funstions
			submitRegistration,
			submitLogin,
			submitLogout,
		};
	},
	
	methods: {},
	// created() {
	// 	const client = axios.create({
	// 		baseURL: "http://127.0.0.1:8000",
	// 	});
	// 	const token = localStorage.getItem("token");
	// 	const headers = {
	// 		Authorization: `Token ${token}`,
	// 		"Content-Type": "application/json",
	// 	};

	// 	client
	// 		.get("api/user/", { headers: headers })
	// 		.then((res) => {
	// 			console.log(res.data);
	// 		})
	// 		.catch((error) => {
	// 			console.log("ERROR", error);
	// 		});
	// },
	mounted() {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");
</style>
