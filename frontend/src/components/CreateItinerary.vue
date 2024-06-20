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
						class="w-full h-full rounded-2xl"
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
							id="post-content"
							v-model="postContent"
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
						id="post-content"
						v-model="postContent"
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
					<div class="flex flex-col w-1/2 mr-5 bg-prime">
						<button
							class="h-[7%] w-auto m-2 bg-second rounded-lg"
							@click.prevent="showModal = true"
						>
							Add place
						</button>
						<div
							class="overflow-auto h-screen bg-second m-2 rounded-lg"
						></div>
					</div>
					<div class="the-map h-full w-1/2 bg-prime"></div>
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
												name="it-location"
												id="it-location"
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
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
export default {
	data() {
		return { showModal: false };
	},
	methods: {
		locatorBtn() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {
					console.log(
						position.coords.latitude,
						position.coords.longitude
					);
					this.getAddressFrom(
						position.coords.latitude,
						position.coords.longitude
					);
				});
				(error) => {
					console.log(error.message);
				};
			} else {
			}
		},
		getAddressFrom(lat, long) {
			axios
				.get(
					"https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
						lat +
						"," +
						long +
						"&key=AIzaSyAlo4jqabMxIygmvXtD-K0tm1HJEecnrEA"
				)
				.then((response) => {
					
					if (response.data.error_message) {
						console.log(response.data.error_message);
					} else {
						console.log(response.data.results[0].formatted_address);
					}
				})
				.catch((error) => {
					console.log(error.message);
				});
		},
	},
	setup() {
		const location = ref("");
		const title = ref("");
		const budget = ref("");
		const description = ref("");

		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});
		const submitItinerary = () => {
			client
				.post("/api/login", {})
				.then((response) => {})
				.catch((error) => {});
		};

		return {
			location,
			title,
			budget,
			description,
			client,
			submitItinerary,
		};
	},
};
</script>

<style scoped></style>
