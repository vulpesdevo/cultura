<template>
	<div
		class="relative flex flex-col w-full px-5 py-5 overflow-auto bg-field dark:bg-dark-notif sm:px-12 sm:pt-10 h-screen transition-colors duration-300"
	>
		<div
			class="fixed top-0 w-full flex justify-start items-center mb-5 bg-field h-16 z-20"
		>
			<button
				@click="toggleMyItineraries"
				class="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 mr-2"
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

		<div
			class="itinerary-container grid grid-cols-1 sm:grid-cols-2 gap-3 mt-7"
			@scroll="onScroll"
		>
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
			<div
				v-if="loading"
				class="loading border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full h-full mx-auto mt-10"
			>
				<div class="animate-pulse flex space-x-4">
					<div
						class="rounded-full bg-gray-500 dark:bg-slate-700 h-10 w-10"
					></div>
					<div class="flex-1 space-y-6 py-1">
						<div
							class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
						></div>
						<div class="space-y-3">
							<div class="grid grid-cols-3 gap-4">
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-2"
								></div>
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-1"
								></div>
							</div>
							<div
								class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
							></div>
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
import axiosClient from "../axios";
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
	try {
		const parsedRatings = ratings;
		if (Array.isArray(parsedRatings) && parsedRatings.length > 0) {
			const total = parsedRatings.reduce(
				(sum, current) => sum + current.rating,
				0
			);
			return total / parsedRatings.length;
		}
		return 0;
	} catch (error) {
		console.error("Error parsing ratings:", error);
		return 0;
	}
};
const page = ref(1); // Current page number
const perPage = 6; // Items per page
const loading = ref(false); // Loading state
const hasMore = ref(true); // Whether more data is available

const fetchItineraries = async () => {
	if (!hasMore.value || loading.value) return; // Avoid multiple calls

	loading.value = true;
	try {
		const moreItineraries = await store.dispatch("fetchItineraries", {
			page: page.value,
			perPage,
		});
		console.log("MORE ITINERARIES : ", store.getters.getItineraries);

		if (!moreItineraries) {
			hasMore.value = false; // No more data available
		}
		page.value++;
	} catch (error) {
		console.error("Error fetching itineraries:", error);
	} finally {
		loading.value = false;
	}
};
const onScroll = (event) => {
	const container = event.target;
	if (
		container.scrollTop + container.clientHeight >=
		container.scrollHeight - 10
	) {
		fetchItineraries(); // Load more data when scrolled to the bottom
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

onMounted(async () => {
	await fetchItineraries();
});
</script>

<style scoped>
/* Your existing styles remain unchanged */
</style>
