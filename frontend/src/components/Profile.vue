<template>
	<div
		class="profile-main flex flex-col items-center align-middle w-full pb-16 sm:pb-10 sm:px-8 py-5 sm:ml-64 overflow-auto h-screen bg-field  dark:bg-dark-notif pt-5 sm:pt-7"
	>
		<div
			class="profile-1 w-screen sm:w-full mt-12 sm:mt-0 px-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface  dark:bg-dark-interface"
			v-show="profile"
		>
			
			<div
				class="profile-img flex flex-col pt-9 items-center align-middle mb-10"
			>
				<img
					class="rounded-full shadow-2xl drop-shadow-xl w-40 sm:w-48 mb-8"
					src="/sample_img/mark.png"
					alt=""
				/>
				<h1
					class="font-bebas-neue profile-name text-5xl sm:text-7xl drop-shadow-lg shadow-black text-prime  dark:text-dark-second"
				>
					{{ profile.fullname }}
				</h1>
			</div>
			<div
				class="profile-details flex justify-center align-middle mb-10 text-prime"
			>
				<div
					class="profile-desc text-xm sm:text-xl flex items-start flex-col me-7 sm:me-32"
				>
					<h1 class="font-montserrat text-prime dark:text-dark-prime mb-2">Username:</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-prime mb-2">Email:</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-prime mb-2">Password:</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-prime mb-2">Country:</h1>
				</div>
				<div class="profile-info text-xm sm:text-xl flex flex-col">
					<h1 class="font-montserrat text-prime dark:text-dark-second mb-2">
						{{ profile.username }}
					</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-second mb-2">
						{{ profile.email }}
					</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-second mb-2">**********</h1>
					<h1 class="font-montserrat text-prime dark:text-dark-second mb-2">
						{{ profile.country }}
					</h1>
				</div>
			</div>
		</div>
		<div class="profile-tabs flex justify-center w-full my-5 px-2">
			<button
				class="font-montserrat text-prime dark:text-dark-second rounded-full h-10 sm:h-12 w-1/2 sm:w-60 text-xl sm:text-3xl"
				@click="activeTab = 'posts'"
				:class="{ 'bg-second dark:text-dark-notif text-white ': activeTab === 'posts' }"
			>
				Posts
			</button>
			<button
				class="font-montserrat text-prime dark:text-dark-second rounded-full h-10 sm:h-12 w-1/2 sm:w-60 text-xl sm:text-3xl ms-5 sm:ms-10"
				@click="activeTab = 'achievements'"
				:class="{
					'bg-second dark:text-dark-notif text-white': activeTab === 'achievements',
				}"
			>
				Achievements
			</button>
		</div>

		<div class="posts-in-profile" v-if="activeTab === 'posts'">
			<div
				class="post-contents w-screen sm:w-full p-3 mt-3 px-6 sm:mt-6 sm:px-9 sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="post-title flex justify-start items-center">
					<div class="flex w-[90%] items-center">
						<h1
							class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-2xl"
						>
							{{ post.title }}
						</h1>
						<small class="text-second ml-5">{{
							timesince(post.date_posted)
						}}</small>
					</div>
					<div class="flex w-[10%] justify-end">
						<button @click="toggleMenu(post._id)" class="">
							<span class="material-icons-outlined dark:text-dark-prime">
								more_horiz
							</span>
						</button>
						<div
							v-if="isMenuOpen === post._id"
							class="absolute mt-5 w-48 bg-white border border-gray-200 rounded-md shadow-lg"
						>
							<!-- @click.prevent="editItem" -->
							<a
								href="#"
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								aria-disabled="true"
								>Edit</a
							>
							<a
								href="#"
								@click.prevent="deleteItem(post._id)"
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								>Delete</a
							>
						</div>
					</div>
				</div>
				<div class="post-content flex w-full mt-4">
					<div class="w-14 h-14 mr-4">
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="rounded-full cursor-pointer object-cover"
						/>
					</div>
					<div class="w-full">
						<div class="flex border-b-2 dark:border-gray-400">
							<small class="font-montserrat text-prime dark:text-dark-prime pr-5">
								@{{ post.author }}
							</small>
							<small class="about-post font-montserrat dark:text-gray-400">
								{{ post.category }} | {{ post.country }}
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify dark:text-dark-prime"
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
		</div>
		<div
			class="achievements w-screen sm:w-full pt-3 px-6 sm:pt-6 sm:px-9"
			v-if="activeTab === 'achievements'"
		></div>

		<div
			class="fixed z-50 inset-0 overflow-y-auto"
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
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
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/2"
				>
					<button
						class="absolute top-0 right-0 m-2 mr-3 text-prime text-2xl"
						@click="showModal = false"
					>
						&times;
					</button>
					<div
						class="post-contents bg-interface w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
						v-for="(data, index) in selectedPost"
						:key="index"
					>
						<div
							class="post-title flex justify-between items-center"
						>
							<h1
								class="font-bebas-neue text-lg text-prime sm:text-2xl"
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
								<div class="flex border-b-2">
									<p class="font-montserrat text-prime pr-5">
										{{ data.author }}
									</p>
									<small class="about-post font-montserrat">
										{{ data.category }} |
										{{ data.country }}
									</small>
								</div>
								<p
									class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
								>
									{{ data.content }}
								</p>
							</div>
						</div>
						<div class="p-2 overflow-auto max-h-60">
							<div
								class="flex items-start bg-gray-200 ml-3 mt-2 sm:ml-10 p-3 rounded-lg"
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
						<div class="reply-post flex w-full mt-4">
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
								class="font-montserrat text-xl bg-second text-interface rounded-full w-28 h-10 hover:bg-second-light cursor-pointer"
							/>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div
			v-if="modalDeleteActive"
			class="fixed flex flex-col z-50 inset-0 overflow-y-auto w-screen bg-black bg-opacity-50 h-screen items-center justify-center"
			role="dialog"
			aria-modal="true"
		>
			<div
				v-if="modalDeleteActive"
				class="flex-col sm:w-1/3 sm:h-[32%] rounded-lg p-4 bg-interface"
			>
				<span
					@click="modalDeleteActive = false"
					class="flex material-icons-outlined justify-end cursor-pointer"
					>close</span
				>
				<h1
					class="flex text-4xl sm:text-3xl text-prime font-bold font-montserrat justify-center"
				>
					Are you sure?
				</h1>
				<p
					class="flex justify-center text-sm sm:text-[15px] my-5 mb-20 sm:my-7 px-3 sm:px-16 font-montserrat text-center"
				>
					You are trying to delete this post. This action cannot be
					undone.
				</p>
				<div class="flex justify-center items-center">
					<button
						class="rounded-xl text-xl text-white mr-4 bg-notif bg-opacity-80 py-2 px-7 font-bebas-neue"
					>
						Cancel
					</button>
					<button
						class="rounded-xl text-xl text-white bg-red-900 py-2 px-7 font-bebas-neue"
						@click="deletePost"
					>
						Delete
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import moment from "moment";
export default {
	data() {
		return {
			showModal: false,
			profile: {
				username: "",
				fullname: "",
				email: "",
				password: "",
				country: "",
			},
			showModal: false,
			posts: [],

			activeTab: "posts", // Default active tab

			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",

			comments: [],
			comments_in_post: [],

			modalDeleteActive: false,
			isMenuOpen: false,
			openedPost_id: null,
		};
	},
	mounted() {
		// this.fetchPosts();
		// setInterval(this.fetchPosts, 5000); // Fetch posts every 5 seconds -->> polling
		// this.fetchComments();
		setInterval(this.fetchComments, 5000);
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

		this.client
			.get("api/user")
			.then((res) => {
				this.profile.username = res.data.user.username;
				this.profile.fullname = res.data.profile.fullname;
				this.profile.country = res.data.profile.country;

				this.profile.email = res.data.profile.email;
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
		this.fetchPosts();
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
		toggleMenu(postId) {
			this.isMenuOpen = this.isMenuOpen === postId ? null : postId;
			this.openedPost_id = postId
		},

		editItem() {
			alert("Edit action triggered");
			this.isMenuOpen = false;
		},
		deleteItem() {
			this.modalDeleteActive = !this.modalDeleteActive;
			this.isMenuOpen = null;
			console.log('the opened : ',this.openedPost_id)
		},
		deletePost() {
			
			this.client
				.post("/api/delete-post", {
					post_id: this.openedPost_id
				})
				.then((response) => {
					console.log(response.data);
					
					this.fetchPosts();
					this.modalDeleteActive = false
					// setInterval(this.fetchComments, 5000);
					
					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
				});
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
					this.showModal = false;
					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
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
		fetchComments() {
			axios
				.get("/api/comments")
				.then((response) => {
					this.comments = response.data;
					console.log("comments:", this.comments);
				})
				.catch((error) => {
					console.log(error);
				});
		},
		fetchPosts() {
			this.client
				.get(`/api/posts-list`)
				.then((response) => {
					this.posts = response.data.reverse();
					// this.comments_in_post = this.posts[0].comments;
					console.log("updateed :", this.posts);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

<style scoped></style>
