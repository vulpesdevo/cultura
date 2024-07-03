<template>
	<div
		class="flex flex-col items-center align-middle w-full  sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-20 sm:pt-3"
	>
		<div
			class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 sm:rounded-lg shadow-lg bg-interface"
		>
			<div class="flex justify-between items-center">
				<div>
					<!-- Text Field for Editing -->
					<div v-if="isEditing" class="relative">
						<input
							v-model="postTitle"
							@blur="handleTitleChange"
							@keyup.enter="handleTitleChange"
							class="font-bebas-neue text-lg text-prime sm:text-3xl rounded-lg border-field px-2"
							autofocus
						/>
						<span
							class="absolute right-0 top-0 mt-1 material-icons-outlined text-field"
						>
							edit_note
						</span>
						<!-- Example using FontAwesome -->
					</div>
					<!-- Text Display -->
					<h1
						v-else
						@click="isEditing = true"
						class="font-bebas-neue text-lg text-prime sm:text-3xl"
					>
						{{ postTitle }}
					</h1>
				</div>
				<div
					class="drop-down-categ w-1/2 flex items-center justify-end font-montserrat"
				>
					<select
						name=""
						id="category-option"
						v-model="categoryOption"
						class="sm:w-1/2 rounded-full bg-field outline-none p-1"
					>
						<option value="" disabled selected>Category</option>
						<option value="Food">Food</option>
						<option value="Traditions">Traditions</option>
						<option value="History">History</option>
					</select>
				</div>
			</div>
			<div class="for-content flex flex-col w-full mt-3">
				<div class="flex">
					<div class="hidden sm:flex w-14 h-14 mr-5 rounded-full">
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="object-cover rounded-full cursor-pointer"
						/>
					</div>
					<textarea
						class="w-full rounded-lg resize-none p-4 outline-none"
						name=""
						id="post-content"
						v-model="postContent"
						cols="30"
						rows=""
						placeholder="What do you want to share?"
					></textarea>
				</div>
				<div
					class="added-img-container flex h-20 sm:ml-[4.5rem] mt-2 rounded-lg"
					v-if="selectedImageUrl"
				>
					<img
						:src="selectedImageUrl"
						alt="Post Image"
						class="object-cover w-32 h-full rounded-lg mr-1"
					/>
				</div>
				<!-- v-if="selectedItinerary" -->
				<div
					class="added-itinerary-container flex items-center bg-field h-10 pl-3 sm:ml-[4.5rem] mt-2 rounded-lg"
					v-if="selectedItinerary"
				>
					{{ selectedItinerary.main_title }} (ID:
					{{ selectedItinerary.id }})
				</div>
			</div>
			<div
				class="about-country font-montserrat flex my-3 items-center justify-between border-b-2 p-1"
			>
				<p class="hidden sm:flex text-prime">
					What country is your post about?
				</p>
				<p class="flex sm:hidden text-prime">Country</p>
				<input
					id="country-post"
					v-model="countryPost"
					type="text"
					ref="autocompletecountry"
					class="bg-field rounded-full pl-3 h-9 w-1/2 outline-none"
					placeholder="Country"
				/>

				<div class="hidden sm:flex sm:w-1/5"></div>
			</div>
			<div class="flex my-3 items-center justify-between">
				<div class="flex">
					<label for="imgSelect">
						<span
							class="material-icons-outlined text-second text-3xl cursor-pointer"
							>image</span
						>
					</label>
					<input
						type="file"
						name=""
						id="imgSelect"
						class="hidden"
						@change="handleFileSelection"
					/>
					<span
						class="material-icons-outlined text-second text-3xl pl-2 cursor-pointer"
						@click="addItineraryModal = true"
						>explore</span
					>
				</div>
				<input
					@click.prevent="submitPost"
					type="submit"
					value="Post"
					class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-12 hover:bg-second-light cursor-pointer"
				/>
			</div>
		</div>
		<section class="posts mb-10">
			<div
				class="post-contents w-screen sm:w-full pt-3 px-6 sm:pt-6 sm:px-9 sm:rounded-lg shadow-lg bg-interface"
			>
				<div class="post-title flex justify-between items-center">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						BEST PULLED NOODLES IN BINONDO
					</h1>
					<small class="text-second">10mins ago</small>
				</div>

				<div class="post-content flex w-full mt-4">
					<div class="w-14 h-14 mr-4">
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full">
						<div class="flex border-b-2">
							<small class="font-montserrat text-prime pr-5">
								@mark0
							</small>
							<small class="about-post font-montserrat">
								Food | Philippines
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
						>
							Slurp-worthy satisfaction awaits at Lan-Zhou Lamien,
							where every strand of their hand-pulled noodles
							tells a tale of culinary mastery. Taste the
							tradition, savor the excellence, and discover why
							they're Manila's noodle maestros.
						</p>
						<div class="sm:h-96 pb-2 sm:p-4">
							<img
								src="/sample_img/binondo.webp"
								alt=""
								class="h-full w-full object-cover rounded-lg"
							/>
						</div>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2"
						@click.prevent="showModal = true"
					></i>
					<span class="material-icons-outlined text-second text-2xl"
						>favorite_border</span
					>
				</div>
			</div>
			<div
				class="post-contents w-full p-3 mt-3 px-6 sm:mt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="post-title flex justify-between items-center">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						{{ post.title }}
					</h1>

					<small class="text-second">{{
						timesince(post.date_posted)
					}}</small>
				</div>

				<div class="post-content flex w-full mt-4">
					<div class="w-14 h-14 mr-4">
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full">
						<div class="flex border-b-2">
							<small class="font-montserrat text-prime pr-5">
								@{{ post.author }}
							</small>
							<small class="about-post font-montserrat">
								{{ post.category }} | {{ post.country }}
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
						>
							{{ post.content }}
						</p>
						<div class="sm:h-96 pb-2 sm:p-4" v-if="post.image">
							<img
								:src="post.image"
								alt=""
								class="h-full w-full object-cover rounded-lg"
							/>
						</div>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2"
						@click.prevent="selectPost(post)"
					></i>
					<span class="material-icons-outlined text-second text-2xl"
						>favorite_border</span
					>
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
					class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
				>
					<div
						class="fixed inset-0 bg-black bg-opacity-70 transition-opacity"
						aria-hidden="true"
					></div>
					<span
						class="hidden sm:inline-block sm:align-middle sm:h-screen"
						aria-hidden="true"
						>&#8203;</span
					>
					<div
						class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/2"
					>
						<button
							class="absolute top-0 right-0 m-2 mr-3 text-prime text-2xl"
							@click="showModal = false"
						>
							&times;
						</button>
						<div
							class="post-contents bg-interface w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
							v-for="(data, index) in selectedPost"
							:key="index"
						>
							<div
								class="post-title flex justify-between items-center"
							>
								<h1
									class="font-bebas-neue text-lg text-prime sm:text-2xl"
								>
									{{ data.title }}
								</h1>
							</div>

							<div class="post-content flex w-full mt-4">
								<div class="w-14 h-14 mr-4">
									<img
										src="/sample_img/mark.png"
										alt="Profile"
										class="rounded-full cursor-pointer"
									/>
								</div>
								<div class="w-full">
									<div class="flex border-b-2">
										<p
											class="font-montserrat text-prime pr-5"
										>
											{{ data.author }}
										</p>
										<small
											class="about-post font-montserrat"
										>
											{{ data.category }} |
											{{ data.country }}
										</small>
									</div>
									<p
										class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
									>
										{{ data.content }}
									</p>
								</div>
							</div>
							<div class="p-2 overflow-auto max-h-60">
								<div
									class="flex items-start bg-gray-200 ml-3 mt-2 sm:ml-10 p-3 rounded-lg"
									v-for="comment in comments_in_post"
									:key="comment._id"
								>
									<div class="w-10 h-10 mr-4">
										<img
											src="/sample_img/mark.png"
											alt="Profile"
											class="rounded-full cursor-pointer"
										/>
									</div>
									<div class="font-montserrat w-full">
										<div
											class="flex justify-between border-b-2 border-gray-300 pb-2 w-full text-xs"
										>
											<small class="text-prime pr-5">
												{{ comment.author }} to
												<span class="text-second">{{
													comment.replied_to
												}}</span>
											</small>
											<small class="text-second">{{
												timesince(comment.date_posted)
											}}</small>
										</div>
										<p
											class="w-full rounded-lg resize-none p-4 text-xs text-justify"
										>
											{{ comment.body }}
										</p>
									</div>
								</div>
							</div>
							<div class="reply-post flex w-full mt-4">
								<div class="w-14 h-14 mr-4">
									<img
										src="/sample_img/mark.png"
										alt="Profile"
										class="rounded-full cursor-pointer"
									/>
								</div>
								<textarea
									class="w-full rounded-lg resize-none p-4 outline-none"
									name=""
									id=""
									v-model="reply"
									cols="30"
									rows=""
									:placeholder="'Replying to ' + data.author"
								></textarea>
							</div>
							<div
								class="flex py-3 items-center justify-between border-t-2 mt-2"
							>
								<div class="flex">
									<label for="imgSelect">
										<span
											class="material-icons-outlined text-second text-3xl"
											>image</span
										>
									</label>
									<input
										type="file"
										name=""
										id="imgSelect"
										class="hidden"
									/>
									<span
										class="material-icons-outlined text-second text-3xl pl-2"
										>explore</span
									>
								</div>
								<input
									type="submit"
									value="Reply"
									@click.prevent="submitReply"
									class="font-montserrat text-xl bg-second text-interface rounded-full w-28 h-10 hover:bg-second-light cursor-pointer"
								/>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div
				class="fixed z-50 inset-0 overflow-y-auto"
				aria-labelledby="modal-title"
				role="dialog"
				aria-modal="true"
				v-if="addItineraryModal"
			>
				<div
					class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
				>
					<div
						class="fixed inset-0 bg-black bg-opacity-70 transition-opacity"
						aria-hidden="true"
					></div>
					<span
						class="hidden sm:inline-block sm:align-middle sm:h-screen"
						aria-hidden="true"
						>&#8203;</span
					>
					<div
						class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/3"
					>
						<div
							class="flex flex-col justify-center items-center bg-interface w-full pt-2 px-6 sm:pt-5 sm:px-9 rounded-lg shadow-lg"
						>
							<h1
								class="font-bebas-neue font-bold text-lg text-prime sm:text-4xl tracking-wider"
							>
								select itinerary
							</h1>

							<div
								class="flex justify-start items-center align-middle h-auto w-full border-b-2"
							>
								<div
									class="flex justify-center items-center font-montserrat text-lg text-prime font-medium w-1/2 h-10 my-2 p-2 mb-2 rounded-md cursor-pointer hover:bg-field"
								>
									+ Create Itinerary
								</div>
							</div>
							<div
								class="flex justify-start items-center text-prime w-full h-12 text-lg font-medium font-montserrat pl-3 my-2 rounded-md cursor-pointer hover:bg-second-light"
								v-for="itinerary in itineraries"
								:key="itinerary._id"
								@click="selectItinerary(itinerary)"
								:class="{
									'bg-second-light':
										selectedItinerary === itinerary,
								}"
							>
								{{ itinerary.main_title }}
							</div>
							<div
								class="flex flex-col items-center align-middle text-center mt-5"
							>
								<div class="flex font-montserrat">
									<button
										class="text-interface text-lg bg-gray-500 p-2 rounded-3xl w-32 h-12 mb-3 hover:bg-gray-400 mr-5"
										@click="addItineraryModal = false"
									>
										Cancel
									</button>
									<input
										type="submit"
										value="Save"
										class="text-interface cursor-pointer text-lg bg-second p-2 rounded-3xl w-32 h-12 mb-3 hover:bg-second-light"
									/>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import moment from "moment";
export default {
	data() {
		return {
			selectedImageUrl: null,
			picture: null,

			auth_user: "",

			isEditing: true,
			postTitle: "POST TITLE",

			addItineraryModal: false,
			showModal: false,

			categoryOption: "",
			postContent: "",
			countryPost: "",
			posts: [],

			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",

			comments: [],
			comments_in_post: [],

			itineraries: [],
			selectedItinerary: null,
		};
	},
	created() {
		this.token = localStorage.getItem("token");
		this.client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				Authorization: `Token ${this.token}`,
				"Content-Type": "application/json",
			},
		});
		this.initializeAutocompleteCountry();
	},
	mounted() {
		this.fetchPosts();
		setInterval(this.fetchPosts, 5000); // Fetch posts every 5 seconds -->> polling
		this.fetchComments();
		setInterval(this.fetchComments, 5000);
		this.initializeAutocompleteCountry();
		
		this.fetchSavedItineraries();
		setInterval(this.fetchSavedItineraries, 5000);
	},
	methods: {
		selectItinerary(itinerary) {
			this.selectedItinerary = itinerary; // Update the selectedItinerary with the clicked one
		},
		handleFileSelection(event) {
			const file = event.target.files[0];
			if (file) {
				this.selectedImageUrl = URL.createObjectURL(file);
				this.picture = file;
				console.log("Image :", this.picture);
			}
		},
		handleTitleChange() {
			if (this.postTitle.trim() === "") {
				this.postTitle = "POST TITLE";
			}
			this.isEditing = false;
		},
		initializeAutocompleteCountry() {
			// Ensures the DOM is updated
			const inputElement = this.$refs.autocompletecountry;

			const autocomplete = new google.maps.places.Autocomplete(
				inputElement,
				{
					types: ["(regions)"],
				}
			);

			// getting the value of
			autocomplete.addListener("place_changed", () => {
				const country = autocomplete.getPlace();
				this.countryPost = country.formatted_address;
			});
		},
		timesince(date) {
			return moment(date).fromNow();
		},
		selectPost(post) {
			this.showModal = true;

			this.selectedPost = [post];
			this.post_id = this.selectedPost[0]._id;
			this.replied_to = this.selectedPost[0].author;
			this.comments_in_post = this.comments.filter(
				(comment) => comment.post_id === this.post_id
			);
		},
		submitPost() {
			if (
				!this.categoryOption.trim() ||
				!this.postContent.trim() ||
				!this.countryPost.trim() ||
				this.postTitle === "POST TITLE"
			) {
				alert("Please fill all fields correctly."); // Inform the user (consider using a more user-friendly notification system)
				return; // Exit the method
			} else {
				let formData = new FormData();
				formData.append("title", this.postTitle);
				formData.append("category", this.categoryOption);
				formData.append("body", this.postContent);
				formData.append("country", this.countryPost);
				if (this.picture && this.picture instanceof File) {
					formData.append("image", this.picture, this.picture.name);
				}
				this.client
					.post("/api/posting", formData, {
						headers: {
							"Content-Type": "multipart/form-data",
						},
					})
					.then((response) => {
						console.log(response.data);
						this.postTitle = "POST TITLE";
						this.categoryOption = "";
						this.postContent = "";
						this.countryPost = "";
						this.selectedImageUrl = null;
					})
					.catch((error) => {
						// Handle error
					});
			}
		},

		submitReply() {
			this.client
				.post("/api/commenting", {
					post_id: this.post_id,
					replied_to: this.replied_to,
					body: this.reply,
				})
				.then((response) => {
					console.log(response.data);
					this.reply = "";
					this.fetchComments();
					setInterval(this.fetchComments, 5000);
					this.showModal = false;
					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
				});
		},
		async fetchSavedItineraries() {
			try {
				const response = await this.client.get("/api/saved-itinerary");
				this.itineraries = response.data;
				console.log(this.itineraries);
			} catch (error) {
				console.error(error);
			}
		},
		fetchComments() {
			axios
				.get("/api/comments")
				.then((response) => {
					this.comments = response.data;
					console.log("comments:", this.comments);
				})
				.catch((error) => {
					console.log(error);
				});
		},
		fetchPosts() {
			axios
				.get("/api/posts")
				.then((response) => {
					this.posts = response.data.reverse();
					console.log("posts:", this.posts);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
	setup() {},
};
</script>
<style scoped></style>
