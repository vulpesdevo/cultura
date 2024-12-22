<template>
	<div class="min-h-screen pt-8 bg-gray-50 dark:bg-notif">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
			<!-- Search Summary -->
			<div class="mb-8">
				<h1
					class="text-xl font-semibold text-gray-900 dark:text-white mb-2"
				>
					Search Results for "{{ searchQuery }}"
				</h1>
				<p class="text-gray-600 dark:text-gray-400">
					{{ totalResults }} results found
				</p>
			</div>

			<!-- Loading State -->
			<div v-if="isLoading" class="flex justify-center py-12">
				<div
					class="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 dark:border-white"
				></div>
			</div>

			<!-- Results Content -->
			<div v-else class="grid gap-8">
				<!-- Users Section -->
				<section v-if="users.length" class="rounded-lg pb-2">
					<div
						class="px-6 py-4 border-b mb-2 border-gray-300 dark:border-gray-700"
					>
						<h2
							class="text-lg font-semibold text-gray-900 dark:text-white"
						>
							Users ({{ users.length }})
						</h2>
					</div>
					<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
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
							<div class="flex items-center p-2 sm:p-4">
								<div class="flex-shrink-0 mr-4">
									<img
										:src="
											user.user_photo ||
											'/placeholder.svg?height=56&width=56'
										"
										:alt="`${user.fullname}'s profile picture`"
										class="size-14 rounded-full object-cover border-2 border-gray-200 dark:border-gray-700"
									/>
								</div>
								<div class="flex-grow">
									<h3
										class="text-xs sm:text-sm font-semibold text-gray-900 dark:text-white mb-1"
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
				</section>

				<!-- Posts Section -->
				<section
					v-if="posts.length"
					class="bg-white dark:bg-dark-field rounded-lg shadow mb-10"
				>
					<div
						class="px-6 py-4 border-b border-gray-200 dark:border-gray-700"
					>
						<h2
							class="text-lg font-medium text-gray-900 dark:text-white"
						>
							Posts ({{ posts.length }})
						</h2>
					</div>
					<ul class="divide-y divide-gray-200 dark:divide-gray-700">
						<li
							v-for="post in posts"
							:key="post._id"
							class="px-6 py-4 hover:bg-gray-50 dark:hover:bg-gray-700 bg-white dark:bg-dark-field"
						>
							<div class="space-y-4">
								<div class="flex items-start space-x-3">
									<img
										:src="
											post.cultura_user.user_photo ||
											'/placeholder.svg?height=40&width=40'
										"
										:alt="post.cultura_user.user.username"
										class="h-10 w-10 rounded-full object-cover"
									/>
									<div class="flex-grow">
										<div
											class="flex items-center justify-between"
										>
											<h3
												class="text-sm font-medium text-gray-900 dark:text-white"
											>
												{{
													post.cultura_user.user
														.username
												}}
											</h3>
											<span
												class="text-sm text-gray-500 dark:text-gray-400"
											>
												{{
													timesince(post.date_posted)
												}}
											</span>
										</div>
										<p
											class="text-sm text-gray-500 dark:text-gray-400"
										>
											{{ post.category }} |
											{{ post.country }}
										</p>
									</div>
								</div>
								<h4
									class="text-xl font-medium font-bebas-neue text-gray-900 dark:text-white"
								>
									{{ post.title }}
								</h4>
								<p
									class="text-gray-600 dark:text-gray-300 line-clamp-3"
								>
									{{ post.content }}
								</p>
								<div v-if="post.image" class="mt-2">
									<img
										:src="post.image"
										:alt="post.title"
										class="w-full h-48 object-cover rounded-md cursor-pointer"
										@click="openImageModal(post.image)"
									/>
								</div>
								<div
									class="flex items-center justify-between mt-4"
								>
									<div class="flex items-center space-x-4">
										<button
											@click="likePost(post._id)"
											class="flex items-center space-x-1 text-gray-500 hover:text-second"
										>
											<HeartIcon
												:class="[
													'h-5 w-5',
													{
														'text-second fill-current':
															post.is_liked,
													},
												]"
											/>
											<span>{{
												formatLikeCount(post.like_count)
											}}</span>
										</button>
										<button
											@click="selectPost(post)"
											class="flex items-center space-x-1 text-gray-500 hover:text-blue-500"
										>
											<ChatBubbleLeftIcon
												class="h-5 w-5"
											/>
											<span>{{
												post.comments?.length || 0
											}}</span>
										</button>
									</div>
									<button
										@click="selectPost(post)"
										class="text-sm text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300"
									>
										View Post
									</button>
								</div>
							</div>
						</li>
					</ul>
				</section>

				<!-- No Results -->
				<div
					v-if="!users.length && !posts.length"
					class="text-center py-12 rounded-lg shadow"
				>
					<MagnifyingGlassIcon
						class="mx-auto h-12 w-12 text-gray-400 dark:text-gray-600 mb-4"
					/>
					<h3
						class="text-lg font-medium text-gray-900 dark:text-white mb-2"
					>
						No results found
					</h3>
					<p class="text-gray-600 dark:text-gray-400">
						Try adjusting your search terms or filters
					</p>
				</div>
			</div>

			<!-- Image Modal -->
			<TransitionRoot appear :show="showImageModal" as="template">
				<Dialog as="div" @close="closeImageModal" class="relative z-50">
					<TransitionChild
						as="template"
						enter="duration-300 ease-out"
						enter-from="opacity-0"
						enter-to="opacity-100"
						leave="duration-200 ease-in"
						leave-from="opacity-100"
						leave-to="opacity-0"
					>
						<div class="fixed inset-0 bg-black bg-opacity-75" />
					</TransitionChild>

					<div class="fixed inset-0 overflow-y-auto">
						<div
							class="flex min-h-full items-center justify-center p-4 text-center"
						>
							<TransitionChild
								as="template"
								enter="duration-300 ease-out"
								enter-from="opacity-0 scale-95"
								enter-to="opacity-100 scale-100"
								leave="duration-200 ease-in"
								leave-from="opacity-100 scale-100"
								leave-to="opacity-0 scale-95"
							>
								<DialogPanel
									class="w-full max-w-3xl transform overflow-hidden rounded-2xl p-6 text-left align-middle shadow-xl transition-all"
								>
									<img
										:src="modalImage"
										alt="Full size image"
										class="w-full h-auto"
									/>
								</DialogPanel>
							</TransitionChild>
						</div>
					</div>
				</Dialog>
			</TransitionRoot>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import moment from "moment";
import {
	Dialog,
	DialogPanel,
	TransitionChild,
	TransitionRoot,
} from "@headlessui/vue";
import {
	ChevronRightIcon,
	ExclamationCircleIcon,
	HeartIcon,
	ChatBubbleLeftIcon,
	MagnifyingGlassIcon,
} from "@heroicons/vue/24/outline";
import axiosClient from "../axios";

const route = useRoute();
const router = useRouter();
const store = useStore();

// State
const searchQuery = ref("");
const users = ref([]);
const posts = ref([]);
const isLoading = ref(true);
const error = ref(null);
const showImageModal = ref(false);
const modalImage = ref("");

// Computed
const totalResults = computed(() => users.value.length + posts.value.length);

// Methods
const loadSearchResults = () => {
	if (route.query.q) {
		const parsedResults = JSON.parse(route.query.q);
		searchQuery.value = route.query.searchTerm || ""; // Update: Added this line
		users.value = parsedResults.users || [];
		posts.value = parsedResults.posts || [];
		isLoading.value = false;
	}
};

const follow = async (userId) => {
	try {
		const response = await axiosClient.post(`/follow/${userId}/follow/`);
		users.value = users.value.map((user) => {
			if (user.user === userId) {
				user.is_followed = response.data.is_followed;
			}
			return user;
		});
	} catch (error) {
		console.error("Error following the user:", error);
	}
};

const likePost = async (postId) => {
	try {
		await axiosClient.post(`/like-posts/${postId}/like_post/`);
		posts.value = posts.value.map((post) => {
			if (post._id === postId) {
				post.is_liked = !post.is_liked;
				post.like_count += post.is_liked ? 1 : -1;
			}
			return post;
		});
	} catch (error) {
		console.error("Error liking the post:", error);
	}
};

const selectPost = (post) => {
	router.push({
		name: "view-post",
		params: { post: post._id },
		query: { n: "" },
	});
};

const timesince = (date) => moment(date).fromNow();

const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
};

const openImageModal = (imageUrl) => {
	modalImage.value = imageUrl;
	showImageModal.value = true;
};

const closeImageModal = () => {
	showImageModal.value = false;
};

// Lifecycle
onMounted(loadSearchResults);

// Watchers
watch(() => route.query.q, loadSearchResults, { immediate: true });
</script>
