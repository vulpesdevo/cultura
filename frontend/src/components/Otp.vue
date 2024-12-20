<template>
	<div
		class="min-h-screen bg-gray-900 flex justify-center items-center absolute w-full top-0 left-0 px-4 sm:px-6 lg:px-8 z-50"
	>
		<div
			class="w-full max-w-md sm:max-w-lg md:max-w-xl lg:max-w-2xl rounded-lg p-4 sm:p-6 md:p-8 bg-interface dark:bg-dark-interface"
		>
			<h1
				class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold text-center mb-4 flex justify-center text-prime dark:text-interface font-bebas-neue my-5"
			>
				ENTER ONE TIME PIN
			</h1>
			<p
				class="text-center text-gray-400 mb-6 text-sm sm:text-base md:text-lg"
			>
				Enter the pin sent to your email for verification
			</p>

			<div
				class="flex mb-6 text-2xl sm:text-3xl md:text-4xl text-center justify-center space-x-2 sm:space-x-4"
			>
				<input
					v-for="(input, index) in inputs"
					:key="index"
					type="text"
					inputmode="numeric"
					maxlength="1"
					class="w-10 h-12 sm:w-12 sm:h-14 md:w-14 md:h-16 lg:w-16 lg:h-18 text-center font-extrabold text-slate-900 bg-slate-200 border border-transparent hover:border-slate-200 appearance-none rounded p-2 sm:p-3 md:p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100"
					:class="{
						'outline-red-500': error,
						'outline-none': input !== '',
					}"
					v-model="inputs[index]"
					@input="handleInput($event, index)"
					@keydown="handleKeyDown($event, index)"
					:ref="
						(el) => {
							if (el) inputRefs[index] = el;
						}
					"
				/>
			</div>

			<!-- Verify and Resend Buttons -->
			<div class="flex justify-center space-x-4">
				<button
					@click="verifyOTP('register')"
					class="rounded-full text-xl sm:text-2xl md:text-3xl text-white mt-3 mb-6 bg-second py-2 px-6 sm:py-3 sm:px-8 md:py-4 md:px-10 font-bebas-neue transition duration-300 ease-in-out hover:bg-opacity-90 flex items-center justify-center"
				>
					<CheckCircleIcon class="h-6 w-6 mr-2" />
					VERIFY
				</button>
				<button
					@click="resendOTP"
					:disabled="isResending"
					class="rounded-full text-xl sm:text-2xl md:text-3xl text-white mt-3 mb-6 bg-gray-600 py-2 px-6 sm:py-3 sm:px-8 md:py-4 md:px-10 font-bebas-neue transition duration-300 ease-in-out hover:bg-opacity-90 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
				>
					<template v-if="!isResending">
						<ArrowPathIcon class="h-6 w-6 mr-2" />
						RESEND
					</template>
					<template v-else>
						<ArrowPathIcon class="h-6 w-6 mr-2 animate-spin" />
						RESENDING...
					</template>
				</button>
			</div>
		</div>
		<Snackbar
			:show="showSnackbar"
			:message="snackbarMessage"
			:type="snackbarType"
			@close="showSnackbar = false"
		/>
	</div>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";
import Snackbar from "./snackbars/Snackbar.vue";
import {
	CheckCircleIcon,
	ArrowPathIcon,
	ClockIcon,
} from "@heroicons/vue/24/solid";

import axiosClient from "../axios";
const store = useStore();
const router = useRouter();
const route = useRoute();

const inputs = ref(new Array(6).fill(""));
const inputRefs = reactive([]);
const error = ref(false);
const isResending = ref(false);

const email = ref(route.query.email);
const fullname = ref(route.query.rname);
const country = ref(route.query.rcountry);
const rusername = ref(route.query.rusername);
const rpassword = ref(route.query.rpassword);

const otp = computed(() => store.state.otpData);

const verifyOTP = async (modal) => {
	if (modal === "register") {
		if (otp.value === parseInt(inputs.value.join(""))) {
			try {
				const userData = {
					email: email.value,
					fullname: fullname.value,
					country: country.value,
					username: rusername.value,
					password: rpassword.value,
				};

				// Register the user
				const registrationResponse = await store.dispatch(
					"register",
					userData
				);

				// Login the user after successful registration
				const loginCredentials = {
					username: rusername.value,
					password: rpassword.value,
				};
				const loginResponse = await store.dispatch(
					"login",
					loginCredentials
				);

				// window.scrollTo(0, 0);
				router.push({ name: "dashboard" });
				// Consider using a toast notification library for better UX
				showMessage(
					`Registered and logged in successfully as ${rusername.value}`,
					"success"
				);
			} catch (error) {
				console.error("ERROR:", error);
				if (error.response && error.response.data) {
					showMessage(
						`An error occurred: ${
							error.response.data.message || "Unknown error"
						}`
					);
				} else {
					showMessage(
						"An error occurred during registration or login"
					);
				}
			}
		} else {
			error.value = true;

			showMessage("Invalid OTP. Please try again.");
		}
	} else if (modal === "forgot-password") {
		if (otp.value === parseInt(inputs.value.join(""))) {
			showMessage(
				"OTP verified. You can now reset your password.",
				"success"
			);
		} else {
			error.value = true;
			showMessage("Wrong one-time password. Please try again.");
		}
	}
};

const handleInput = (event, index) => {
	const input = event.target;
	let value = input.value;

	// Ensure the input is a number and only one character
	value = value.replace(/[^0-9]/g, "").slice(0, 1);
	inputs.value[index] = value;

	// Move to next input if current is filled
	if (value !== "" && index < inputs.value.length - 1) {
		inputRefs[index + 1].focus();
	}

	// Trigger verification if all inputs are filled
	if (inputs.value.every((input) => input !== "")) {
		verifyOTP("register");
	}
};

const handleKeyDown = (event, index) => {
	// Handle backspace
	if (event.key === "Backspace" && index > 0 && inputs.value[index] === "") {
		inputRefs[index - 1].focus();
	}
};

const resendOTP = async () => {
	isResending.value = true;
	try {
		const response = await store.dispatch("sendOtp", {
			email: email.value,
			username: rusername.value,
		});
		showMessage(`OTP sent successfully to ${email.value}`, "success");
	} catch (error) {
		console.error("Error resending OTP:", error);
		showMessage("Failed to resend OTP. Please try again.");
	} finally {
		isResending.value = false;
	}
};

// Snackbar state
const showSnackbar = ref(false);
const snackbarMessage = ref("");
const snackbarType = ref("error");
const showMessage = (message, type = "error") => {
	snackbarMessage.value = message;
	snackbarType.value = type;
	showSnackbar.value = true;
	setTimeout(() => {
		showSnackbar.value = false;
	}, 5000); // Hide after 5 seconds
};
</script>
