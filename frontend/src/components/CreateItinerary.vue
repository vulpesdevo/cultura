<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-14 sm:pt-3"
	>
		<div
			class="field-editable flex flex-col justify-start items-center w-full bg-field sm:bg-white rounded-2xl p-1"
		>
			<div
				class="fixed sm:relative flex flex-col justify-between title-image h-[20rem] sm:h-96 w-screen sm:w-full rounded-2xl bg-field sm:bg-transparent z-10"
			>
				<div
					class="w-screen sm:w-full sm:h-[87%] bg-second sm:rounded-2xl"
				>
					<img
						src="/sample_img/binondo.webp"
						alt="sample-img-binondo"
						class="w-full h-full object-cover sm:rounded-2xl"
					/>
				</div>
				<div
					class="flex absolute left-[3.2rem] bottom-[4rem] sm:bottom-0 sm:left-[7.7rem] bg-prime w-3/4 h-16 sm:h-24 z-10 rounded-md text-center items-center justify-center"
				>
					<h1
						class="font-bebas-neue text-interface text-center text-3xl sm:text-6xl"
					>
						BINOndo guide for 2024
					</h1>
				</div>
				<div
					class="sm:hidden flex items-center justify-center h-14 w-full"
					id="navs"
				>
					<div
						class="w-3/4 justify-center items-center font-montserrat"
					>
						<button
							class="bg-second h-9 w-1/2 rounded-full"
							:class="{
								'bg-second text-interface':
									currentView === 'overview',
								'bg-transparent text-black':
									currentView !== 'overview',
							}"
							@click="showItinerary('overview')"
						>
							<a href="#overview-section" class="h-full w-full"
								>Overview</a
							>
						</button>
						<button
							class="h-9 w-1/2 rounded-full"
							:class="{
								'bg-second text-interface':
									currentView === 'itinerary',
								'bg-transparent text-black':
									currentView !== 'itinerary',
							}"
							@click="showItinerary('itinerary')"
						>
							<a href="#itinerary-section" class="h-full w-full"
								>Itinerary</a
							>
						</button>
					</div>
				</div>
			</div>

			<section
				class="mt-80 itinerary-1 flex flex-col items-center sm:mt-10 px-16 w-full"
				id="overview-section"
			>
				<button
					@click="saveMainItinerary"
					class="bg-second w-full h-10 rounded-lg mb-3"
				>
					Save
				</button>
				<div class="post-content flex w-screen sm:w-full">
					<div
						class="hidden w-[9.2%] sm:flex items-start justify-center"
					>
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="w-14 h-14 rounded-full cursor-pointer"
						/>
					</div>
					<div class="w-full mx-3 mt-3 sm:m-0">
						<div class="flex">
							<small
								class="hidden sm:flex items-center justify-center font-montserrat text-prime text-base pb-3"
							>
								@{{username}}
							</small>
							<p
								class="font-montserrat sm:hidden pb-1 text-lg text-prime"
							>
								Description
							</p>
						</div>
						<textarea
							class="w-full sm:w-[90.5%] rounded-lg resize-none p-4 outline-none bg-gray-200"
							name=""
							id="set-about"
							v-model="setAboutMe"
							cols="30"
							rows="2"
							placeholder="What do you want to share?"
						></textarea>
					</div>
				</div>
				<div
					class="flex flex-col items-center justify-center w-screen sm:mx-0 sm:mt-4 sm:w-full"
				>
					<p
						class="font-montserrat text-prime w-full px-3 mb-2 text-lg sm:text-xl sm:font-semibold"
					>
						General Tips
					</p>
					<div
						class="flex items-center justify-center w-full px-3 sm:px-0 sm:w-[83%]"
					>
						<textarea
							class="w-full rounded-lg resize-none p-4 outline-none bg-gray-200"
							name=""
							id="set-tips"
							v-model="setTips"
							cols="30"
							rows="2"
							placeholder="What do you want to share?"
						></textarea>
					</div>
				</div>
				<div
					class="font-montserrat flex flex-col justify-center items-center w-screen sm:w-full py-3"
				>
					<p
						class="text-prime text-lg sm:text-xl sm:font-semibold m-3 pl-3 sm:px-2 w-full text-left"
					>
						Budgeting
					</p>

					<div
						class="flex sm:justify-between w-full px-3 sm:p-0 sm:w-[83%] h-20 text-interface"
					>
						<div
							class="flex flex-col justify-center items-center bg-prime w-1/2 mr-2 rounded-lg"
						>
							<p class="">Total Budget</p>
							<p class="text-2xl">₱ {{ this.total_budget }}</p>
						</div>
						<div
							class="flex flex-col justify-center bg-prime w-3/4 rounded-lg p-3"
						>
							<p class="">Currency</p>
							<p class="pb-1 text-xl">PHP Philippine Peso</p>
						</div>
					</div>
				</div>
			</section>
			<section
				class="itinerary-2 pt-10 sm:pt-0 flex flex-col h-[45rem] w-screen sm:w-full my-5"
				id="itinerary-section"
			>
				<h1
					class="hidden sm:flex items-center justify-center text-center text-prime text-xl mb-4"
				>
					Main Itinerary
				</h1>
				<div
					id="the-itineraries"
					class="flex justify-center w-full h-auto sm:h-[700px] px-3 pb-5 sm:px-16"
				>
					<div
						class="flex flex-col justify-center-center w-full sm:w-1/2 m-0 sm:mr-5 pb-5 sm:pb-0"
					>
						<button
							class="font-montserrat text-interface h-10 sm:h-[7%] w-auto mb-2 bg-second rounded-lg"
							@click.prevent="showModal = true"
							@click="initializeAutocomplete"
						>
							Add place
						</button>
						<div
							class="sm:overflow-auto h-screen rounded-lg"
							style="scrollbar-width: none"
						>
							<div
								class="flex-col justify-center items-center w-full h-56 sm:h-80 font-montserrat text-prime bg-interface drop-shadow-md mb-3 rounded-lg"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-normal sm:justify-evenly items-center"
								>
									<h1 class="text-2xl py-3 text-center">
										Lucky Chinatown Mall
									</h1>
									<p
										class="text-justify text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16"
									>
										Lucky Chinatown offers a unique blend of
										history, tradition and modern shopping
										and world-class leisure experience.
									</p>
									<div
										class="flex w-full h-8 text-center items-center justify-end sm:justify-center"
									>
										<p class="bg-second w-24 rounded-full">
											P2000
										</p>
									</div>
									<!-- <p class="rounded-full bg-second text-center inline-block py-1 px-2"
										:style="{ width: `${text.length * 10}px` }"
									>{{ text }}</p> -->
								</div>
							</div>
							<div
								class="flex-col justify-center items-center w-full h-56 sm:h-80 font-montserrat text-prime bg-white sm:bg-interface drop-shadow-md mb-3 rounded-lg"
								v-for="(itinerary, index) in list_itineraries"
								:key="index"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-normal sm:justify-evenly items-center"
								>
									<h1 class="text-2xl py-3 text-center">
										{{ itinerary.title }}
									</h1>
									<p
										class="text-justify text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16"
									>
										{{ itinerary.description }}
									</p>
									<div
										class="flex w-full h-8 text-center items-center justify-end sm:justify-center"
									>
										<p class="bg-second w-24 rounded-full">
											P{{ itinerary.budget }}
										</p>
									</div>
									<!-- <p class="rounded-full bg-second text-center inline-block py-1 px-2"
										:style="{ width: `${text.length * 10}px` }"
									>{{ text }}</p> -->
								</div>
							</div>
						</div>
					</div>
					<div
						:class="{
							'translate-y-0': showMap,
							'translate-y-full': !showMap,

							'duration-500': true,
							'ease-in-out': true,
						}"
						class="absolute sm:static sm:flex h-full items-center w-screen sm:w-1/2 rounded-lg bottom-0 left-0 transform sm:transform-none z-20 bg-interface overflow-hidden sm:overflow-visible"
					>
						<div
							id="the-map"
							class="the-map h-full w-full rounded-lg"
						></div>
					</div>
				</div>
			</section>
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
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle w-screen sm:w-[35%]"
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
							class="font-bebas-neue text-2xl pt-5 sm:text-3xl leading-6 font-medium text-prime"
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
										<label for="it-description "
											>Add description</label
										>
										<textarea
											class="rounded-lg resize-none mt-2 p-4 outline-none bg-field"
											name=""
											id="it-description"
											v-model="description"
											cols="30"
											rows="4"
											placeholder="Add notes, links, descriptions or whatever you want your fellow travelers to know about this place!"
										></textarea>
									</div>
									<div class="hidden">
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
									/>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
		<!-- Floating Action Button -->
		<button
			class="flex sm:hidden items-center justify-center fixed bottom-20 right-5 bg-second active:bg-prime text-white font-bold rounded-full h-16 w-16 z-40"
			@click="toggleMap"
		>
			<span class="material-icons-outlined"> map </span>
			<!-- Icon or text for your button -->
		</button>
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
// import { Loader } from "@googlemaps/js-api-loader";

export default {
	data() {
		return {
			main_title: "Lucky Chinatown Mall",
			setTips: "",
			setAboutMe: "",
			total_budget: 0,

			username:"",

			location: "",
			title: "",
			budget: "",
			description: "",
			latitude: "",
			longitude: "",
			showModal: false,
			client: null, // Initialize axios client later

			showModal: false,
			latitude: 0,
			longitude: 0,
			location: null,
			list_itineraries: [],
			itineraryIds: [],

			// This property controls which view is currently visible
			currentView: "itinerary", // 'overview' or 'itinerary'
			showMap: false,
		};
	},
	computed: {
		// Define isMobile as a computed property
		isMobile() {
			// This example uses 768px as the threshold for mobile devices
			return window.innerWidth < 768;
		},
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
		this.client
			.get("api/user")
			.then((res) => {
				this.username = res.data.user.username;
				
			})
			.catch((error) => {
				console.log("ERROR", error.message);
				
			});
		this.fetchItineraries();
	},
	mounted() {
		this.initializeAutocomplete();
	},
	methods: {
		toggleMap() {
			this.showMap = !this.showMap;
		},
		showItinerary(view) {
			this.currentView = view;

			this.$nextTick(() => {
				const navHeight = document.querySelector("#navs")
					? document.querySelector("#navs").offsetHeight
					: 0;
				let targetSection;

				if (view === "itinerary") {
					targetSection =
						document.getElementById("itinerary-section");
				} else {
					// Default to overview-section or handle other cases
					targetSection = document.getElementById("overview-section");
				}

				if (targetSection) {
					const offsetTop = targetSection.offsetTop - navHeight;

					window.scrollTo({
						top: offsetTop,
						behavior: "smooth",
					});
				}
			});
		},
		saveMainItinerary() {
			this.client
				.post("/api/save-itinerary", {
					main_image: null,
					main_title: this.main_title,
					main_description: this.setAboutMe,
					gen_tips: this.setTips,
					total_budget: this.total_budget,
					itineraries: this.itineraryIds,
				})
				.then((response) => {
					console.log(response.data);
				})
				.catch((error) => {
					console.error(error);
				});
		},
		submitItinerary() {
			this.client
				.post("/api/create-itinerary", {
					title: this.title,
					place_name: this.location,
					longitude: this.longitude,
					latitude: this.latitude,
					budget: this.budget,
					description: this.description,
				})
				.then((response) => {
					console.log(response.data);
					this.showModal = false;
					this.fetchItineraries();
				})
				.catch((error) => {
					console.error(error);
				});
		},
		getCurrentLocation() {
			return new Promise((resolve, reject) => {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(
						(position) => {
							resolve({
								latitude: position.coords.latitude,
								longitude: position.coords.longitude,
							});
						},
						(error) => {
							reject(error);
						}
					);
				} else {
					reject(
						new Error(
							"Geolocation is not supported by this browser."
						)
					);
				}
			});
		},

		// Step 2 & 3: Calculate Distances and Sort Itineraries
		async sortItinerariesByProximity() {
			try {
				const currentLocation = await this.getCurrentLocation();
				this.list_itineraries.forEach((itinerary) => {
					itinerary.distance = this.calculateDistance(
						currentLocation.latitude,
						currentLocation.longitude,
						itinerary.latitude,
						itinerary.longitude
					);
				});

				this.list_itineraries.sort((a, b) => a.distance - b.distance);

				// After sorting, you can now update the map
				this.showLocationOntheMap();
			} catch (error) {
				console.error(error);
			}
		},

		// Helper Method: Calculate Distance Between Two Coordinates
		calculateDistance(lat1, lon1, lat2, lon2) {
			const R = 6371; // Radius of the earth in km
			const dLat = this.deg2rad(lat2 - lat1);
			const dLon = this.deg2rad(lon2 - lon1);
			const a =
				Math.sin(dLat / 2) * Math.sin(dLat / 2) +
				Math.cos(this.deg2rad(lat1)) *
					Math.cos(this.deg2rad(lat2)) *
					Math.sin(dLon / 2) *
					Math.sin(dLon / 2);
			const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
			const distance = R * c; // Distance in km
			return distance;
		},

		// Helper Method: Convert Degrees to Radians
		deg2rad(deg) {
			return deg * (Math.PI / 180);
		},
		async fetchItineraries() {
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
			try {
				const response = await client.get("/api/itinerary");
				this.list_itineraries = response.data;
				console.log("list_itineraries:", this.list_itineraries);
				this.itineraryIds = this.list_itineraries.map(
					(itinerary) => itinerary.id
				);
				console.log("itineraryIds:", this.itineraryIds);

				this.total_budget = this.list_itineraries.reduce(
					(sum, itinerary) => sum + itinerary.budget,
					0
				);
				console.log("Total Budget:", this.total_budget);
				// Sort the itineraries by proximity before showing them on the map

				await this.sortItinerariesByProximity();
				this.showLocationOntheMap();
			} catch (error) {
				console.log(error);
			}
		},
		initializeMap(latitude, longitude) {
			new google.maps.Map(document.getElementById("the-map"), {
				center: { lat: latitude, lng: longitude },
				zoom: 8,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
			});
			// Optionally, add a marker at the location
		},
		showLocationOntheMap() {
			// const lat = 37.7749;
			// const lng = -122.4194;
			if (this.list_itineraries.length === 0) {
				// If list_itineraries is empty, use the user's current location or a default location
				navigator.geolocation.getCurrentPosition(
					(position) => {
						const { latitude, longitude } = position.coords;
						this.initializeMap(latitude, longitude);
					},
					() => {
						// Fallback to a default location if unable to get the user's location
						const defaultLat = 37.7749; // Example default latitude
						const defaultLng = -122.4194; // Example default longitude
						this.initializeMap(defaultLat, defaultLng);
					}
				);
			} else {
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
				const end =
					this.list_itineraries[this.list_itineraries.length - 1];
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
					origin: new google.maps.LatLng(
						start.latitude,
						start.longitude
					),
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
						console.error(
							"Directions request failed due to " + status
						);
					}
				});

				// Extend bounds to include start and end
				bounds.extend(
					new google.maps.LatLng(start.latitude, start.longitude)
				);
				bounds.extend(
					new google.maps.LatLng(end.latitude, end.longitude)
				);
				map.fitBounds(bounds);
			}
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
	// setup() {
	// 	const setTips = ref("");
	// 	const setAboutMe = ref("");
	// 	const location = ref("");
	// 	const title = ref("");
	// 	const budget = ref("");
	// 	const description = ref("");
	// 	const latitude = ref("");
	// 	const longitude = ref("");

	// 	const showModal = ref(false);
	// 	const token = localStorage.getItem("token");
	// 	const headers = {
	// 		Authorization: `Token ${token}`,
	// 		"Content-Type": "application/json",
	// 	};
	// 	const client = axios.create({
	// 		baseURL: "http://127.0.0.1:8000",
	// 		withCredentials: true,
	// 		timeout: 5000,
	// 		xsrfCookieName: "csrftoken",
	// 		xsrfHeaderName: "X-Csrftoken",
	// 		headers: headers,
	// 	});

	// 	const submitItinerary = () => {
	// 		client
	// 			.post("/api/create-itinerary", {
	// 				title: title.value,
	// 				place_name: location.value,
	// 				longitude: longitude.value,
	// 				latitude: latitude.value,
	// 				budget: budget.value,
	// 				description: description.value,
	// 			})
	// 			.then((response) => {
	// 				console.log(response.data);
	// 				showModal.value = false;
	// 			})
	// 			.catch((error) => {
	// 				console.error(error);
	// 			});
	// 	};

	// 	return {
	// 		setTips,
	// 		setAboutMe,
	// 		location,
	// 		title,
	// 		budget,
	// 		description,
	// 		latitude,
	// 		longitude,

	// 		showModal,
	// 		submitItinerary,
	// 	};
	// },
};
</script>

<style scoped></style>
