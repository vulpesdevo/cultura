<template>
	<div
		class="flex flex-col w-full px-5 py-5 overflow-auto bg-field dark:bg-dark-notif sm:px-12 sm:pt-10 h-screen"
	>
		<div class="flex justify-between items-center mb-5">
			<button
				@click="toggleMyItineraries"
				class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
			>
				{{
					showMyItineraries
						? "Show All Itineraries"
						: "Show My Itineraries"
				}}
			</button>
			<router-link
				to="create-itinerary"
				class="flex px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
			>
				<PlusIcon class="h-5 w-5 mr-2" />
				Create Itinerary
			</router-link>
		</div>

		<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-7">
			<div
				v-for="(itinerary, index) in filteredItineraries"
				:key="itinerary.id"
				@click="goToViewItinerary(itinerary.id)"
				class="h-full bg-interface dark:bg-dark-field rounded-xl overflow-hidden shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer"
			>
				<!-- Image Container -->
				<div class="aspect-[16/9] overflow-hidden rounded-t-xl">
					<img
						:src="itinerary.main_image"
						:alt="itinerary.main_title"
						class="w-full h-full object-cover"
					/>
				</div>

				<!-- Content Container -->
				<div class="p-6">
					<div class="flex justify-between items-start mb-3">
						<h2
							class="text-3xl font-bold text-prime dark:text-white tracking-wide font-['Bebas_Neue']"
						>
							{{ itinerary.main_title }}
						</h2>
						<div class="flex items-center">
							<StarIcon class="size-4 text-blue-400" />
							<span
								class="ml-2 text-prime dark:text-white text-xs"
							>
								{{
									calculateAvgRating(
										itinerary.rating
									).toFixed(1)
								}}
								/ 5
							</span>
						</div>
					</div>

					<p class="text-prime dark:text-gray-300 text-xs mb-4">
						{{
							isFullTextShown[index]
								? itinerary.main_description
								: truncateText(itinerary.main_description, 100)
						}}
						<button
							@click.stop="toggleText(index)"
							class="text-blue-400 hover:text-blue-300 ml-2 focus:outline-none"
						>
							{{
								isFullTextShown[index] ? "see less" : "see more"
							}}
						</button>
					</p>

					<!-- User Info -->
					<div class="flex items-center gap-3">
						<img
							:src="itinerary.user_photo"
							:alt="itinerary.creator_name"
							class="w-12 h-12 rounded-full object-cover"
						/>
						<div class="flex items-center gap-2">
							<span
								class="text-prime dark:text-gray-300 text-xs border-r-2 pr-2"
							>
								@{{ itinerary.creator_name }}
							</span>
							<span class="text-second text-xs">
								{{ formatDate(itinerary.date_posted) }}
							</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { StarIcon, PlusIcon } from "@heroicons/vue/24/outline";

const store = useStore();
const router = useRouter();

const showMyItineraries = ref(false);
const isFullTextShown = ref({});

const allItineraries = computed(() => store.getters.getItineraries.reverse());
const currentUserId = computed(() => store.state.user.data.user.id);

const filteredItineraries = computed(() => {
	if (showMyItineraries.value) {
		return allItineraries.value.filter(
			(itinerary) => itinerary.owner === currentUserId.value
		);
	}
	return allItineraries.value;
});

const toggleMyItineraries = () => {
	showMyItineraries.value = !showMyItineraries.value;
};

const calculateAvgRating = (ratings) => {
	if (!ratings || ratings.length === 0) return 0;
	let ratingValues;
	try {
		ratingValues = JSON.parse(ratings).map((r) => r.rating);
	} catch (error) {
		console.error("Error parsing ratings:", error);
		return 0;
	}
	if (!Array.isArray(ratingValues) || ratingValues.length === 0) return 0;
	const total = ratingValues.reduce((sum, current) => sum + current, 0);
	return total / ratingValues.length;
};

const fetchItineraries = async () => {
	try {
		await store.dispatch("fetchItineraries");
	} catch (error) {
		console.error(error);
	}
};

const goToViewItinerary = (itineraryId) => {
	router.push({
		name: "view-itinerary",
		query: { id: itineraryId },
	});
};

const toggleText = (index) => {
	isFullTextShown.value[index] = !isFullTextShown.value[index];
};

const truncateText = (text, length) => {
	if (text.length <= length) return text;
	return text.slice(0, length) + "...";
};

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleDateString("en-US", {
		month: "long",
		day: "numeric",
		year: "numeric",
	});
};

watch(filteredItineraries, (newVal) => {
	isFullTextShown.value = newVal.reduce((acc, _, index) => {
		acc[index] = false;
		return acc;
	}, {});
});

onMounted(() => {
	fetchItineraries();
});
</script>

<style scoped>
/* Your existing styles remain unchanged */
</style>
