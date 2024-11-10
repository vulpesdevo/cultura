<template>
	<div
		class="flex flex-col w-full px-5 py-5 overflow-auto bg-field dark:bg-dark-notif sm:px-28 sm:pt-3 h-screen"
	>
		<div
			class="flex justify-end items-center text-end w-full sm:w-11/12 h-10"
		>
			<router-link
				to="create-itinerary"
				class="flex items-center justify-center rounded-full font-montserrat h-full w-32 text-xl text-center bg-second text-white"
				>+ Create</router-link
			>
		</div>

		<div
			class="cont-itinerary mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface dark:bg-dark-interface cursor-pointer sm:w-11/12 sm:px-6"
			v-for="(itinerary, index) in itineraries"
			:key="itinerary.id"
		>
			<div class="mt-2 sm:px-5 sm:pt-5 mb-10 w-full">
				<img
					class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-auto"
					:src="itinerary.main_image"
					alt=""
				/>
				<div class="w-full h-auto py-2">
					<!-- <div class="flex flex-row justify-start items-center"> -->
					<div class="flex justify-between items-center mt-5">
						<h1
							class="font-bebas-neue text-prime dark:text-interface text-3xl sm:text-4xl"
						>
							{{ itinerary.main_title }}
						</h1>
						<!-- | RATING CONTAINER-->
						<div class="flex items-center">
							<i
								class="fa-solid fa-star sm:text-2xl text-xl text-second"
							></i>
							<div
								class="sm:text-lg ml-2 font-montserrat text-sm text-prime dark:text-white"
							>
								{{ avgRating.toFixed(1) }} / 5
							</div>
						</div>
					</div>
					<p
						class="font-montserrat text-sm text-justify h-auto dark:text-interface"
					>
						{{
							isFullTextShown[index]
								? itinerary.main_description
								: itinerary.main_description.length > 100
								? itinerary.main_description.substring(0, 100) +
								  "..."
								: itinerary.main_description
						}}
						<!-- Toggle link -->
						<a
							href="#"
							@click="goToViewItinerary(itinerary.id)"
							class="text-blue-500"
						>
							{{
								isFullTextShown[index] ? "see less" : "see more"
							}}
						</a>
					</p>
				</div>
				<div class="flex justify-between">
					<div class="flex items-center mt-5">
						<img
							class="rounded-full size-12 object-cover shadow-2xl drop-shadow-xl sm:w-[80px]sm:mb-8"
							:src="itinerary.user_photo"
							alt=""
						/>
						<h1
							class="font-montserrat font-semibold text-prime dark:text-interface ml-2 pr-2 border border-l-0 border-y-0 border-r-prime dark:border-r-interface hover:underline cursor-pointer sm:font-normal sm:text-sm sm:ml-5 sm:pr-5"
						>
							@{{ itinerary.creator_name }}
						</h1>
						<h1
							class="font-montserrat text-xs text-second ml-2 sm:text-sm sm:ml-5"
						>
							{{
								new Date(
									itinerary.date_posted
								).toLocaleDateString("en-US", {
									month: "long",
									day: "numeric",
									year: "numeric",
								})
							}}
						</h1>
					</div>
				</div>
			</div>
		</div>

		<div class="mt-10"></div>
	</div>
</template>
<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import ViewItinerary from "./ViewItinerary.vue";

const store = useStore();
const router = useRouter();

const itineraries = computed(() => store.getters.getItineraries);
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
		params: { itinerarydata },
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
