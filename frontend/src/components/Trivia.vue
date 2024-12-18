<template>
	<div
		class="h-screen bg-field dark:bg-notif py-8 px-4 sm:px-6 lg:px-8 transition-colors duration-300"
	>
		<div class="max-w-7xl mx-auto">
			<!-- Header -->
			<div
				class="bg-second rounded-lg shadow-lg mb-8 p-6 sm:p-10 transform hover:scale-[1.02] transition-all duration-300"
			>
				<h1
					class="text-4xl sm:text-5xl font-montserrat font-bold text-interface dark:text-dark-interface text-center mb-4"
				>
					Learn With CulturaLink
				</h1>
				<p
					class="text-base text-interface dark:text-dark-interface text-center max-w-3xl mx-auto opacity-90"
				>
					Visit the Trivia tab occasionally for fresh and exciting
					trivia about cultures from around the world!
				</p>
			</div>

			<!-- Trivia Cards -->
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
				<div
					v-for="(question, index) in triviaQuestions"
					:key="index"
					class="bg-interface dark:bg-dark-interface rounded-lg shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl transform hover:scale-[1.02]"
				>
					<div class="p-6">
						<div class="flex items-center justify-between mb-4">
							<span
								class="text-xs font-semibold font-montserrat text-second dark:text-second-light uppercase tracking-wide"
							>
								{{ question.category }}
							</span>
							<span
								class="text-xs font-medium text-prime dark:text-dark-prime"
							>
								Question #{{ index + 1 }}
							</span>
						</div>
						<h2
							class="text-base font-montserrat text-prime dark:text-dark-prime mb-4"
						>
							{{ question.question }}
						</h2>
						<div
							class="mt-4 pt-4 border-t font-montserrat border-field dark:border-dark-field"
						>
							<button
								@click="toggleAnswer(index)"
								class="text-second dark:text-second-light hover:text-second-light dark:hover:text-second transition-colors duration-300 focus:outline-none rounded"
							>
								{{
									showAnswers[index]
										? "Hide Answer"
										: "Show Answer"
								}}
							</button>
							<transition name="fade">
								<p
									v-if="showAnswers[index]"
									class="mt-2 text-prime text-xs dark:text-dark-prime"
								>
									{{ question.answer }}
								</p>
							</transition>
						</div>
					</div>
				</div>
			</div>

			<!-- Loading and Error States -->
			<div v-if="loading" class="text-center mt-8">
				<div
					class="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-second"
				></div>
				<p class="mt-2 text-prime dark:text-dark-prime">
					Loading trivia questions...
				</p>
			</div>
			<div
				v-if="error"
				class="text-center mt-8 text-red-600 dark:text-red-400"
			>
				{{ error }}
			</div>

			<!-- Fetch More Button -->
			<div class="mt-8 text-center">
				<button
					@click="fetchTriviaQuestions"
					class="bg-second hover:bg-second-light dark:bg-second dark:hover:bg-second-dark text-interface dark:text-dark-interface font-bold py-3 px-6 rounded-full transition-colors duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-second-light dark:focus:ring-second-dark"
					:disabled="loading || requestCount >= 10"
				>
					<span v-if="requestCount >= 10">Limit Reached</span>
					<span v-else>Fetch More Trivia</span>
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const triviaQuestions = ref([]);
const loading = ref(false);
const error = ref(null);
const requestCount = ref(0);
const showAnswers = ref([]);

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
		showAnswers.value.push(false);
		requestCount.value += 1;
		console.log("Trivia Questions:", triviaQuestions.value);
	} catch (err) {
		error.value = `Failed to fetch trivia questions: ${err.message}`;
		console.error("Failed to fetch trivia questions:", err);
	} finally {
		loading.value = false;
	}
};

const toggleAnswer = (index) => {
	showAnswers.value[index] = !showAnswers.value[index];
};

let intervalId;

onMounted(() => {
	fetchTriviaQuestions(); // Fetch initial questions

	intervalId = setInterval(() => {
		requestCount.value = 0; // Reset request count every hour
	}, 3600000); // 1 hour in milliseconds
});

onBeforeUnmount(() => {
	clearInterval(intervalId);
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
	opacity: 0;
}
</style>
