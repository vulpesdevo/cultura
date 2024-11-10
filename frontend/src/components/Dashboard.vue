<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-28 py-5 overflow-auto scroll-smooth h-screen sm:pt-3 bg-field dark:bg-dark-notif px-2"
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
							class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-3xl rounded-lg border-field dark:bg-dark-field p-[.23rem] px-2 w-full ring-1 ring-gray-600 outline-[.5px] outline-none"
							placeholder="POST TITLE"
							autofocus
						/>
						<span
							class="absolute right-1 top-1 mt-1 material-icons-outlined text-field"
						>
							edit_note
						</span>
						<!-- Example using FontAwesome -->
					</div>
					<!-- Text Display -->
					<h1
						v-else
						@click="isEditing = true"
						class="font-bebas-neue p-[.23rem] text-lg w-full text-prime dark:text-dark-prime sm:text-3xl"
					>
						{{ postTitle }}
					</h1>
				</div>
				<div
					class="drop-down-categ w-1/2 flex items-center justify-end font-montserrat"
				>
					<select
						id="category-option"
						v-model="categoryOption"
						class="appearance-none outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg ring-1 ring-gray-600 block w-3/4 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
					>
						<option class="mb-2" value="" disabled selected>
							Category
						</option>
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
							:src="post_profile_display"
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
					class="added-itinerary-container flex items-center justify-between bg-field dark:bg-dark-second-dark h-10 w-1/3 p-3 sm:ml-[4.5rem] mt-2 rounded-lg"
					v-if="selectedItinerary"
				>
					<p class="">{{ selectedItinerary.main_title }}</p>
					<span
						class="material-icons-outlined text-second text-2xl cursor-pointer"
						@click="selectedItinerary = null"
						>close</span
					>
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
					v-model="countryPost"
					type="text"
					ref="autocompletecountry"
					id="autocompletecountry"
					placeholder="Enter country"
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
			class="border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
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
		<div
			v-if="!posts.length"
			class="border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
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
		<div
			v-if="!posts.length"
			class="border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
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
		<!-- <PostSection /> -->

		<!-- POST SECTION -->
		<section class="posts w-full mb-10 sm:mb-0">
			<div
				class="relative post-contents w-full p-3 mt-3 px-6 sm:mt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="post-title flex justify-center items-center">
					<div
						class="flex w-full sm:w-[90%] justify-between items-center mr-5"
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
					<!-- REPORT BUTTON -->
					<router-link
						:to="{
							name: 'report',
							query: { post_id: post._id, user_id: auth_user },
						}"
					>
						<div>
							<i
								class="fa-solid fa-circle-exclamation text-second text-2xl cursor-pointer"
							></i>
						</div>
					</router-link>
				</div>

				<div class="post-content flex w-full mt-4 dark:text-dark-prime">
					<div class="w-14 h-14 mr-4">
						<img
							:src="post.author_user_photo"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full">
						<div
							class="flex border-b-2 dark:border-gray-400 w-full mb-5"
						>
							<div class="w-1/2">
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
							<!-- Toggle between "Save" and "Edit" -->
							<!-- <div class="w-1/2 text-right">
								
								<span
									class="px-5 material-icons-outlined text-second text-2xl cursor-pointer custom-cursor-on-hover"
									@click="toggleEdit(post)"
								>
									{{ post.isEditing ? "save" : "edit" }}
								</span>
							</div> -->
						</div>

						<!-- Conditional rendering for the post content -->
						<p
							v-if="!post.isEditing"
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify whitespace-normal"
						>
							{{ post.content }}
						</p>

						<!-- Editable text input when in editing mode -->
						<textarea
							v-else
							v-model="post.editedContent"
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify whitespace-normal bg-interface dark:bg-dark-interface border border-prime dark:border-dark-prime text-prime dark:text-dark-prime"
						></textarea>

						<!-- Image Section -->
						<div
							class="sm:h-96 pb-2 sm:p-4"
							v-if="!post.isEditing && post.image"
						>
							<img
								:src="post.image"
								alt=""
								class="h-full object-contain rounded-lg"
							/>
						</div>

						<div
							v-else-if="post.image || post.isEditing"
							class="sm:h-96 pb-2 sm:p-4"
						>
							<input
								type="file"
								@change="handleImageUpload($event, post)"
								accept="image/*"
								class="file-input text-prime dark:text-dark-prime"
							/>
							<img
								v-if="post.previewImage"
								:src="post.previewImage"
								alt="Preview"
								class="h-full object-contain rounded-lg mt-2"
							/>
						</div>

						<!-- Optional: Itinerary -->
						<div
							class="h-auto pb-2 sm:p-4"
							v-if="post.itinerary_in_post"
						>
							<div
								class="cont-itinerary mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface dark:bg-dark-interface cursor-pointer sm:w-11/12 sm:px-6"
								:key="post.itinerary_in_post.id"
								@click="
									goToViewItinerary(post.itinerary_in_post.id)
								"
							>
								<div
									class="mt-2 sm:px-5 pb-5 sm:pt-5 mb-10 w-full"
								>
									<img
										class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-auto"
										:src="post.itinerary_in_post.main_image"
										alt=""
									/>
									<div class="w-full h-auto py-2">
										<h1
											class="font-bebas-neue text-prime dark:text-interface text-3xl mt-5 sm:text-4xl"
										>
											{{
												post.itinerary_in_post
													.main_title
											}}
										</h1>
										<p
											class="font-montserrat text-sm text-justify h-20 overflow-hidden dark:text-interface"
										>
											{{
												post.itinerary_in_post
													.main_description
											}}
										</p>
									</div>
								</div>
							</div>
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
										:src="data.author_user_photo"
										alt="Profile"
										class="rounded-full cursor-pointer"
									/>
								</div>
								<div class="w-full">
									<div
										class="flex border-b-2 dark:border-gray-700 justify-between"
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
							<div
								class="reply-post flex justify-between items-start w-auto mt-4"
							>
								<img
									:src="post_profile_display"
									alt="Profile"
									class="rounded-full object-cover size-12 cursor-pointer mr-2"
								/>
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
		</section>
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
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/3 w-full"
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
								<!-- <input
										type="submit"
										value="Save"
										class="text-interface cursor-pointer text-lg bg-second p-2 rounded-3xl w-32 h-12 mb-3 hover:bg-second-light"
									/> -->
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import { useDark, useToggle } from "@vueuse/core";
import moment from "moment";
import { clean } from "profanity-cleaner";
import filipinoBadWords from "../custom-badwords";
import { useRouter } from "vue-router";

const router = useRouter();

const store = useStore();

const posts = ref([]);
const post_profile_display = ref(null);
const selectedImageUrl = ref(null);
const picture = ref(null);
const auth_user = ref(0);
const isEditing = ref(true);
const postTitle = ref("");
const addItineraryModal = ref(false);
const showModal = ref(false);
const categoryOption = ref("");
const postContent = ref("");
const countryPost = ref("");
const selectedPost = ref([]);
const reply = ref("");
const replied_to = ref("");
const post_id = ref("");
const comments = ref([]);
const comments_in_post = ref([]);
const itineraries = ref([]);
const itineraries_frompost = ref([]);
const selectedItinerary = ref(null);
const id_of_selected = ref("");
const isFullTextShown = ref({});

const isDark = useDark();
const toggleDark = useToggle(isDark);

onMounted(() => {
	store.dispatch("fetchUserData").then((res) => {
		post_profile_display.value = res.profile[0]?.user_photo;
		auth_user.value = res.user?.id;
	});
	store.dispatch("fetchPosts").then(() => {
		posts.value = store.getters.getPosts;
	});
	store.dispatch("fetchItineraries").then(() => {
		itineraries.value = store.getters.getItineraries;
	});
	setInterval(() => {
		store.dispatch("fetchItineraries").then(() => {
			itineraries.value = store.getters.getItineraries;
		});
	}, 5000);
});

// Methods
const toggleEdit = (post) => {
	if (post.isEditing) {
		post.content = post.editedContent;
		if (post.previewImage) {
			post.image = post.previewImage;
		}
	} else {
		post.editedContent = post.content;
		post.previewImage = post.image;
	}
	post.isEditing = !post.isEditing;
};

const handleImageUpload = (event, post) => {
	const file = event.target.files[0];
	if (file) {
		const reader = new FileReader();
		reader.onload = (e) => {
			post.previewImage = e.target.result;
		};
		reader.readAsDataURL(file);
	}
};

const likePost = async (post_id) => {
	try {
		await store.dispatch("likePost", post_id);
		store.dispatch("fetchPosts").then(() => {
			posts.value = store.getters.getPosts;
		});
	} catch (error) {
		console.error("Error liking the post:", error);
	}
};

const selectPost = (post) => {
	showModal.value = true;
	selectedPost.value = [post];
	post_id.value = selectedPost.value[0]._id;
	replied_to.value = selectedPost.value[0].author;
	comments_in_post.value =
		posts.value.find((p) => p._id === post_id.value)?.comments || [];
};

const submitPost = async () => {
	if (
		!categoryOption.value.trim() ||
		!postContent.value.trim() ||
		!countryPost.value.trim() ||
		postTitle.value === "POST TITLE"
	) {
		alert("Please fill all fields correctly.");
		return;
	} else {
		let formData = new FormData();
		formData.append("title", postTitle.value);
		formData.append("category", categoryOption.value);
		formData.append("body", postContent.value);
		formData.append("country", countryPost.value);
		formData.append("itinerary_id", id_of_selected.value);
		if (picture.value && picture.value instanceof File) {
			formData.append("image", picture.value, picture.value.name);
		}
		try {
			await store.dispatch("submitPost", formData);
			postTitle.value = "POST TITLE";
			categoryOption.value = "";
			postContent.value = "";
			countryPost.value = "";
			selectedImageUrl.value = null;
			store.dispatch("fetchPosts").then(() => {
				posts.value = store.getters.getPosts;
			});
		} catch (error) {
			console.log("Error submitting post:", error);
		}
	}
};

const submitReply = async () => {
	try {
		await store.dispatch("submitReply", {
			post_id: post_id.value,
			replied_to: replied_to.value,
			body: reply.value,
		});
		reply.value = "";
		store.dispatch("fetchPosts").then(() => {
			posts.value = store.getters.getPosts;
		});
	} catch (error) {
		console.error(error);
	}
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const handleFileSelection = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		picture.value = file;
	}
};

const initializeAutocompleteCountry = () => {
	const inputElement = document.getElementById("autocompletecountry");
	if (inputElement) {
		const autocomplete = new google.maps.places.Autocomplete(inputElement, {
			types: ["(regions)"],
		});
		autocomplete.addListener("place_changed", () => {
			const place = autocomplete.getPlace();
			if (place && place.formatted_address) {
				countryPost.value = place.formatted_address;
			}
		});
	}
};
const selectItinerary = (itinerary) => {
	selectedItinerary.value = itinerary;
	id_of_selected.value = itinerary.id;
	addItineraryModal.value = false;
};
const goToViewItinerary = (itineraryId) => {
	// Logic to navigate to the itinerary view page
	// Assuming you are using Vue Router
	router.push({ name: "view-itinerary", params: { id: itineraryId } });
};

onMounted(() => {
	initializeAutocompleteCountry();
});
</script>
<style scoped></style>
