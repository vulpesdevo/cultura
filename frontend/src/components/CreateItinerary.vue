<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-20 sm:pt-3"
	>
		<div
			class="field-editable flex flex-col justify-start items-center w-full bg-interface rounded-2xl p-1"
		>
			<div class="relative title-image h-96 w-full rounded-2xl">
				<div class="w-full h-[87%] bg-second rounded-2xl">
					<img
						src="/sample_img/binondo.webp"
						alt="sample-img-binondo"
						class="w-full h-full object-cover rounded-2xl"
					/>
				</div>
				<div
					class="flex absolute bottom-0 left-32 bg-prime w-3/4 h-24 z-10 rounded-lg text-center items-center justify-center"
				>
					<h1
						class="font-bebas-neue text-interface text-center text-6xl"
					>
						BINOndo guide for 2024
					</h1>
				</div>
			</div>
			<div class="flex flex-col items-center mt-10 px-16 w-full">
				<div class="post-content flex w-full">
					<div class="w-14 h-14 mr-4">
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="rounded-full cursor-pointer"
						/>
					</div>
					<div class="w-full">
						<div class="flex">
							<p
								class="font-montserrat text-prime text-base pb-3"
							>
								@mark0
							</p>
						</div>
						<textarea
							class="w-[93%] rounded-lg resize-none p-4 outline-none bg-gray-200"
							name=""
							id="set-about"
							v-model="setAboutMe"
							cols="30"
							rows="4"
							placeholder="What do you want to share?"
						></textarea>
					</div>
				</div>
				<div class="flex flex-col w-full">
					<label
						for=""
						class="font-montserrat text-prime text-xl font-semibold m-3"
						>General Tips</label
					>
					<textarea
						class="w-[86%] rounded-lg resize-none ml-16 p-4 outline-none bg-gray-200"
						name=""
						id="set-tips"
						v-model="setTips"
						cols="30"
						rows="4"
						placeholder="What do you want to share?"
					></textarea>
				</div>
				<div
					class="font-montserrat flex flex-col justify-center items-center w-full py-3"
				>
					<label
						for=""
						class="text-prime text-xl font-semibold m-3 pl-4 w-full text-left"
						>Budgeting</label
					>

					<div class="flex justify-between w-3/4 h-20 text-interface">
						<div
							class="flex flex-col justify-center items-center bg-prime w-1/2 mr-10 rounded-lg"
						>
							<p class="">Total Budget</p>
							<p class="text-2xl">₱ 2000</p>
						</div>
						<div
							class="flex flex-col justify-center bg-prime w-1/2 rounded-lg p-3"
						>
							<p class="">Currency</p>
							<p class="pb-1 text-xl">PHP Philippine Peso</p>
						</div>
					</div>
				</div>
			</div>
			<div class="flex flex-col h-[45rem] w-full my-5">
				<h1 class="text-center text-prime text-xl mb-4">
					Main Itinerary
				</h1>
				<div class="flex w-full h-[700px] px-16">
					<div class="flex flex-col w-1/2 mr-5">
						<button
							class="h-[7%] w-auto m-2 bg-second rounded-lg"
							@click.prevent="showModal = true"
							@click="initializeAutocomplete"
						>
							Add place
						</button>
						<div
							class="overflow-auto h-screen m-2 rounded-lg"
							style="scrollbar-width: none"
						>
							<div
								class="f</div>lex-col justify-center items-center w-full h-80 font-montserrat text-prime bg-stone-200 mb-3 rounded-lg"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-evenly items-center"
								>
									<h1 class="text-2xl py-3 text-center">
										Lucky Chinatown Mall
									</h1>
									<p class="text-justify text-sm px-4">
										Lucky Chinatown offers a unique blend of
										history, tradition and modern shopping
										and world-class leisure experience.
									</p>
									<p
										class="flex rounded-full bg-second w-24 h-8 text-center items-center justify-center mt-7"
									>
										P2000
									</p>
									<!-- <p class="rounded-full bg-second text-center inline-block py-1 px-2"
										:style="{ width: `${text.length * 10}px` }"
									>{{ text }}</p> -->
								</div>
							</div>
							<div
								class="flex-col justify-center items-center w-full h-80 font-montserrat text-prime bg-stone-200 shadow-lg mb-3 rounded-lg"
								v-for="(itinerary, index) in list_itineraries"
								:key="index"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-evenly items-center"
								>
									<h1 class="text-2xl py-3 text-center">
										{{ itinerary.title }}
									</h1>
									<p class="text-justify text-sm px-4">
										{{ itinerary.description }}
									</p>
									<p
										class="flex rounded-full bg-second w-24 h-8 text-center items-center justify-center mt-7"
									>
										P{{ itinerary.budget }}
									</p>
									<!-- <p class="rounded-full bg-second text-center inline-block py-1 px-2"
										:style="{ width: `${text.length * 10}px` }"
									>{{ text }}</p> -->
								</div>
							</div>
						</div>
					</div>
					<div class="h-full w-1/2 px-5 pb-5 pt-2">
						<div
							id="the-map"
							class="h-full w-full rounded-lg"
						></div>
					</div>
				</div>
			</div>
		</div>

		<div
			class="fixed z-50 inset-0 overflow-y-auto"
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
		>
			<div
				class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0 w-screen"
			>
				<div
					class="fixed inset-0 bg-black bg-opacity-70 transition-opacity w-screen"
					aria-hidden="true"
				></div>
				<span
					class="hidden sm:inline-block sm:align-middle sm:h-screen"
					aria-hidden="true"
					>&#8203;</span
				>
				<div
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle w-[35%]"
				>
					<div
						class="bg-interface px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<div
							class="flex justify-center items-center w-full h-52 rounded-lg bg-field"
						>
							<p>+ Add Image</p>
						</div>
						<h3
							class="font-bebas-neue text-5xl pt-5 sm:text-3xl leading-6 font-medium text-prime"
							id="modal-title"
						>
							add place
						</h3>

						<form class="mt-2" @submit.prevent="submitItinerary">
							<div class="flex">
								<div
									class="w-full px-3 text-start text-sm font-montserrat"
								>
									<div class="">
										<label for="it-title">Title</label>
										<input
											type="text"
											placeholder="Title"
											name="it-title"
											id="it-title"
											v-model="title"
											class="mt-2 pl-5 w-full rounded-full h-12 bg-field"
										/>
									</div>
									<div class="mt-2">
										<label for="it-location"
											>Set Location's Pin</label
										>
										<div
											class="flex relative justify-center items-center"
										>
											<input
												type="text"
												placeholder="Location"
												name="auto-complete"
												ref="autocomplete"
												id="autocomplete"
												v-model="location"
												class="mt-2 pl-5 w-full rounded-full h-12 bg-field"
											/>
											<span
												class="flex justify-center items-center material-icons-outlined absolute right-0 bottom-0 text-prime text-center bg-gray-500 hover:bg-gray-400 w-12 h-12 rounded-full cursor-pointer"
												@click="locatorBtn"
											>
												location_searching
											</span>
										</div>
									</div>
									<div class="mt-2">
										<label for="it-budget"
											>Set a Budget</label
										>
										<input
											type="text"
											placeholder="Budget"
											name="it-budget"
											id="it-budget"
											v-model="budget"
											class="mt-2 pl-5 w-full rounded-full h-12 bg-field"
										/>
									</div>
									<div class="flex flex-col mt-2">
										<label for="it-description"
											>Add description</label
										>
										<textarea
											class="rounded-lg resize-none p-4 outline-none bg-field"
											name=""
											id="it-description"
											v-model="description"
											cols="30"
											rows="4"
											placeholder="Add notes, links, descriptions or whatever you want your fellow travelers to know about this place!"
										></textarea>
									</div>
									<div class="">
										<input type="text" v-model="latitude" />
										<input
											type="text"
											v-model="longitude"
										/>
									</div>
								</div>
							</div>

							<div
								class="flex flex-col items-center align-middle text-center mt-5"
							>
								<div class="flex font-montserrat">
									<button
										class="text-interface text-lg bg-gray-500 p-2 rounded-3xl w-32 h-14 mb-3 hover:bg-gray-400 mr-5"
										@click="showModal = false"
									>
										Cancel
									</button>
									<input
										type="submit"
										value="Save"
										class="text-interface text-lg bg-second p-2 rounded-3xl w-32 h-14 mb-3 hover:bg-second-light"
										@click="fetchItineraries"
									/>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
// import { Loader } from "@googlemaps/js-api-loader";

export default {
	data() {
		return {
			showModal: false,
			latitude: 0,
			longitude: 0,
			location: null,
			list_itineraries: [],
		};
	},
	mounted() {
		this.initializeAutocomplete();

		this.fetchItineraries();

		if (!this.list_itineraries) {
			setInterval(this.fetchItineraries, 1000);
		}

		// this.$nextTick(() => {
		// 	try {
		// 		new google.maps.places.Autocomplete(
		// 			document.getElementById("auto-complete")
		// 		);
		// 	} catch (error) {
		// 		console.error(
		// 			"Error initializing Google Places Autocomplete:",
		// 			error
		// 		);
		// 	}
		// });
	},
	methods: {
		fetchItineraries() {
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			const client = axios.create({
				baseURL: "http://127.0.0.1:8000",
				withCredentials: true,
				timeout: 5000,
				xsrfCookieName: "csrftoken",
				xsrfHeaderName: "X-Csrftoken",
				headers: headers,
			});
			client
				.get("/api/itinerary")
				.then((response) => {
					this.list_itineraries = response.data;
					console.log("list_itineraries:", this.list_itineraries);
					// this.list_itineraries.forEach((item) => { ;
					// 	this.showLocationOntheMap(latitude, longitude);
					// });
					this.showLocationOntheMap();
				})
				.catch((error) => {
					console.log(error);
				});
		},
		showLocationOntheMap() {
			// const lat = 37.7749;
			// const lng = -122.4194;

			const map = new google.maps.Map(
				document.getElementById("the-map"),
				{
					mapTypeId: google.maps.MapTypeId.ROADMAP,
					mapId: "2c9b57c42de97202",
				}
			);

			let bounds = new google.maps.LatLngBounds();
			const directionsService = new google.maps.DirectionsService();
			const directionsRenderer = new google.maps.DirectionsRenderer({
				map: map,
			});

			// Assuming the first item is the start, the last is the end, and the rest are waypoints
			const start = this.list_itineraries[0];
			const end = this.list_itineraries[this.list_itineraries.length - 1];
			const waypoints = this.list_itineraries
				.slice(1, -1)
				.map((itinerary) => ({
					location: new google.maps.LatLng(
						itinerary.latitude,
						itinerary.longitude
					),
					stopover: true,
				}));

			const request = {
				origin: new google.maps.LatLng(start.latitude, start.longitude),
				destination: new google.maps.LatLng(
					end.latitude,
					end.longitude
				),
				waypoints: waypoints,
				travelMode: google.maps.TravelMode.DRIVING,
				optimizeWaypoints: false, // Set to true if you want Google to reorder the waypoints for the shortest route
			};

			directionsService.route(request, (result, status) => {
				if (status == google.maps.DirectionsStatus.OK) {
					directionsRenderer.setDirections(result);
				} else {
					console.error("Directions request failed due to " + status);
				}
			});

			// Extend bounds to include start and end
			bounds.extend(
				new google.maps.LatLng(start.latitude, start.longitude)
			);
			bounds.extend(new google.maps.LatLng(end.latitude, end.longitude));
			map.fitBounds(bounds);

			// Optional: adjust the zoom level after fitting bounds if the zoom is too close or too far
			// This is a workaround because fitBounds does not let you specify max zoom level
		},
		initializeAutocomplete() {
			this.$nextTick(() => {
				// Ensures the DOM is updated
				const inputElement = this.$refs.autocomplete;

				// Define the bounds for the Cavite area

				const autocomplete = new google.maps.places.Autocomplete(
					inputElement
				);

				autocomplete.addListener("place_changed", () => {
					// Get the place object from the autocomplete widget
					const place = autocomplete.getPlace();

					// Check if the place has a geometry property
					if (place.geometry) {
						// Extract the latitude and longitude from the place's geometry
						this.latitude = place.geometry.location.lat();
						this.longitude = place.geometry.location.lng();
						this.location = place.formatted_address;
						// Now you can use the latitude and longitude for whatever you need
					} else {
						console.log("Selected place does not have a geometry");
					}
				});
			});
		},
		locatorBtn() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(
					(position) => {
						const { latitude, longitude } = position.coords;
						this.getAddressFrom(latitude, longitude);
					},
					(error) => {
						console.log(error.message);
					}
				);
			}
		},
		getAddressFrom(lat, long) {
			axios
				.get(
					`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${long}&key=AIzaSyAlo4jqabMxIygmvXtD-K0tm1HJEecnrEA`
				)
				.then((response) => {
					const address = response.data.error_message
						? response.data.error_message
						: response.data.results[0].formatted_address;

					console.log(address);
					const inputElement = this.$refs.autocomplete;
					inputElement.value = address;
				})
				.catch((error) => {
					console.log(error.message);
				});
		},
	},
	setup() {
		const setTips = ref("");
		const setAboutMe = ref("");
		const location = ref("");
		const title = ref("");
		const budget = ref("");
		const description = ref("");
		const latitude = ref("");
		const longitude = ref("");

		const showModal = ref(false);
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: headers,
		});

		const submitItinerary = () => {
			client
				.post("/api/create-itinerary", {
					title: title.value,
					place_name: location.value,
					longitude: longitude.value,
					latitude: latitude.value,
					budget: budget.value,
					description: description.value,
				})
				.then((response) => {
					console.log(response.data);
					showModal.value = false;
				})
				.catch((error) => {
					console.error(error);
				});
		};

		return {
			setTips,
			setAboutMe,
			location,
			title,
			budget,
			description,
			latitude,
			longitude,

			showModal,
			submitItinerary,
		};
	},
};
</script>

<style scoped></style>
