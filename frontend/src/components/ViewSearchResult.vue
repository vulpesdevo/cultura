<template lang="">
	<div
		class="flex flex-col items-center align-middle w-full sm:px-11 md:px-24 lg:px-20 py-5 overflow-auto overflow-x-hidden scroll-smooth h-screen sm:pt-3 bg-field dark:bg-dark-notif px-2"
	>
		<section class="w-full mb-10 sm:mb-0">
			<div v-if="users.length > 0" class="flex flex-col w-full">
				<label
					for=""
					class="text-prime dark:text-interface text-lg pb-2"
					>Users:</label
				>
				<div class="w-full grid sm:grid-cols-2 gap-4">
					<router-link
						v-for="user in users"
						:key="user?.id"
						:to="{
							name: 'user-profile',
							params: { username: user?.id },
							query: { id: user?.id },
						}"
						class="bg-white dark:bg-dark-field shadow-lg rounded-xl overflow-hidden transition-all duration-300 hover:shadow-xl"
					>
						<div class="flex items-center p-4 sm:p-6">
							<div class="flex-shrink-0 mr-4">
								<img
									:src="user.user_photo"
									:alt="`${user.fullname}'s profile picture`"
									class="size-14 rounded-full object-cover border-2 border-gray-200 dark:border-gray-700"
								/>
							</div>
							<div class="flex-grow">
								<h3
									class="text-sm sm:text-xl font-semibold text-gray-900 dark:text-white mb-1"
								>
									{{ user.fullname }}
								</h3>
								<div
									class="flex sm:flex-row flex-col items-center space-x-2"
								>
									<p
										class="text-xs text-gray-600 dark:text-gray-300"
									>
										{{ user.country }}
									</p>
									<p
										class="text-xs text-gray-500 dark:text-gray-400 truncate"
									>
										{{ user.email }}
									</p>
								</div>
							</div>
							<div class="flex-shrink-0 ml-4">
								<ChevronRightIcon
									class="w-6 h-6 text-gray-400"
								/>
							</div>
						</div>
					</router-link>
				</div>
			</div>
			<div v-if="posts" class="flex flex-col pt-4">
				<label for="" class="text-prime dark:text-interface text-lg"
					>Posts:</label
				>
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
										<div
											class="flex items-center space-x-2"
										>
											<router-link
												v-if="
													post.cultura_user?.user
														.username ===
													user.user.username
												"
												:to="{ name: 'profile' }"
												class="font-medium text-xs text-gray-900 dark:text-white hover:underline"
											>
												@{{
													post.cultura_user?.user
														.username
												}}
											</router-link>
											<span
												v-else
												@click="
													gotoUser(post.cultura_user)
												"
												class="font-medium text-xs text-gray-900 dark:text-white cursor-pointer hover:underline"
											>
												@{{
													post.cultura_user?.user
														.username
												}}
											</span>
											<span
												class="text-sm text-gray-500 dark:text-gray-400"
												>•</span
											>
											<span
												class="text-xs text-gray-500 dark:text-gray-400"
											>
												{{
													timesince(post.date_posted)
												}}
											</span>
										</div>
										<div
											class="text-xs text-gray-500 dark:text-gray-400"
										>
											{{ post.category }} |
											{{ post.country }}
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
											<i
												class="fas fa-search-plus text-4xl"
											></i>
										</span>
									</div>
								</div>

								<div v-else-if="post.image" class="space-y-4">
									<label class="block">
										<span class="sr-only"
											>Choose image</span
										>
										<input
											type="file"
											@change="
												handleImageUpload($event, post)
											"
											accept="image/*"
											class="block w-full text-sm text-gray-500 dark:text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 dark:file:bg-gray-700 dark:file:text-gray-200 hover:file:bg-blue-100 dark:hover:file:bg-gray-600 transition-all duration-200"
										/>
									</label>
									<img
										v-if="post.previewImage"
										:src="post.previewImage"
										alt="Preview"
										class="w-full h-auto max-h-[20rem] object-cover rounded-xl cursor-pointer"
										@click="
											openImageModal(post.previewImage)
										"
									/>
								</div>

								<!-- Itinerary Section -->
								<div
									v-else
									v-for="itinerary in post.itinerary_in_post"
									:key="itinerary.id"
									class="mt-4 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-200 cursor-pointer"
									@click="goToViewItinerary(itinerary.id)"
								>
									<img
										v-if="itinerary.main_image"
										:src="itinerary.main_image"
										alt=""
										class="w-full h-48 object-cover"
									/>

									<div
										class="p-4 bg-gray-50 dark:bg-gray-800"
									>
										<h3
											class="text-sm sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
										>
											{{ itinerary.main_title }}
										</h3>
										<p
											class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
										>
											{{ itinerary.main_description }}
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
									<span class="text-xs">{{
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
										<span class="text-xs">{{
											formatLikeCount(post.like_count)
										}}</span>
									</button>
									<div
										v-if="post.likers.length > 0"
										class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-48 bg-white dark:bg-gray-800 rounded-md shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 ease-in-out"
									>
										<div
											class="p-2 max-h-40 overflow-y-auto space-y-2"
											v-for="like in post.likers"
										>
											<router-link
												to="/profile"
												v-if="
													like?.user.username ===
													user?.user.username
												"
												class="flex items-center space-x-2 cursor-pointer py-1 px-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition"
												><img
													:src="like.user_photo"
													alt="User"
													class="size-5 rounded-full object-cover"
												/><span
													class="text-xs text-gray-700 dark:text-gray-300"
												>
													You
												</span></router-link
											>
											<div
												v-else
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
												>
													{{ like.user.username }}
												</span>
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
						<div
							class="flex min-h-screen items-center justify-center p-4"
						>
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
									<h2
										class="text-2xl font-semibold text-white"
									>
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
													<span
														class="text-gray-500 text-sm"
														>{{ data.category }} |
														{{ data.country }}</span
													>
												</div>
											</div>
											<p
												class="mt-1 text-gray-300 text-sm"
											>
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
											<div
												class="flex items-center space-x-2"
											>
												<span
													class="text-white font-medium"
													>{{ comment.author }}</span
												>
												<span class="text-gray-500"
													>to</span
												>
												<span class="text-blue-400">{{
													comment.replied_to
												}}</span>
												<span
													class="text-gray-500 text-sm"
													>{{
														timesince(
															comment.date_posted
														)
													}}</span
												>
											</div>
											<p
												class="mt-1 text-gray-300 text-sm"
											>
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
												@click="
													addItineraryModal = false
												"
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
		</section>
	</div>
</template>
<script setup>
import axios from "axios";
import { ref, reactive, onMounted, computed } from "vue";
import { useDark, useToggle } from "@vueuse/core";
import moment from "moment";
import { useStore } from "vuex";
import { useRouter, useRoute } from "vue-router";
import { XIcon, ThumbsUpIcon } from "lucide-vue-next";
import axiosClient from "../axios";
import { ChevronRightIcon } from "@heroicons/vue/24/outline";

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
const store = useStore();

const router = useRouter();
const route = useRoute();

const post_profile_display = ref(null);
const selectedImageUrl = ref(null);
const picture = ref(null);
const auth_user = ref("");
const isEditing = ref(true);
const postTitle = ref("");
const addItineraryModal = ref(false);
const showModal = ref(false);
const categoryOption = ref("");
const postContent = ref("");
const countryPost = ref("");
const posts = ref([]);
const users = ref([]);
const result = ref(null);
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
const user = computed(() => store.state.user.data);

const token = sessionStorage.getItem("TOKEN");

const client = axios.create({
	baseURL: "https://apicultura.futurewebbuilders.design",
	withCredentials: true,
	timeout: 5000,
	xsrfCookieName: "csrftoken",
	xsrfHeaderName: "X-Csrftoken",
	headers: {
		Authorization: `Token ${token}`,
		"Content-Type": "application/json",
	},
});

onMounted(() => {
	if (!route.query.q) {
		router.push({ name: "dashboard" });
	} else {
		result.value = JSON.parse(route.query.q);
		console.log("valid object", result.value);
		posts.value = result.value.posts;
		users.value = result.value.users;
		console.log("user", result.value.users);
	}
});

const follow = (userId) => {
	axiosClient
		.post(`/follow/${userId}/follow/`)
		.then((response) => {
			console.log(response.data);
			const userIndex = users.value.findIndex(
				(user) => user.user === userId
			);

			result.value.users = result.value.users.map((user) => {
				if (user.user === userId) {
					user.is_followed = response.data.is_followed;
				}
				if (userIndex !== -1) {
					users.value[userIndex].is_followed =
						response.data.is_followed;
				}
				return user;
			});
		})
		.catch((error) => {
			console.error("Error following the user:", error);
		});
};

const goToViewItinerary = (itineraryId) => {
	console.log("ITINERARY ", itineraryId);

	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};

const likePost = (post_id) => {
	axiosClient
		.post(`/like-posts/${post_id}/like_post/`)
		.then((response) => {
			console.log(response.data);
			fetchPosts();
		})
		.catch((error) => {
			console.error("Error liking the post:", error);
		});
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const selectPost = (post) => {
	// showModal.value = true;
	selectedPost.value = [post];
	// console.log("GET POST", selectedPost.value[0]._id);
	const _id = selectedPost.value[0]._id;
	// replied_to.value = selectedPost.value[0].author;
	// comments_in_post.value =
	// 	posts.value.find((p) => p._id === post_id.value)?.comments || [];
	// console.log("the id : ", comments_in_post.value);
	router.push({
		name: "view-post",
		params: { post: _id },
		query: { n: "" },
	});
};

const submitReply = () => {
	axiosClient
		.post("/commenting", {
			post_id: post_id.value,
			replied_to: replied_to.value,
			body: reply.value,
		})
		.then((response) => {
			console.log(response.data);
			reply.value = "";
			fetchPosts();
		})
		.catch((error) => {
			console.error(error);
		});
};

const fetchPosts = () => {
	axiosClient
		.get(`/posts-list`)
		.then((response) => {
			posts.value = response.data.reverse();
			if (posts.value.length > 0) {
				console.log("GET POST fetch", selectedPost.value);
				itineraries_frompost.value = posts.value[0].itinerary_in_post;
				comments_in_post.value =
					posts.value.find((p) => p._id === post_id.value)
						?.comments || [];
				console.log("the id : ", comments_in_post.value);
			}
			console.log("updated :", posts.value[0]);
		})
		.catch((error) => {
			console.log(error);
		});
};
const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
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

const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>
