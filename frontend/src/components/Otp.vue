<template>
	<div
		class="h-screen bg-gray-900 flex justify-center items-center absolute w-full top-0 left-0 px-8 z-50"
	>
		<div
			class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface self-start mt-36"
		>
			<h1
				class="text-4xl font-bold text-center mb-4 flex justify-center first-line:sm:text-7xl text-prime dark:text-interface font-bebas-neue my-5"
			>
				ENTER ONE TIME PIN
			</h1>
			<p class="text-center text-gray-400 mb-6">
				Enter the pin sent to your email for verification
			</p>

			<div class="flex mb-6 text-4xl text-center justify-evenly sm:px-28">
				<input
					v-for="(input, index) in inputs"
					:key="index"
					type="text"
					maxlength="1"
					class="w-12 sm:w-16 h-16 text-center text-2xl font-extrabold text-slate-900 bg-slate-200 border border-transparent hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100"
					:class="{
						'outline-red-500': error,
						'outline-none': input !== '', // add this line
					}"
					v-model="inputs[index]"
					@keyup="moveFocus($event, index)"
					@input="
						inputs[index] = $event.target.value.replace(
							/[^0-9]/g,
							''
						)
					"
					:ref="(el) => (inputsRefs[index] = el)"
				/>
			</div>

			<!-- Verify Button -->
			<div class="flex justify-center">
				<button
					@click="verifyOTP('register')"
					class="rounded-full text-2xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue"
				>
					VERIFY
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import Vue3OtpInput from "vue3-otp-input";
import { mapState } from "vuex";
export default {
	data() {
		return {
			// authentication and authorization
			otp: this.$route.query.otp,
			email: this.$route.query.email,
			fullname: this.$route.query.rname,
			country: this.$route.query.rcountry,
			rusername: this.$route.query.rusername,
			rpassword: this.$route.query.rpassword,

			input1: "", // Comment: Placeholder for the first input field
			input2: "", // Comment: Placeholder for the second input field
			input3: "", // Comment: Placeholder for the third input field
			input4: "", // Comment: Placeholder for the fourth input field
			input5: "", // Comment: Placeholder for the fifth input field
			input6: "", // Comment: Placeholder for the sixth input field

			showRePassword: false, // Comment: Controls the visibility of the re-enter password field
			showPassword: false, // Comment: Controls the visibility of the password field

			// inputs: ["", "", "", "", "", ""], // Comment: Placeholder for an array of input values
			inputs: new Array(6).fill(""), // Comment: Placeholder for an array of input values with a length of 6
			inputsRefs: [], // Comment: Placeholder for an array of input field references

			error: false, // Comment: Indicates whether an error occurred
			error_user: false, // Comment: Indicates whether there is an error related to the user
			error_email: false, // Comment: Indicates whether there is an error related to the email// To store the OTP value
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

		this.url = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});
	},
	computed: {
		...mapState(["otp"]),
	},
	methods: {
		verifyOTP(modal) {
			console.log(this.otp);
			if (modal == "register") {
				if (this.otp === parseInt(this.inputs.join(""))) {
					this.url
						.post("/api/registration", {
							email: this.email,
							fullname: this.rname,
							country: this.rcountry,
							username: this.rusername,
							password: this.rpassword,
						})
						.then((response) => {
							this.url
								.post("/api/login", {
									username: this.rusername,
									password: this.rpassword,
								})
								.then((response) => {
									this.showModal = false;
									this.modalOTPActive = false;
									const token = response.data.token; // Replace with your token
									localStorage.setItem("token", token);
									// localStorage.setItem(
									//  "username",
									//  response.data.user.username
									// );
									document.cookie =
										"name=value; SameSite=Lax; Secure";
									console.log("logged in!");
									window.scrollTo(0, 0);
									this.$router
										.push({ name: "dashboard" })
										.then(() => {
											window.location.reload();
										});
								});
							this.createToast(
								`Logged in as\n${this.rusername}`,
								"success"
							);
						})
						.catch((error) => {
							console.log("ERROR: ", error);
							// showRegisterModal.value = true;
							// registerSuccess.value = false;
						});
				} else {
					this.error = true;
					console.log(
						this.otp,
						" failed to verify the ",
						parseInt(this.inputs.join(""))
					);
				}
			}
			if (modal == "forgot-password") {
				console.log(parseInt(this.inputs.join("")));
				if (this.otp === parseInt(this.inputs.join(""))) {
					this.fpmodalOTPActive = false;
					this.modalChangeActive = true;
				} else {
					this.error = true;
					this.createToast("Wrong one-time password", "error");
				}
			}
		},
		moveFocus(event, index) {
			if (event.key.match(/^[0-9]$/)) {
				if (index < this.inputs.length - 1) {
					this.inputsRefs[index + 1].focus();
				}
			} else if (event.keyCode === 8) {
				// backspace key
				if (index > 0) {
					this.inputsRefs[index - 1].focus();
				}
			}
		},
	},
};
</script>

<style scoped></style>
