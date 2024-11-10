<template>
	<div
		class="flex flex-col items-center just align-middle w-full sm:px-8 pb-2 overflow-x-hidden h-screen bg-field dark:bg-dark-notif px-2"
	>
		<div
			class="post-contents w-screen p-5 mb-5 pb-3 pt-7 px-6 sm:mt-0 sm:px-52 shadow-lg bg-[#7f93e9] dark:bg-[#111731]"
		>
			<div class="post-title flex justify-center items-center">
				<div class="flex w-full justify-between items-center">
					<h1
						class="font-bebas-neue text-center text-5xl text-prime dark:text-dark-prime sm:text-5xl justify-center w-full flex my-5"
					>
						Learn With CulturaLink
					</h1>
				</div>
			</div>
			<div class="post-content flex w-full mt-4 dark:text-dark-prime">
				<div class="w-full">
					<div class="flex w-full mb-10">
						<!-- Trivia Sub-Title -->
						<div class="w-full">
							<h1
								class="font-montserrat text-sm text-prime dark:text-dark-prime text-center sm:text-lg justify-center flex"
							>
								Visit the Trivia tab occasionally for fresh and
								exciting trivia about cultures from around the
								world!
							</h1>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- Trivia One -->
		<div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
			<div
				v-for="(question, index) in triviaQuestions"
				:key="index"
				class="w-full h-auto rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
			>
				<div
					class="p-6 sm:p-9 post-content flex w-full dark:text-dark-prime"
				>
					<div class="w-full">
						<div class="flex w-full justify-start mb-5">
							<p
								class="text-start font-montserrat w-full rounded-lg resize-none text-sm whitespace-normal"
							>
								<span
									class="text-xs text-opacity-50 text-interface"
									>category: </span
								>{{ question.category }}
							</p>
						</div>
						<div class="flex w-full mb-5">
							<!-- Trivia Sub-Title -->
							<div class="w-full">
								<h1
									class="font-montserrat text-sm text-prime dark:text-dark-prime sm:text-lg justify-start flex"
								>
									{{ question.question }}
								</h1>
							</div>
						</div>
						<!-- Trivia Content -->
						<div class="flex w-full justify-end">
							<p
								class="text-end font-montserrat w-full rounded-lg resize-none text-sm whitespace-normal"
							>
								<span
									class="text-xs text-opacity-50 text-interface"
									>answer: </span
								>{{ question.answer }}
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from "vue";

export default {
	setup() {
		const triviaQuestions = ref([]);
		const loading = ref(false);
		const error = ref(null);
		const showSnackbar = ref(false);
		const requestCount = ref(0);

		const apiKey = "14L4SCh7Me4KaDH1xLnMmw==wik53BlNsvI2cN3k"; // Replace with your actual API key
		const categories = [
			"artliterature",
			"sciencenature",
			"general",
			"fooddrink",
			"peopleplaces",
			"historyholidays",
			"entertainment",
			"toysgames",
			"music",
			"mathematics",
			"religionmythology",
			"sportsleisure",
		];

		const getRandomCategory = () => {
			const randomIndex = Math.floor(Math.random() * categories.length);
			return categories[randomIndex];
		};

		const fetchTriviaQuestions = async () => {
			if (requestCount.value >= 10) {
				console.log("Request limit reached for this hour.");
				return;
			}

			loading.value = true;
			error.value = null;
			const category = getRandomCategory();

			try {
				const response = await fetch(
					`https://api.api-ninjas.com/v1/trivia?category=${category}`,
					{
						headers: {
							"X-Api-Key": apiKey,
						},
					}
				);

				if (!response.ok) {
					throw new Error(
						`Network response was not ok: ${response.statusText}`
					);
				}

				const data = await response.json();
				triviaQuestions.value.push(...data);
				requestCount.value += 1;
				console.log("Trivia Questions:", triviaQuestions.value);
			} catch (err) {
				error.value = `Failed to fetch trivia questions: ${err.message}`;
				console.error("Failed to fetch trivia questions:", err);
			} finally {
				loading.value = false;
			}
		};

		let intervalId;

		onMounted(() => {
			intervalId = setInterval(() => {
				if (requestCount.value < 10) {
					fetchTriviaQuestions();
				}
			}, 100); // 100 milliseconds

			setInterval(() => {
				requestCount.value = 0; // Reset request count every hour
			}, 3600000); // 1 hour in milliseconds
		});

		onBeforeUnmount(() => {
			clearInterval(intervalId);
		});

		return {
			triviaQuestions,
			loading,
			error,
			showSnackbar,
			fetchTriviaQuestions,
		};
	},
};
</script>

<style scoped></style>
