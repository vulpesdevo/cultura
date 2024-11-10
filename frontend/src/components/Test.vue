<template>
	<div class="w-full relative overflow-hidden h-screen z-50">
		<!-- Initial Modal -->
		<div :class="{ 'blur-background': tamNoResponse }">
			<div
				v-show="tamModalActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamModalActive"
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface"
				>
					<h1
						class="flex text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-7 justify-center"
					>
						We Could Use Your Help!
					</h1>
					<p
						class="flex text-center text-xs sm:text-xl my-5 mb-7 sm:my-10 px-7 sm:px-20 font-montserrat dark:text-interface"
					>
						Before you go, do you have a moment to answer a few
						questions about your experience with CulturaLink?
					</p>

					<div class="flex justify-center">
						<button
							@click="maybeLater"
							class="rounded-full text-lg text-white mt-3 mb-6 bg-gray-500 py-3 sm:py-3 px-3 sm:px-7 font-bebas-neue justify-center"
						>
							Maybe Later
						</button>
						<button
							@click="
								(tamOneActive = true), (tamModalActive = false)
							"
							class="rounded-full text-xl text-white mt-3 mb-6 ms-10 sm:ms-24 bg-second hover:bg-blue-700 py-3 sm:py-3 px-4 sm:px-7 font-bebas-neue justify-center"
						>
							Continue
						</button>
					</div>
				</div>
			</div>

			<!-- Question 1 Modal -->
			<div
				v-show="tamOneActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamOneActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">1</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							CulturaLink promotes understanding and appreciation
							of diverse cultures.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response1"
									value="Strongly Agree"
									v-model="selectedResponse1"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response1"
									value="Agree"
									v-model="selectedResponse1"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response1"
									value="Neutral"
									v-model="selectedResponse1"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response1"
									value="Disagree"
									v-model="selectedResponse1"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response1"
									value="Strongly Disagree"
									v-model="selectedResponse1"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="nextQuestion1"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Next
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Question 2 Modal -->
			<div
				v-show="tamTwoActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamTwoActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">2</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							CulturaLink supports meaningful cultural exchange.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response2"
									value="Strongly Agree"
									v-model="selectedResponse2"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response2"
									value="Agree"
									v-model="selectedResponse2"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response2"
									value="Neutral"
									v-model="selectedResponse2"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response2"
									value="Disagree"
									v-model="selectedResponse2"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response2"
									value="Strongly Disagree"
									v-model="selectedResponse2"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="nextQuestion2"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Next
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Question 3 Modal -->
			<div
				v-show="tamThreeActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamThreeActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">3</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							It is easy to find and connect with users from
							different cultural backgrounds.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response3"
									value="Strongly Agree"
									v-model="selectedResponse3"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response3"
									value="Agree"
									v-model="selectedResponse3"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response3"
									value="Neutral"
									v-model="selectedResponse3"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response3"
									value="Disagree"
									v-model="selectedResponse3"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response3"
									value="Strongly Disagree"
									v-model="selectedResponse3"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="nextQuestion3"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Next
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Question 4 Modal -->
			<div
				v-show="tamFourActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamFourActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">4</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							CulturaLink offers valuable resources for learning
							about different cultures.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response4"
									value="Strongly Agree"
									v-model="selectedResponse4"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response4"
									value="Agree"
									v-model="selectedResponse4"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response4"
									value="Neutral"
									v-model="selectedResponse4"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response4"
									value="Disagree"
									v-model="selectedResponse4"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response4"
									value="Strongly Disagree"
									v-model="selectedResponse4"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="nextQuestion4"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Next
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Question 5 Modal -->
			<div
				v-show="tamFiveActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamFiveActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">5</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							CulturaLink's platform is user-friendly and easy to
							navigate.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response5"
									value="Strongly Agree"
									v-model="selectedResponse5"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response5"
									value="Agree"
									v-model="selectedResponse5"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response5"
									value="Neutral"
									v-model="selectedResponse5"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response5"
									value="Disagree"
									v-model="selectedResponse5"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response5"
									value="Strongly Disagree"
									v-model="selectedResponse5"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="nextQuestion5"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Next
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Question 6 Modal -->
			<div
				v-show="tamSixActive"
				class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
			>
				<div
					v-if="tamSixActive"
					class="fixed inset-0 flex items-center justify-center"
				>
					<div
						class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
					>
						<div class="flex justify-between items-center mb-4">
							<h2 class="text-2xl font-bold dark:text-interface">
								Question <span class="text-second">6</span> of 6
							</h2>
						</div>
						<p class="mb-4 dark:text-interface">
							I would recommend CulturaLink to others interested
							in cultural exchange.
						</p>
						<div class="mb-4 dark:text-interface">
							<label class="block mb-2">
								<input
									type="radio"
									name="response6"
									value="Strongly Agree"
									v-model="selectedResponse6"
									class="mr-2"
									required
								/>
								Strongly Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response6"
									value="Agree"
									v-model="selectedResponse6"
									class="mr-2"
									required
								/>
								Agree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response6"
									value="Neutral"
									v-model="selectedResponse6"
									class="mr-2"
									required
								/>
								Neutral
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response6"
									value="Disagree"
									v-model="selectedResponse6"
									class="mr-2"
									required
								/>
								Disagree
							</label>
							<label class="block mb-2">
								<input
									type="radio"
									name="response6"
									value="Strongly Disagree"
									v-model="selectedResponse6"
									class="mr-2"
									required
								/>
								Strongly Disagree
							</label>
						</div>
						<div class="flex justify-end">
							<button
								@click="submitSurvey"
								class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
							>
								Submit
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- No Response Modal -->
		</div>
		<div
			v-show="tamNoResponse"
			class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
		>
			<div
				v-if="tamNoResponse"
				class="fixed inset-0 flex items-center justify-center"
			>
				<div
					class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
				>
					<div class="flex justify-between items-center mb-4">
						<h2 class="text-2xl font-bold dark:text-interface">
							Please Select an Option
						</h2>
					</div>
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
		</div>
		<div
			v-show="tamCompleteResponse"
			class="flex flex-col sm:flex-row w-full bg-black bg-opacity-40 h-screen align-middle items-center justify-center px-8 sm:px-0"
		>
			<div
				v-if="tamCompleteResponse"
				class="fixed inset-0 flex items-center justify-center"
			>
				<div
					class="bg-white rounded-lg shadow-lg p-6 w-11/12 sm:w-1/2 lg:w-1/3 dark:bg-dark-interface"
				>
					<h1
						class="flex text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-7 justify-center"
					>
						Thank You!
					</h1>
					<p
						class="flex text-center text-xs sm:text-xl my-5 mb-7 sm:my-10 px-7 sm:px-20 font-montserrat dark:text-interface"
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
	</div>
</template>

<script>
import axios from "axios";
import router from "../routes";
import { useDark, useToggle } from "@vueuse/core";
import { ref } from "vue";
export default {
	data() {
		return {
			tamModalActive: true,
			tamOneActive: false,
			tamTwoActive: false,
			tamThreeActive: false,
			tamFourActive: false,
			tamFiveActive: false,
			tamSixActive: false,
			tamNoResponse: false,
			tamCompleteResponse: false,
			selectedResponse1: "",
			selectedResponse3: "",
			selectedResponse2: "",
			selectedResponse4: "",
			selectedResponse5: "",
			selectedResponse6: "",
			responses: [],
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
		nextQuestion1() {
			if (this.selectedResponse1) {
				this.tamOneActive = false;
				this.tamTwoActive = true;
				this.responses.push(this.response1);
				console.log("res1", this.selectedResponse1); // Reset the selected response for the next question
			} else {
				this.tamNoResponse = true;
			}
		},
		nextQuestion2() {
			if (this.selectedResponse2) {
				this.tamTwoActive = false;
				this.tamThreeActive = true;
				this.responses.push(this.response2);
				console.log("res2", this.selectedResponse2); // Reset the selected response for the next question
			} else {
				this.tamNoResponse = true;
			}
		},
		nextQuestion3() {
			if (this.selectedResponse3) {
				this.tamThreeActive = false;
				this.tamFourActive = true;
				this.responses.push(this.response3);
				console.log("res3", this.selectedResponse3); // Reset the selected response for the next question
			} else {
				this.tamNoResponse = true;
			}
		},
		nextQuestion4() {
			if (this.selectedResponse4) {
				this.tamFourActive = false;
				this.tamFiveActive = true;
				this.responses.push(this.response4);
				console.log("res4", this.selectedResponse4); // Reset the selected response for the next question
			} else {
				this.tamNoResponse = true;
			}
		},
		nextQuestion5() {
			if (this.selectedResponse5) {
				this.tamFiveActive = false;
				this.tamSixActive = true;
				this.responses.push(this.response5);
				console.log("res5", this.selectedResponse5); // Reset the selected response for the next question
			} else {
				this.tamNoResponse = true;
			}
		},
		// nextQuestion6() {
		// 	if (this.selectedResponse6) {
		// 		this.tamFiveActive = false;
		//         this.tamSixActive = true;
		//         this.responses.push(this.response6)
		// 		console.log('res6',this.selectedResponse6) // Reset the selected response for the next question
		// 	} else {
		// 		this.tamNoResponse = true;
		// 	}
		// },
		submitSurvey() {
			if (this.selectedResponse6) {
				this.tamSixActive = false;
				this.responses.push(this.response6);
				console.log("res6", this.selectedResponse6); // Reset the selected response for the next survey
				this.tamCompleteResponse = true;
				this.client
					.post(`api/get-survey`, {
						q1: this.selectedResponse1,
						q2: this.selectedResponse2,
						q3: this.selectedResponse3,
						q4: this.selectedResponse4,
						q5: this.selectedResponse5,
						q6: this.selectedResponse6,
					})
					.then((response) => {
						// Handle success response
						console.log(response.data);
						// this.$router.push({ name: "SurveyComplete" });

						// Optionally, update your UI based on the successful like
					})
					.catch((error) => {
						// Handle error
						console.error("Error:", error);
					});
			} else {
				this.tamNoResponse = true;
			}
		},
		logout() {
			this.client
				.post("api/logout")
				.then((res) => {
					// console.log("User logged out:", res);
					// this.user.isAuthenticated = false;

					sessionStorage.removeItem("TOKEN");
					// localStorage.setItem("isSurvey", true);
					window.scrollTo(0, 0);
					router.push({ name: "login" }).then(() => {
						window.location.reload();
					});
				})
				.catch((error) => {
					console.log(error);
					router.push({ name: "test" });
				});
		},
	},
};
</script>

<style scoped>
/* Add your custom styles here */
.blur-background {
	filter: blur(2px);
	transition: filter 0.3s;
}
</style>
