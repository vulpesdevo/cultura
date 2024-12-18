<template>
	<div :class="{ dark: isDark }" class="min-h-screen w-full overflow-hidden">
		<div
			class="min-h-screen bg-white dark:bg-gray-900 transition-colors duration-300 flex flex-col"
		>
			<div class="flex-grow flex flex-col">
				<!-- Initial Modal -->
				<div
					v-show="tamModalActive"
					class="fixed inset-0 flex items-center justify-center px-4 py-12 sm:px-6 lg:px-8 bg-white dark:bg-gray-900 transition-colors duration-300"
				>
					<div
						class="w-full max-w-2xl bg-white dark:bg-gray-800 rounded-2xl shadow-xl transition-all duration-300"
					>
						<div class="p-8">
							<h1
								class="text-4xl sm:text-5xl text-blue-600 dark:text-blue-400 font-bold text-center mb-8 transition-colors"
							>
								We Could Use Your Help!
							</h1>
							<p
								class="text-gray-600 dark:text-gray-300 text-lg sm:text-xl text-center mb-8 transition-colors"
							>
								Before you go, do you have a moment to answer a
								few questions about your experience with
								CulturaLink?
							</p>
							<div class="flex justify-center space-x-6">
								<button
									@click="maybeLater"
									class="px-6 py-3 text-lg rounded-full bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 transition-all duration-300"
								>
									Maybe Later
								</button>
								<button
									@click="continueSurvey"
									class="px-6 py-3 text-lg rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-all duration-300"
								>
									Continue
								</button>
							</div>
						</div>
					</div>
				</div>

				<!-- Survey Modal -->
				<div
					v-if="tamOneActive"
					class="fixed inset-0 flex flex-col bg-white dark:bg-gray-900 transition-colors duration-300"
				>
					<div class="p-6 bg-white dark:bg-gray-800 shadow-md z-10">
						<h2
							class="text-2xl font-bold text-gray-800 dark:text-gray-200 text-center transition-colors"
						>
							CulturaLink Survey
						</h2>
						<p
							class="text-gray-600 dark:text-gray-300 text-center mt-2 transition-colors"
						>
							Please answer all questions as honestly as possible.
						</p>
					</div>

					<div class="flex-grow overflow-y-auto">
						<div class="max-w-4xl mx-auto p-6">
							<form
								@submit.prevent="submitSurvey"
								class="space-y-8"
							>
								<div
									v-for="(question, index) in questions"
									:key="index"
									class="p-6 rounded-lg bg-gray-50 dark:bg-gray-800 transition-colors shadow-md"
								>
									<p
										class="text-gray-800 dark:text-gray-200 text-lg mb-6 transition-colors"
									>
										{{ question.text }}
									</p>
									<div
										class="grid grid-cols-2 sm:grid-cols-5 gap-4"
									>
										<label
											v-for="option in options"
											:key="option"
											class="flex flex-col items-center space-y-2 cursor-pointer group"
										>
											<div class="relative">
												<input
													type="radio"
													:name="'response' + index"
													:value="option"
													v-model="responses[index]"
													required
													class="sr-only peer"
												/>
												<div
													class="w-6 h-6 rounded-full border-2 border-gray-300 dark:border-gray-500 peer-checked:border-blue-500 peer-checked:bg-blue-500 transition-all duration-300"
												></div>
												<div
													class="absolute inset-0 flex items-center justify-center opacity-0 peer-checked:opacity-100 transition-opacity duration-300"
												>
													<div
														class="w-2 h-2 rounded-full bg-white"
													></div>
												</div>
											</div>
											<span
												class="text-sm text-gray-600 dark:text-gray-400 group-hover:text-blue-500 transition-colors"
											>
												{{ option }}
											</span>
										</label>
									</div>
								</div>
							</form>
						</div>
					</div>

					<div class="p-6 bg-white dark:bg-gray-800 shadow-md z-10">
						<div class="flex justify-center items-center space-x-6">
							<router-link
								to="/"
								class="px-10 py-3 text-lg font-medium rounded-full border border-second text-second hover:border-blue-700 transition-all duration-300"
							>
								Back
							</router-link>
							<button
								@click="submitSurvey"
								class="px-8 py-3 text-lg font-medium rounded-full bg-second text-white hover:bg-blue-600 transition-all duration-300"
							>
								Submit
							</button>
						</div>
					</div>
				</div>

				<!-- No Response Modal -->
				<div
					v-if="tamNoResponse"
					class="fixed inset-0 flex items-center justify-center bg-black/50 z-50"
				>
					<div
						class="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-6 m-4 transition-all duration-300"
					>
						<h2
							class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4 transition-colors"
						>
							Please Select an Option
						</h2>
						<p
							class="text-gray-600 dark:text-gray-400 mb-6 transition-colors"
						>
							You need to select an option for each question
							before proceeding.
						</p>
						<div class="flex justify-end">
							<button
								@click="tamNoResponse = false"
								class="px-6 py-2 rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-all duration-300"
							>
								Close
							</button>
						</div>
					</div>
				</div>

				<!-- Complete Response Modal -->
				<div
					v-if="tamCompleteResponse"
					class="fixed inset-0 flex items-center justify-center bg-black/50 z-50"
				>
					<div
						class="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 m-4 transition-all duration-300"
					>
						<h1
							class="text-3xl sm:text-4xl font-bold text-blue-600 dark:text-blue-400 mb-6 text-center transition-colors"
						>
							Thank You!
						</h1>
						<p
							class="text-gray-600 dark:text-gray-300 text-lg text-center mb-8 transition-colors"
						>
							Thank you for your feedback! The developers greatly
							appreciate your help in making CulturaLink better.
						</p>
						<div class="flex justify-center">
							<button
								@click.prevent="logout"
								class="px-8 py-3 text-lg font-medium rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-all duration-300"
							>
								Logout
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { SunIcon, MoonIcon } from "lucide-vue-next";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const router = useRouter();
const store = useStore();

const isDark = ref(false);
const tamModalActive = ref(true);
const tamOneActive = ref(false);
const tamNoResponse = ref(false);
const tamCompleteResponse = ref(false);

const questions = ref([
	{
		text: "CulturaLink promotes understanding and appreciation of diverse cultures.",
	},
	{ text: "CulturaLink supports meaningful cultural exchange." },
	{
		text: "It is easy to find and connect with users from different cultural backgrounds.",
	},
	{ text: "Navigating through CulturaLink is simple and intuitive." },
	{
		text: "I intend to use CulturaLink to learn more about different cultures.",
	},
	{ text: "I would recommend CulturaLink to others." },
]);

const options = [
	"Strongly Disagree",
	"Disagree",
	"Neutral",
	"Agree",
	"Strongly Agree",
];

const responses = ref(Array(6).fill(""));

// Theme management
const toggleTheme = () => {
	isDark.value = !isDark.value;
	localStorage.setItem("culturalink-theme", isDark.value ? "dark" : "light");
};

onMounted(() => {
	// Load saved theme preference
	const savedTheme = localStorage.getItem("culturalink-theme");
	isDark.value =
		savedTheme === "dark" ||
		(!savedTheme &&
			window.matchMedia("(prefers-color-scheme: dark)").matches);
});

const maybeLater = () => {
	tamModalActive.value = false;
	router.push({ name: "dashboard" });
};

const continueSurvey = () => {
	tamOneActive.value = true;
	tamModalActive.value = false;
};

const submitSurvey = () => {
	if (responses.value.includes("")) {
		tamNoResponse.value = true;
	} else {
		axiosClient
			.post("/get-survey", {
				q1: responses.value[0],
				q2: responses.value[1],
				q3: responses.value[2],
				q4: responses.value[3],
				q5: responses.value[4],
				q6: responses.value[5],
			})
			.then(() => {
				tamCompleteResponse.value = true;
			})
			.catch((error) => {
				console.error("Error submitting survey:", error);
			});
	}
};

const logout = async () => {
	try {
		await store.dispatch("logout");
		router.push({ name: "login" });
	} catch (error) {
		router.push({ name: "tamsurvey" });
		console.error("Error during logout:", error);
	}
};
</script>

<style>
/* Base transitions */
.transition-all {
	transition-property: all;
	transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
	transition-duration: 300ms;
}

/* Smooth theme transition */
.dark {
	color-scheme: dark;
}

/* Custom radio button animations */
@keyframes radioScale {
	0% {
		transform: scale(0.8);
	}
	50% {
		transform: scale(1.1);
	}
	100% {
		transform: scale(1);
	}
}

input[type="radio"]:checked + div {
	animation: radioScale 0.3s ease-in-out;
}

/* Custom scrollbar styles */
.overflow-y-auto {
	scrollbar-width: thin;
	scrollbar-color: rgba(156, 163, 175, 0.5) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
	width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
	background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
	background-color: rgba(156, 163, 175, 0.5);
	border-radius: 3px;
}

.dark .overflow-y-auto {
	scrollbar-color: rgba(75, 85, 99, 0.5) transparent;
}

.dark .overflow-y-auto::-webkit-scrollbar-thumb {
	background-color: rgba(75, 85, 99, 0.5);
}
</style>
