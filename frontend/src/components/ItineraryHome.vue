<template>
	<div
		class="flex flex-col w-full px-5 py-5 overflow-auto bg-field pt-20 sm:px-28 sm:ml-64 sm:pt-3"
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
			class="mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface sm:w-11/12 sm:px-6 sm:h-[650px]"
		>
			<div class="sm:h-96 mt-2 sm:px-5 sm:pt-5 mb-10 w-full">
				<img
					class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-full"
					src="/sample_img/binondo.webp"
					alt=""
				/>
				<div class="w-full h-auto py-4">
					<h1
						class="font-bebas-neue text-prime text-3xl mt-5 sm:text-4xl"
					>
						BINONDO GUIDE FOR 2024
					</h1>
					<p class="font-montserrat text-sm sm:text-sm text-justify">
						My name is Elle, and I am a proud Filipino who has a
						deep appreciation for visiting Binondo in Manila.
						Binondo is renowned as the world's oldest Chinatown, and
						it holds a special place in my heart for its rich
						cultural heritage and vibrant atmosphere....
					</p>
				</div>
				<div class="flex items-center mt-5">
					<img
						class="rounded-full w-12 shadow-2xl drop-shadow-xl sm:w-[80px]sm:mb-8"
						src="/sample_img/mark.png"
						alt=""
					/>
					<h1
						class="font-montserrat font-semibold text-prime ml-2 pr-2 border border-l-0 border-y-0 border-r-prime hover:underline cursor-pointer sm:font-normal sm:text-sm sm:ml-5 sm:pr-5"
					>
						@Jake_Citrus
					</h1>
					<h1
						class="font-montserrat text-xs text-second ml-2 sm:text-sm sm:ml-5"
					>
						June 19, 2024hihihihihihiih
					</h1>
				</div>
			</div>
		</div>
		<div
			class="cont-itinerary mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface sm:w-11/12 sm:px-6"
			v-for="(itinerary, index) in itineraries"
			:key="index"
			
		>
			<div class="mt-2 sm:px-5 sm:pt-5 mb-10 w-full">
				<img
					class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-full"
					src="/sample_img/binondo.webp"
					alt=""
				/>
				<div class="w-full h-auto py-2">
					<h1
						class="font-bebas-neue text-prime text-3xl mt-5 sm:text-4xl"
					>
						{{ itinerary.main_title }}
					</h1>
					<p class="font-montserrat text-sm text-justify h-auto">
						{{
							isFullTextShown[index]
								? itinerary.main_description
								: itinerary.main_description.length > 500
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
						class="font-montserrat font-semibold text-prime ml-2 pr-2 border border-l-0 border-y-0 border-r-prime hover:underline cursor-pointer sm:font-normal sm:text-sm sm:ml-5 sm:pr-5"
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
export default {
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
		toggleText(index) {
			this.isFullTextShown[index] = !this.isFullTextShown[index];
		},
		async fetchItineraries() {
			try {
				const response = await this.client.get("/api/save-itinerary");
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
