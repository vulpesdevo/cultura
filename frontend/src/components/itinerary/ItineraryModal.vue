<template>
	<div
		class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4"
	>
		<div class="bg-white dark:bg-gray-800 rounded-lg w-full max-w-md">
			<div class="p-6">
				<h3
					class="text-xl font-bold mb-4 text-gray-800 dark:text-white"
				>
					Select Itinerary
				</h3>
				<div class="max-h-60 overflow-y-auto mb-4">
					<div
						v-for="itinerary in itineraries"
						:key="itinerary.id"
						@click="selectItinerary(itinerary)"
						class="mb-2 p-2 bg-gray-100 dark:bg-gray-700 rounded cursor-pointer hover:bg-gray-200 dark:hover:bg-gray-600"
					>
						<h4 class="font-bold text-gray-800 dark:text-white">
							{{ itinerary.main_title }}
						</h4>
						<p class="text-sm text-gray-600 dark:text-gray-300">
							{{ itinerary.main_description }}
						</p>
					</div>
				</div>
				<div class="flex justify-end">
					<button
						@click="$emit('close')"
						class="px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400"
					>
						Cancel
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
defineProps(["itineraries"]);
const emit = defineEmits(["close", "selected-itinerary"]);

const selectItinerary = (itinerary) => {
	emit("selected-itinerary", itinerary);
};
</script>
