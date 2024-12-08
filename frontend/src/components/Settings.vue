<template>
	<div
		class="flex flex-col items-center just align-middle w-full sm:px-8 py-2 overflow-x-hidden h-screen bg-field dark:bg-dark-notif sm:pt-7 px-2"
	>
		<div
			class="flex flex-col justify-start w-full text-prime bg-[#E8E8E8] dark:bg-dark-interface p-7 mb-5 sm:mb-10 sm:p-7 sm:px-20 rounded-3xl"
		>
			<h1
				class="flex justify-center text-3xl sm:text-5xl text-prime dark:text-dark-prime font-bebas-neue"
			>
				General Settings
			</h1>
			<div
				class="flex items-center w-full font-montserrat text-prime dark:text-dark-prime mt-4 sm:mt-7 mb-3"
			>
				<UserCircleIcon class="size-7 text-second" />
				<h1
					class="text-sm sm:text-lg font-montserrat ml-2 dark:text-white"
					:class="isDark ? 'font-normal' : 'font-bold'"
				>
					Profile
				</h1>
			</div>

			<div class="py-2">
				<h2>
					<button
						class="font-montserrat dark:text-interface flex items-center justify-between w-full text-left py-2"
						@click.prevent="accordionOpen = !accordionOpen"
						:aria-expanded="accordionOpen"
					>
						<span class="text-xs sm:text-sm"
							>Profile Information</span
						>
						<svg
							class="fill-indigo-500 shrink-0 ml-8"
							width="16"
							height="16"
							xmlns="http://www.w3.org/2000/svg"
						>
							<rect
								y="7"
								width="16"
								height="2"
								rx="1"
								class="transform origin-center transition duration-200 ease-out"
								:class="{ '!rotate-180': accordionOpen }"
							/>
							<rect
								y="7"
								width="16"
								height="2"
								rx="1"
								class="transform origin-center rotate-90 transition duration-200 ease-out"
								:class="{ '!rotate-180': accordionOpen }"
							/>
						</svg>
					</button>
				</h2>

				<div
					role="region"
					class="grid text-sm text-slate-600 overflow-hidden transition-all duration-300 ease-in-out"
					:class="
						accordionOpen
							? 'grid-rows-[1fr] opacity-100'
							: 'grid-rows-[0fr] opacity-0'
					"
				>
					<div class="overflow-hidden">
						<form>
							<div class="relative text-left">
								<label
									for=""
									class="hidden sm:flex mb-2 text-sm font-medium text-prime dark:text-dark-prime"
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
									id="setemail"
									v-model="setemail"
									:class="[
										isGmailEmail
											? 'outline-green-400'
											: 'outline-red-400',
									]"
									class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime"
									required
									:disabled="!editing"
									placeholder="name@flowbite.com"
								/>
							</div>

							<div class="mb-6 mt-7 sm:mt-2">
								<label
									for="country"
									class="hidden sm:flex mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Country</label
								>
								<input
									type="text"
									id="setcountry"
									v-model="setcountry"
									ref="setautocompletecountry"
									class="text-prime text-sm rounded-3xl w-full p-2.5 pl-10 outline-none bg-field dark:bg-dark-second-dark dark:text-interface"
									placeholder="United States"
									:disabled="!editing"
								/>
							</div>
							<div
								class="flex items-start mt-3 mb-4"
								v-if="isGmailEmail && editing"
							>
								<label
									for=""
									class="w-1/2 text-end dark:text-dark-second-dark"
									>verify password:</label
								>
								<div class="relative w-3/4 px-1">
									<input
										:type="
											showsetPass ? 'text' : 'password'
										"
										id="setpassword"
										v-model="setpassword"
										class="text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-none"
										placeholder="Verify Password"
										required
										:disabled="!editing"
									/>
									<button
										class="absolute right-5 top-2"
										@click.prevent="
											showsetPass = !showsetPass
										"
									>
										<i
											class="fas dark:text-gray-400"
											:class="
												showsetPass
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>
							<div class="flex justify-end mb-5 sm:mt-10">
								<button
									v-if="editing"
									class="bg-[#7F7979] rounded-3xl text-white flex items-center justify-center w-16 ml-6 h-9 px-3 sm:px-6 py-2 sm:py-3"
									@click.prevent="editing = false"
								>
									Cancel
								</button>

								<button
									v-if="!editing"
									class="bg-second rounded-3xl text-white flex items-center justify-center w-16 ml-6 h-9 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3"
									@click.prevent="editing = true"
								>
									Edit
								</button>
								<button
									v-else
									class="bg-second rounded-3xl text-white flex items-center justify-center w-16 ml-6 h-9 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3"
									@click.prevent="changeInformation"
								>
									Save
								</button>
							</div>
						</form>
					</div>
				</div>
			</div>
			<div class="py-2">
				<h2>
					<button
						class="font-montserrat dark:text-interface flex items-center justify-between w-full text-left py-2"
						@click.prevent="changePassOpen = !changePassOpen"
						:aria-expanded="changePassOpen"
					>
						<span class="text-xs sm:text-sm">Change Password</span>
						<svg
							class="fill-indigo-500 shrink-0 ml-8"
							width="16"
							height="16"
							xmlns="http://www.w3.org/2000/svg"
						>
							<rect
								y="7"
								width="16"
								height="2"
								rx="1"
								class="transform origin-center transition duration-200 ease-out"
								:class="{ '!rotate-180': changePassOpen }"
							/>
							<rect
								y="7"
								width="16"
								height="2"
								rx="1"
								class="transform origin-center rotate-90 transition duration-200 ease-out"
								:class="{ '!rotate-180': changePassOpen }"
							/>
						</svg>
					</button>
				</h2>

				<div
					role="region"
					class="grid text-sm text-slate-600 overflow-hidden transition-all duration-300 ease-in-out"
					:class="
						changePassOpen
							? 'grid-rows-[1fr] opacity-100'
							: 'grid-rows-[0fr] opacity-0'
					"
				>
					<div class="overflow-hidden">
						<form>
							<div
								v-if="oldPasswordInvalid"
								id="alert-2"
								class="flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
								role="alert"
							>
								<div class="ms-3 text-sm font-medium">
									{{ error }}
								</div>
								<button
									type="button"
									class="ms-auto -mx-1.5 -my-1.5 bg-red-50 text-red-500 rounded-lg focus:ring-2 focus:ring-red-400 p-1.5 hover:bg-red-200 inline-flex items-center justify-center h-8 w-8 dark:bg-gray-800 dark:text-red-400 dark:hover:bg-gray-700"
									data-dismiss-target="#alert-2"
									aria-label="Close"
									@click="oldPasswordInvalid = false"
								>
									<span class="sr-only">Close</span>
									<svg
										class="w-3 h-3"
										aria-hidden="true"
										xmlns="http://www.w3.org/2000/svg"
										fill="none"
										viewBox="0 0 14 14"
									>
										<path
											stroke="currentColor"
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
										/>
									</svg>
								</button>
							</div>
							<div
								class="mb-6 mt-5 flex justify-between items-center"
							>
								<label
									for="old-password"
									class="hidden sm:block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Old Password</label
								>

								<div class="relative w-full sm:w-3/4 px-1">
									<input
										:type="
											showOldPassword
												? 'text'
												: 'password'
										"
										id="old-password"
										v-model="old_password"
										:class="[
											'text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-none',
											{
												'outline-red-600':
													oldPasswordInvalid,
											},
										]"
										placeholder="Old Password"
										required
										:disabled="!passediting"
									/>
									<button
										class="absolute right-5 top-2"
										@click.prevent="
											showOldPassword = !showOldPassword
										"
									>
										<i
											class="fas dark:text-gray-400"
											:class="
												showOldPassword
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>

							<div
								class="sm:mb-2 flex justify-between items-center"
							>
								<label
									for="new-password"
									class="hidden sm:block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>New Password</label
								>
								<div class="relative w-full sm:w-3/4 px-1">
									<input
										:type="
											showNewPassword
												? 'text'
												: 'password'
										"
										id="new-password"
										v-model="new_password"
										class="text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-none"
										placeholder="New Password"
										required
										:disabled="!passediting"
									/>
									<button
										class="absolute right-5 top-2"
										@click.prevent="
											showNewPassword = !showNewPassword
										"
									>
										<i
											class="fas dark:text-gray-400"
											:class="
												showNewPassword
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>
							<div
								class="flex flex-col justify-end items-end mt-0 sm:mt-1 mb-2"
							>
								<div
									class="flex w-full sm:w-3/4 h-20 dark:text-dark-second-dark"
								>
									<div
										class="flex flex-col items-end justify-evenly w-5 h-full"
									>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="
													passwordStrength.hasCapitalLetter
												"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="
													passwordStrength.hasSymbol
												"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="
													passwordStrength.hasNumber
												"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="
													passwordStrength.hasMinLength
												"
											>
												check_circle
											</span>
										</div>
									</div>
									<div
										class="flex flex-col justify-evenly h-20 items-start pt-[.45rem]"
									>
										<label
											for="has-capital-letter"
											class="ml-2 text-xs h-4"
											>has capital letter</label
										>

										<label
											for="has-symbol"
											class="ml-2 text-xs h-4"
											>has symbol</label
										>

										<label
											for="has-number"
											class="ml-2 text-xs h-4"
											>has number</label
										>

										<label
											for="has-min-length"
											class="ml-2 text-xs h-4"
											>has at least 8 characters</label
										>
									</div>
								</div>
							</div>
							<div class="mb-6 flex justify-between items-center">
								<label
									for="confirm-password"
									class="hidden sm:block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Confirm Password</label
								>
								<div class="relative w-full sm:w-3/4 px-1">
									<input
										:type="
											showConfirmPassword
												? 'text'
												: 'password'
										"
										id="confirm-password"
										v-model="confirm_password"
										class="text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-none"
										placeholder="Confirm New Password"
										required
										:disabled="!passediting"
									/>
									<button
										class="absolute right-5 top-2"
										@click.prevent="
											showConfirmPassword =
												!showConfirmPassword
										"
									>
										<i
											class="fas dark:text-gray-400"
											:class="
												showConfirmPassword
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>
							<div class="flex justify-end mb-10 sm:mt-10">
								<button
									v-if="passediting"
									class="bg-[#7F7979] rounded-3xl text-white flex items-center justify-center w-16 ml-6 h-9 px-3 sm:px-6 py-2 sm:py-3"
									@click.prevent="passediting = false"
								>
									Cancel
								</button>

								<button
									v-if="!passediting"
									class="bg-second rounded-3xl text-white flex items-center justify-center w-16 ml-6 h-9 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3"
									@click.prevent="passediting = true"
								>
									Edit
								</button>
								<input
									v-else
									type="submit"
									value="Save"
									@click.prevent="changePassword"
									:class="[
										!isValidNewPassword ||
										!isValidConfirmPassword
											? 'cursor-not-allowed'
											: 'cursor-pointer',
										'bg-second rounded-3xl text-white flex items-center justify-center  w-16 ml-6 h-9 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3',
									]"
									:disabled="
										!isValidNewPassword ||
										!isValidConfirmPassword
									"
								/>
							</div>
						</form>
					</div>
				</div>
			</div>

			<div class="flex sm:mb-4">
				<label
					class="flex w-full justify-end items-center cursor-pointer select-none text-dark dark:text-white"
				>
					<div class="flex w-full justify-between">
						<span
							class="text-prime dark:text-dark-prime font-montserrat text-xs sm:text-sm mb-1"
							>Protect your posts</span
						>
						<div class="relative">
							<input
								type="checkbox"
								class="sr-only"
								@change="onToggleChange"
								v-model="isPrivate"
							/>
							<div
								:class="{ '!bg-second': isPrivate }"
								class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
							></div>
							<div
								:class="{
									'translate-x-full !bg-primary dark:!bg-white !bg-white':
										isPrivate,
								}"
								class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
							></div>
						</div>
					</div>
				</label>
			</div>
			<div
				v-if="showModal"
				class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
			>
				<div
					class="bg-interface dark:bg-dark-field p-8 rounded-xl shadow-lg text-center space-y-4 w-[550px] h-[300px] sm:ml-32 flex flex-col justify-center"
				>
					<h3
						class="text-xl mb-2 font-montserrat text-prime dark:text-white font-bold"
					>
						{{ modalTitle }}
					</h3>
					<p class="font-montserrat text-sm dark:text-white">
						{{ modalMessage }}
					</p>
					<div class="flex space-x-4 pt-9 justify-center">
						<button
							@click="confirmPrivacy(false)"
							class="bg-gray-500 text-white px-5 py-2 rounded-full text-base font-montserrat font-bold"
						>
							Cancel
						</button>
						<button
							@click="confirmPrivacy(true)"
							class="bg-second text-white px-5 py-2 rounded-full text-base font-montserrat font-bold"
						>
							Continue
						</button>
					</div>
				</div>
			</div>
			<div
				class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7"
			>
				<SunIcon class="size-7 text-second" />
				<h1
					class="text-sm sm:text-lg font-montserrat ml-2 dark:text-white"
					:class="isDark ? 'font-normal' : 'font-bold'"
				>
					Theme
				</h1>
			</div>
			<h1
				class="text-[#887D7D] dark:text-dark-second-dark font-montserrat text-xs sm:text-sm sm:my-3"
			>
				Customize how you want CulturaLink to look like on your device
			</h1>
			<div class="flex">
				<label
					class="flex w-full justify-end items-center cursor-pointer select-none text-dark dark:text-white"
				>
					<div class="flex w-full justify-between">
						<span
							class="text-prime dark:text-dark-prime font-montserrat text-sm sm:text-sm mb-1"
							>Theme</span
						>
						<div class="relative">
							<input
								type="checkbox"
								class="sr-only"
								@change="toggleDark()"
							/>
							<div
								:class="{ '!bg-second  ': isDark }"
								class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
							></div>
							<div
								:class="{
									'translate-x-full !bg-primary dark:!bg-white !bg-white':
										isDark,
								}"
								class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
							></div>
						</div>
					</div>
				</label>
			</div>
		</div>
		<footer>
			<div
				class="flex flex-col mb-12 sm:mb-0 bg-prime dark:bg-dark-interface w-screen sm:w-full"
			>
				<div
					class="flex flex-col sm:flex-row justify-between w-full sm:px-6 py-7 pe-3"
				>
					<div
						class="flex flex-col items-center sm:items-start w-full sm:border-r-2 border-second px-4"
					>
						<img
							class="w-1/2 sm:w-96 h-auto -mt-7 sm:-mt-10"
							src="/ULTURALINK-DMLong.png"
							alt=""
						/>
						<div class="w-full -mt-5 sm:-mt-16">
							<p
								class="text-wrap w-full text-white text-[9px] text-center sm:text-justify pb-3 sm:text-xs"
							>
								CulturaLink is a dynamic platform designed to
								foster cultural exchange and travel planning
								through user-generated content and itineraries.
								This project is proudly developed by students:
								Gabrentina, Galan, and Tecson as part of their
								academic pursuit,
							</p>
						</div>
					</div>

					<div class="flex items-center justify-center w-full">
						<UserCircleIcon
							class="h-8 w-8 sm:size-10 text-second sm:ml-3"
						/>
						<EnvelopeIcon
							class="h-8 w-8 sm:size-10 text-second sm:ml-5"
						/>
						<PhoneIcon
							class="h-8 w-8 sm:size-10 text-second sm:ml-5"
						/>
					</div>
				</div>
				<div class="flex bg-second h-7 justify-center items-center">
					<h4 class="text-prime text-[12px] sm:text-sm">
						Copyright © 2024 | In Affiliation with
						<span class="text-white"
							>St Dominic College of Asia</span
						>
					</h4>
				</div>
			</div>
		</footer>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, reactive } from "vue";
import { useDark, useToggle } from "@vueuse/core";
import {
	LockClosedIcon,
	UserCircleIcon,
	SunIcon,
	EnvelopeIcon,
	PhoneIcon,
} from "@heroicons/vue/24/outline";
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();
const store = useStore();
const router = useRouter();
import axios from "axios";

const isDark = useDark();
const toggleDark = useToggle(isDark);

const accordionOpen = ref(false);
const changePassOpen = ref(false);

const setemail = ref("");
const setcountry = ref("");
const setpassword = ref("");
const old_password = ref("");
const new_password = ref("");
const confirm_password = ref("");
const showOldPassword = ref(false);
const showsetPass = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);

const setautocompletecountry = ref(null);

// PRIVACY Settings
const isPrivate = ref(false);
const showModal = ref(false);
const modalTitle = ref("");
const modalMessage = ref("");

const onToggleChange = () => {
	showModal.value = true;
	modalTitle.value = isPrivate.value
		? "Make Account Public?"
		: "Make Account Private?";
	modalMessage.value = isPrivate.value
		? "Are you sure you want to make your account public? Anyone will be able to see your posts."
		: "Are you sure you want to make your account private? Only your followers will be able to see your posts.";
};

const confirmPrivacy = async (confirm) => {
	if (confirm) {
		try {
			await store.dispatch("updatePrivacy", isPrivate.value);
			console.log("Privacy updated successfully");
			createToast(
				`Your account is now ${
					isPrivate.value ? "private" : "public"
				}.`,
				"success"
			);
		} catch (error) {
			console.error("Error updating privacy:", error);
			createToast(
				"Failed to update privacy settings. Please try again.",
				"error"
			);
			// Revert the toggle if the API call fails
			isPrivate.value = !isPrivate.value;
		}
	} else {
		// If the user cancels, revert the toggle
		isPrivate.value = !isPrivate.value;
	}
	showModal.value = false;
};

const editing = ref(false);
const passediting = ref(false);
const oldPasswordInvalid = ref(false);
const error = ref(null);

const passwordStrength = ref({
	hasCapitalLetter: false,
	hasSymbol: false,
	hasNumber: false,
	hasMinLength: false,
});

const isGmailEmail = computed(() => {
	const emailRegex = /^[A-Za-z0-9._%+-]+@gmail\.com$/;
	return emailRegex.test(setemail.value);
});

const isValidNewPassword = computed(() => {
	const password = new_password.value;
	passwordStrength.value.hasCapitalLetter = /[A-Z]/.test(password);
	passwordStrength.value.hasSymbol = /[!@#$%^&*(),.?":{}|<>]/.test(password);
	passwordStrength.value.hasNumber = /\d/.test(password);
	passwordStrength.value.hasMinLength = password.length >= 8;
	return (
		passwordStrength.value.hasCapitalLetter &&
		passwordStrength.value.hasSymbol &&
		passwordStrength.value.hasNumber &&
		passwordStrength.value.hasMinLength
	);
});

const isValidConfirmPassword = computed(() => {
	return confirm_password.value === new_password.value;
});

const client = axios.create({
	baseURL: "http://127.0.0.1:8000",
	withCredentials: true,
	timeout: 5000,
	xsrfCookieName: "csrftoken",
	xsrfHeaderName: "X-Csrftoken",
});

const changeInformation = async () => {
	try {
		const response = await client.post("/api/update-information", {
			password: setpassword.value,
			email: setemail.value,
			country: setcountry.value,
		});
		console.log("Changed:", response.data);
		createToast("Information updated successfully.", "success");
		editing.value = false;
		setpassword.value = "";
	} catch (error) {
		console.error("Error updating information:", error);
		createToast(
			error.response?.data?.error || "An error occurred",
			"error"
		);
	}
};

const changePassword = async () => {
	try {
		const response = await client.post("/api/change-password", {
			password: old_password.value,
			new_password: new_password.value,
		});
		console.log("Changed:", response.data);
		createToast("Password changed successfully.", "success");
		passediting.value = false;
		resetPasswordFields();
	} catch (error) {
		console.error("Error changing password:", error);
		oldPasswordInvalid.value = true;
		error.value = error.response?.data?.error || "An error occurred";
		setTimeout(() => {
			oldPasswordInvalid.value = false;
		}, 5000);
	}
};

const resetPasswordFields = () => {
	old_password.value = "";
	new_password.value = "";
	confirm_password.value = "";
};

const createToast = (message, type) => {
	const toast = document.createElement("div");
	toast.className = `fixed bottom-4 right-4 p-4 rounded-md text-white ${
		type === "success" ? "bg-green-500" : "bg-red-500"
	} transition-opacity duration-300 opacity-0`;
	toast.textContent = message;

	document.body.appendChild(toast);

	// Fade in
	setTimeout(() => {
		toast.classList.remove("opacity-0");
	}, 10);

	// Fade out and remove
	setTimeout(() => {
		toast.classList.add("opacity-0");
		setTimeout(() => {
			document.body.removeChild(toast);
		}, 300);
	}, 3000);
};

const initializeAutocompleteCountry = () => {
	const input = setautocompletecountry.value;
	if (!input) {
		console.error("Country input element not found");
		return;
	}

	const autocomplete = new google.maps.places.Autocomplete(input, {
		types: ["(regions)"],
	});

	autocomplete.addListener("place_changed", () => {
		const place = autocomplete.getPlace();
		if (!place.address_components) {
			console.error("No address components found");
			return;
		}

		const countryComponent = place.address_components.find((component) =>
			component.types.includes("country")
		);

		if (countryComponent) {
			setcountry.value = countryComponent.long_name;
		} else {
			console.error("Country not found in place data");
		}
	});
};

onMounted(() => {
	accordionOpen.value = false;
	changePassOpen.value = false;
	initializeAutocompleteCountry();
});
</script>

<style></style>
