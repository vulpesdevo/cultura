<template>
	<div
		class="relative min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100 p-4"
	>
		<transition name="fade" mode="out-in">
			<div
				v-if="showSnackbar && triviaQuestions.length > 0"
				class="fixed bottom-4 right-4 bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg w-80 max-h-64 overflow-y-auto"
			>
				<button
					@click="showSnackbar = false"
					class="absolute top-2 right-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
				>
					&times;
				</button>
				<div
					v-for="(question, index) in triviaQuestions"
					:key="index"
					class="mb-4"
				>
					<p
						class="font-semibold text-sm text-gray-600 dark:text-gray-300"
					>
						{{ question.category }}
					</p>
					<p class="font-medium mb-1">{{ question.question }}</p>
					<p class="text-sm text-gray-700 dark:text-gray-300">
						Answer: {{ question.answer }}
					</p>
				</div>
			</div>
		</transition>
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
				triviaQuestions.value = data;
				showSnackbar.value = true;

				// Auto-hide snackbar after 5 seconds
				setTimeout(() => (showSnackbar.value = false), 5000);
			} catch (err) {
				error.value = `Failed to fetch trivia questions: ${err.message}`;
				console.error("Failed to fetch trivia questions:", err);
			} finally {
				loading.value = false;
			}
		};

		onMounted(() => {
			fetchTriviaQuestions();
			const intervalId = setInterval(fetchTriviaQuestions, 10000); // Fetch new questions every 60 seconds

			onBeforeUnmount(() => {
				clearInterval(intervalId);
			});
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

<style scoped>
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
	opacity: 0;
}
</style>
