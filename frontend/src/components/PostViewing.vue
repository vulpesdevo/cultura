<template lang="">
	<div
		class="bg-gray-100 dark:bg-notif h-screen overflow-auto pt-5 pb-5 px-4 sm:px-6 lg:px-28"
	>
		<div v-if="isLoading" class="flex items-center justify-center h-screen">
			<div
				class="w-12 h-12 border-t-4 border-blue-500 border-solid rounded-full animate-spin"
			></div>
		</div>
		<div v-else>
			<button
				@click="goBack"
				class="mb-6 flex items-center space-x-2 text-gray-600 hover:text-gray-800 dark:text-gray-300 dark:hover:text-white transition-colors duration-200"
			>
				<ArrowLeftIcon class="h-5 w-5" />
				<span class="text-sm font-medium">Back</span>
			</button>
			<div
				v-for="post in posts"
				:key="post._id"
				class="bg-white dark:bg-dark-field rounded-lg shadow-lg mb-8"
			>
				<!-- Post Header -->
				<div
					class="p-4 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between"
				>
					<div class="flex items-center space-x-3">
						<img
							:src="post.cultura_user.user_photo"
							alt="Profile"
							class="w-10 h-10 rounded-full object-cover"
						/>
						<div>
							<h2
								class="font-semibold text-gray-900 dark:text-white"
							>
								{{ post.title }}
							</h2>
							<div
								class="flex items-center text-sm text-gray-500 dark:text-gray-400"
							>
								<span>@{{ post.author }}</span>
								<span class="mx-1">•</span>
								<span>{{ timesince(post.date_posted) }}</span>
							</div>
						</div>
					</div>
					<div class="text-sm text-gray-500 dark:text-gray-400">
						{{ post.category }} | {{ post.country }}
					</div>
				</div>

				<!-- Post Content -->
				<div class="p-4">
					<p class="text-gray-800 dark:text-gray-200 mb-4">
						{{ post.content }}
					</p>
					<img
						v-if="post.image"
						:src="post.image"
						alt="Post image"
						class="w-auto h-40 max-h-96 object-cover rounded-lg mb-4"
					/>

					<!-- Itinerary Preview (if available) -->
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

						<div class="p-4 bg-gray-50 dark:bg-gray-800">
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

				<!-- Post Actions -->
				<div
					class="px-4 py-2 border-t border-gray-200 dark:border-gray-700 flex items-center justify-between"
				>
					<button
						@click="showComments = !showComments"
						class="flex items-center space-x-1 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
					>
						<ChatBubbleLeftIcon class="h-5 w-5" />
						<span>{{ post.comments.length }} Comments</span>
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
							<HeartIcon v-if="post.is_liked" class="h-5 w-5" />
							<HeartIcon v-else class="h-5 w-5" />
							<span>{{ formatLikeCount(post.like_count) }}</span>
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

				<!-- Comments Section -->
				<div
					v-if="showComments"
					class="px-4 py-2 bg-gray-50 dark:bg-dark-field rounded-lg pb-3"
				>
					<div
						class="h-40 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-300 dark:scrollbar-thumb-gray-600"
					>
						<div
							class="flex justify-center items-center h-full text-gray-500 dark:text-gray-400"
							v-if="!post.comments.length"
						>
							Be first to Comment
						</div>
						<div
							v-else
							v-for="comment in post.comments"
							:key="comment._id"
							class="mb-4 last:mb-0"
						>
							<div class="flex items-start space-x-3">
								<img
									:src="comment.author?.user_photo"
									alt="Commenter"
									class="w-8 h-8 rounded-full"
								/>
								<div class="flex-1">
									<div
										class="bg-white dark:bg-gray-700 rounded-lg p-3 shadow"
									>
										<div
											class="flex items-center justify-between mb-2"
										>
											<div class="space-x-2">
												<span
													@click="
														gotoUser(comment.author)
													"
													class="font-semibold text-xs text-gray-900 dark:text-white hover:underline cursor-pointer"
													>{{
														comment.author.user
															?.username
													}}</span
												>
												<span
													class="text-xs text-gray-500 dark:text-gray-400"
													>{{
														timesince(
															comment?.date_posted
														)
													}}</span
												>
											</div>
											<div
												v-if="
													comment.author.user?.id ===
														user.user?.id &&
													!editingCommentId
												"
												class="flex space-x-2"
											>
												<button
													@click="startEdit(comment)"
													class="text-xs text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-300"
												>
													<PencilSquareIcon
														class="h-4 w-4"
													/>
												</button>
												<button
													@click="
														confirmDeleteComment(
															comment
														)
													"
													class="text-xs text-red-500 hover:text-red-600 dark:text-red-400 dark:hover:text-red-300"
												>
													<TrashIcon
														class="h-4 w-4"
													/>
												</button>
											</div>
										</div>
										<div
											v-if="
												editingCommentId === comment._id
											"
										>
											<textarea
												v-model="editedCommentText"
												class="w-full px-3 py-2 text-sm text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 dark:bg-gray-700 dark:text-gray-200 dark:border-gray-600"
												rows="3"
											></textarea>
											<div
												class="mt-2 flex justify-end space-x-2"
											>
												<button
													@click="cancelEdit"
													class="px-3 py-1 text-sm text-gray-600 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200 flex items-center"
												>
													<XMarkIcon
														class="h-4 w-4 mr-1"
													/>
													Cancel
												</button>
												<button
													@click="
														saveEdit(comment._id)
													"
													class="px-3 py-1 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600 flex items-center"
												>
													<CheckIcon
														class="h-4 w-4 mr-1"
													/>
													Save
												</button>
											</div>
										</div>
										<p
											v-else
											class="text-sm text-gray-800 dark:text-gray-200"
										>
											{{ comment.body }}
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- New Comment Form -->
					<form @submit.prevent="submitReply" class="mt-4">
						<div class="flex items-start space-x-3">
							<img
								:src="user.user_photo"
								alt="Your profile"
								class="w-8 h-8 rounded-full"
							/>
							<div class="flex-1">
								<textarea
									v-model="reply"
									placeholder="Write a comment..."
									class="w-full px-3 py-2 text-sm text-gray-700 border rounded-lg focus:outline-none focus:border-blue-500 dark:bg-gray-800 dark:text-gray-200 dark:border-gray-600"
									rows="3"
								></textarea>
								<div class="mt-2 flex justify-end items-center">
									<button
										type="submit"
										class="px-4 py-2 bg-blue-500 text-white rounded-full text-sm font-medium hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 flex items-center"
										:disabled="!reply.trim()"
									>
										<PaperAirplaneIcon class="h-4 w-4" />
									</button>
								</div>
							</div>
						</div>
					</form>
				</div>
				<!-- Delete Confirmation Modal -->
				<div
					v-if="showDeleteModal"
					class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
				>
					<div
						class="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-sm w-full mx-4"
					>
						<h3
							class="text-lg font-semibold mb-4 text-gray-900 dark:text-white"
						>
							Confirm Delete
						</h3>
						<p class="mb-6 text-gray-600 dark:text-gray-300">
							Are you sure you want to delete this comment? This
							action cannot be undone.
						</p>
						<div class="flex justify-end space-x-4">
							<button
								@click="cancelDelete"
								class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-400"
							>
								Cancel
							</button>
							<button
								@click="deleteComment"
								class="px-4 py-2 text-sm font-medium text-white bg-red-500 rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
							>
								Delete
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import moment from "moment";
import { useStore } from "vuex";
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
	TrashIcon,
} from "@heroicons/vue/24/solid";
import axiosClient from "../axios";
const store = useStore();
const router = useRouter();
const route = useRoute();
const posts = ref([]);
const reply = ref("");
const showComments = ref(false);
const isLoading = ref(true);
const currentUserPhoto = ref("/path/to/default/user/photo.jpg"); // Replace with actual user photo
const editingCommentId = ref(null);
const editedCommentText = ref("");
const showDeleteModal = ref(false);
const commentToDelete = ref(null);

const client = axios.create({
	baseURL: "https://apicultura.futurewebbuilders.design",
	withCredentials: true,
	headers: {
		Authorization: `Token ${sessionStorage.getItem("TOKEN")}`,
		"Content-Type": "application/json",
	},
});
const user = computed(() => store.state.user.data);
const fetchUser = async () => {
	try {
		await store.dispatch("fetchUserData");
		console.log("User data fetched:", user.value);
	} catch (error) {
		console.error("Error fetching user data:", error);
	}
};
const confirmDeleteComment = (comment) => {
	commentToDelete.value = comment;
	showDeleteModal.value = true;
};

const cancelDelete = () => {
	showDeleteModal.value = false;
	commentToDelete.value = null;
};

const deleteComment = async () => {
	if (!commentToDelete.value) return;

	await store
		.dispatch("deleteComment", {
			_id: commentToDelete.value._id,
		})
		.then((response) => {
			console.log("Comment deleted:", response);

			return fetchPost(); // Refetch posts to update the comment list
		})
		.then(() => {
			showDeleteModal.value = false;
			commentToDelete.value = null;
		})
		.catch((error) => {
			console.error("Error deleting comment:", error);
		});
};
onMounted(async () => {
	isLoading.value = true;
	try {
		await fetchPost();
		await fetchUser();
	} catch (error) {
		console.error("Error fetching data:", error);
	} finally {
		isLoading.value = false;
	}
});
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
const likePost = (post_id) => {
	axiosClient
		.post(`/like-posts/${post_id}/like_post/`)
		.then((response) => {
			console.log(response.data);
			fetchPost();
		})
		.catch((error) => {
			console.error("Error liking the post:", error);
		});
};
const fetchPost = async () => {
	try {
		const response = await axiosClient.get(
			`/liked-post-view/${route.params.post}/${route.query.n}`
		);
		console.log("RESPONSE", response);
		posts.value = response.data;
	} catch (error) {
		console.error("Error fetching post:", error);
	}
};

const submitReply = async () => {
	if (!reply.value.trim()) return;

	try {
		await axiosClient.post("/commenting", {
			post_id: posts.value[0]._id, // Assuming we're commenting on the first post
			body: reply.value,
		});
		reply.value = "";
		await fetchPost(); // Refetch posts to show new comment
	} catch (error) {
		console.error("Error submitting reply:", error);
	}
};

const goToViewItinerary = (itineraryId) => {
	console.log("ITINERARY ", itineraryId);

	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
};

const toggleComments = () => {
	showComments.value = !showComments.value;
};

const startEdit = (comment) => {
	editingCommentId.value = comment._id;
	editedCommentText.value = comment.body;
};

const cancelEdit = () => {
	editingCommentId.value = null;
	editedCommentText.value = "";
};

const saveEdit = async (commentId) => {
	if (!editedCommentText.value.trim()) return;

	try {
		await axiosClient.put(`/comments/${commentId}`, {
			body: editedCommentText.value,
		});
		await fetchPost(); // Refetch posts to show updated comment
		editingCommentId.value = null;
		editedCommentText.value = "";
	} catch (error) {
		console.error("Error updating comment:", error);
	}
};

function goBack() {
	router.go(-1);
}
</script>

<style>
.scrollbar-thin::-webkit-scrollbar {
	width: 6px;
}

.scrollbar-thin::-webkit-scrollbar-track {
	background: transparent;
}

.scrollbar-thin::-webkit-scrollbar-thumb {
	background-color: #cbd5e0;
	border-radius: 3px;
}

.dark .scrollbar-thin::-webkit-scrollbar-thumb {
	background-color: #4a5568;
}

.line-clamp-2 {
	display: -webkit-box;
	-webkit-line-clamp: 2;
	-webkit-box-orient: vertical;
	overflow: hidden;
}
</style>
