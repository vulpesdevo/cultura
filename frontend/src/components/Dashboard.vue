<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-20 sm:pt-3"
	>
		<div
			class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
		>
			<div class="flex justify-between items-center">
				<h1 class="font-bebas-neue text-lg text-prime sm:text-3xl">
					POST TITLE
				</h1>
				<div
					class="drop-down-categ w-1/2 flex items-center justify-end font-montserrat"
				>
					<select
						name=""
						id="category-option"
						v-model="categoryOption"
						class="sm:w-1/2 rounded-full bg-field outline-none p-1"
					>
						<option value="" disabled selected>Category</option>
						<option value="Food">Food</option>
						<option value="Traditions">Traditions</option>
						<option value="History">History</option>
					</select>
				</div>
			</div>
			<div class="for-content flex w-full mt-4">
				<div class="hidden sm:flex w-14 h-14 mr-4">
					<img
						src="/sample_img/mark.png"
						alt="Profile"
						class="rounded-full cursor-pointer"
					/>
				</div>
				<textarea
					class="w-full rounded-lg resize-none p-4 outline-none"
					name=""
					id="post-content"
					v-model="postContent"
					cols="30"
					rows=""
					placeholder="What do you want to share?"
				></textarea>
			</div>
			<div
				class="about-country font-montserrat flex my-3 items-center justify-between border-b-2 p-1"
			>
				<p class="hidden sm:flex text-prime">
					What coutry is your post about?
				</p>
				<p class="flex sm:hidden text-prime">Country</p>
				<input
					id="country-post"
					v-model="countryPost"
					type="text"
					class="bg-field rounded-full pl-3 h-9 w-1/2 outline-none"
					placeholder=""
				/>

				<div class="hidden sm:flex sm:w-1/5"></div>
			</div>
			<div class="flex my-3 items-center justify-between">
				<div class="flex">
					<label for="imgSelect">
						<span
							class="material-icons-outlined text-second text-3xl"
							>image</span
						>
					</label>
					<input type="file" name="" id="imgSelect" class="hidden" />
					<span
						class="material-icons-outlined text-second text-3xl pl-2"
						>explore</span
					>
				</div>
				<input
					@click.prevent="submitPost"
					type="submit"
					value="Post"
					class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-12 hover:bg-second-light cursor-pointer"
				/>
			</div>
		</div>
		<section class="posts mb-10">
			<div
				class="post-contents w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
			>
				<div class="post-title flex justify-between items-center">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						BEST PULLED NOODLES IN BINONDO
					</h1>
					<small class="text-second">10mins ago</small>
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
							<small class="font-montserrat text-prime pr-5">
								@mark0
							</small>
							<small class="about-post font-montserrat">
								Food | Philippines
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
						>
							Slurp-worthy satisfaction awaits at Lan-Zhou Lamien,
							where every strand of their hand-pulled noodles
							tells a tale of culinary mastery. Taste the
							tradition, savor the excellence, and discover why
							they're Manila's noodle maestros.
						</p>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2"
						@click.prevent="showModal = true"
					></i>
					<span class="material-icons-outlined text-second text-2xl"
						>favorite_border</span
					>
				</div>
			</div>
			<div
				class="post-contents w-full pt-3 mt-3 px-6 sm:mt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="post-title flex justify-between items-center">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						BEST PULLED NOODLES IN BINONDO
					</h1>

					<small class="text-second">{{
						timesince(post.date_posted)
					}}</small>
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
							<small class="font-montserrat text-prime pr-5">
								@{{ post.author }}
							</small>
							<small class="about-post font-montserrat">
								{{ post.title }} | {{ post.country }}
							</small>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
						>
							{{ post.content }}
						</p>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2"
						@click.prevent="selectPost(post)"
					></i>
					<span class="material-icons-outlined text-second text-2xl"
						>favorite_border</span
					>
				</div>
			</div>
			<div
				class="fixed z-10 inset-0 overflow-y-auto"
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
									BEST PULLED NOODLES IN BINONDO
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
										<p
											class="font-montserrat text-prime pr-5"
										>
											{{ data.author }}
										</p>
										<small
											class="about-post font-montserrat"
										>
											{{ data.title }} |
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
		</section>
	</div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import moment from "moment";
export default {
	data() {
		return {
			auth_user: "",

			showModal: false,
			categoryOption: "",
			postContent: "",
			countryPost: "",
			posts: [],

			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",

			comments: [],
			comments_in_post: [],
		};
	},
	mounted() {
		this.fetchPosts();
		setInterval(this.fetchPosts, 5000); // Fetch posts every 5 seconds
		this.fetchComments();
		setInterval(this.fetchComments, 5000);
	},
	methods: {
		timesince(date) {
			return moment(date).fromNow();
		},
		selectPost(post) {
			this.showModal = true;

			this.selectedPost = [post];
			this.post_id = this.selectedPost[0]._id;
			this.replied_to = this.selectedPost[0].author;
			this.comments_in_post = this.comments.filter(
				(comment) => comment.post_id === this.post_id
			);
		},

		submitReply() {
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			const client = axios.create({
				baseURL: "http://127.0.0.1:8000",
				withCredentials: true,
				timeout: 5000,
				xsrfCookieName: "csrftoken",
				xsrfHeaderName: "X-Csrftoken",
				headers: headers,
			});
			client
				.post("/api/commenting", {
					post_id: this.post_id,
					replied_to: this.replied_to,
					body: this.reply,
				})
				.then((response) => {
					console.log(response.data);
					this.reply = "";
					this.fetchComments();
					setInterval(this.fetchComments, 5000);
					this.showModal = false;
					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
				});
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
			axios
				.get("/api/posts")
				.then((response) => {
					this.posts = response.data.reverse();
					console.log("posts:", this.posts);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
	setup() {
		const categoryOption = ref("");
		const postContent = ref("");
		const countryPost = ref("");

		//Reply

		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: headers,
		});

		const submitPost = () => {
			client
				.post("/api/posting", {
					title: categoryOption.value,
					body: postContent.value,
					country: countryPost.value,
				})
				.then((response) => {
					console.log(response.data);
					categoryOption.value = "";
					postContent.value = "";
					countryPost.value = "";
				})
				.catch((error) => {});
		};

		return {
			categoryOption,
			postContent,
			countryPost,
			submitPost,

			//reply-post
			// replyContent,
			// submitreply,
		};
	},
};
</script>
<style scoped></style>
