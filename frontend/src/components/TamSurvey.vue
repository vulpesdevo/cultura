<template>
	<div class="w-full relative overflow-auto h-screen z-50">
		<!-- Initial Modal -->
		<div
			:class="{ 'blur-background': tamNoResponse || tamCompleteResponse }"
		>
			<div
				v-show="tamModalActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 min-h-screen items-center justify-center px-8 sm:px-0"
			>
				<div
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface"
				>
					<h1
						class="text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-7 text-center"
					>
						We Could Use Your Help!
					</h1>
					<p
						class="text-center text-xs sm:text-xl my-5 mb-7 px-7 sm:px-20 font-montserrat dark:text-interface"
					>
						Before you go, do you have a moment to answer a few
						questions about your experience with CulturaLink?
					</p>
					<div class="flex justify-center">
						<button
							@click="maybeLater"
							class="rounded-full text-lg text-white mt-3 mb-6 bg-gray-500 py-3 px-3 sm:px-7 font-bebas-neue"
						>
							Maybe Later
						</button>
						<button
							@click="continueSurvey"
							class="rounded-full text-xl text-white mt-3 mb-6 ms-10 sm:ms-24 bg-second hover:bg-blue-700 py-3 px-4 sm:px-7 font-bebas-neue"
						>
							Continue
						</button>
					</div>
				</div>
			</div>

			<!-- Survey Modal -->
			<div
				v-if="tamOneActive"
				class="min-h-screen flex items-center justify-center bg-interface dark:bg-dark-interface"
			>
				<div
					class="w-full max-w-7xl bg-white dark:bg-dark-interface p-8 rounded-lg shadow-lg mt-5 px-0 sm:px-20"
				>
					<p
						class="text-center text-md sm:text-xl mb-14 px-6 sm:px-20 font-montserrat dark:text-interface"
					>
						Please answer all questions as honestly as possible.
					</p>
					<form @submit.prevent="submitSurvey">
						<table class="w-full text-left mb-14">
							<thead class="text-xs sm:text-lg">
								<tr>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Questions
									</th>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Strongly Agree
									</th>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Agree
									</th>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Neutral
									</th>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Disagree
									</th>
									<th
										class="pb-7 font-semibold text-center dark:text-interface"
									>
										Strongly Disagree
									</th>
								</tr>
							</thead>
							<tbody>
								<tr
									v-for="(question, index) in questions"
									:key="index"
									class="border-t border-gray-300 dark:border-gray-600"
								>
									<td
										class="w-96 py-6 px-5 text-xs sm:text-lg font-montserrat dark:text-interface"
									>
										{{ question.text }}
									</td>
									<td class="text-center w-20">
										<input
											type="radio"
											:name="'response' + index"
											value="Strongly Agree"
											v-model="responses[index]"
											required
										/>
									</td>
									<td class="text-center w-20">
										<input
											type="radio"
											:name="'response' + index"
											value="Agree"
											v-model="responses[index]"
											required
										/>
									</td>
									<td class="text-center w-20">
										<input
											type="radio"
											:name="'response' + index"
											value="Neutral"
											v-model="responses[index]"
											required
										/>
									</td>
									<td class="text-center w-20">
										<input
											type="radio"
											:name="'response' + index"
											value="Disagree"
											v-model="responses[index]"
											required
										/>
									</td>
									<td class="text-center w-40 sm:w-20">
										<input
											type="radio"
											:name="'response' + index"
											value="Strongly Disagree"
											v-model="responses[index]"
											required
										/>
									</td>
								</tr>
							</tbody>
						</table>
						<div class="flex justify-center">
							<button
								type="submit"
								class="bg-second hover:bg-blue-700 text-white py-3 px-6 rounded-full font-bebas-neue"
							>
								Submit
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>

		<!-- No Response Modal -->
		<div
			v-if="tamNoResponse"
			class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-40"
		>
			<div
				class="bg-white dark:bg-dark-interface rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3"
			>
				<h2 class="text-2xl font-bold dark:text-interface mb-4">
					Please Select an Option
				</h2>
				<p class="mb-4 dark:text-interface">
					You need to select an option before proceeding.
				</p>
				<div class="flex justify-end">
					<button
						@click="tamNoResponse = false"
						class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
					>
						Close
					</button>
				</div>
			</div>
		</div>

		<!-- Complete Response Modal -->
		<div
			v-if="tamCompleteResponse"
			class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-40"
		>
			<div
				class="bg-white dark:bg-dark-interface rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3"
			>
				<h1
					class="text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-7 text-center"
				>
					Thank You!
				</h1>
				<p
					class="text-center text-xs sm:text-xl my-5 mb-7 px-7 sm:px-20 font-montserrat dark:text-interface"
				>
					Thank you for your feedback! The developers greatly
					appreciate your help in making CulturaLink better.
				</p>
				<div class="flex justify-center">
					<button
						@click.prevent="logout"
						class="bg-second text-white py-3 sm:py-3 px-4 sm:px-7 rounded-full hover:bg-blue-700"
					>
						Logout
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
const router = useRouter();
const store = useStore();
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
const responses = ref(Array(6).fill(""));

let token = "";
let client = null;

onMounted(() => {
	// token = sessionStorage.getItem("TOKEN");
	// client = axios.create({
	// 	baseURL: "http://127.0.0.1:8000",
	// 	withCredentials: true,
	// 	timeout: 5000,
	// 	xsrfCookieName: "csrftoken",
	// 	xsrfHeaderName: "X-Csrftoken",
	// 	headers: {
	// 		Authorization: `Token ${token}`,
	// 		"Content-Type": "application/json",
	// 	},
	// });
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
		console.log(responses.value[0]);
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

<style scoped>
.blur-background {
	filter: blur(2px);
	transition: filter 0.3s;
}
</style>
