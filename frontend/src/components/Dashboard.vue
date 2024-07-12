<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-28 py-5 sm:ml-64 overflow-auto scroll-smooth h-screen pt-20 sm:pt-3 bg-light-field dark:bg-dark-notif px-2"
	>
		<div
			class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
		>
			<div class="flex justify-between items-center w-full">
				<div class="w-1/2">
					<!-- Text Field for Editing -->
					<div v-if="isEditing" class="relative w-full">
						<input
							v-model="postTitle"
							@blur="handleTitleChange"
							@keyup.enter="handleTitleChange"
							class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-3xl rounded-lg border-field dark:bg-dark-field px-2 w-full"
							placeholder="POST TITLE"
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
						class="font-bebas-neue text-lg w-full text-prime dark:text-dark-prime sm:text-3xl"
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
						class="form-select sm:w-1/2 rounded-full bg-field dark:bg-dark-field outline-none p-1 dark:text-dark-prime"
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
						class="w-full rounded-lg resize-none p-4 outline-none dark:bg-dark-field dark:text-dark-prime"
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
				class="about-country font-montserrat flex my-3 items-center justify-between border-b-2 dark:border-dark-field p-1"
			>
				<p class="hidden sm:flex text-prime dark:text-dark-prime">
					What country is your post about?
				</p>
				<p class="flex sm:hidden text-prime dark:text-dark-prime">
					Country
				</p>
				<input
					id="country-post"
					v-model="countryPost"
					type="text"
					ref="autocompletecountry"
					placeholder="Country"
					class="bg-field dark:bg-dark-second-dark dark:text-dark-prime rounded-full pl-4 ml-2 h-9 w-1/2 outline-none"
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
					class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-10 sm:h-12 hover:bg-second-light cursor-pointer"
				/>
			</div>
		</div>
		<div
			v-if="!posts.length"
			class="border border-gray-300 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
		>
			<div class="animate-pulse flex space-x-4">
				<div
					class="rounded-full bg-gray-300 dark:bg-slate-700 h-10 w-10"
				></div>
				<div class="flex-1 space-y-6 py-1">
					<div
						class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
					></div>
					<div class="space-y-3">
						<div class="grid grid-cols-3 gap-4">
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-2"
							></div>
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-1"
							></div>
						</div>
						<div
							class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
						></div>
					</div>
				</div>
			</div>
		</div>
		<div
			v-if="!posts.length"
			class="border border-gray-300 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
		>
			<div class="animate-pulse flex space-x-4">
				<div
					class="rounded-full bg-gray-300 dark:bg-slate-700 h-10 w-10"
				></div>
				<div class="flex-1 space-y-6 py-1">
					<div
						class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
					></div>
					<div class="space-y-3">
						<div class="grid grid-cols-3 gap-4">
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-2"
							></div>
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-1"
							></div>
						</div>
						<div
							class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
						></div>
					</div>
				</div>
			</div>
		</div>
		<div
			v-if="!posts.length"
			class="border border-gray-300 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
		>
			<div class="animate-pulse flex space-x-4">
				<div
					class="rounded-full bg-gray-300 dark:bg-slate-700 h-10 w-10"
				></div>
				<div class="flex-1 space-y-6 py-1">
					<div
						class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
					></div>
					<div class="space-y-3">
						<div class="grid grid-cols-3 gap-4">
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-2"
							></div>
							<div
								class="h-2 bg-gray-300 dark:bg-slate-700 rounded col-span-1"
							></div>
						</div>
						<div
							class="h-2 bg-gray-300 dark:bg-slate-700 rounded"
						></div>
					</div>
				</div>
			</div>
		</div>
		<section class="posts mb-10 sm:mb-0">
			<div
				class="relative post-contents w-full p-3 mt-3 px-6 sm:mt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="post-title flex justify-center items-center">
					<div
						class="flex w-full sm:w-[90%] justify-between items-center"
					>
						<h1
							class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-2xl"
						>
							{{ post.title }}
						</h1>
						<small class="text-second ml-5">{{
							timesince(post.date_posted)
						}}</small>
					</div>
				</div>
				<!-- Post Delete Modal Button Includes "isMenuOpen" and "toggleMenu" in script-->

				<!-- Post Delete Modal, Includes "modalDeleteActive" and "deleteItem" in script -->

				<div class="post-content flex w-full mt-4 dark:text-dark-prime">
					<div class="w-14 h-14 mr-4">
						<img
							:src="post.author_user_photo"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full">
						<div class="flex border-b-2 dark:border-gray-400">
							<small
								class="font-montserrat text-prime dark:text-dark-prime pr-5"
							>
								@{{ post.author }}
							</small>
							<small
								class="about-post font-montserrat dark:text-gray-400"
							>
								{{ post.category }} | {{ post.country }}
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify whitespace-normal"
						>
							{{ post.content }}
						</p>
						<div class="sm:h-96 pb-2 sm:p-4" v-if="post.image">
							<img
								:src="post.image"
								alt=""
								class="h-full object-contain rounded-lg"
							/>
						</div>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2 cursor-pointer"
						@click.prevent="selectPost(post)"
					></i>
					<div
						@click="likePost(post._id)"
						class="flex items-center justify-start w-14"
					>
						<span
							v-if="post.is_liked"
							class="material-icons-outlined text-second text-[1.7rem] cursor-pointer"
						>
							favorite
						</span>
						<span
							v-else
							class="material-icons-outlined text-second text-[1.7rem] cursor-pointer"
							>favorite_border</span
						>
						<small class="text-prime dark:text-dark-prime pl-1">
							{{
								post.like_count >= 1000
									? (post.like_count / 1000).toFixed(1) + "k"
									: post.like_count
							}}
						</small>
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
					class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
					v-for="data in selectedPost"
					:key="data._id"
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
							class="absolute top-0 right-0 m-2 mr-3 text-prime dark:text-interface text-2xl"
							@click="showModal = false"
						>
							&times;
						</button>
						<div
							class="post-contents bg-interface dark:bg-dark-interface w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
						>
							<div
								class="post-title flex justify-between items-center"
							>
								<h1
									class="font-bebas-neue text-lg text-prime dark:text-second sm:text-2xl"
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
									<div
										class="flex border-b-2 dark:border-gray-700"
									>
										<p
											class="font-montserrat text-prime dark:text-interface pr-5"
										>
											{{ data.author }}
										</p>
										<small
											class="about-post font-montserrat dark:text-gray-400"
										>
											{{ data.category }} |
											{{ data.country }}
										</small>
									</div>
									<p
										class="font-montserrat w-full rounded-lg resize-none p-4 text-xs text-justify dark:text-interface"
									>
										{{ data.content }}
									</p>
								</div>
							</div>
							<div class="p-2 overflow-auto max-h-60">
								<div
									class="flex items-start bg-gray-200 dark:bg-transparent dark:border-gray-400 dark:border-b ml-3 mt-2 sm:ml-10 p-3 rounded-lg dark:rounded-none"
									v-for="comment in comments_in_post"
									:key="comment._id"
								>
									<div class="w-10 h-10 mr-4">
										<img
											:src="comment.author_user_photo"
											alt="Profile"
											class="rounded-full cursor-pointer"
										/>
									</div>
									<div class="font-montserrat w-full">
										<div
											class="flex justify-between border-b-[.5px] border-gray-300 dark:border-gray-700 pb-2 w-full text-xs"
										>
											<small
												class="text-prime dark:text-interface pr-5"
											>
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
											class="w-full rounded-lg resize-none p-4 text-xs text-justify whitespace-normal dark:text-interface"
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
									class="w-full rounded-lg resize-none p-4 outline-none dark:border dark:bg-dark-interface dark:text-dark-prime"
									name=""
									id=""
									v-model="reply"
									cols="30"
									rows=""
									:placeholder="'Replying to ' + data.author"
								></textarea>
							</div>
							<div
								class="flex py-3 items-center justify-end border-t-2 dark:border-t-0 mt-2"
							>
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
import { useDark, useToggle } from "@vueuse/core";
import moment from "moment";
export default {
	data() {
		return {
			selectedImageUrl: null,
			picture: null,

			auth_user: "",

			isEditing: true,
			postTitle: "",

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
		this.fetchPosts();
		this.initializeAutocompleteCountry();
	},
	mounted() {
		// this.fetchPosts();
		// setInterval(this.fetchPosts, 5000); // Fetch posts every 5 seconds -->> polling
		// this.fetchComments();
		// setInterval(this.fetchComments, 5000);
		this.initializeAutocompleteCountry();

		this.fetchSavedItineraries();
		setInterval(this.fetchSavedItineraries, 5000);
	},
	methods: {
		likePost(post_id) {
			this.client
				.post(`api/like-posts/${post_id}/like_post/`)
				.then((response) => {
					// Handle success response
					console.log(response.data);
					this.fetchPosts();
					// Optionally, update your UI based on the successful like
				})
				.catch((error) => {
					// Handle error
					console.error("Error liking the post:", error);
				});
		},
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
				this.isEditing = true;
			} else {
				this.isEditing = false;
			}
		},
		initializeAutocompleteCountry() {
			// Ensures the DOM is updated
			const inputElement = this.$refs.autocompletecountry;
			console.log("elemt: ", inputElement);
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
			console.log("GET POST", this.selectedPost);
			this.post_id = this.selectedPost[0]._id;

			this.replied_to = this.selectedPost[0].author;
			this.comments_in_post =
				this.posts.find((p) => p._id === this.post_id)?.comments || [];
			console.log("the id : ", this.comments_in_post);
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
						this.fetchPosts();
					})
					.catch((error) => {
						console.log("huy bad ka ");
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
					// this.fetchComments();
					this.fetchPosts();

					// setInterval(this.fetchComments, 5000);

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
			} catch (error) {
				console.error(error);
			}
		},
		fetchComments() {
			this.client
				.get("/api/comments")
				.then((response) => {
					this.comments = response.data;
				})
				.catch((error) => {
					console.log(error);
				});
		},
		fetchPosts() {
			this.client
				.get(`/api/posts-list`)
				.then((response) => {
					this.posts = response.data.reverse();
					if (this.posts.length > 0) {
						// Set selectedPost to the first post
						console.log("GET POST fetch", this.selectedPost);
						this.post_id = this.selectedPost[0]._id;

						this.replied_to = this.selectedPost[0].author;
						this.comments_in_post =
							this.posts.find((p) => p._id === this.post_id)
								?.comments || [];
						console.log("the id : ", this.comments_in_post);
					}

					// this.comments_in_post = this.posts[0].comments;
					console.log("updateed :", this.posts);
				})
				.catch((error) => {
					console.log(error);
				});
		},

		editItem() {
			alert("Edit action triggered");
			this.isMenuOpen = false;
		},
		deleteItem() {
			this.modalDeleteActive = !this.modalDeleteActive;
		},
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		return { isDark, toggleDark };
	},
};
</script>
<style scoped></style>
