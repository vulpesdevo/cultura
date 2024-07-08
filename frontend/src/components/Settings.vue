<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-8 py-2 sm:ml-64 overflow-auto h-screen bg-field dark:bg-dark-notif pt-[4.5rem] sm:pt-7 px-2"
	>
		<div
			class="flex-col justify-start w-full text-prime  bg-[#E8E8E8] dark:bg-dark-interface p-7 mb-5 sm:mb-10 sm:p-7 sm:px-20 rounded-3xl"
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
				<h1 class="text-xl sm:text-2xl ms-2 sm:ms-4 " :class="isDark ? 'font-normal' : 'font-bold'">
					Profile
				</h1>
				
			</div>

			<div class="relative mt-10 mb-5">
				<h6 class="mb-0">
					<button
						class="border-slate-100 dark:border-dark-second-dark  text-slate-700 rounded-t-1 group relative flex w-full cursor-pointer items-center border-b border-solid sm:p-2 text-left font-semibold text-dark-500 transition-all ease-in dark:text-dark-prime"
						@click="toggleAccordion('profile')"
					>
						<h1
							class="text-prime font-montserrat text-lg sm:text-xl font-normal sm:font-bold sm:ms-[2.85rem] ms-0 dark:text-dark-prime"
						>
							Profile Information
						</h1>
						<i
							:class="[
								'toggle-icon absolute right-0 pt-1 text-base transition-transform fa',
								profileIsOpen
									? 'fa-chevron-up'
									: 'fa-chevron-down',
							]"
						></i>
					</button>
				</h6>
				<transition
					@before-enter="beforeEnter"
					@enter="enter"
					@before-leave="beforeLeave"
					@leave="leave"
				>
					<div
						v-if="profileIsOpen"
						class="overflow-hidden transition-all duration-300 ease-in-out"
					>
						<div class="sm:ms-32 sm:pe-28 pt-5 text-prime">
							<form>
								<div class="mb-6">
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime "
										>Username</label
									>
									<input
										type="email"
										id="email"
										class="text-prime  text-sm rounded-3xl w-full p-2.5 pl-6 bg-field dark:bg-dark-second-dark"
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
										id="email"
										class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field dark:bg-dark-second-dark"
										placeholder="john.doe@company.com"
										
									/>
								</div>
								<div class="mb-6">
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
										>Password</label
									>
									<input
										type="email"
										id="email"
										class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field dark:bg-dark-second-dark"
										placeholder="**************"
										
									/>
								</div>
								<div class="mb-6">
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
										>Country</label
									>
									<input
										type="email"
										id="email"
										class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field dark:bg-dark-second-dark"
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
				</transition>
			</div>

			<div class="relative mb-3">
				<h6 class="mb-0">
					<button
						class="border-slate-100 dark:border-dark-second-dark text-slate-700 rounded-t-1 group relative flex w-full cursor-pointer items-center border-b border-solid sm:p-2 text-left font-semibold text-dark-500 transition-all ease-in dark:text-dark-prime"
						@click="toggleAccordion('chngpass')"
					>
						<h1
							class="text-prime font-montserrat text-lg sm:text-xl font-normal sm:font-bold sm:ms-[2.85rem] dark:text-dark-prime"
						>
							Change Password
						</h1>
						<i
							:class="[
								'toggle-icon absolute right-0 pt-1 text-base transition-transform fa',
								chgPassIsOpen
									? 'fa-chevron-up'
									: 'fa-chevron-down',
							]"
						></i>
					</button>
				</h6>
				<transition
					@before-enter="beforeEnter"
					@enter="enter"
					@before-leave="beforeLeave"
					@leave="leave"
				>
					<div
						v-if="chgPassIsOpen"
						class="overflow-hidden transition-all duration-300 ease-in-out"
					>
						<div class="sm:ms-32 sm:pe-28 pt-5 text-prime">
							<form>
								<div
									class="mb-6 flex justify-between items-center"
								>
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
										>Old Password</label
									>
									<input
										type="email"
										id="email"
										class="text-prime text-sm rounded-3xl w-3/4 h-10 pl-6 bg-field dark:bg-dark-second-dark"
										placeholder="**************"
										
									/>
								</div>
								<div
									class="mb-6 flex justify-between items-center"
								>
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime dark:text-dark-prime"
										>New Password</label
									>
									<input
										type="email"
										id="email"
										class="text-prime text-sm rounded-3xl w-3/4 h-10 pl-6 bg-field dark:bg-dark-second-dark"
										placeholder="**************"
										
									/>
								</div>
								<div
									class="mb-6 flex justify-between items-center"
								>
									<label
										for="email"
										class="block mb-2 text-sm font-medium text-prime  dark:text-dark-prime"
										>Confirm New Password</label
									>
									<input
										type="email"
										id="email"
										class="text-prime text-sm rounded-3xl w-3/4 h-10 pl-6 bg-field dark:bg-dark-second-dark"
										placeholder="**************"
										
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
				</transition>
			</div>

			<div
				class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7 mb-3 sm:mb-5"
			>
				<span
					class="material-icons-outlined text-2xl sm:text-3xl text-second"
					>notifications</span
				>
				<h1 class="text-xl sm:text-2xl ms-2 sm:ms-4 dark:text-dark-prime " :class="isDark ? 'font-normal' : 'font-bold'">
					Notifications
				</h1>
			</div>
			<h1
				class="text-[#887D7D] dark:text-dark-prime font-montserrat text-sm mb-3 sm:text-xl sm:ms-14 sm:mb-6"
			>
				Customize where you want your notifications to show up.
			</h1>
			<div class="flex-col w-full">
				<!-- test -->
				<!-- <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-14 sm:mb-7">In-app Notifications</span> -->
				<div class="flex sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime font-montserrat text-lg sm:text-xl sm:ms-[3.5rem] mb-1"
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
									class="block h-7 rounded-full box bg-field dark:bg-dark-second-dark w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedInApp,
									}"
									class="absolute flex items-center justify-center w-5 h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime  font-montserrat text-lg sm:text-xl sm:ms-[3.5rem] mb-1"
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
									class="block h-7 rounded-full box bg-field dark:bg-dark-second-dark w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedBanner,
									}"
									class="absolute flex items-center justify-center w-5 h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime  font-montserrat text-lg sm:text-xl sm:ms-[3.5rem] mb-1"
								>Vibration</span
							>
							<div class="relative">
								<input
									type="checkbox"
									class="sr-only"
									@change="handleCheckboxChangeVibration"
								/>
								<div
									:class="{ '!bg-second': isCheckedVibration }"
									class="block h-7 rounded-full box bg-field dark:bg-dark-second-dark w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedVibration,
									}"
									class="absolute flex items-center justify-center w-5 h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
								></div>
							</div>
						</div>
					</label>
				</div>
				<div class="flex sm:mb-4">
					<label
						class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
					>
						<div class="flex w-full justify-between">
							<span
								class="text-prime dark:text-dark-prime  font-montserrat text-lg mb-3 sm:text-xl sm:ms-[3.5rem] sm:mb-7"
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
									class="block h-7 rounded-full box bg-field dark:bg-dark-second-dark w-12"
								></div>
								<div
									:class="{
										'translate-x-full !bg-primary dark:!bg-white !bg-white':
											isCheckedSound,
									}"
									class="absolute flex items-center justify-center w-5 h-5 transition bg-second rounded-full dot left-1 top-1 dark:bg-dark-5"
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
				<h1 class="text-xl sm:text-2xl ms-2 sm:ms-4 dark:text-dark-prime  " :class="isDark ? 'font-normal' : 'font-bold'">
					Theme
				</h1>
			</div>
			<h1
				class="text-[#887D7D]  dark:text-dark-prime  font-montserrat text-sm mb-3 sm:text-xl sm:ms-14 sm:mb-10"
			>
				Customize how you want CulturaLink to look like on your device
			</h1>
			<div class="flex sm:mb-4">
				<label
					class="flex w-full sm:w-4/5 justify-end items-center cursor-pointer select-none text-dark dark:text-white"
				>
					<div class="flex w-full justify-between">
						<span
							class="text-prime  dark:text-dark-prime  font-montserrat text-lg sm:text-xl sm:ms-[3.5rem] mb-1"
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
								class="block h-7 rounded-full box bg-field dark:bg-dark-second-dark w-12"
							></div>
							<div
								:class="{
									'translate-x-full bg-primary dark:bg-white':
										isDark,
								}"
								class="absolute flex items-center justify-center w-5 h-5 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5"
							></div>
						</div>
					</div>
				</label>
			</div>
		</div>
		<footer>
			<div
				class="flex flex-col mb-10 sm:mb-0 bg-prime w-screen sm:w-full"
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
import { useDark,useToggle } from "@vueuse/core";
import { ref } from "vue";
export default {
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);
		
		return { isDark,toggleDark };
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
			// Initial state of the accordion
		};
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
	},
	methods: {
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
				this.settings = response.data;
				this.isCheckedInApp = this.settings[0].in_app_notification;
				this.isCheckedBanner = this.settings[0].banner_notification;
				this.isCheckedVibration = this.settings[0].vibration;
				this.isCheckedSound = this.settings[0].sound;
				this.isCheckedTheme = this.settings[0].theme;
				console.log(this.settings);
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
