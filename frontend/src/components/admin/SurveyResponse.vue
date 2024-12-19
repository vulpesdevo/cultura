<template>
	<div class="h-screen bg-gray-100 dark:bg-gray-900 py-8 px-4 sm:px-6">
		<div class="mx-auto pb-20 sm:pb-7">
			<div
				class="mb-10 flex sm:flex-row flex-col justify-between items-start"
			>
				<!-- Survey Donut Chart -->
				<div class="w-full md:w-[45%] mb-6 md:mb-0">
					<div
						class="bg-white dark:bg-gray-800 shadow-lg rounded-lg overflow-hidden"
					>
						<div class="py-5">
							<SurveyDonutChart :surveys="surveys" />
						</div>
					</div>
				</div>

				<!-- Survey Stats -->
				<div class="w-full sm:w-1/2 md:pl-8">
					<div
						class="bg-white dark:bg-gray-800 shadow-lg rounded-lg overflow-hidden"
					>
						<div class="px-4 py-5 sm:p-6">
							<h2
								class="text-base font-semibold text-gray-900 dark:text-white mb-4"
							>
								Survey Statistics
							</h2>
							<div class="grid grid-cols-3 gap-3">
								<div
									class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg"
								>
									<p
										class="text-xs text-gray-500 dark:text-gray-400"
									>
										Total Responses
									</p>
									<p
										class="text-sm font-bold text-gray-900 dark:text-white"
									>
										{{ surveys.length }}
									</p>
								</div>
								<div
									class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg"
								>
									<p
										class="text-xs text-gray-500 dark:text-gray-400"
									>
										Average Score
									</p>
									<p
										class="text-sm font-bold text-gray-900 dark:text-white"
									>
										{{ calculateAverageScore().toFixed(2) }}
									</p>
								</div>
								<div
									class="bg-gray-50 dark:bg-gray-700 p-2 pt-3 rounded-lg"
								>
									<p
										class="text-xs text-gray-500 dark:text-gray-400"
									>
										Most Common Response
									</p>
									<p
										class="text-sm font-bold text-gray-900 dark:text-white"
									>
										{{ getMostCommonResponse() }}
									</p>
								</div>
							</div>
						</div>
					</div>
					<div class="mt-4 text-center flex justify-start">
						<button
							@click="fetchSurveys"
							class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors duration-300"
						>
							Refresh Surveys
						</button>
					</div>
				</div>
			</div>

			<div
				v-if="surveys && surveys.length"
				class="grid grid-cols-1 gap-6 sm:grid-cols-3"
			>
				<div
					v-for="survey in surveys"
					:key="survey.id"
					class="bg-white dark:bg-gray-800 overflow-hidden shadow-lg rounded-lg"
				>
					<div class="px-4 py-5 sm:p-6">
						<div class="flex items-center mb-4">
							<img
								:src="survey.cultura_user.user_photo"
								alt="User photo"
								class="w-12 h-12 rounded-full mr-4"
							/>
							<div>
								<h3
									class="text-lg font-medium text-gray-900 dark:text-white"
								>
									{{ survey.cultura_user.fullname }}
								</h3>
								<p
									class="text-sm text-gray-500 dark:text-gray-400"
								>
									@{{ survey.cultura_user.user.username }}
								</p>
							</div>
						</div>

						<div class="space-y-4">
							<div
								v-for="(response, question) in surveyResponses"
								:key="question"
								class="relative pt-1"
							>
								<div class="flex items-center justify-between">
									<div class="relative group">
										<span
											class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blue-600 bg-blue-200 dark:text-blue-200 dark:bg-blue-800 cursor-help"
										>
											{{ question }}
										</span>
										<div
											class="absolute left-0 bottom-0 mb-2 w-64 p-2 bg-gray-900 text-white text-xs rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-10"
										>
											{{ surveyResponses[question] }}
										</div>
									</div>
									<div class="text-right">
										<span
											class="text-xs font-semibold inline-block text-blue-600 dark:text-blue-400"
										>
											{{ survey[question] }}
										</span>
									</div>
								</div>
								<div
									class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-blue-200 dark:bg-blue-800"
								>
									<div
										:style="{
											width: getResponseWidth(
												survey[question]
											),
										}"
										class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500 dark:bg-blue-400"
									></div>
								</div>
							</div>
						</div>
					</div>
					<div class="px-4 py-4 sm:px-6 bg-gray-50 dark:bg-gray-700">
						<div class="text-sm">
							<p class="text-gray-500 dark:text-gray-400">
								Country:
								<span
									class="font-medium text-gray-900 dark:text-white"
									>{{ survey.cultura_user.country }}</span
								>
							</p>
						</div>
					</div>
				</div>
			</div>

			<div v-else-if="loading" class="text-center py-12">
				<div
					class="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-500"
				></div>
				<p class="mt-2 text-gray-600 dark:text-gray-400">
					Loading survey responses...
				</p>
			</div>

			<div v-else class="text-center py-12">
				<p class="text-gray-600 dark:text-gray-400">
					No survey responses available.
				</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeMount } from "vue";
import { useStore } from "vuex";
import SurveyDonutChart from "./SurveyDonutChart.vue";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useStore();

const surveys = computed(() => store.getters.surveys);
const loading = ref(false);

const surveyResponses = {
	q1: "CulturaLink promotes understanding and appreciation of diverse cultures.",
	q2: "CulturaLink supports meaningful cultural exchange.",
	q3: "It is easy to find and connect with users from different cultural backgrounds.",
	q4: "Navigating through CulturaLink is simple and intuitive.",
	q5: "I intend to use CulturaLink to learn more about different cultures.",
	q6: "I would recommend CulturaLink to others.",
};

const getResponseWidth = (response) => {
	const responseValues = {
		"Strongly Disagree": "20%",
		Disagree: "40%",
		Neutral: "60%",
		Agree: "80%",
		"Strongly Agree": "100%",
	};
	return responseValues[response] || "0%";
};

const fetchSurveys = async () => {
	loading.value = true;
	try {
		await store.dispatch("fetchSurveys");
	} catch (error) {
		console.error("Error fetching surveys:", error);
	} finally {
		loading.value = false;
	}
};

const calculateAverageScore = () => {
	if (!surveys.value || surveys.value.length === 0) return 0;

	const scoreMap = {
		"Strongly Disagree": 1,
		Disagree: 2,
		Neutral: 3,
		Agree: 4,
		"Strongly Agree": 5,
	};

	let totalScore = 0;
	let totalResponses = 0;

	surveys.value.forEach((survey) => {
		Object.values(survey).forEach((response) => {
			if (scoreMap.hasOwnProperty(response)) {
				totalScore += scoreMap[response];
				totalResponses++;
			}
		});
	});

	return totalResponses > 0 ? totalScore / totalResponses : 0;
};

const getMostCommonResponse = () => {
	if (!surveys.value || surveys.value.length === 0) return "N/A";

	const responseCounts = {};
	surveys.value.forEach((survey) => {
		Object.values(survey).forEach((response) => {
			responseCounts[response] = (responseCounts[response] || 0) + 1;
		});
	});

	return Object.entries(responseCounts).reduce((a, b) =>
		a[1] > b[1] ? a : b
	)[0];
};

onBeforeMount(async () => {
	await store
		.dispatch("fetchUserData")
		.then(async (response) => {
			if (!response.profile.is_admin) {
				router.push({ name: "NotFound" });
			} else {
				await fetchSurveys();
			}
		})
		.catch((error) => {
			console.error("Error fetching user data:", error);
			router.push({ name: "NotFound" });
		});
});
</script>
