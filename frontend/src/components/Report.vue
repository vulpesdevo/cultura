<template>
	<div
		class="h-screen bg-gray-900 flex justify-center items-center px-4 py-12"
	>
		<div
			class="w-full max-w-3xl bg-white dark:bg-gray-800 rounded-lg shadow-xl overflow-hidden"
		>
			<div class="p-8">
				<h2
					class="text-3xl font-bold text-gray-900 dark:text-white text-center mb-6"
				>
					Report Content
				</h2>
				<div class="mb-8">
					<div class="flex items-center">
						<div
							v-for="stepNumber in 3"
							:key="stepNumber"
							class="flex items-center"
						>
							<div
								:class="[
									'rounded-full h-8 w-8 flex items-center justify-center border-2',
									step >= stepNumber
										? 'border-blue-500 bg-blue-500 text-white'
										: 'border-gray-300 text-gray-300',
								]"
							>
								{{ stepNumber }}
							</div>
							<div
								v-if="stepNumber < 3"
								:class="[
									'flex-1 h-1 mx-2',
									step > stepNumber
										? 'bg-blue-500'
										: 'bg-gray-300',
								]"
							></div>
						</div>
					</div>
				</div>

				<div v-if="step === 1">
					<h3
						class="text-xl font-semibold text-gray-900 dark:text-white mb-4"
					>
						Why are you reporting this post?
					</h3>
					<p class="text-gray-600 dark:text-gray-400 mb-6">
						If you believe this post suggests someone is in
						immediate danger, contact local authorities first for
						help before reporting it to CulturaLink.
					</p>
					<div class="space-y-4">
						<label
							v-for="category in categories"
							:key="category"
							class="flex items-center p-4 border rounded-lg cursor-pointer transition-colors"
							:class="[
								selectedCategory === category
									? 'border-blue-500 bg-blue-50 dark:bg-blue-900'
									: 'border-gray-200 dark:border-gray-700',
							]"
						>
							<input
								type="radio"
								:value="category"
								v-model="selectedCategory"
								class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
							/>
							<span class="ml-3 text-gray-900 dark:text-white">{{
								category
							}}</span>
						</label>
					</div>
				</div>

				<div v-if="step === 2">
					<h3
						class="text-xl font-semibold text-gray-900 dark:text-white mb-4"
					>
						Please elaborate on the problem
					</h3>
					<textarea
						v-model="reportDetails"
						rows="5"
						class="w-full p-3 border rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
						placeholder="Provide a brief explanation for your report..."
					></textarea>
				</div>

				<div v-if="step === 3">
					<h3
						class="text-xl font-semibold text-gray-900 dark:text-white mb-4"
					>
						Confirm your report
					</h3>
					<p class="text-gray-600 dark:text-gray-400 mb-6">
						Please review the details of your report carefully. Once
						submitted, the report cannot be changed or undone.
					</p>
					<div
						class="bg-gray-100 dark:bg-gray-700 rounded-lg p-4 mb-4"
					>
						<p class="text-gray-900 dark:text-white">
							<strong>Category:</strong> {{ selectedCategory }}
						</p>
						<p class="text-gray-900 dark:text-white mt-2">
							<strong>Details:</strong> {{ reportDetails }}
						</p>
					</div>
				</div>

				<div class="flex justify-between mt-8">
					<button
						@click="goBack"
						class="px-6 py-2 border border-gray-300 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
					>
						{{ step === 1 ? "Cancel" : "Back" }}
					</button>
					<button
						@click="step === 3 ? submitReport() : nextStep()"
						:disabled="!canProceed"
						class="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
					>
						{{ step === 3 ? "Submit" : "Next" }}
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";
import axiosClient from "../axios";
const router = useRouter();
const route = useRoute();
const store = useStore();

const step = ref(1);
const selectedCategory = ref("");
const reportDetails = ref("");
const categories = [
	"Violent, hateful, or disturbing content",
	"Scam or false information",
	"Bullying, harassment or abuse",
	"Adult Content",
];

const postId = route.query.post_id;
const userId = route.query.user_id;
console.log("post: " + postId + " user:" + userId);

const canProceed = computed(() => {
	if (step.value === 1) return selectedCategory.value !== "";
	if (step.value === 2) return reportDetails.value.trim() !== "";
	return true;
});

const nextStep = () => {
	if (canProceed.value) step.value++;
};

const goBack = () => {
	if (step.value === 1) {
		router.push("/dashboard");
	} else {
		step.value--;
	}
};

const submitReport = async () => {
	try {
		const response = await store.dispatch("createReport", {
			post_id: postId,
			category: selectedCategory.value,
			details: reportDetails.value,
		});
		console.log("Report sent successfully:", response);
		router.push({ name: "dashboard" });
	} catch (error) {
		console.error("Error sending report:", error);
		// Handle error (e.g., show an error message)
	}
};
</script>
