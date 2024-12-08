<template>
	<div
		class="flex flex-col w-full px-5 py-5 overflow-auto bg-field dark:bg-dark-notif sm:px-12 sm:pt-10 h-screen"
	>
		<div class="flex justify-end items-center text-end w-full h-10">
			<router-link
				to="create-itinerary"
				class="flex items-center justify-center rounded-full font-montserrat px-6 py-2 text-lg font-semibold text-white text-center bg-gradient-to-r from-purple-500 to-indigo-600 transform transition-all duration-300 ease-in-out shadow-md hover:scale-105 hover:from-purple-600 hover:to-indigo-700 hover:shadow-lg"
			>
				+ Create
			</router-link>
		</div>

		<div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-7">
			<div
				v-for="(itinerary, index) in itineraries"
				:key="itinerary.id"
				@click="goToViewItinerary(itinerary.id)"
				class="bg-dark-field rounded-xl overflow-hidden shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300 cursor-pointer"
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
							class="text-3xl font-bold text-white tracking-wide font-['Bebas_Neue']"
						>
							{{ itinerary.main_title }}
						</h2>
						<div class="flex items-center">
							<StarIcon class="size-4 text-blue-400" />
							<span class="ml-2 text-white text-xs"
								>{{ avgRating.toFixed(1) }} / 5</span
							>
						</div>
					</div>

					<p class="text-gray-300 text-xs mb-4">
						{{
							isFullTextShown[index]
								? itinerary.main_description
								: truncateText(itinerary.main_description, 100)
						}}
						<button
							@click="toggleText(index)"
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
							<span class="text-gray-300 text-xs border-r-2 pr-2"
								>@{{ itinerary.creator_name }}</span
							>

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
import ViewItinerary from "./ViewItinerary.vue";
import { StarIcon } from "@heroicons/vue/24/outline";
const store = useStore();
const router = useRouter();

const itineraries = computed(() => store.getters.getItineraries.reverse());
const isFullTextShown = ref({});
const allRatings = ref([4, 3.5, 5, 4.2]); // Simulated ratings from different users

const avgRating = computed(() => {
	if (allRatings.value.length === 0) return 0;
	const total = allRatings.value.reduce((sum, current) => sum + current, 0);
	return total / allRatings.value.length;
});

const fetchItineraries = async () => {
	try {
		await store.dispatch("fetchItineraries");
	} catch (error) {
		console.error(error);
	}
};

const goToViewItinerary = (itinerarydata) => {
	router.push({
		name: "view-itinerary",
		query: { id: itinerarydata },
	});
};

const toggleText = (index) => {
	isFullTextShown.value[index] = !isFullTextShown.value[index];
};

watch(itineraries, (newVal) => {
	isFullTextShown.value = newVal.reduce((acc, _, index) => {
		acc[index] = false; // Initialize all as false (collapsed)
		return acc;
	}, {});
});
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
onMounted(() => {
	fetchItineraries();
});
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);

fieldset,




/****** Style Star Rating Widget *****/

.rating {
	border: none;
	float: left;
}

.rating > input {
	display: none;
}
.rating > label:before {
	margin: 5px;
	font-size: 1.25em;
	font-family: FontAwesome;
	display: inline-block;
	content: "\f005";
}

.rating > .half:before {
	content: "\f089";
	position: absolute;
}

.rating > label {
	color: #ddd;
	float: right;
}

/***** CSS Magic to Highlight Stars on Hover *****/

.rating > input:checked ~ label, /* show gold star when clicked */
.rating:not(:checked) > label:hover, /* hover current star */
.rating:not(:checked) > label:hover ~ label {
	color: #ffd700;
} /* hover previous stars in list */

.rating > input:checked + label:hover, /* hover current star when changing rating */
.rating > input:checked ~ label:hover,
.rating > label:hover ~ input:checked ~ label, /* lighten current selection */
.rating > input:checked ~ label:hover ~ label {
	color: #ffed85;
}
</style>
