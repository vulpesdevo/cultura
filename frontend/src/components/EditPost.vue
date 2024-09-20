<template>
	<div
		class="profile-main flex flex-col items-center align-middle w-full pb-16 sm:pb-10 sm:px-8 py-5 sm:ml-64 overflow-auto overflow-x-hidden h-screen bg-field dark:bg-dark-notif pt-5 sm:pt-7"
	>
		<div
			class="w-screen sm:w-full p-3 mt-16 sm:mt-3 px-6 sm:px-9 sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
		>
			<form @submit.prevent="handleSubmit">
				<div class="post-title flex justify-start items-center">
					<div class="flex w-full items-center">
						<input
							v-model="post.title"
							type="text"
							class="font-bebas-neue text-lg bg-[#12182c41] m-2 p-5 rounded-lg text-prime dark:text-dark-prime sm:text-2xl focus:border-second focus:outline-none w-4/5 sm:w-full"
							placeholder="Enter post title"
						/>
						<!-- <small
							class="text-second flex w-3/4 sm:w-[10%] justify-end relative"
							>{{ timesince(post.date_posted) }}</small
						> -->
					</div>
					<!-- <div class="flex w-[10%] justify-end relative">
						<button type="button" @click="toggleMenu" class="">
							<span
								class="material-icons-outlined dark:text-dark-prime"
							>
								more_horiz
							</span>
						</button>
						<div
							v-if="isMenuOpen"
							class="absolute mt-5 w-48 bg-white border border-gray-200 rounded-md shadow-lg"
						>
							<a
								href="#"
								@click.prevent="handleSubmit"
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								>Save</a
							>
							<a
								href="#"
								@click.prevent="cancelEdit"
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								>Cancel</a
							>
						</div>
					</div> -->
				</div>
				<div class="post-content flex w-full h-auto mt-4">
					<div class="w-14 h-14 mr-4">
						<img
							:src="post.author_user_photo"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full h-full">
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
						<textarea
							v-model="post.content"
							class="font-montserrat w-full mt-3 p-5 rounded-lg resize-none text-sm text-justify bg-[#12182c41] dark:text-dark-prime border-none focus:outline-none"
							placeholder="Enter post content"
						></textarea>

						<div
							class="flex items-center justify-center w-screen h-full sm:w-1/3 bg-field dark:bg-notif hover:bg-gray-300 sm:rounded-2xl cursor-pointer z-10"
						>
							<label
								for="imgSelect"
								class="w-screen sm:w-full h-full flex items-center justify-center bg-field dark:bg-gray-400 cursor-pointer rounded-xl"
							>
								<img
									:class="{ hidden: !selectedImageUrl }"
									:src="selectedImageUrl"
									class="size-full object-cover rounded-xl z-0"
									alt="Selected image"
								/>
								<div
									:class="{ hidden: selectedImageUrl }"
									class="flex items-center justify-center font-montserrat size-36 text-prime dark:text-dark-prime text-xl z-0"
								>
									<span>+ Add Image</span>
								</div>
							</label>
						</div>
						<input
							type="file"
							id="imgSelect"
							class="hidden"
							@change="handleFileSelection"
						/>
					</div>
				</div>
				<div class="flex my-3 items-center justify-end">
					<input
						@click.prevent="updatePost"
						type="submit"
						value="Save"
						class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-10 sm:h-12 hover:bg-second-light cursor-pointer"
					/>
				</div>
			</form>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { useRoute } from "vue-router";
export default {
	name: "EditPost",
	data() {
		return {
			post: {
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
			},
			picture: null,
			isMenuOpen: false,
			selectedImageUrl: null,
		};
	},
	created() {
		const route = useRoute();
		const postParam = route.params.post;
		if (postParam) {
			this.post = JSON.parse(postParam);
		}
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
	},
	methods: {
		handleFileSelection(event) {
			const file = event.target.files[0];
			if (file) {
				this.selectedImageUrl = URL.createObjectURL(file);
				this.picture = file;
				console.log("Image :", this.picture);
			}
		},
		updatePost() {
			if (!this.post.content.trim() || this.post.title === "POST TITLE") {
				alert("Please fill all fields correctly."); // Inform the user (consider using a more user-friendly notification system)
				return; // Exit the method
			} else {
				let formData = new FormData();
				formData.append("title", this.post.title);
				formData.append("body", this.post.content);

				if (this.picture && this.picture instanceof File) {
					formData.append("image", this.picture, this.picture.name);
				}
				this.client
					.put(`/api/posting/${this.post._id}/`, formData, {
						headers: {
							"Content-Type": "multipart/form-data",
						},
					})
					.then((response) => {
						console.log(response.data);
						this.$router.push({ name: "profile" }); // Redirect to the post list or another appropriate page
					})
					.catch((error) => {
						console.log(
							"An error occurred while updating the post."
						);
					});
			}
		},
		timesince(date) {
			return moment(date).fromNow();
		},
		toggleMenu() {
			this.isMenuOpen = !this.isMenuOpen;
		},
		handleImageUpload(event) {
			const file = event.target.files[0];
			if (file) {
				const reader = new FileReader();
				reader.onload = (e) => {
					this.post.image = e.target.result;
				};
				reader.readAsDataURL(file);
			}
		},
		handleSubmit() {
			// Log the params object with the stringified post
			const params = {
				post: JSON.stringify(this.post),
			};
			console.log("Params:", params);

			// Here you would typically send the updated post data to your backend
			console.log("Submitting updated post:", this.post);
			// You can add your API call or state management logic here
		},
		cancelEdit() {
			// Here you would typically reset the form or navigate away
			console.log("Cancelling edit");
		},
	},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat&display=swap");
@import url("https://fonts.googleapis.com/icon?family=Material+Icons+Outlined");

.font-bebas-neue {
	font-family: "Bebas Neue", sans-serif;
}

.font-montserrat {
	font-family: "Montserrat", sans-serif;
}

/* Add these custom color classes to match your theme */
.text-prime {
	@apply text-gray-900;
}

.dark .text-dark-prime {
	@apply text-white;
}

.text-second {
	@apply text-blue-500;
}

.bg-interface {
	@apply bg-white;
}

.dark .bg-dark-interface {
	@apply bg-gray-800;
}
</style>
