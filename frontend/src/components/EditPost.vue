<template>
	<div class="h-screen bg-gray-900 text-white px-4 overflow-auto">
		<div class="max-w-5xl mx-auto">
			<!-- Header -->
			<h1 class="text-3xl font-bold mb-8 pt-4">Edit Post</h1>

			<div class="bg-gray-800 rounded-xl p-6 shadow-xl">
				<form @submit.prevent="handleSubmit" class="space-y-6">
					<!-- Author Info -->
					<div class="flex items-center space-x-4">
						<img
							:src="post.author_user_photo"
							alt="Profile"
							class="w-12 h-12 rounded-full object-cover ring-2 ring-blue-500"
						/>
						<div>
							<div class="flex items-center space-x-2">
								<span class="font-medium"
									>@{{ post.author }}</span
								>
								<span class="text-gray-400">•</span>
								<span class="text-gray-400"
									>{{ post.category }} |
									{{ post.country }}</span
								>
							</div>
						</div>
					</div>

					<!-- Title Input -->
					<div>
						<input
							v-model="post.title"
							type="text"
							class="w-full bg-gray-700 border-0 rounded-lg p-4 text-xl font-semibold focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							placeholder="Enter post title"
							:class="{
								'border-red-500': validationErrors.title,
							}"
						/>
						<p
							v-if="validationErrors.title"
							class="mt-1 text-red-500 text-sm"
						>
							{{ validationErrors.title }}
						</p>
					</div>

					<!-- Content Input -->
					<div>
						<textarea
							v-model="post.content"
							rows="4"
							class="w-full bg-gray-700 border-0 rounded-lg p-4 resize-none focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							placeholder="What's on your mind?"
							:class="{
								'border-red-500': validationErrors.content,
							}"
						></textarea>
						<p
							v-if="validationErrors.content"
							class="mt-1 text-red-500 text-sm"
						>
							{{ validationErrors.content }}
						</p>
					</div>

					<!-- Image Upload -->
					<div class="relative">
						<div
							class="relative rounded-lg overflow-hidden"
							:class="{ 'h-64': selectedImageUrl || post.image }"
						>
							<img
								v-if="selectedImageUrl || post.image"
								:src="selectedImageUrl || post.image"
								alt="Post image"
								class="w-full h-full object-cover"
							/>
							<div
								v-else
								class="h-48 bg-gray-700 rounded-lg border-2 border-dashed border-gray-600 flex items-center justify-center cursor-pointer hover:bg-gray-600 transition-colors duration-200"
								@click="triggerFileInput"
							>
								<div class="text-center">
									<i
										class="fas fa-image text-3xl mb-2 text-gray-400"
									></i>
									<p class="text-gray-400">
										Click to add an image
									</p>
								</div>
							</div>

							<!-- Image Controls -->
							<div
								v-if="selectedImageUrl || post.image"
								class="absolute top-2 right-2 flex space-x-2"
							>
								<button
									type="button"
									@click="triggerFileInput"
									class="p-2 bg-gray-900 bg-opacity-75 rounded-full hover:bg-opacity-100 transition-all duration-200"
									title="Change image"
								>
									<i class="fas fa-camera text-white"></i>
								</button>
								<button
									type="button"
									@click="removeImage"
									class="p-2 bg-gray-900 bg-opacity-75 rounded-full hover:bg-opacity-100 transition-all duration-200"
									title="Remove image"
								>
									<i class="fas fa-times text-white"></i>
								</button>
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

					<!-- Action Buttons -->
					<div class="flex justify-end space-x-4 pt-4">
						<button
							type="button"
							@click="cancelEdit"
							class="px-6 py-2 rounded-full bg-gray-700 hover:bg-gray-600 transition-colors duration-200"
						>
							Cancel
						</button>
						<button
							type="submit"
							:disabled="isSubmitting"
							class="px-6 py-2 rounded-full bg-blue-500 hover:bg-blue-600 transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
						>
							<span v-if="isSubmitting" class="animate-spin">
								<i class="fas fa-spinner"></i>
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
import axios from "axios";
import axiosClient from "../axios";

const route = useRoute();
const router = useRouter();
const fileInput = ref(null);
const selectedImageUrl = ref(null);
const isSubmitting = ref(false);

const validationErrors = reactive({
	title: "",
	content: "",
});

const post = reactive({
	_id: "",
	title: "",
	author: "",
	author_user_photo: "",
	category: "",
	country: "",
	content: "",
	image: null,
	date_posted: new Date(),
	is_liked: false,
	like_count: 0,
});

// Initialize axios client
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
	const postParam = route.params.post;
	if (postParam) {
		const parsedPost = JSON.parse(postParam);
		Object.assign(post, parsedPost);
	}
});

const validateForm = () => {
	let isValid = true;
	validationErrors.title = "";
	validationErrors.content = "";

	if (!post.title.trim()) {
		validationErrors.title = "Title is required";
		isValid = false;
	}

	if (!post.content.trim()) {
		validationErrors.content = "Content is required";
		isValid = false;
	}

	return isValid;
};

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

const handleSubmit = async () => {
	if (!validateForm()) {
		return;
	}

	isSubmitting.value = true;

	try {
		const formData = new FormData();
		formData.append("title", post.title);
		formData.append("body", post.content);

		if (post.image instanceof File) {
			formData.append("image", post.image);
		}

		await client.put(`/api/posting/${post._id}/`, formData, {
			headers: {
				"Content-Type": "multipart/form-data",
			},
		});

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
</script>

<style scoped>
/* Ensure smooth transitions */
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
	opacity: 0;
}
</style>
