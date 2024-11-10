<template>
	<div class="w-full relative overflow-auto min-h-screen z-50">
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

<script>
import axios from "axios";
import router from "../routes";

export default {
	data() {
		return {
			tamModalActive: true,
			tamOneActive: false,
			tamNoResponse: false,
			tamCompleteResponse: false,
			questions: [
				{
					text: "CulturaLink promotes understanding and appreciation of diverse cultures.",
				},
				{ text: "CulturaLink supports meaningful cultural exchange." },
				{
					text: "It is easy to find and connect with users from different cultural backgrounds.",
				},
				{
					text: "Navigating through CulturaLink is simple and intuitive.",
				},
				{
					text: "I intend to use CulturaLink to learn more about different cultures.",
				},
				{ text: "I would recommend CulturaLink to others." },
			],
			responses: Array(6).fill(""),
		};
	},
	created() {
		this.token = sessionStorage.getItem("TOKEN");
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
	},
	methods: {
		maybeLater() {
			this.tamModalActive = false;
			router.push({ name: "dashboard" });
		},
		continueSurvey() {
			this.tamOneActive = true;
			this.tamModalActive = false;
		},
		submitSurvey() {
			if (this.responses.includes("")) {
				this.tamNoResponse = true;
			} else {
				this.client
					.post("api/get-survey", {
						q1: this.responses[0],
						q2: this.responses[1],
						q3: this.responses[2],
						q4: this.responses[3],
						q5: this.responses[4],
						q6: this.responses[5],
					})
					.then(() => {
						this.tamCompleteResponse = true;
					})
					.catch((error) => {
						console.error("Error submitting survey:", error);
					});
				console.log(this.responses[0]);
			}
		},
		logout() {
			this.client
				.post("api/logout")
				.then(() => {
					sessionStorage.removeItem("TOKEN");
					router.push({ name: "login" }).then(() => {
						window.location.reload();
					});
				})
				.catch((error) => {
					console.log("Logout error:", error);
				});
		},
	},
};
</script>

<style scoped>
.blur-background {
	filter: blur(2px);
	transition: filter 0.3s;
}
</style>
