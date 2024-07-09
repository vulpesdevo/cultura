<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-20 sm:pt-3"
	>
		<div
			class="relative post-contents w-full p-3  sm:mt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
			v-for="post in posts"
			:key="post._id"
		>
			<div class="post-title flex justify-start items-center">
				<div class="flex w-full items-center justify-between sm:justify-normal">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						{{ post.title }}
					</h1>
					<small class="text-second ml-5">{{
						timesince(post.date_posted)
					}}</small>
				</div>
				<!-- <div class="flex w-1/2 justify-end">
					<button @click="toggleMenu" class="">
						<span class="material-icons-outlined">
							more_horiz
						</span>
					</button>
					<div
						v-if="isMenuOpen"
						class="absolute mt-5 w-48 bg-white border border-gray-200 rounded-md shadow-lg"
					>
						
						<a
							href="#"
							class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
							aria-disabled="true"
							>Edit</a
						>
						<a
							href="#"
							@click.prevent="deleteItem"
							class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
							>Delete</a
						>
					</div>
				</div> -->
			</div>
			<!-- Post Delete Modal Button Includes "isMenuOpen" and "toggleMenu" in script-->

			<!-- Post Delete Modal, Includes "modalDeleteActive" and "deleteItem" in script -->

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
						{{ post.content }} {{ post.is_liked }}
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
			<div
				class="flex items-center justify-end border-b-2 pb-2 border-field"
			>
				<i
					class="fa-regular fa-comment text-second text-2xl pr-2 cursor-pointer"
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
					<small class="text-prime pl-1">
						{{
							post.like_count >= 1000
								? (post.like_count / 1000).toFixed(1) + "k"
								: post.like_count
						}}
					</small>
				</div>
			</div>
			<div
				class="post-contents w-full pt-3 sm:pt-6 mb-7 sm:mb-0"
				v-for="(data, index) in selectedPost"
				:key="index"
			>
				<div class="">
					<div
						class="flex items-start bg-gray-200 mt-2 p-3 rounded-lg"
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
				<div id="comment_reply" class="reply-post flex w-full mt-4">
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
						class="font-montserrat text-xl bg-second text-interface rounded-full w-28 h-9"
						:class="
							reply === ''
								? 'cursor-not-allowed'
								: 'cursor-pointer hover:bg-second-light'
						"
						:disabled="reply === ''"
					/>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import moment from "moment";
export default {
	data() {
		return {
			posts: [],
			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",
			showModal: false,
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
	},
	mounted() {
		// this.fetchComments();
		// setInterval(this.fetchComments, 5000);
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
		timesince(date) {
			return moment(date).fromNow();
		},
		fetchPosts() {
			this.client
				.get(`/api/liked-post-view/${this.$route.params.post_id_notif}/${this.$route.params.notif_id}`)
				.then((response) => {
					this.posts = response.data;
					this.selectedPost = response.data;
					this.post_id = this.selectedPost[0]._id;
                    this.replied_to = this.selectedPost[0].author;
                    this.comments_in_post = this.posts[0].comments
					console.log("updateed :", this.posts);
					console.log(this.replied_to);
					
				})
				.catch((error) => {
					console.log(error);
				});
		},
		// fetchComments() {

		// 	this.client
		// 		.get("/api/comments")
		// 		.then((response) => {
		//             this.comments = response.data;

		// 		})
		// 		.catch((error) => {
		// 			console.log(error);
		// 		});
		// },
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
					this.fetchPosts();

					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
				});
		},
		selectPost() {},
	},
};
</script>

<style scoped></style>
