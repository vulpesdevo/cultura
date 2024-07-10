<template>
	<section
		class="bg-interface dark:bg-dark-notif h-screen w-screen flex flex-col justify-center items-center sm:flex-row p-0 sm:p-20"
	>
		<div
			class="logo-container sm:w-1/2 flex justify-center items-center align-middle pt-10 sm:pt-1"
		>
			<img
				class="h-56 sm:w-screen sm:h-auto"
				:src="isDark ?  '/logo1Light.png':'/culturalink_logo.png'"
				alt="cultura-logo"
			/>
		</div>
		<div
			class="flex flex-col justify-center items-center sm:w-1/2 align-middle text-center"
		>
			<h3
				class="sm:pl-0 flex text-center text-prime dark:text-dark-prime text-2xl sm:text-5xl mb-3 w-auto"
			>
				Share. Learn. Connect.
			</h3>
			<h1
				class="font-bebas-neue text-6xl text-prime dark:text-dark-prime text-center mb-6 tracking-widest sm:text-9xl"
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
					class="pl-5 bg-field dark:bg-dark-second-dark dark:text-dark-prime rounded-full mb-4 w-80 sm:w-96 h-14"
				/>
				<input
					type="password"
					name="lpassword"
					v-model="password"
					placeholder="Password"
					class="pl-5 bg-field dark:bg-dark-second-dark dark:text-dark-prime rounded-full mb-2 w-80 sm:w-96 h-14"
				/>
				<a class="text-center text-second mb-10" @click="toggleModal"
					>Forgot passsword?</a
				>
				<input
					type="submit"
					value="Log in"
					class="font-bebas-neue text-3xl bg-second text-interface p-2 rounded-full w-52 h-14 mb-6 hover:bg-second-light"
				/>
				<span class="flex"
					><p class="text-black dark:text-dark-prime">
						Don't have an account?
					</p>
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
			class="fixed z-50 inset-0 overflow-y-auto"
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
		>
			<div
				class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0 w-screen"
			>
				<div
					class="fixed inset-0 bg-black bg-opacity-70 transition-opacity w-full"
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
					<!-- <button
						class="absolute top-0 right-0 m-2 text-prime text-2xl"
						@click="showModal = false"
					>
						&times;
					</button> -->
					<span
						@click="showModal = false"
						class="flex material-icons-outlined justify-end absolute top-0 right-0 m-2 text-prime dark:text-dark-prime text-2xl"
						>close</span
					>
					<div
						class="bg-interface dark:bg-dark-notif px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<h3
							class="font-bebas-neue text-5xl pt-5 sm:text-7xl leading-6 font-medium text-prime dark:text-dark-prime"
							id="modal-title"
						>
							SIGN UP
						</h3>
						<p
							class="font-montserrat text-prime dark:text-dark-prime pt-2 pb-5 text-lg sm:text-2xl"
						>
							Create your account
						</p>
						<form class="mt-2" @submit.prevent="submitRegistration">
							<div class="flex flex-wrap">
								<div class="w-full md:w-1/2 px-3">
									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Username</label
										>

										<input
											type="text"
											placeholder="Username"
											name="rusername"
											v-model="rusername"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
										/>
									</div>
									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Email</label
										>

										<div
											class="absolute inset-y-0 start-0 flex sm:mt-6 items-center ps-3.5 pointer-events-none"
										>
											<svg
												class="w-4 h-4 text-gray-500 dark:text-gray-400"
												aria-hidden="true"
												xmlns="http://www.w3.org/2000/svg"
												fill="currentColor"
												viewBox="0 0 20 16"
											>
												<path
													d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"
												/>
												<path
													d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"
												/>
											</svg>
										</div>
										<input
											type="email"
											id="input-group-1"
											name="email"
											v-model="email"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
											placeholder="name@flowbite.com"
										/>
									</div>

									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Full Name</label
										>
										<input
											type="text"
											placeholder="Name"
											name="name"
											v-model="rname"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
										/>
									</div>
								</div>
								<div class="w-full md:w-1/2 px-3">
									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Country</label
										>

										<input
											type="text"
											placeholder="Country"
											name="country"
											v-model="rcountry"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
										/>
									</div>

									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Password</label
										>

										<input
											type="password"
											placeholder="Password"
											name="rpassword"
											v-model="rpassword"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
										/>
									</div>

									<div class="relative text-left">
										<label for="" class="hidden sm:flex"
											>Re-enter Password</label
										>

										<input
											type="password"
											placeholder="Re-enter Password"
											name="repassword"
											v-model="repassword"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
										/>
									</div>
								</div>
							</div>

							<div
								class="flex flex-col items-center align-middle text-center"
							>
								<p
									class="py-5 text-prime dark:text-dark-prime font-montserrat text-xs"
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
		<!-- Forgot Password Modal -->
		<div
			v-show="modalActive"
			class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
		>
			<div
				v-if="modalActive"
				class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-36"
			>
				<span
					@click="modalActive = false"
					class="flex material-icons-outlined justify-end"
					>close</span
				>
				<h1
					class="flex text-4xl sm:text-7xl text-prime font-bebas-neue my-5 justify-center"
				>
					reset your password
				</h1>
				<p
					class="flex text-center text-sm sm:text-lg my-5 mb-7 sm:my-7 px-7 sm:px-20 font-montserrat"
				>
					A one-time PIN will be emailed to you to help reset your
					password.
				</p>
				<form>
					<div class="flex-col mb-6 px-5 sm:px-28">
						<label
							for="email"
							class="flex ms-3 mb-2 text-sm font-bold text-prime justify-start"
							>Email</label
						>
						<input
							type="email"
							id="email"
							class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
							placeholder="christina.tecson@sdca.edu.ph"
							disabled
						/>
					</div>
				</form>
				<div class="flex justify-center">
					<button
						@click="(modalOTPActive = true), (modalActive = false)"
						class="rounded-full text-xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue justify-center"
					>
						Send OTP
					</button>
				</div>
			</div>
		</div>
		<div
			v-show="modalOTPActive"
			class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
		>
			<div
				v-if="modalOTPActive"
				class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-36"
			>
				<span
					@click="modalOTPActive = false"
					class="flex material-icons-outlined justify-end"
					>close</span
				>
				<h1
					class="flex justify-center text-4xl sm:text-7xl text-prime font-bebas-neue my-5"
				>
					ENTER ONE TIME PIN
				</h1>
				<p
					class="flex justify-center text-sm sm:text-lg my-5 mb-7 sm:my-7 px-7 sm:px-20 font-montserrat text-center"
				>
					Enter the pin sent to your email for verification
				</p>
				<form>
					<div class="flex mb-6 text-4xl text-center sm:px-28">
						<input
							v-model="input1"
							@input="moveFocus($event, 'input2')"
							@keydown.backspace="moveBack($event, 'input0')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input1"
						/>
						<input
							v-model="input2"
							@input="moveFocus($event, 'input3')"
							@keydown.backspace="moveBack($event, 'input1')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input2"
						/>
						<input
							v-model="input3"
							@input="moveFocus($event, 'input4')"
							@keydown.backspace="moveBack($event, 'input2')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input3"
						/>
						<input
							v-model="input4"
							@input="moveFocus($event, 'input5')"
							@keydown.backspace="moveBack($event, 'input3')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input4"
						/>
						<input
							v-model="input5"
							@input="moveFocus($event, 'input6')"
							@keydown.backspace="moveBack($event, 'input4')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input5"
						/>
						<input
							v-model="input6"
							@keydown.backspace="moveBack($event, 'input5')"
							type="text"
							maxlength="1"
							class="text-prime text-center sm:text-5xl mx-1 px-5 py-3 rounded-xl w-full bg-field"
							ref="input6"
						/>
					</div>
				</form>
				<div class="flex justify-center">
					<button
						@click="
							(modalOTPActive = false), (modalChangeActive = true)
						"
						class="rounded-full text-2xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue"
					>
						Verify
					</button>
				</div>
			</div>
		</div>
		<div
			v-show="modalChangeActive"
			class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
		>
			<div
				v-if="modalChangeActive"
				class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-36"
			>
				<span
					@click="modalChangeActive = false"
					class="flex material-icons-outlined justify-end"
					>close</span
				>
				<h1
					class="flex text-4xl sm:text-7xl text-prime font-bebas-neue my-5 justify-center"
				>
					Change Password
				</h1>
				<form>
					<div class="flex-col mb-6 px-5 sm:px-28">
						<label
							for="password"
							class="flex ms-3 mb-2 text-sm font-bold text-prime justify-start"
							>Old Password</label
						>
						<input
							type="password"
							id="password"
							class="sm:mb-10 text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
							placeholder="christina.tecson@sdca.edu.ph"
							disabled
						/>
						<label
							for="newpassword"
							class="flex ms-3 mb-2 text-sm font-bold text-prime justify-start"
							>New Password</label
						>
						<input
							type="password"
							id="newpassword"
							class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
							placeholder="christina.tecson@sdca.edu.ph"
							disabled
						/>
					</div>
				</form>
				<div class="flex justify-center">
					<button
						@click="modalInvalidActive = true"
						class="rounded-full text-xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue justify-center"
					>
						Confirm
					</button>
				</div>
			</div>
		</div>
		<div
			v-show="modalInvalidActive"
			class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
		>
			<div
				v-if="modalInvalidActive"
				class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-52"
			>
				<span
					@click="modalInvalidActive = false"
					class="flex material-icons-outlined justify-end"
					>close</span
				>
				<h1
					class="flex text-4xl sm:text-7xl text-prime font-bebas-neue my-5 justify-center"
				>
					invalid one time pin
				</h1>
				<p
					class="flex justify-center text-sm sm:text-lg my-5 mb-20 sm:my-7 px-7 sm:px-28 font-montserrat text-center"
				>
					It seems like you entered the wrong pin. Please try again.
				</p>
			</div>
		</div>
	</section>
</template>

<script>
import axios from "axios";
import { useDark, useToggle } from "@vueuse/core";
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
			modalActive: false,
			modalOTPActive: false,
			modalChangeActive: false,
			modalInvalidActive: false,
			input1: "",
			input2: "",
			input3: "",
			input4: "",
			input5: "",
			input6: "",
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
				window.scrollTo(0, 0);
				router.push({ name: "dashboard" }).then(() => {
					window.location.reload();
				});
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

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
								// localStorage.setItem(
								// 	"username",
								// 	response.data.user.username
								// );
								document.cookie =
									"name=value; SameSite=Lax; Secure";
								console.log("logged in!");
								window.scrollTo(0, 0);
								router.push({ name: "dashboard" }).then(() => {
									window.location.reload();
								});
							});
					})
					.catch((error) => {
						console.log("ERROR: ", error);
						// showRegisterModal.value = true;
						// registerSuccess.value = false;
					});
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

					window.scrollTo(0, 0);

					router.push({ name: "dashboard" }).then(() => {
						window.location.reload();
					});
				})
				.catch((error) => {});
		};

		const submitLogout = () => {
			client.post("/api/logout").then((res) => {
				console.log("Logged out user:", res.data);
			});
		};

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

			isDark,
			toggleDark,
		};
	},

	methods: {
		toggleModal() {
			this.modalActive = !this.modalActive;
		},
		toggleChangeModal() {
			this.modalChangeActive = !this.modalChangeActive;
		},
		moveFocus(event, nextInput) {
			if (event.target.value.length === 1) {
				this.$refs[nextInput].focus();
			}
		},
		moveBack(event, prevInput) {
			if (event.target.value.length === 0 && prevInput !== "input1") {
				this.$refs[prevInput].focus();
			}
		},
	},
	mounted() {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");
</style>
