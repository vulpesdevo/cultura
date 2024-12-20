<template>
	<div
		class="bg-gray-200 dark:bg-notif h-screen overflow-auto pt-5 pb-5 px-4 sm:px-6 lg:px-28"
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
			<div class="bg-white dark:bg-dark-field rounded-lg shadow-lg">
				<form @submit.prevent="handleSubmit" class="space-y-6 p-6">
					<!-- Post Header -->
					<div class="flex items-center space-x-3">
						<img
							:src="post.cultura_user.user_photo"
							alt="Profile"
							class="w-10 h-10 rounded-full object-cover"
						/>
						<div>
							<input
								v-model="post.title"
								type="text"
								class="font-semibold text-gray-900 dark:text-white bg-transparent border-b border-gray-300 dark:border-gray-700 focus:border-blue-500 dark:focus:border-blue-400 focus:outline-none w-full"
								placeholder="Enter post title"
							/>
							<div
								class="flex items-center text-sm text-gray-500 dark:text-gray-400"
							>
								<span>@{{ post.author }}</span>
								<span class="mx-1">•</span>
								<span>{{ timesince(post.date_posted) }}</span>
							</div>
						</div>
					</div>

					<!-- Post Content -->
					<div>
						<textarea
							v-model="post.content"
							rows="4"
							class="w-full ring-1 ring-blue-700 border-0 dark:bg-dark-field rounded-lg p-4 text-gray-800 dark:text-gray-200 resize-none focus:ring-1 focus:ring-blue-500 transition-all duration-200"
							placeholder="What's on your mind?"
						></textarea>
					</div>

					<!-- Image Upload -->
					<div v-if="post.image" class="relative">
						<div
							class="relative rounded-lg overflow-hidden cursor-pointer"
							:class="{ 'h-64': selectedImageUrl || post.image }"
							@click="triggerFileInput"
						>
							<img
								v-if="selectedImageUrl || post.image"
								:src="selectedImageUrl || post.image"
								alt="Post image"
								class="w-full h-full object-cover"
							/>
							<div
								v-else
								class="h-48 bg-gray-200 dark:bg-gray-700 rounded-lg border-2 border-dashed border-gray-400 dark:border-gray-600 flex items-center justify-center hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200"
							>
								<div class="text-center">
									<PhotoIcon
										class="h-12 w-12 text-gray-400 dark:text-gray-500 mb-2"
									/>
									<p class="text-gray-500 dark:text-gray-400">
										Click to add or change image
									</p>
								</div>
							</div>
						</div>
						<input
							ref="fileInput"
							type="file"
							class="hidden"
							accept="image/*"
							@change="handleFileSelection"
						/>
					</div>
					<!-- Itinerary Preview -->
					<div
						v-if="
							post.itinerary_in_post &&
							post.itinerary_in_post.length > 0
						"
					>
						<h3
							class="text-lg font-semibold mb-2 text-gray-900 dark:text-white"
						>
							Attached Itinerary
						</h3>
						<div
							v-for="itinerary in post.itinerary_in_post"
							:key="itinerary.id"
							class="mt-4 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700 transition-all duration-200"
						>
							<img
								v-if="itinerary.main_image"
								:src="itinerary.main_image"
								alt=""
								class="w-full h-48 object-cover"
							/>
							<div class="p-4 bg-gray-50 dark:bg-gray-700">
								<h4
									class="text-sm sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
								>
									{{ itinerary.main_title }}
								</h4>
								<p
									class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
								>
									{{ itinerary.main_description }}
								</p>
							</div>
						</div>
					</div>

					<!-- Action Buttons -->
					<div class="flex justify-end space-x-4 pt-4">
						<button
							type="button"
							@click="cancelEdit"
							class="px-6 py-2 rounded-full bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200"
						>
							Cancel
						</button>
						<button
							type="submit"
							:disabled="isSubmitting"
							class="px-6 py-2 rounded-full bg-blue-500 text-white hover:bg-blue-600 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
						>
							<span v-if="isSubmitting" class="animate-spin">
								<ArrowPathIcon class="h-5 w-5" />
							</span>
							<span>{{
								isSubmitting ? "Saving..." : "Save Changes"
							}}</span>
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axiosClient from "../axios";
import moment from "moment";
import {
	ArrowLeftIcon,
	PhotoIcon,
	CameraIcon,
	XMarkIcon,
	ArrowPathIcon,
} from "@heroicons/vue/24/solid";

const route = useRoute();
const router = useRouter();
const fileInput = ref(null);
const selectedImageUrl = ref(null);
const isSubmitting = ref(false);
const isLoading = ref(true);
const posts = ref([]);

const post = reactive({
	_id: "",
	title: "",
	author: "",
	cultura_user: { user_photo: "" },
	category: "",
	country: "",
	content: "",
	image: null,
	date_posted: new Date(),
});

onMounted(async () => {
	isLoading.value = true;
	try {
		await fetchPost();
		if (posts.value.length > 0) {
			Object.assign(post, posts.value[0]);
		}
	} catch (error) {
		console.error("Error fetching post:", error);
	} finally {
		isLoading.value = false;
	}
});

const triggerFileInput = () => {
	fileInput.value.click();
};

const handleFileSelection = (event) => {
	const file = event.target.files[0];
	if (file) {
		if (file.size > 5 * 1024 * 1024) {
			alert("Image size should be less than 5MB");
			return;
		}
		selectedImageUrl.value = URL.createObjectURL(file);
		post.image = file;
	}
};

const removeImage = () => {
	selectedImageUrl.value = null;
	post.image = null;
	if (fileInput.value) {
		fileInput.value.value = "";
	}
};

const fetchPost = async () => {
	try {
		const response = await axiosClient.get(
			`/liked-post-view/${route.params.post_id}/`
		);
		posts.value = response.data;
	} catch (error) {
		console.error("Error fetching post:", error);
	}
};

const handleSubmit = async () => {
	isSubmitting.value = true;

	try {
		const formData = new FormData();
		formData.append("title", post.title);
		formData.append("body", post.content);

		if (post.image instanceof File) {
			formData.append("image", post.image);
		}

		const response = await axiosClient.put(
			`/posting/${route.params.post_id}/`,
			formData,
			{
				headers: {
					"Content-Type": "multipart/form-data",
				},
			}
		);

		router.push({ name: "profile" });
	} catch (error) {
		console.error("Error updating post:", error);
		alert("Failed to update post. Please try again.");
	} finally {
		isSubmitting.value = false;
	}
};

const cancelEdit = () => {
	router.push({ name: "profile" });
};

const goBack = () => {
	router.go(-1);
};

const timesince = (date) => {
	return moment(date).fromNow();
};
</script>

<style scoped>
/* Add any additional styles here */
</style>
