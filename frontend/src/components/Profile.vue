<template>
	<div
		class="profile-main flex flex-col items-center align-middle w-full pb-16 sm:pb-10 sm:px-8 py-5 sm:ml-64 overflow-auto overflow-x-hidden h-screen bg-field dark:bg-dark-notif pt-5 sm:pt-7"
	>
		<div
			class="profile-1 w-screen sm:w-full mt-12 sm:mt-0 px-3 sm:pt-6 sm:px-9 rounded-sm sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
			v-show="profile"
		>
			<div
				class="profile-img flex flex-col pt-9 items-center align-middle mb-2 sm:mb-5"
			>
				<div
					class="flex items-center justify-center bg-prime dark:bg-second relative rounded-full w-40 h-40 sm:w-52 sm:h-52 sm:mb-8 mb-4 p-[.2rem] group"
				>
					<img
						v-if="!changingPhoto"
						:class="{ hidden: changingPhoto }"
						class="rounded-full shadow-2xl w-[9.5rem] h-[9.5rem] sm:w-full sm:h-full object-cover border-interface dark:border-dark-interface border-8"
						:src="profile.user_photo"
						alt=""
					/>
					<img
						v-else
						class="rounded-full shadow-2xl w-[9.5rem] h-[9.5rem] sm:w-full sm:h-full object-cover border-interface dark:border-dark-interface border-8"
						:src="selectedImageUrl"
						alt=""
					/>
					<label
						v-if="!changingPhoto"
						for="imgSelect"
						class="flex items-center justify-center absolute bottom-0 right-3 h-10 w-10 rounded-full bg-black transition duration-300 ease-in-out cursor-pointer bg-opacity-0 group-hover:bg-opacity-50"
					>
						<span
							class="material-icons-outlined text-interface dark:text-second text-xl text-opacity-0 dark:text-opacity-0 group-hover:text-opacity-100 group-hover:dark:text-opacity-100"
							>download</span
						>
					</label>
					<div
						v-if="changingPhoto"
						for=""
						class="flex items-center justify-center absolute top-0 right-3 h-10 w-10 rounded-full bg-black transition duration-300 ease-in-out cursor-pointer bg-opacity-50"
						@click="cancelProfile"
					>
						<span
							class="material-icons-outlined text-red-400 text-xl"
							>clear</span
						>
					</div>
					<div
						v-if="changingPhoto"
						for=""
						class="flex items-center justify-center absolute bottom-0 right-3 h-10 w-10 rounded-full bg-black transition duration-300 ease-in-out cursor-pointer bg-opacity-50"
						@click="changeProfile"
					>
						<span
							class="material-icons-outlined text-green-400 text-xl"
							>done</span
						>
					</div>
				</div>
				<input
					type="file"
					name=""
					id="imgSelect"
					class="hidden"
					@change="handleFileSelection"
				/>
				<div
					v-if="!profile.fullname"
					class="animate-pulse bg-gray-400 bg-opacity-40 h-[2.5rem] sm:h-[4.5rem] w-1/2 rounded-lg"
				></div>
				<h1
					class="font-bebas-neue profile-name text-4xl sm:text-7xl text-prime dark:text-dark-second"
				>
					{{ profile.fullname }}
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
						v-if="!profile.username"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>
					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2 h-4"
					>
						{{ profile.username }}
					</small>
					<div
						v-if="!profile.email"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>
					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2 h-4"
					>
						{{ profile.email }}
					</small>
					<div
						v-if="!profile.country"
						class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
					></div>

					<small
						class="font-montserrat text-prime dark:text-dark-second mb-2"
					>
						{{ profile.country }}
					</small>
				</div>
			</div>
		</div>
		<div class="profile-tabs flex justify-center w-full my-5 sm:px-2">
			<button
				class="font-montserrat text-prime h-10 sm:h-12 w-1/3 sm:w-64 text-sm sm:text-2xl mx-2 sm:mx-0 pb-3 sm:pb-0"
				@click="activeTab = 'posts'"
				:class="{
					'rounded-none border-b-4 border-second sm:border-none sm:rounded-full sm:bg-second dark:text-white ':
						activeTab === 'posts',
					'bg-none text-second': activeTab !== 'posts',
				}"
			>
				Posts
			</button>
			<button
				class="font-montserrat text-prime h-10 sm:h-12 w-1/3 sm:w-64 text-sm sm:text-2xl mx-2 sm:mx-0 pb-3 sm:pb-0"
				@click="activeTab = 'achievements'"
				:class="{
					'rounded-none border-b-4 border-second sm:border-none sm:rounded-full sm:bg-second dark:text-white':
						activeTab === 'achievements',
					'bg-none text-second': activeTab !== 'achievements',
				}"
			>
				Achievements
			</button>
			<button
				class="font-montserrat text-prime h-10 sm:h-12 w-1/3 sm:w-64 text-sm sm:text-2xl mx-2 sm:mx-0 pb-3 sm:pb-0"
				@click="activeTab = 'follower_tab'"
				:class="{
					'rounded-none border-b-4 border-second sm:border-none sm:rounded-full sm:bg-second dark:text-white':
						activeTab === 'follower_tab',
					'bg-none text-second': activeTab !== 'follower_tab',
				}"
			>
				Followers ({{ users.length }})
			</button>
		</div>
		<div class="w-full px-2" v-if="activeTab === 'follower_tab'">
			<div class="w-full">
				<div class="w-full grid sm:grid-cols-2 gap-4">
					<router-link
						class="w-full bg-interface dark:bg-dark-interface flex shadow-lg h-24 justify-between items-center p-5 text-prime dark:text-interface rounded-xl"
						v-for="user in users"
						:key="user.id"
						:to="{
							name: 'user-profile',
							params: {
								username: user.user_data[0].username,
								user: JSON.stringify(user.user_data[0]),
							},
						}"
					>
						<div
							class="w-16 h-20 mr-2 sm:mr-4 flex justify-center items-center"
						>
							<img
								:src="user.user_data[0].user_photo"
								alt="Profile"
								class="rounded-full cursor-pointer"
							/>
						</div>
						<div class="font-montserrat text-left w-full">
							<p class="font-bold">
								{{ user.user_data[0].fullname }}
							</p>
							<small class="flex-col text-nowrap"
								>{{ user.user_data[0].country }} |
								{{ user.user_data[0].email }}</small
							>
						</div>
					</router-link>
				</div>
			</div>
		</div>

		<div class="posts-in-profile w-full" v-if="activeTab === 'posts'">
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
					<div class="flex w-[10%] justify-end relative">
						<button @click="toggleMenu(post._id)" class="">
							<span
								class="material-icons-outlined dark:text-dark-prime"
							>
								more_horiz
							</span>
						</button>
						<div
							v-if="isMenuOpen === post._id"
							class="absolute mt-5 w-48 bg-white border border-gray-200 rounded-md shadow-lg"
						>
							<!-- @click.prevent="editItem" -->
							<!-- <a
								href="#"
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								aria-disabled="true"
								>Edit</a
							> -->
							<router-link
								class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
								:to="{
									name: 'editpost',
									params: {
										post: JSON.stringify(post),
									},
								}"
							>
								Edit
							</router-link>
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
						<div class="h-auto pb-2 sm:p-4" v-else>
							<div
								class="cont-itinerary mt-6 pt-4 px-6 items-center align-middle rounded-lg shadow-lg bg-interface dark:bg-dark-interface cursor-pointer sm:w-11/12 sm:px-6"
								:key="post.itinerary_in_post.id"
								v-if="post.itinerary_in_post"
								@click="
									goToViewItinerary(post.itinerary_in_post.id)
								"
							>
								<div
									class="mt-2 sm:px-5 pb-5 sm:pt-5 mb-10 w-full"
								>
									<img
										class="rounded-lg shadow-2xl object-cover drop-shadow-xl w-full h-auto"
										:src="post.itinerary_in_post.main_image"
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
						<img
							src="`/achievements/welcome-wanderer.png`"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/content-creator.png`"
							:class="{ 'brightness-[10%]': !hasContentCreator }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/guide-guru.png`"
							:class="{ 'brightness-[10%]': !hasGuideGuru }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/like-leader.png`"
							:class="{ 'brightness-[10%]': !hasLikeLeader }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/share-star.png`"
							:class="{ 'brightness-[10%]': !hasShareStar }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/comment-connoisseur.png`"
							:class="{
								'brightness-[10%]': !hasCommentConnoisseur,
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
								'brightness-[10%]': !hasExplorerExtraordinaire,
							}"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/knowledge-seeker.png`"
							:class="{ 'brightness-[10%]': !hasKnowledgeSeeker }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/trend-setter.png`"
							:class="{ 'brightness-[10%]': !hasTrendsetter }"
							alt=""
						/>
					</div>
					<div
						class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
					>
						<img
							:src="`/achievements/cultura-contributor.png`"
							:class="{
								'brightness-[10%]': !hasCulturaContributor,
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
		<div
			v-if="modalDeleteActive"
			class="fixed flex flex-col z-50 inset-0 overflow-y-auto w-screen bg-black bg-opacity-50 h-screen items-center justify-center"
			role="dialog"
			aria-modal="true"
		>
			<div
				v-if="modalDeleteActive"
				class="flex-col sm:w-1/3 sm:h-[32%] rounded-lg p-4 bg-interface dark:bg-dark-interface"
			>
				<span
					@click="modalDeleteActive = false"
					class="flex material-icons-outlined justify-end cursor-pointer dark:text-interface"
					>close</span
				>
				<h1
					class="flex text-4xl sm:text-3xl text-prime dark:text-interface font-bold font-montserrat justify-center"
				>
					Are you sure?
				</h1>
				<p
					class="flex justify-center text-sm sm:text-[15px] my-5 mb-20 sm:my-7 px-3 sm:px-16 font-montserrat text-center dark:text-interface"
				>
					You are trying to delete this post. This action cannot be
					undone.
				</p>
				<div class="flex justify-center items-center">
					<button
						class="rounded-xl text-xl text-white mr-4 bg-notif dark:bg-dark-second-dark bg-opacity-80 py-2 px-7 font-bebas-neue"
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
			hasContentCreator: false,
			hasGuideGuru: false,
			hasLikeLeader: false,
			hasShareStar: false,
			hasCommentConnoisseur: false,
			hasExplorerExtraordinaire: false,
			hasKnowledgeSeeker: false,
			hasTrendsetter: false,
			hasCulturaContributor: false,

			showModal: false,
			profile: {
				username: "",
				user_photo: "",
				fullname: "",
				email: "",
				password: "",
				country: "",
			},
			showModal: false,
			posts: [],
			users: [],

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

			// forprofile
			selectedImageUrl: "/default_profile.png",

			changingPhoto: false,
			picture: null,
			checkedAfterDelay: false,
		};
	},
	mounted() {
		setTimeout(() => {
			this.checkedAfterDelay = true;
		}, 5000);
		// this.fetchPosts();
		// setInterval(this.fetchPosts, 5000); // Fetch posts every 5 seconds -->> polling
		// this.fetchComments();
		// setInterval(this.fetchComments, 5000);
		// Check if the user has met the criteria for each achievement
		// and update the corresponding data property
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
		this.fetchUser();
		this.fetchPosts();
	},
	methods: {
		follow(userId) {
			console.log("The user", userId);
			this.client
				.post(`api/follow/${userId}/follow/`)
				.then((response) => {
					// Handle success response
					console.log(response.data);
					// Update the is_followed property of the user object
					this.fetchPosts();
					// const userIndex = this.users.findIndex(
					// 	(user) => user.user === userId
					// );

					// this.users = this.users.map(user => {
					// 	if (user.user === userId) {
					// 		user.is_followed = response.data.is_followed;
					// 	}
					// 	if (userIndex !== -1) {
					// 	this.users[userIndex].is_followed =
					// 		response.data.is_followed;
					// }
					// 	return user;
					// });

					// Optionally, update your UI based on the successful follow
				})
				.catch((error) => {
					// Handle error
					console.error("Error following the user:", error);
				});
		},
		fetchUser() {
			this.client
				.get("api/user")
				.then((res) => {
					this.profile.username = res.data.user.username;
					this.profile.fullname = res.data.profile[0].fullname;
					this.profile.country = res.data.profile[0].country;
					// if (!res.data.profile.user_photo) {
					// 	this.profile.user_photo = res.data.profile.user_photo;
					// }
					this.profile.user_photo = res.data.profile[0].user_photo;
					this.profile.email = res.data.profile[0].email;
					this.changingPhoto = false;

					if (res.data.profile[0].content_creator >= 5) {
						this.hasContentCreator = true;
					}
					if (res.data.profile[0].guide_guru >= 1) {
						this.hasGuideGuru = true;
					}
					if (res.data.profile[0].like_leader >= 10) {
						this.hasLikeLeader = true;
					}
					if (res.data.profile[0].share_star >= 10) {
						this.hasShareStar = true;
					}
					if (res.data.profile[0].comment_connoisseur >= 5) {
						this.hasCommentConnoisseur = true;
					}
					if (res.data.profile[0].explorer_extraordinaire >= 10) {
						this.hasExplorerExtraordinaire = true;
					}
					if (res.data.profile[0].knowledge_seeker >= 15) {
						this.hasKnowledgeSeeker = true;
					}
					if (res.data.profile[0].trend_setter >= 50) {
						this.hasTrendsetter = true;
					}
					if (
						res.data.profile[0].content_creator >= 20 &&
						res.data.profile[0].guide_guru >= 10
					) {
						this.hasCulturaContributor = true;
					}
				})
				.catch((error) => {
					console.log("ERROR", error);
				});
		},
		handleFileSelection(event) {
			console.log("Image : TRIGERRED");
			const file = event.target.files[0];

			if (file) {
				this.selectedImageUrl = URL.createObjectURL(file);
				this.picture = file;
				this.changingPhoto = true;
				console.log("Image :", this.picture);
			}
		},
		cancelProfile() {
			this.changingPhoto = false;

			document.getElementById("imgSelect").value = "";
		},
		changeProfile() {
			let formData = new FormData();

			if (this.picture && this.picture instanceof File) {
				formData.append("image", this.picture, this.picture.name);
			}
			console.log("FORM :", formData);
			this.client
				.post("/api/change-profile", formData, {
					headers: {
						"Content-Type": "multipart/form-data",
					},
				})
				.then((response) => {
					console.log("CHANGE PROFILE !!");
					this.fetchUser();
				})
				.catch((error) => {
					console.error(error);
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
		toggleMenu(postId) {
			this.isMenuOpen = this.isMenuOpen === postId ? null : postId;
			this.openedPost_id = postId;
		},

		editItem() {
			alert("Edit action triggered");
			this.isMenuOpen = false;
		},
		deleteItem() {
			this.modalDeleteActive = !this.modalDeleteActive;
			this.isMenuOpen = null;
			console.log("the opened : ", this.openedPost_id);
		},
		deletePost() {
			this.client
				.post("/api/delete-post", {
					post_id: this.openedPost_id,
				})
				.then((response) => {
					console.log(response.data);

					this.fetchPosts();
					this.modalDeleteActive = false;
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
		// fetchComments() {
		// 	axios
		// 		.get("/api/comments")
		// 		.then((response) => {
		// 			this.comments = response.data;
		// 			console.log("comments:", this.comments);
		// 		})
		// 		.catch((error) => {
		// 			console.log(error);
		// 		});
		// },
		edit_post(post_data) {
			// console.log("FGFGF", user_data[0].username);
			this.$router.push({
				name: "editpost",
				params: {
					user: JSON.stringify(data),
				},
			});
		},
		view_user(user_data) {
			// console.log("FGFGF", user_data[0].username);
			this.$router.push({
				name: "user-profile",
				params: {
					username: user_data[0].username,
					user: JSON.stringify(user_data[0]),
				},
			});
		},
		fetchPosts() {
			this.client
				.get(`/api/profile-posts`)
				.then((response) => {
					this.posts = response.data.posts.reverse();
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
					this.users = response.data.followers;
					console.log("updateed asdasd:", response.data.followers);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

<style scoped></style>
