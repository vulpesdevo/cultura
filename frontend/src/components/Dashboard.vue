<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-11 md:px-24 lg:px-20 py-5 overflow-auto scroll-smooth h-screen sm:pt-3 bg-field dark:bg-dark-notif px-2"
	>
		<div
			class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
		>
			<div class="flex justify-between items-center w-full">
				<div class="w-1/2">
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
					</div>
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
				<div class="flex space-x-2">
					<div class="hidden sm:flex size-14 rounded-full">
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
				<p
					class="hidden sm:flex text-sm text-prime dark:text-dark-prime"
				>
					What country is your post about?
				</p>
				<p
					class="flex sm:hidden text-sm text-prime dark:text-dark-prime"
				>
					Country
				</p>
				<input
					id="country-post"
					v-model="countryPost"
					type="text"
					ref="autocompletecountry"
					placeholder="Country"
					class="bg-field dark:bg-dark-second-dark dark:text-dark-prime text-xs rounded-full pl-4 ml-2 h-9 w-1/2 outline-none"
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
		<section class="posts w-full mb-10 sm:mb-0">
			<div>
				<div
					class="relative post-contents w-full p-6 mt-4 rounded-xl shadow-lg bg-white dark:bg-dark-field transition-all duration-200 hover:shadow-xl font-montserrat"
					v-for="post in posts"
					:key="post._id"
				>
					<!-- Header Section -->
					<div class="flex items-start justify-between mb-4">
						<div class="flex items-center space-x-3">
							<div
								class="w-12 h-12 rounded-full overflow-hidden ring-2 ring-gray-100 dark:ring-gray-700"
							>
								<img
									:src="post.cultura_user.user_photo"
									alt="Profile"
									class="w-full h-full object-cover"
								/>
							</div>
							<div class="flex flex-col space-y-1">
								<div class="flex items-center space-x-2">
									<span
										@click="gotoUser(post.cultura_user)"
										class="font-medium text-xs text-gray-900 dark:text-white cursor-pointer hover:underline"
										>@{{ post.author }}</span
									>
									<span
										class="text-sm text-gray-500 dark:text-gray-400"
										>•</span
									>
									<span
										class="text-xs text-gray-500 dark:text-gray-400"
										>{{ timesince(post.date_posted) }}</span
									>
								</div>
								<div
									class="text-xs text-gray-500 dark:text-gray-400"
								>
									{{ post.category }} | {{ post.country }}
								</div>
							</div>
						</div>

						<div class="flex items-center">
							<router-link
								:to="{
									name: 'report',
									query: {
										post_id: post._id,
										user_id: auth_user,
									},
								}"
								class="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full transition-colors duration-200"
							>
								<i
									class="fa-solid fa-circle-exclamation text-gray-400 hover:text-red-500 text-xl"
								></i>
							</router-link>
						</div>
					</div>

					<!-- Title Section -->
					<h1
						class="font-bebas-neue text-2xl font-bold text-second mb-3 leading-4 tracking-wider"
					>
						{{ post.title }}
					</h1>

					<!-- Content Section -->
					<div class="space-y-4">
						<p
							v-if="!post.isEditing"
							class="text-gray-600 dark:text-gray-300 leading-relaxed"
						>
							{{ post.content }}
						</p>

						<textarea
							v-else
							v-model="post.editedContent"
							class="w-full p-4 rounded-lg border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							rows="4"
						></textarea>

						<!-- Image Section -->
						<div
							v-if="!post.isEditing && post.image"
							class="relative rounded-xl overflow-hidden cursor-pointer"
							@click="openImageModal(post.image)"
						>
							<img
								:src="post.image"
								alt=""
								class="w-full h-auto max-h-[20rem] object-cover"
							/>
							<div
								class="absolute inset-0 bg-black bg-opacity-0 hover:bg-opacity-10 transition-all duration-200 flex items-center justify-center"
							>
								<span
									class="text-white opacity-0 hover:opacity-100 transition-opacity duration-200"
								>
									<i class="fas fa-search-plus text-4xl"></i>
								</span>
							</div>
						</div>

						<div v-else-if="post.image" class="space-y-4">
							<label class="block">
								<span class="sr-only">Choose image</span>
								<input
									type="file"
									@change="handleImageUpload($event, post)"
									accept="image/*"
									class="block w-full text-sm text-gray-500 dark:text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 dark:file:bg-gray-700 dark:file:text-gray-200 hover:file:bg-blue-100 dark:hover:file:bg-gray-600 transition-all duration-200"
								/>
							</label>
							<img
								v-if="post.previewImage"
								:src="post.previewImage"
								alt="Preview"
								class="w-full h-auto max-h-[20rem] object-cover rounded-xl cursor-pointer"
								@click="openImageModal(post.previewImage)"
							/>
						</div>

						<!-- Itinerary Section -->
						<div
							v-if="!post?.itinerary_in_post === []"
							class="mt-4 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-200 cursor-pointer"
							@click="
								goToViewItinerary(post?.itinerary_in_post?.id)
							"
						>
							<img
								:src="post?.itinerary_in_post?.main_image"
								alt=""
								class="w-full h-48 object-cover"
							/>
							<div class="p-4 bg-gray-50 dark:bg-gray-800">
								<h3
									class="text-xl font-bold text-gray-900 dark:text-white mb-2"
								>
									{{ post?.itinerary_in_post?.main_title }}
								</h3>
								<p
									class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
								>
									{{
										post?.itinerary_in_post
											?.main_description
									}}
								</p>
							</div>
						</div>
					</div>

					<!-- Actions Section -->
					<div
						class="flex items-center justify-end space-x-4 mt-4 pt-4 border-t border-gray-100 dark:border-gray-700"
					>
						<button
							@click.prevent="selectPost(post)"
							class="flex items-center space-x-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 transition-colors duration-200"
						>
							<ChatBubbleLeftIcon class="size-4" />
							<span class="text-sm">{{
								post.comments?.length || 0
							}}</span>
						</button>

						<div class="relative group">
							<button
								@click="likePost(post._id)"
								class="flex items-center space-x-1"
								:class="
									post.is_liked
										? 'text-second'
										: 'text-gray-500 hover:text-second'
								"
							>
								<HeartIcon
									v-if="post.is_liked"
									class="size-4"
								/>
								<HeartIcon v-else class="size-4" />
								<span>{{
									formatLikeCount(post.like_count)
								}}</span>
							</button>
							<div
								v-if="post.likers.length > 0"
								class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 ease-in-out"
							>
								<div
									class="p-2 max-h-40 overflow-y-auto space-y-2"
								>
									<div
										v-for="like in post.likers"
										:key="like.id"
										@click="gotoUser(like)"
										class="flex items-center space-x-2 cursor-pointer py-1 px-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition"
									>
										<img
											:src="like.user_photo"
											alt="User"
											class="size-5 rounded-full object-cover"
										/>
										<span
											class="text-xs text-gray-700 dark:text-gray-300"
											>{{ like.user.username }}</span
										>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Image Modal -->
				<div
					v-if="showImageModal"
					class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-75"
					@click="closeImageModal"
				>
					<div class="max-w-4xl w-full max-h-screen p-4">
						<img
							:src="modalImage"
							alt="Full size image"
							class="w-full h-auto max-h-full object-contain"
						/>
					</div>
				</div>
			</div>

			<div
				class="comments-modal fixed z-50 inset-0 overflow-y-auto"
				aria-labelledby="modal-title"
				role="dialog"
				aria-modal="true"
				v-if="showModal"
			>
				<div class="flex min-h-screen items-center justify-center p-4">
					<div
						class="fixed inset-0 bg-black/90 transition-opacity"
						aria-hidden="true"
					></div>

					<div
						class="relative w-full max-w-2xl bg-[#1c1c1f] rounded-xl shadow-xl overflow-hidden"
					>
						<!-- Header -->
						<div
							class="flex items-center justify-between p-6 border-b border-gray-800"
						>
							<h2 class="text-2xl font-semibold text-white">
								Comments
							</h2>
							<button
								@click="showModal = false"
								class="text-gray-400 hover:text-white transition-colors"
							>
								<XIcon class="h-6 w-6" />
							</button>
						</div>

						<!-- Post Content -->
						<div
							v-for="data in selectedPost"
							:key="data._id"
							class="p-6 border-b border-gray-800"
						>
							<div class="flex space-x-4">
								<img
									:src="data.author_user_photo"
									alt="Profile"
									class="h-10 w-10 rounded-full object-cover"
								/>
								<div class="flex-1 min-w-0">
									<div
										class="flex items-center justify-between"
									>
										<div
											class="flex items-center space-x-2"
										>
											<span
												class="text-white font-medium"
												>{{ data.author }}</span
											>
											<span class="text-gray-500 text-sm"
												>{{ data.category }} |
												{{ data.country }}</span
											>
										</div>
									</div>
									<p class="mt-1 text-gray-300 text-sm">
										{{ data.content }}
									</p>
								</div>
							</div>
						</div>

						<!-- Comments List -->
						<div
							class="overflow-y-auto max-h-[400px] p-6 space-y-6"
						>
							<div
								v-for="comment in comments_in_post"
								:key="comment._id"
								class="flex space-x-4 relative"
							>
								<div class="flex-shrink-0">
									<img
										:src="comment.author_user_photo"
										alt="Profile"
										class="h-10 w-10 rounded-full object-cover"
									/>
								</div>
								<div class="flex-1 min-w-0">
									<div class="flex items-center space-x-2">
										<span class="text-white font-medium">{{
											comment.author
										}}</span>
										<span class="text-gray-500">to</span>
										<span class="text-blue-400">{{
											comment.replied_to
										}}</span>
										<span class="text-gray-500 text-sm">{{
											timesince(comment.date_posted)
										}}</span>
									</div>
									<p class="mt-1 text-gray-300 text-sm">
										{{ comment.body }}
									</p>
									<!-- <div
										class="flex items-center space-x-4 mt-2"
									>
										<button
											class="flex items-center space-x-1 text-gray-400 hover:text-white transition-colors"
										>
											<ThumbsUpIcon class="h-4 w-4" />
										</button>
										<button
											class="text-gray-400 hover:text-white transition-colors text-sm"
										>
											Reply
										</button>
									</div> -->
								</div>
							</div>
						</div>

						<!-- Reply Input -->
						<div class="p-6 border-t border-gray-800">
							<div class="flex space-x-4">
								<img
									:src="post_profile_display"
									alt="Profile"
									class="h-10 w-10 rounded-full object-cover"
								/>
								<div class="flex-1">
									<textarea
										v-model="reply"
										rows="3"
										class="w-full bg-gray-800 border border-gray-700 rounded-lg p-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
										:placeholder="
											'Replying to ' +
											selectedPost[0]?.author
										"
									></textarea>
									<div
										class="flex justify-end mt-3 space-x-3"
									>
										<button
											@click.prevent="submitReply"
											class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-full text-sm font-medium transition-colors"
										>
											Reply
										</button>
									</div>
								</div>
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
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useDark, useToggle } from "@vueuse/core";
import axios from "axios";
import moment from "moment";
import { clean } from "profanity-cleaner";
import { XIcon, ThumbsUpIcon } from "lucide-vue-next";
import {
	ChatBubbleLeftIcon,
	HeartIcon,
	PencilSquareIcon,
	XMarkIcon,
	CheckIcon,
	PhotoIcon,
	FaceSmileIcon,
	PaperAirplaneIcon,
	ArrowLeftIcon,
} from "@heroicons/vue/24/solid";

import filipinoBadWords from "../custom-badwords";

const store = useStore();
const router = useRouter();
const isDark = useDark();
const toggleDark = useToggle(isDark);

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
const comments_in_post = ref([]);
const itineraries = ref([]);
const selectedItinerary = ref(null);
const id_of_selected = ref("");
const isFullTextShown = ref({});

const showImageModal = ref(false);
const modalImage = ref("");
// functions for image modal
const openImageModal = (imageUrl) => {
	modalImage.value = imageUrl;
	showImageModal.value = true;
};

const closeImageModal = () => {
	showImageModal.value = false;
};

const client = axios.create({
	baseURL: "http://127.0.0.1:8000",
	withCredentials: true,
	timeout: 5000,
	xsrfCookieName: "csrftoken",
	xsrfHeaderName: "X-Csrftoken",
	headers: {
		Authorization: `Token ${sessionStorage.getItem("TOKEN")}`,
		"Content-Type": "application/json",
	},
});

const fetchUser = async () => {
	try {
		const res = await store.dispatch("fetchUserData");
		console.log(res);

		post_profile_display.value = res.profile?.user_photo;
		auth_user.value = res.user.id;
	} catch (error) {
		console.error("Error fetching user:", error);
	}
};

const fetchPosts = async () => {
	try {
		await store.dispatch("fetchPosts");

		posts.value = store.getters.getPosts;
		console.log("POSTS:  ", posts.value);
	} catch (error) {
		console.error("Error fetching posts:", error);
	}
};
const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
};
const handleFileSelection = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		picture.value = file;
	}
};

const handleTitleChange = () => {
	if (postTitle.value.trim() === "") {
		isEditing.value = true;
	} else {
		isEditing.value = false;
	}
};

const initializeAutocompleteCountry = () => {
	const inputElement = document.getElementById("country-post");
	if (
		inputElement &&
		window.google &&
		window.google.maps &&
		window.google.maps.places
	) {
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

const timesince = (date) => {
	return moment(date).fromNow();
};

const likePost = async (postId) => {
	try {
		await store.dispatch("likePost", postId);
		await fetchPosts();
	} catch (error) {
		console.error("Error liking the post:", error);
	}
};

const selectPost = (post) => {
	// showModal.value = true;
	// selectedPost.value = [post];
	// post_id.value = post._id;
	// replied_to.value = post.author;
	// comments_in_post.value = post.comments || [];
	router.push({
		name: "view-post",
		params: { post: post._id },
		query: { n: "" },
	});
};
const gotoUser = async (user) => {
	router.push({
		name: "user-profile",
		params: {
			username: user.user.username,
		},
		query: {
			id: user.id,
		},
	});
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
	}

	const formData = new FormData();
	formData.append("title", postTitle.value);
	formData.append("category", categoryOption.value);
	formData.append("body", postContent.value);
	formData.append("country", countryPost.value);
	if (id_of_selected.value) {
		formData.append("itinerary_id", id_of_selected.value);
	}
	if (picture.value instanceof File) {
		formData.append("image", picture.value, picture.value.name);
	}

	try {
		await client.post("/api/posting", formData, {
			headers: { "Content-Type": "multipart/form-data" },
		});
		postTitle.value = "POST TITLE";
		categoryOption.value = "";
		postContent.value = "";
		countryPost.value = "";
		selectedImageUrl.value = null;
		picture.value = null;
		selectedItinerary.value = null;
		id_of_selected.value = "";
		await fetchPosts();
	} catch (error) {
		console.error("Error submitting post:", error);
	}
};

const submitReply = async () => {
	try {
		await client.post("/api/commenting", {
			post_id: post_id.value,
			replied_to: replied_to.value,
			body: reply.value,
		});
		reply.value = "";
		await fetchPosts();
		const updatedPost = posts.value.find((p) => p._id === post_id.value);
		if (updatedPost) {
			comments_in_post.value = updatedPost.comments || [];
		}
	} catch (error) {
		console.error("Error submitting reply:", error);
	}
};

const fetchSavedItineraries = async () => {
	try {
		await store.dispatch("fetchItineraries");
		itineraries.value = store.getters.getItineraries;
	} catch (error) {
		console.error("Error fetching saved itineraries:", error);
	}
};

const selectItinerary = (itinerary) => {
	selectedItinerary.value = itinerary;
	id_of_selected.value = itinerary.id;
	addItineraryModal.value = false;
};

const goToViewItinerary = (itineraryId) => {
	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};

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

onMounted(async () => {
	await fetchUser();
	await fetchPosts();
	await fetchSavedItineraries();
	initializeAutocompleteCountry();
	setInterval(fetchSavedItineraries, 5000);
});
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>
