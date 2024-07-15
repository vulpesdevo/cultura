<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-28 py-5 sm:ml-64 overflow-auto scroll-smooth h-screen pt-20 sm:pt-3 bg-field dark:bg-dark-notif px-2"
	>
		<section class="mb-10 sm:mb-0">
			<div class="flex flex-col">
				<label
					for=""
					class="text-prime dark:text-interface text-lg pb-2"
					>Users:</label
				>
				<div class="grid sm:grid-cols-2 gap-4">
					<div
						class="w-full bg-interface dark:bg-dark-interface flex shadow-lg h-24 justify-between items-center p-5 text-prime dark:text-interface rounded-xl"
					>
						<div
							class="w-20 h-20 mr-2 flex justify-center items-center"
						>
							<img
								src="/sample_img/mark.png"
								alt="Profile"
								class="rounded-full cursor-pointer"
							/>
						</div>
						<div class="font-montserrat text-left w-full">
							<p class="font-bold">Mark francis N. Galan</p>
							<small>Philippines | mark@gmail.com</small>
						</div>
					</div>
					<router-link
						:to="{
							name: 'user-profile',
							params: {
								username: user.username,
								user: JSON.stringify(user),
							},
						}"
						class="w-full bg-interface dark:bg-dark-interface flex shadow-lg h-24 justify-between items-center p-5 text-prime dark:text-interface rounded-xl"
						v-for="user in users"
						:key="user.id"
					>
						<div
							class="w-20 h-20 mr-4 flex justify-center items-center"
						>
							<img
								:src="user.user_photo"
								alt="Profile"
								class="rounded-full cursor-pointer"
							/>
						</div>
						<div class="font-montserrat text-left w-full">
							<p class="font-bold">{{ user.fullname }}</p>
							<small>{{ user.country }} | {{ user.email }}</small>
						</div>

						<button
							v-if="user.is_followed"
							class="bg-dark-second-dark w-36 h-8 rounded-xl"
							@click.prevent="follow(user.user)"
						>
							Followed
						</button>
						<button
							v-if="!user.is_followed"
							class="bg-second w-36 h-8 rounded-xl"
							@click.prevent="follow(user.user)"
						>
							Follow
						</button>
					</router-link>
				</div>
			</div>
			<div class="flex flex-col pt-4">
				<label for="" class="text-prime dark:text-interface text-lg"
					>Posts:</label
				>
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
					<div
						class="post-content flex w-full mt-4 dark:text-dark-prime"
					>
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
							<div class="h-auto pb-2 sm:p-4" v-else>
								<div
									class="cont-itinerary mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface dark:bg-dark-interface cursor-pointer sm:w-11/12 sm:px-6"
									:key="post.itinerary_in_post.id"
									@click="
										goToViewItinerary(
											post.itinerary_in_post.id
										)
									"
								>
									<div
										class="mt-2 sm:px-5 pb-5 sm:pt-5 mb-10 w-full"
									>
										<img
											class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-auto"
											:src="
												post.itinerary_in_post
													.main_image
											"
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
										? (post.like_count / 1000).toFixed(1) +
										  "k"
										: post.like_count
								}}
							</small>
						</div>
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
			post_profile_display: null,
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
			users: [],
			result:null,

			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",

			comments: [],
			comments_in_post: [],

			itineraries: [],
			itineraries_frompost: [],
			selectedItinerary: null,
			id_of_selected: "",
			isFullTextShown: {},
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
		// this.posts = this.$route.params.result;
	},
	beforeRouteEnter(to, from, next) {
		if (!to.params.result) {
			next({ name: "dashboard" });
		} else {
			next();
		}
	},

	mounted() {
		this.result = JSON.parse(this.$route.params.result);
		console.log("valid object", this.result);
		this.posts = this.result.posts;
		this.users = this.result.users;
	},
	methods: {
		follow(userId) {
			this.client
				.post(`api/follow/${userId}/follow/`)
				.then((response) => {
					// Handle success response
					console.log(response.data);
					// Update the is_followed property of the user object
					const userIndex = this.users.findIndex(
						(user) => user.user === userId
					);
					
					this.result.users = this.result.users.map(user => {
						if (user.user === userId) {
							user.is_followed = response.data.is_followed;
						}
						if (userIndex !== -1) {
						this.users[userIndex].is_followed =
							response.data.is_followed;
					}
						return user;
					});
					
					

					// Optionally, update your UI based on the successful follow
				})
				.catch((error) => {
					// Handle error
					console.error("Error following the user:", error);
				});
		},
		goToViewItinerary(itinerarydata) {
			this.$router.push({
				name: "view-itinerary",
				params: { itinerarydata },
			});
		},
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
		fetchPosts() {
			this.client
				.get(`/api/posts-list`)
				.then((response) => {
					this.posts = response.data.reverse();
					if (this.posts.length > 0) {
						// Set selectedPost to the first post
						console.log("GET POST fetch", this.selectedPost);
						// this.post_id = this.selectedPost[0]._id;
						this.itineraries_frompost =
							this.posts[0].itinerary_in_post;
						// this.replied_to = this.selectedPost[0].author;
						this.comments_in_post =
							this.posts.find((p) => p._id === this.post_id)
								?.comments || [];
						console.log("the id : ", this.comments_in_post);
					}

					// this.comments_in_post = this.posts[0].comments;
					console.log("updateed :", this.posts[0]);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		return { isDark, toggleDark };
	},
};
</script>
