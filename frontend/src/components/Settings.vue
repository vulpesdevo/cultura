<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-8 py-2 sm:ml-64 overflow-auto h-screen bg-field dark:bg-dark-notif pt-[4.5rem] sm:pt-7 px-2"
	>
		<div
			class="flex-col justify-start w-full text-prime bg-[#E8E8E8] dark:bg-dark-interface p-7 mb-5 sm:mb-10 sm:p-7 sm:px-20 rounded-3xl"
		>
			<h1
				class="flex justify-center text-3xl sm:text-5xl text-prime dark:text-dark-prime font-bebas-neue"
			>
				General Settings
			</h1>
			<div
				class="flex items-center w-full font-montserrat text-prime dark:text-dark-prime mt-4 sm:mt-7 mb-3"
			>
				<span
					class="material-icons-outlined text-2xl sm:text-3xl text-second"
					>account_circle</span
				>
				<h1
					class="text-xl sm:text-2xl ms-2 sm:ms-4"
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
						<span class="text-sm sm:text-lg"
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
							<div class="mb-6 mt-5">
								<label
									for="username"
									class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Username</label
								>
								<input
									type="text"
									id="setusername"
									v-model="setusername"
									class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field outline-none dark:bg-dark-second-dark dark:text-interface"
									placeholder="John"
								/>
							</div>
							<div class="mb-6">
								<label
									for="email"
									class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Email address</label
								>
								<input
									type="email"
									id="setemail"
									v-model="setemail"
									class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 outline-none bg-field dark:bg-dark-second-dark dark:text-interface"
									placeholder="john.doe@company.com"
								/>
							</div>

							<div class="mb-6">
								<label
									for="country"
									class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
									>Country</label
								>
								<input
									type="text"
									id="setcountry"
									v-model="setcountry"
									ref="setautocompletecountry"
									class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 outline-none bg-field dark:bg-dark-second-dark dark:text-interface"
									placeholder="United States"
								/>
							</div>
							<div class="flex justify-end mb-10 sm:mt-10">
								<button
									class="bg-[#7F7979] rounded-3xl text-white px-3 sm:px-6 py-2 sm:py-3"
								>
									Cancel
								</button>
								<button
									class="bg-second rounded-3xl text-white ml-6 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3"
								>
									Edit/Save
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
						<span class="text-sm sm:text-lg">Change Password</span>
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
							<div class="mb-6 mt-5 flex justify-between items-center">
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
											{ 'outline-red-600': oldPasswordInvalid }
										]"
										placeholder="Old Password"
										required
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
												v-if="hasCapitalLetter"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasSymbol"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasNumber"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasMinLength"
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
									class="bg-[#7F7979] rounded-3xl text-white px-3 sm:px-6 py-2 sm:py-3"
								>
									Cancel
								</button>
								<input
									type="submit"
									value="Save"
									@click.prevent="changePassword"
									:class="[
										!isValidNewPassword ||
										!isValidConfirmPassword
											? 'cursor-not-allowed'
											: 'cursor-pointer',
										'bg-second rounded-3xl text-white ml-6 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3',
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

			<div
				class="flex items-center w-full font-montserrat text-prime mt-7 mb-3 sm:mb-5"
			>
				<span
					class="material-icons-outlined text-2xl sm:text-3xl text-second"
					>notifications</span
				>
				<h1
					class="text-xl sm:text-2xl ms-2 sm:ms-4 dark:text-dark-prime"
					:class="isDark ? 'font-normal' : 'font-bold'"
				>
					Notifications
				</h1>
			</div>
			<h1
				class="text-[#887D7D] dark:text-dark-second-dark font-montserrat text-sm mb-3 sm:text-xl sm:ms-14 sm:mb-6"
			>
				Customize where you want your notifications to show up.
			</h1>
			<div class="flex-col w-full">
				<!-- test -->
				<!-- <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-14 sm:mb-7">In-app Notifications</span> -->
				<div class="flex mb-2 sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime font-montserrat text-sm sm:text-xl sm:ms-[3.5rem] mb-1"
								>In-App Notifications</span
							>
							<div class="relative">
								<input
									type="checkbox"
									class="sr-only"
									@change="handleCheckboxChangeInApp"
								/>
								<div
									:class="{ '!bg-second': isCheckedInApp }"
									class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedInApp,
									}"
									class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex mb-2 sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime font-montserrat text-sm sm:text-xl sm:ms-[3.5rem] mb-1"
								>Banner Notifications</span
							>
							<div class="relative">
								<input
									type="checkbox"
									class="sr-only"
									@change="handleCheckboxChangeBanner"
								/>
								<div
									:class="{ '!bg-second': isCheckedBanner }"
									class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedBanner,
									}"
									class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex mb-2 sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime font-montserrat text-sm sm:text-xl sm:ms-[3.5rem] mb-1"
								>Vibration</span
							>
							<div class="relative">
								<input
									type="checkbox"
									class="sr-only"
									@change="handleCheckboxChangeVibration"
								/>
								<div
									:class="{
										'!bg-second': isCheckedVibration,
									}"
									class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedVibration,
									}"
									class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex mb-2 sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime font-montserrat text-sm mb-3 sm:text-xl sm:ms-[3.5rem] sm:mb-7"
								>Sound</span
							>
							<div class="relative">
								<input
									type="checkbox"
									class="sr-only"
									@change="handleCheckboxChangeSound"
								/>
								<div
									:class="{ '!bg-second': isCheckedSound }"
									class="block h-6 sm:h-7 rounded-full box bg-field dark:bg-dark-second-dark w-10 sm:w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedSound,
									}"
									class="absolute flex items-center justify-center w-4 h-4 sm:w-5 sm:h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
			</div>
			<div
				class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7 mb-3 sm:mb-5"
			>
				<span
					class="material-icons-outlined text-2xl sm:text-3xl text-second"
					>contrast</span
				>
				<h1
					class="text-xl sm:text-2xl ms-2 sm:ms-4 dark:text-dark-prime"
					:class="isDark ? 'font-normal' : 'font-bold'"
				>
					Theme
				</h1>
			</div>
			<h1
				class="text-[#887D7D] dark:text-dark-second-dark font-montserrat text-sm mb-3 sm:text-xl sm:ms-14 sm:mb-10"
			>
				Customize how you want CulturaLink to look like on your device
			</h1>
			<div class="flex sm:mb-4">
				<label
					class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
				>
					<div class="flex w-full justify-between">
						<span
							class="text-prime dark:text-dark-prime font-montserrat text-sm sm:text-xl sm:ms-[3.5rem] mb-1"
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
						<span
							class="material-icons-outlined sm:ml-3 text-second text-3xl sm:text-7xl"
							>account_circle</span
						>
						<span
							class="material-icons-outlined sm:ml-5 text-second text-3xl sm:text-7xl"
							>email</span
						>
						<span
							class="material-icons-outlined sm:ml-5 text-second text-3xl sm:text-7xl"
							>call</span
						>
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

<script>
import axios from "axios";
import { useDark, useToggle } from "@vueuse/core";
import { ref, onMounted } from "vue";
export default {
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);
		const accordionOpen = ref(false);
		const changePassOpen = ref(false);
		onMounted(() => {
			accordionOpen.value = false;
			changePassOpen.value = false;
		});
		return { isDark, toggleDark, accordionOpen, changePassOpen };
	},
	data() {
		return {
			profileIsOpen: false,
			chgPassIsOpen: false,
			isCheckedInApp: false,
			isCheckedBanner: false,
			isCheckedVibration: false,
			isCheckedSound: false,
			isCheckedTheme: false,
			settings: [],

			new_password: "",
			old_password: "",
			confirm_password: "",
			showOldPassword: false,
			showNewPassword: false,
			showConfirmPassword: false,
			hasCapitalLetter: false,
			hasSymbol: false,
			hasNumber: false,
			hasMinLength: false,

			oldPasswordInvalid: false,
			error:null,
			timer: null,

			setusername: "",
			setemail: "",
			setcountry: "",
			inputElement: null,
			// Initial state of the accordion
		};
	},
	computed: {
		isValidNewPassword() {
			const password = this.new_password;
			this.hasCapitalLetter = /[A-Z]/.test(password);
			this.hasSymbol = /[!@#$%^&*(),.?":{}|<>]/.test(password);
			this.hasNumber = /\d/.test(password);
			this.hasMinLength = password.length >= 8;
			return (
				this.hasCapitalLetter &&
				this.hasSymbol &&
				this.hasNumber &&
				this.hasMinLength
			);
		},
		isValidConfirmPassword() {
			return this.confirm_password === this.new_password;
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
		this.getClientSettings();
		this.initializeAutocompleteCountry();
	},
	mounted() {
		this.initializeAutocompleteCountry();
	},
	methods: {
		changePassword() {
			this.client
				.post("/api/change-password", {
					password: this.old_password,
					new_password: this.new_password,
				})
				.then((res) => {
					console.log("Changed:", res.data);
					const toast = document.createElement("div");
					toast.id = "toast-simple";
					toast.className = "flex items-center justify-center w-full max-w-xs p-4 space-x-4 rtl:space-x-reverse text-green-700 bg-white divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow dark:text-green-700 dark:divide-gray-700 dark:bg-gray-800";
					toast.setAttribute("role", "alert");
					
					
					
					const message = document.createElement("div");
					message.className = "text-sm text-center font-normal";
					message.textContent = "Change password successfully.";
					
					
					toast.appendChild(message);
					
					const toastContainer = document.createElement("div");
					toastContainer.className = "fixed bottom-10 right-4 sm:bottom-4 sm:right-2 sm:transform sm:-translate-x-1/2";
					
					if (window.innerWidth <= 641) {
						toastContainer.className = "fixed bottom-16 left-1/2 transform -translate-x-1/2";
					}
					
					toastContainer.appendChild(toast);
					document.body.appendChild(toastContainer);
					
					setTimeout(() => {
						toastContainer.remove();
					}, 5000);
				
				})
				.catch((error) => {
					console.log("ERROR", error);
					console.log("Error message:", error.message);
					console.log("Error code:", error.code);
					console.log("Response data:", error.response.data.error);
					this.oldPasswordInvalid = true;
					this.error = error.response.data.error;
					this.timer = setTimeout(() => {
						this.oldPasswordInvalid = false;
					}, 5000); // 5 seconds
				});
		},
		initializeAutocompleteCountry() {
			// Ensures the DOM is updated
			// this.inputElement = this.$refs.setautocompletecountry;
			// console.log("the element :", this.inputElement);
			this.inputElement = this.$refs.setautocompletecountry;
			console.log("the elemento :", this.inputElement);
			const autocomplete = new google.maps.places.Autocomplete(
				this.inputElement,
				{
					types: ["(regions)"],
				}
			);

			// getting the value of
			autocomplete.addListener("place_changed", () => {
				const country = autocomplete.getPlace();
				this.setcountry = country.formatted_address;
			});
		},
		handleCheckboxChangeInApp() {
			this.isCheckedInApp = !this.isCheckedInApp;
			this.getSettings();
		},
		handleCheckboxChangeBanner() {
			this.isCheckedBanner = !this.isCheckedBanner;
			this.getSettings();
		},
		handleCheckboxChangeVibration() {
			this.isCheckedVibration = !this.isCheckedVibration;
			this.getSettings();
		},
		handleCheckboxChangeSound() {
			this.isCheckedSound = !this.isCheckedSound;
			this.getSettings();
		},
		handleCheckboxChangeTheme() {
			this.isCheckedTheme = !this.isCheckedTheme;
			this.getSettings();
		},
		getSettings() {
			this.client
				.post("/api/user-settings", {
					in_app_notif: this.isCheckedInApp,
					banner_notif: this.isCheckedBanner,
					vibration: this.isCheckedVibration,
					sound: this.isCheckedSound,
					theme: this.isCheckedTheme,
				})
				.then((res) => {
					console.log("Changed:", res.data);
				})
				.catch((error) => {
					console.log("ERROR", error);
				});
		},
		async getClientSettings() {
			try {
				const response = await this.client.get("/api/user-settings");
				this.settings = response.data.set;
				this.isCheckedInApp = this.settings[0].in_app_notification;
				this.isCheckedBanner = this.settings[0].banner_notification;
				this.isCheckedVibration = this.settings[0].vibration;
				this.isCheckedSound = this.settings[0].sound;
				this.isCheckedTheme = this.settings[0].theme;
				console.log(response.data.user_information);
			} catch (error) {
				console.error(error);
			}
		},
		toggleAccordion(accordion) {
			if (accordion === "profile") {
				this.profileIsOpen = !this.profileIsOpen;
			} else {
				this.chgPassIsOpen = !this.chgPassIsOpen;
			}
		},
		beforeEnter(el) {
			el.style.height = "0";
		},
		enter(el) {
			el.style.height = el.scrollHeight + "px";
		},
		beforeLeave(el) {
			el.style.height = el.scrollHeight + "px";
		},
		leave(el) {
			el.style.height = "0";
		},
	},
};
</script>

<style></style>
