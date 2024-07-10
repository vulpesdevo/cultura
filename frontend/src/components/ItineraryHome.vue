<template>
	<div
		class="flex flex-col w-full px-5 py-5 overflow-auto bg-field dark:bg-dark-notif pt-20 sm:px-28 sm:ml-64 sm:pt-3 h-screen"
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
			@click="goToViewItinerary(itinerary.id)"
		>
			
			<div class="mt-2 sm:px-5 sm:pt-5 mb-10 w-full">
				<img
					class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-auto"
					:src="itinerary.main_image"
					alt=""
				/>
				<div class="w-full h-auto py-2">
					<h1
						class="font-bebas-neue text-prime dark:text-interface text-3xl mt-5 sm:text-4xl"
					>
						{{ itinerary.main_title }}
					</h1>
					<p class="font-montserrat text-sm text-justify h-auto dark:text-interface">
						{{
							isFullTextShown[index]
								? itinerary.main_description
								: itinerary.main_description.length > 100
								? itinerary.main_description.substring(0, 100) +"..."
								: itinerary.main_description
						}}
						<!-- Toggle link -->
						<a
							href="#"
							@click.prevent="toggleText(index)"
							class="text-blue-500"
						>
							{{
								isFullTextShown[index] ? "see less" : "see more"
							}}
						</a>
					</p>
				</div>
				<div class="flex items-center mt-5">
					<img
						class="rounded-full w-12 shadow-2xl drop-shadow-xl sm:w-[80px]sm:mb-8"
						src="/sample_img/mark.png"
						alt=""
					/>
					<h1
						class="font-montserrat font-semibold text-prime dark:text-interface  ml-2 pr-2 border border-l-0 border-y-0 border-r-prime dark:border-r-interface hover:underline cursor-pointer sm:font-normal sm:text-sm sm:ml-5 sm:pr-5"
					>
						@{{ itinerary.creator_name }}
					</h1>
					<h1
						class="font-montserrat text-xs text-second ml-2 sm:text-sm sm:ml-5"
					>
						{{
							new Date(itinerary.date_posted).toLocaleDateString(
								"en-US",
								{
									month: "long",
									day: "numeric",
									year: "numeric",
								}
							)
						}}
					</h1>
				</div>
			</div>
		</div>

		<div class="mt-10"></div>
	</div>
</template>

<script>
import axios from "axios";
import ViewItinerary from "./ViewItinerary.vue";
export default {
	components: {
		ViewItinerary,
	},
	data() {
		return {
			itineraries: [],
			isFullTextShown: {}, // Initialize as empty object
		};
	},
	watch: {
		// Watcher to update isFullTextShown when itineraries changes
		itineraries(newVal) {
			this.isFullTextShown = newVal.reduce((acc, _, index) => {
				acc[index] = false; // Initialize all as false (collapsed)
				return acc;
			}, {});
		},
	},
	mounted() {
		this.fetchItineraries();
	},
	created() {
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		this.client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: headers,
		});
		this.fetchItineraries();
	},
	methods: {
		goToViewItinerary(itinerarydata) {
			this.$router.push({ name: "view-itinerary", params: { itinerarydata } });
		},
		toggleText(index) {
			this.isFullTextShown[index] = !this.isFullTextShown[index];
		},
		async fetchItineraries() {
			try {
				const response = await this.client.get("/api/saved-itinerary");
				this.itineraries = response.data;
				console.log(this.itineraries);
			} catch (error) {
				console.error(error);
			}
		},
	},
};
</script>

<style></style>
