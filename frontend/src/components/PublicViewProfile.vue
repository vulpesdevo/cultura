<template lang="">
	<div
		class="flex flex-col items-center align-middle w-full sm:px-24 py-5 overflow-auto overflow-x-hidden scroll-smooth h-screen sm:pt-7 pt-5 bg-field dark:bg-dark-notif px-2"
	>
		<div
			class="relative profile-card flex sm:flex-row flex-col justify-center sm:justify-normal w-screen sm:w-full sm:mt-0 px-3 sm:px-9 rounded-sm sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
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
			</div>
			<div class="flex flex-col justify-center items-center sm:pl-6">
				<!-- Name Section -->
				<div class="mb-4">
					<div
						v-if="!user.fullname"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-[2.5rem] sm:h-[4.5rem] w-48 rounded-lg"
					></div>
					<h1
						class="font-bebas-neue profile-name text-3xl sm:text-6xl text-prime dark:text-dark-second text-nowrap"
					>
						{{ user.fullname }}
					</h1>
				</div>

				<!-- User Details Grid -->
				<div
					class="profile-details flex justify-center w-full align-middle mb-4 text-prime space-x-1"
				>
					<div
						class="profile-desc text-xm sm:text-base flex items-end justify-center sm:items-start flex-col sm:justify-between w-full sm:w-1/3"
					>
						<small
							v-for="(label, index) in labels"
							:key="index"
							class="font-montserrat text-prime dark:text-gray-400"
						>
							{{ label }}:
						</small>
					</div>

					<div
						class="profile-info text-xm sm:text-base flex items-start justify-center sm:items-start flex-col sm:justify-between w-full sm:w-1/2"
					>
						<div v-for="(field, index) in fields" :key="index">
							<div
								v-if="!user || !user[field]"
								class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
							></div>
							<small
								v-else
								class="font-montserrat text-prime dark:text-dark-second h-4"
							>
								{{ user[field] || "N/A" }}
							</small>
						</div>
					</div>
				</div>
			</div>
			<div
				class="sm:absolute sm:bottom-0 sm:-left-10 flex w-full items-center justify-center sm:justify-end sm:items-end mb-5 space-x-2 sm:space-x-4"
			>
				<!-- Enhanced Followers Count -->
				<div
					class="flex justify-center items-center sm:justify-end w-full h-8 text-sm sm:text-base space-x-2"
				>
					<div
						class="flex items-center justify-center space-x-1 px-3 py-1 bg-gray-100 dark:bg-gray-800 rounded-full transition-all duration-200"
					>
						<UserIcon class="w-4 h-4 text-second" />
						<span
							class="font-medium text-prime dark:text-interface"
						>
							{{ user.follow_count }}
						</span>
						<span class="text-gray-600 dark:text-gray-400"
							>Followers</span
						>
					</div>
					<!-- Enhanced Follow/Unfollow Button -->
					<button
						v-if="user.is_followed"
						@click.prevent="follow(user.user.id)"
						class="flex items-center justify-center w-32 h-7 py-4 rounded-full border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 text-sm font-medium transition-all duration-200 hover:bg-gray-100 dark:hover:bg-gray-800 hover:border-gray-400 dark:hover:border-gray-500 focus:outline-none focus:ring-2 focus:ring-gray-400 dark:focus:ring-gray-500"
					>
						<UserMinusIcon class="w-4 h-4" />
						Unfollow
					</button>

					<button
						v-else
						@click.prevent="follow(user.user.id)"
						class="flex items-center justify-center w-32 h-7 py-4 rounded-full bg-second text-white text-sm font-medium transition-all duration-200 hover:bg-opacity-90 transform hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-second focus:ring-offset-2 dark:focus:ring-offset-gray-800"
					>
						<UserPlusIcon class="w-4 h-4 mr-1" />
						Follow
					</button>
				</div>
			</div>
		</div>
		<div class="profile-tabs w-full my-5 px-4 sm:px-6 md:px-8">
			<div class="max-w-3xl mx-auto">
				<nav
					class="flex flex-wrap justify-center space-x-2 sm:space-x-4"
					aria-label="Profile tabs"
				>
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="setActiveTab(tab.id)"
						:class="[
							'px-4 py-2 text-sm sm:text-base font-medium rounded-full transition-all duration-200  ',
							activeTab === tab.id
								? 'bg-second text-white shadow-lg'
								: 'bg-gray-700 text-gray-300 hover:bg-gray-600 hover:text-white',
						]"
						:aria-current="
							activeTab === tab.id ? 'page' : undefined
						"
					>
						<span class="flex items-center space-x-2">
							<component
								:is="tab.icon"
								class="w-4 h-4 sm:w-5 sm:h-5"
							/>
							<span>{{ tab.name }}</span>
						</span>
					</button>
				</nav>
			</div>
		</div>

		<div class="posts-in-profile w-full mb-10" v-if="activeTab === 'posts'">
			<div
				v-if="!posts.length && checkedAfterDelay"
				class="flex items-center justify-center text-3xl text-gray-500 font-bold text-center h-48"
			>
				No Post Yet
			</div>
			<div v-if="!posts.length && !checkedAfterDelay">
				<div
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
			</div>
			<div
				v-if="!user.is_private || user.is_followed"
				class="relative post-contents w-full p-6 mt-4 rounded-xl shadow-lg bg-white dark:bg-dark-field transition-all duration-200 hover:shadow-xl font-montserrat"
				v-for="post in posts"
				:key="post._id"
			>
				<div class="flex items-start justify-between mb-4">
					<div class="flex items-center space-x-3">
						<div
							class="w-12 h-12 rounded-full overflow-hidden ring-2 ring-gray-100 dark:ring-gray-700"
						>
							<img
								:src="post.author_user_photo"
								alt="Profile"
								class="w-full h-full object-cover"
							/>
						</div>
						<div class="flex flex-col space-y-1">
							<div class="flex items-center space-x-2">
								<span
									class="font-medium text-xs text-gray-900 dark:text-white"
									>@{{ post.author }}</span
								>
								<span
									class="text-xs text-gray-500 dark:text-gray-400"
									>•</span
								>
								<span
									class="text-xs text-gray-500 dark:text-gray-400"
									>{{ timesince(post.date_posted) }}</span
								>
							</div>
							<div
								class="text-xs text-gray-500 dark:text-gray-400"
							>
								{{ post.category }} | {{ post.country }}
							</div>
						</div>
					</div>
				</div>

				<!-- Title Section -->
				<h1
					class="text-xl font-medium font-bebas-neue text-gray-900 dark:text-second mb-3"
				>
					{{ post.title }}
				</h1>

				<!-- Content Section -->
				<div class="space-y-4">
					<p
						class="text-xs text-gray-600 dark:text-gray-300 leading-relaxed"
					>
						{{ post.content }}
					</p>

					<!-- Image Section -->
					<div
						class="flex sm:flex-row flex-col sm:space-x-2 space-y-2 sm:space-y-0 items-start"
					>
						<div
							v-if="!post.isEditing && post.image"
							class="relative w-1/2 rounded-xl overflow-hidden cursor-pointer"
							:class="{
								'w-full': !post.itinerary_in_post,
							}"
							@click="openImageModal(post.image)"
						>
							<img
								:src="post.image"
								alt=""
								class="w-full max-h-[15rem] object-cover"
							/>
							<div
								class="absolute inset-0 bg-black bg-opacity-0 hover:bg-opacity-10 transition-all duration-200 flex items-center justify-center"
							>
								<span
									class="text-white opacity-0 hover:opacity-100 transition-opacity duration-200"
								>
									<i class="fas fa-search-plus text-4xl"></i>
								</span>
							</div>
						</div>
						<div
							v-if="post.itinerary_in_post"
							:key="post.itinerary_in_post.id"
							class="rounded-xl w-full overflow-hidden border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-200 cursor-pointer"
							@click="
								goToViewItinerary(post.itinerary_in_post.id)
							"
						>
							<img
								v-if="post.itinerary_in_post.main_image"
								:src="post.itinerary_in_post.main_image"
								alt=""
								class="w-full h-48 object-cover"
							/>
							<div class="p-4 bg-gray-50 dark:bg-gray-800">
								<h3
									class="text-sm sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
								>
									{{ post.itinerary_in_post.main_title }}
								</h3>
								<p
									class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
								>
									{{
										post.itinerary_in_post.main_description
									}}
								</p>
							</div>
						</div>
					</div>
				</div>
				<!-- Actions Section -->
				<!-- Actions Section -->
				<div
					class="flex items-center justify-end space-x-4 mt-4 pt-4 border-t border-gray-100 dark:border-gray-700"
				>
					<button
						@click.prevent="selectPost(post)"
						class="flex items-center space-x-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 transition-colors duration-200"
					>
						<ChatBubbleLeftIcon class="size-4" />
						<span class="text-sm">{{
							post.comments?.length || 0
						}}</span>
					</button>

					<div class="relative group">
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
				<!-- Image Modal -->
				<div
					v-if="showImageModal"
					class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-75"
					@click="closeImageModal"
				>
					<div class="max-w-4xl w-full max-h-screen p-4">
						<img
							:src="modalImage"
							alt="Full size image"
							class="w-full h-auto max-h-full object-contain"
						/>
					</div>
				</div>
			</div>
			<div
				v-else
				class="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6 text-center"
			>
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Private Account
				</h2>
				<p class="text-gray-600 dark:text-gray-300">
					This account is private. Follow to see their posts.
				</p>
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
							:class="{
								'brightness-[10%]': user.like_leader < 10,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/share-star.png`"
							:class="{
								'brightness-[10%]': user.share_star < 10,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/comment-connoisseur.png`"
							:class="{
								'brightness-[10%]':
									user.comment_connoisseur < 5,
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
							:class="{
								'brightness-[10%]': user.trend_setter < 50,
							}"
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
<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import axiosClient from "../axios";
import { useDark, useToggle } from "@vueuse/core";
import moment from "moment";

import {
	CogIcon,
	CameraIcon,
	EnvelopeIcon,
	GlobeAltIcon,
	UserIcon,
	PhotoIcon,
	TrophyIcon,
	HeartIcon,
	ArrowLeftIcon,
	UserPlusIcon,
	UserMinusIcon,
} from "@heroicons/vue/24/outline";

import {
	ChatBubbleLeftIcon,
	PencilSquareIcon,
	XMarkIcon,
	CheckIcon,
	FaceSmileIcon,
	PaperAirplaneIcon,
} from "@heroicons/vue/24/solid";
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();
const store = useStore();
const router = useRouter();
const isDark = useDark();
const toggleDark = useToggle(isDark);

const hasContentCreator = ref(false);
const hasGuideGuru = ref(false);
const hasLikeLeader = ref(false);
const hasShareStar = ref(false);
const hasCommentConnoisseur = ref(false);
const hasExplorerExtraordinaire = ref(false);
const hasKnowledgeSeeker = ref(false);
const hasTrendsetter = ref(false);
const hasCulturaContributor = ref(false);

const visitor_user = computed(() => store.state.user.data);
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
const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
};

const profile = ref(false);
const activeTab = ref("posts");
const tabs = [
	{ id: "posts", name: "Posts", icon: PhotoIcon },
	{ id: "achievements", name: "Achievements", icon: TrophyIcon },
];

const setActiveTab = (tabId) => {
	activeTab.value = tabId;
};

const showModal = ref(false);

const commentsInPost = ref([]);
const reply = ref("");
const postProfileDisplay = ref(null);
const selectedImageUrl = ref(null);
const picture = ref(null);

const authUser = ref("");
const isEditing = ref(true);
const postTitle = ref("");

const addItineraryModal = ref(false);

const categoryOption = ref("");
const postContent = ref("");
const countryPost = ref("");

const posts = ref([]);
const user = ref([]);

const userId = ref(0);
const selectedPost = ref([]);
const repliedTo = ref("");
const postId = ref("");

const comments = ref([]);

const itineraries = ref([]);
const itinerariesFromPost = ref([]);
const selectedItinerary = ref(null);
const idOfSelected = ref("");
const isFullTextShown = ref({});
const userID = ref(route.query.id);
const checkedAfterDelay = ref(false);
let client;
const id_get_post = ref(null);

const labels = ["Username", "Email", "Country"];
const fields = ["username", "email", "country"];

const fetchUser = async () => {
	const res = await store.dispatch("viewCulturaUser", userID.value);
	user.value = {
		...res,
		username: res.user.username,
	};

	id_get_post.value = user.value.user.id;
	fetchPosts(id_get_post.value);
};
onMounted(() => {
	setTimeout(() => {
		checkedAfterDelay.value = true;
	}, 5000);

	// console.log("USER ID::", userId.value);
	fetchUser();
});

const token = sessionStorage.getItem("TOKEN");
client = axios.create({
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

const follow = (id) => {
	axiosClient
		.post(`/follow/${id}/follow/`)
		.then((response) => {
			// user.value.is_followed = response.data.is_followed;
			// user.value.follow_count = response.data.follow_count;
			fetchUser();
		})
		.catch((error) => {
			console.error("Error following the user:", error);
		});
};

const goToViewItinerary = (itineraryId) => {
	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};
const showImageModal = ref(false);
const modalImage = ref("");
// functions for image modal
const openImageModal = (imageUrl) => {
	modalImage.value = imageUrl;
	showImageModal.value = true;
};
const closeImageModal = () => {
	showImageModal.value = false;
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const likePost = async (postId) => {
	try {
		await store.dispatch("likePost", postId);
		// Update the posts array
		posts.value = posts.value.map((post) => {
			if (post._id === postId) {
				post.is_liked = !post.is_liked;
				post.like_count += post.is_liked ? 1 : -1;
			}
			return post;
		});
		// await fetchPosts();
	} catch (error) {
		console.error("Error liking the post:", error);
	}
};

const selectPost = (post) => {
	// showModal.value = true;
	// selectedPost.value = [post];
	// post_id.value = post._id;
	// replied_to.value = post.author;
	// comments_in_post.value = post.comments || [];
	router.push({
		name: "view-post",
		params: { post: post._id },
		query: { n: "" },
	});
};
const submitReply = () => {
	axiosClient
		.post("/commenting", {
			post_id: postId.value,
			replied_to: repliedTo.value,
			body: reply.value,
		})
		.then((response) => {
			// console.log(response.data);
			reply.value = "";

			fetchPosts(id_get_post.value);
		})
		.catch((error) => {
			console.error(error);
		});
};

const fetchPosts = async (id) => {
	try {
		const response = await store.dispatch("fetchPublicProfilePosts", id);
		// console.log("POSTS::", response);

		posts.value = response.reverse();
	} catch (error) {
		console.error("Error fetching posts:", error);
	}
};
</script>
