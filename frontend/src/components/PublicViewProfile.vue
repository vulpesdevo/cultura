<template>
	<div
		class="flex flex-col items-center align-middle w-full sm:px-28 py-5 sm:ml-64 overflow-auto scroll-smooth h-screen pt-20 sm:pt-3 bg-field dark:bg-dark-notif px-2"
	>
		<div
			class="profile-1 w-screen sm:w-full mt-12 sm:mt-0 px-3 sm:pt-6 sm:px-9 rounded-sm sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
			v-show="user"
		>
			<div
				class="profile-img flex flex-col pt-9 items-center align-middle mb-2 sm:mb-5"
			>
				<div
					class="flex items-center justify-center bg-prime dark:bg-second relative rounded-full w-40 h-40 sm:w-52 sm:h-52 sm:mb-8 mb-4 p-[.2rem] group"
				>
					<img
						class="rounded-full shadow-2xl w-[9.5rem] h-[9.5rem] sm:w-full sm:h-full object-cover border-interface dark:border-dark-interface border-8"
						:src="user.user_photo"
						alt=""
					/>
				</div>

				<div
					v-if="!user.fullname"
					class="animate-pulse bg-gray-400 bg-opacity-40 h-[2.5rem] sm:h-[4.5rem] w-1/2 rounded-lg"
				></div>
				<h1
					class="font-bebas-neue profile-name text-4xl sm:text-7xl text-prime dark:text-dark-second"
				>
					{{ user.fullname }}
				</h1>
			</div>
			<div
				class="profile-details flex justify-center w-full align-middle mb-4 sm:mb-10 text-prime"
			>
				<div
					class="profile-desc text-xm sm:text-xl flex items-end flex-col justify-between sm:mr-3 w-1/2"
				>
					<small
						class="font-montserrat text-prime dark:text-dark-prime mb-2"
					>
						Username:
					</small>
					<small
						class="font-montserrat text-prime dark:text-dark-prime mb-2"
					>
						Email:
					</small>

					<small
						class="font-montserrat text-prime dark:text-dark-prime mb-2"
					>
						Country:
					</small>
				</div>

				<div
					class="profile-info text-xm sm:text-xl ml-3 flex flex-col justify-between w-1/2"
				>
					<div
						v-if="!user.username"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>
					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2 h-4"
					>
						{{ user.username }}
					</small>
					<div
						v-if="!user.email"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>
					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2 h-4"
					>
						{{ user.email }}
					</small>
					<div
						v-if="!user.country"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>

					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2"
					>
						{{ user.country }}
					</small>
				</div>
			</div>
		</div>
		<div class="profile-tabs flex justify-center w-full my-5 px-2">
			<button
				class="font-montserrat text-prime rounded-full h-10 sm:h-12 w-1/2 sm:w-64 text-xl sm:text-2xl"
				@click="activeTab = 'posts'"
				:class="{
					'bg-second text-white': activeTab === 'posts',
					'bg-none text-second': activeTab !== 'posts',
				}"
			>
				Posts
			</button>
			<button
				class="font-montserrat text-prime rounded-full h-10 sm:h-12 w-1/2 sm:w-64 text-xl sm:text-2xl ms-5 sm:ms-10"
				@click="activeTab = 'achievements'"
				:class="{
					'bg-second text-white': activeTab === 'achievements',
					'bg-none text-second': activeTab !== 'achievements',
				}"
			>
				Achievements
			</button>
		</div>

		<div class="posts-in-profile w-full" v-if="activeTab === 'posts'">
			<div
				v-if="!posts.length"
				class="border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
			>
				<div class="animate-pulse flex space-x-4">
					<div
						class="rounded-full bg-gray-500 dark:bg-slate-700 h-10 w-10"
					></div>
					<div class="flex-1 space-y-6 py-1">
						<div
							class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
						></div>
						<div class="space-y-3">
							<div class="grid grid-cols-3 gap-4">
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-2"
								></div>
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-1"
								></div>
							</div>
							<div
								class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
							></div>
						</div>
					</div>
				</div>
			</div>
			<div
				v-if="!posts.length"
				class="border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto"
			>
				<div class="animate-pulse flex space-x-4">
					<div
						class="rounded-full bg-gray-500 dark:bg-slate-700 h-10 w-10"
					></div>
					<div class="flex-1 space-y-6 py-1">
						<div
							class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
						></div>
						<div class="space-y-3">
							<div class="grid grid-cols-3 gap-4">
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-2"
								></div>
								<div
									class="h-2 bg-gray-500 dark:bg-slate-700 rounded col-span-1"
								></div>
							</div>
							<div
								class="h-2 bg-gray-500 dark:bg-slate-700 rounded"
							></div>
						</div>
					</div>
				</div>
			</div>
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
				</div>
				<div class="post-content flex w-full mt-4">
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
			class="flex justify-center items-center achievements w-full pt-3 px-3 sm:pt-6 sm:px-9"
			v-if="activeTab === 'achievements'"
		>
			<div class="flex justify-center items-center w-screen sm:w-full">
				<div class="grid grid-cols-5 gap-1 sm:gap-0 sm:w-3/4">
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img src="/achievements/welcome-wanderer.png" alt="" />
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/content-creator.png`"
							:class="{
								'brightness-[10%]': user.content_creator < 5,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/guide-guru.png`"
							:class="{ 'brightness-[10%]': user.guide_guru < 1 }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/like-leader.png`"
							:class="{ 'brightness-[10%]': user.like_leader < 10 }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/share-star.png`"
							:class="{ 'brightness-[10%]': user.share_star < 10 }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/comment-connoisseur.png`"
							:class="{
								'brightness-[10%]': user.comment_connoisseur < 5,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/explorer-extraordinaire.png`"
							:class="{
								'brightness-[10%]':
									user.explorer_extraordinaire < 10,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/knowledge-seeker.png`"
							:class="{
								'brightness-[10%]': user.knowledge_seeker < 15,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/trend-setter.png`"
							:class="{ 'brightness-[10%]': user.trend_setter < 50 }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/cultura-contributor.png`"
							:class="{
								'brightness-[10%]':
									user.content_creator < 20 ||
									user.guide_guru < 10,
							}"
							alt=""
						/>
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
						v-for="(data, index) in selectedPost"
						:key="index"
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
									:src="data.author_user_photo"
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
									:src="data.author_user_photo"
									alt="Profile"
									class="rounded-full cursor-pointer"
								/>
							</div>
							<textarea
								class="w-full rounded-lg resize-none p-4 outline-none dark:border dark:bg-dark-interface dark:text-interface"
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
			hasContentCreator: false,
			hasGuideGuru: false,
			hasLikeLeader: false,
			hasShareStar: false,
			hasCommentConnoisseur: false,
			hasExplorerExtraordinaire: false,
			hasKnowledgeSeeker: false,
			hasTrendsetter: false,
			hasCulturaContributor: false,

			profile: false,
			activeTab: "posts",
			showModal: false,

			comments_in_post: [],
			reply: "",
			post_profile_display: null,
			selectedImageUrl: null,
			picture: null,

			auth_user: "",

			isEditing: true,
			postTitle: "",

			addItineraryModal: false,

			categoryOption: "",
			postContent: "",
			countryPost: "",

			posts: [],
			user: [],
			user_id: 0,
			selectedPost: [],
			reply: "",
			replied_to: "",
			post_id: "",

			comments: [],

			itineraries: [],
			itineraries_frompost: [],
			selectedItinerary: null,
			id_of_selected: "",
			isFullTextShown: {},
		};
	},
	mounted() {
		const user = JSON.parse(this.$route.params.user);
		// const posts = JSON.parse(this.$route.params.posts);
		// console.log("valid object", posts);
		// this.posts = posts;
		this.user = user;

		this.user_id = this.user.user;
		this.fetchPosts(this.user_id);
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		return { isDark, toggleDark };
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
		// this.fetchPosts();
	},
	methods: {
		timesince(date) {
			return moment(date).fromNow();
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
					this.fetchPosts(this.user_id);

					// setInterval(this.fetchComments, 5000);

					// Handle successful response here
				})
				.catch((error) => {
					console.error(error);
					// Handle error here
				});
		},
		fetchPosts(uses_id) {
			console.log("this.user_id : ", uses_id);
			this.client
				.get(`/api/public-profile-posts/`, {
					params: {
						user_id: uses_id,
					},
				})
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
					console.log("updateed :", this.posts);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>
