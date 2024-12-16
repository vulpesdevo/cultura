<template>
	<div
		class="bg-gray-100 dark:bg-notif h-screen overflow-hidden pt-5 pb-5 px-4 sm:px-6 lg:px-14"
	>
		<!-- Loading component -->
		<div
			v-if="isLoading"
			class="flex items-center justify-center bg-opacity-50 size-full"
		>
			<div class="rounded-lg p-6">
				<div class="flex items-center space-x-4">
					<div
						class="w-12 h-12 border-t-4 border-blue-500 border-solid rounded-full animate-spin"
					></div>
				</div>
			</div>
		</div>

		<div v-else>
			<div
				class="relative profile-main flex flex-col items-center align-middle w-full pb-16 sm:pb-10 py-5 overflow-auto overflow-x-hidden h-screen bg-field dark:bg-dark-notif pt-5 sm:pt-7"
			>
				<div
					class="relative profile-card flex sm:flex-row flex-col justify-center sm:justify-normal w-screen sm:w-full sm:mt-0 px-3 sm:px-9 rounded-sm sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
					v-show="profile"
				>
					<!-- Settings Button -->
					<router-link
						:to="{ name: 'settings' }"
						class="absolute top-4 right-4 p-2 rounded-full bg-gray-700 hover:bg-gray-600 transition-colors duration-200"
						aria-label="Settings"
					>
						<CogIcon class="w-6 h-6 text-gray-300" />
					</router-link>
					<!-- Left Column - Profile Image -->
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
					</div>

					<!-- Right Column - User Details -->
					<div
						class="flex flex-col justify-center items-center sm:pl-6"
					>
						<!-- Name Section -->
						<div class="mb-4">
							<div
								v-if="!profile.fullname"
								class="animate-pulse bg-gray-400 bg-opacity-40 h-[2.5rem] sm:h-[4.5rem] w-48 rounded-lg"
							></div>
							<h1
								class="font-bebas-neue profile-name text-3xl sm:text-6xl text-prime dark:text-dark-second text-nowrap"
							>
								{{ profile.fullname }}
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
									class="font-montserrat text-prime dark:text-gray-400"
									>Username:</small
								>
								<small
									class="font-montserrat text-prime dark:text-gray-400"
									>Email:</small
								>
								<small
									class="font-montserrat text-prime dark:text-gray-400"
									>Country:</small
								>
							</div>

							<div
								class="profile-info text-xm sm:text-base flex items-start justify-center sm:items-start flex-col sm:justify-between w-full sm:w-1/2"
							>
								<div
									v-if="!profile.username"
									class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
								></div>
								<small
									class="font-montserrat text-prime dark:text-dark-second h-4"
								>
									@{{ profile.username }}
								</small>

								<div
									v-if="!profile.email"
									class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
								></div>
								<small
									class="font-montserrat text-prime dark:text-dark-second h-4"
								>
									{{ profile.email }}
								</small>

								<div
									v-if="!profile.country"
									class="animate-pulse bg-gray-400 bg-opacity-40 h-4 w-40 sm:w-48 rounded-lg"
								></div>
								<small
									class="font-montserrat text-prime dark:text-dark-second mb"
								>
									{{ profile.country }}
								</small>
							</div>
						</div>
					</div>
					<!-- Stats Section -->
					<div
						class="flex justify-center items-center space-x-5 sm:items-end sm:justify-end w-full sm:m-5 pb-4 sm:pb-0 font-montserrat"
					>
						<div class="text-center">
							<div
								class="text-base font-semibold text-prime dark:text-dark-second"
							>
								{{ posts.length }}
							</div>
							<div
								class="text-sm text-gray-600 dark:text-gray-400"
							>
								Posts
							</div>
						</div>
						<div class="text-center">
							<div
								class="text-base font-semibold text-prime dark:text-dark-second"
							>
								{{ followers.length }}
							</div>
							<div
								class="text-sm text-gray-600 dark:text-gray-400"
							>
								Followers
							</div>
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
				<div class="w-full p-4" v-if="activeTab === 'follower_tab'">
					<div class="w-full">
						<div class="w-full grid sm:grid-cols-2 gap-4">
							<router-link
								class="w-full bg-interface dark:bg-dark-interface flex shadow-lg h-24 justify-between items-center p-5 text-prime dark:text-interface rounded-xl"
								v-for="user in followers"
								:key="user.id"
								:to="{
									name: 'user-profile',
									params: {
										username: user.user_data[0].username,
									},
									query: {
										id: user.user_data[0].id,
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

				<div
					class="posts-in-profile w-full"
					v-if="activeTab === 'posts'"
				>
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
						class="relative post-contents w-full p-6 mt-4 rounded-xl shadow-lg bg-white dark:bg-dark-field transition-all duration-200 hover:shadow-xl font-montserrat"
						v-for="post in posts"
						:key="post._id"
					>
						<!-- Header Section -->
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
											>{{
												timesince(post.date_posted)
											}}</span
										>
									</div>
									<div
										class="text-xs text-gray-500 dark:text-gray-400"
									>
										{{ post.category }} | {{ post.country }}
									</div>
								</div>
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

						<!-- Title Section -->
						<h1
							class="text-xl font-medi text-gray-900 dark:text-second mb-3"
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
								v-if="post.image"
								class="relative rounded-xl overflow-hidden cursor-pointer"
								@click="openImageModal(post.image)"
							>
								<img
									:src="post.image"
									alt=""
									class="w-full h-auto max-h-[20rem] object-cover"
								/>
								<div
									class="absolute inset-0 bg-black bg-opacity-0 hover:bg-opacity-10 transition-all duration-200 flex items-center justify-center"
								>
									<span
										class="text-white opacity-0 hover:opacity-100 transition-opacity duration-200"
									>
										<i
											class="fas fa-search-plus text-4xl"
										></i>
									</span>
								</div>
							</div>

							<!-- Itinerary Section -->
							<div
								v-if="post.itinerary_in_post"
								class="mt-4 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-200 cursor-pointer"
								@click="
									goToViewItinerary(post.itinerary_in_post.id)
								"
							>
								<img
									:src="post.itinerary_in_post.main_image"
									alt=""
									class="w-full h-48 object-cover"
								/>
								<div class="p-4 bg-gray-50 dark:bg-gray-800">
									<h3
										class="text-xl font-bold text-gray-900 dark:text-white mb-2"
									>
										{{ post.itinerary_in_post.main_title }}
									</h3>
									<p
										class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
									>
										{{
											post.itinerary_in_post
												.main_description
										}}
									</p>
								</div>
							</div>
						</div>

						<!-- Actions Section -->
						<div
							class="flex items-center justify-end space-x-4 mt-4 pt-4 border-t border-gray-100 dark:border-gray-700"
						>
							<button
								@click.prevent="selectPost(post)"
								class="flex items-center space-x-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 transition-colors duration-200"
							>
								<i class="fa-regular fa-comment text-xl"></i>
								<span class="text-sm">{{
									post.comments?.length || 0
								}}</span>
							</button>

							<button
								@click="likePost(post._id)"
								class="flex items-center space-x-2 text-gray-500 hover:text-second dark:text-gray-400 dark:hover:text-second transition-colors duration-200"
							>
								<span class="material-icons-outlined text-xl">
									{{
										post.is_liked
											? "favorite"
											: "favorite_border"
									}}
								</span>
								<span class="text-sm">
									{{
										post.like_count >= 1000
											? (post.like_count / 1000).toFixed(
													1
											  ) + "k"
											: post.like_count
									}}
								</span>
							</button>
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
					class="flex justify-center items-center achievements w-full p-4 sm:px-9"
					v-if="activeTab === 'achievements'"
				>
					<div
						class="flex justify-center items-center w-screen sm:w-full"
					>
						<div class="grid grid-cols-5 gap-1 sm:gap-0 sm:w-3/4">
							<div
								v-for="(achievement, index) in achievements"
								:key="index"
								class="relative"
							>
								<div
									class="flex justify-center items-center h-[5rem] w-[5rem] sm:h-[10rem] sm:w-[10rem]"
								>
									<img
										:src="achievement.image"
										:alt="achievement.name"
										:class="{
											'brightness-[10%]':
												!achievement.achieved,
										}"
										class="cursor-help"
										@mouseenter="showTooltip(index)"
										@mouseleave="hideTooltip"
									/>
								</div>
								<div
									v-if="activeTooltip === index"
									class="absolute sm:bottom-[80%] right-0 transform translate-x-1/2 mb-2 p-3 bg-dark-interface text-white text-sm rounded-lg w-64 transition-all duration-200 z-10"
								>
									<div class="flex items-start gap-1">
										<img
											v-if="achievement.achieved"
											:src="achievement.image"
											:alt="achievement.name"
											class="size-16 object-contain"
										/>
										<div class="flex-1 min-w-0">
											<strong class="block mb-1">{{
												achievement.name
											}}</strong>
											<p class="text-xs mb-1 break-words">
												{{ achievement.description }}
											</p>
											<p
												class="text-xs"
												:class="
													achievement.achieved
														? 'text-green-400'
														: 'text-gray-400'
												"
											>
												{{
													achievement.achieved
														? "Achieved!"
														: achievement.encouragement
												}}
											</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div
					class="comments-modal fixed z-50 inset-0 overflow-y-auto"
					aria-labelledby="modal-title"
					role="dialog"
					aria-modal="true"
					v-if="showModal"
				>
					<div
						class="flex min-h-screen items-center justify-center p-4"
					>
						<div
							class="fixed inset-0 bg-black/90 transition-opacity"
							aria-hidden="true"
						></div>

						<div
							class="relative w-full max-w-2xl bg-[#1c1c1f] rounded-xl shadow-xl overflow-hidden"
						>
							<!-- Header -->
							<div
								class="flex items-center justify-between p-6 border-b border-gray-800"
							>
								<h2 class="text-2xl font-semibold text-white">
									Comments
								</h2>
								<button
									@click="showModal = false"
									class="text-gray-400 hover:text-white transition-colors"
								>
									<XIcon class="h-6 w-6" />
								</button>
							</div>

							<!-- Post Content -->
							<div
								v-for="data in selectedPost"
								:key="data._id"
								class="p-6 border-b border-gray-800"
							>
								<div class="flex space-x-4">
									<img
										:src="data.author_user_photo"
										alt="Profile"
										class="h-10 w-10 rounded-full object-cover"
									/>
									<div class="flex-1 min-w-0">
										<div
											class="flex items-center justify-between"
										>
											<div
												class="flex items-center space-x-2"
											>
												<span
													class="text-white font-medium"
													>{{ data.author }}</span
												>
												<span
													class="text-gray-500 text-sm"
													>{{ data.category }} |
													{{ data.country }}</span
												>
											</div>
										</div>
										<p class="mt-1 text-gray-300 text-sm">
											{{ data.content }}
										</p>
									</div>
								</div>
							</div>

							<!-- Comments List -->
							<div
								class="overflow-y-auto max-h-[400px] p-6 space-y-6"
							>
								<div
									v-for="comment in comments_in_post"
									:key="comment._id"
									class="flex space-x-4 relative"
								>
									<div class="flex-shrink-0">
										<img
											:src="comment.author_user_photo"
											alt="Profile"
											class="h-10 w-10 rounded-full object-cover"
										/>
									</div>
									<div class="flex-1 min-w-0">
										<div
											class="flex items-center space-x-2"
										>
											<span
												class="text-white font-medium"
												>{{ comment.author }}</span
											>
											<span class="text-gray-500"
												>to</span
											>
											<span class="text-blue-400">{{
												comment.replied_to
											}}</span>
											<span
												class="text-gray-500 text-sm"
												>{{
													timesince(
														comment.date_posted
													)
												}}</span
											>
										</div>
										<p class="mt-1 text-gray-300 text-sm">
											{{ comment.body }}
										</p>
										<!-- <div
                        class="flex items-center space-x-4 mt-2"
                      >
                        <button
                          class="flex items-center space-x-1 text-gray-400 hover:text-white transition-colors"
                        >
                          <ThumbsUpIcon class="h-4 w-4" />
                        </button>
                        <button
                          class="text-gray-400 hover:text-white transition-colors text-sm"
                        >
                          Reply
                        </button>
                      </div> -->
									</div>
								</div>
							</div>

							<!-- Reply Input -->
							<div class="p-6 border-t border-gray-800">
								<div class="flex space-x-4">
									<img
										:src="profile.user_photo"
										alt="Profile"
										class="h-10 w-10 rounded-full object-cover"
									/>
									<div class="flex-1">
										<textarea
											v-model="reply"
											rows="3"
											class="w-full bg-gray-800 border border-gray-700 rounded-lg p-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
											:placeholder="
												'Replying to ' +
												selectedPost[0]?.author
											"
										></textarea>
										<div
											class="flex justify-end mt-3 space-x-3"
										>
											<button
												@click.prevent="submitReply"
												class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-full text-sm font-medium transition-colors"
											>
												Reply
											</button>
										</div>
									</div>
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
							You are trying to delete this post. This action
							cannot be undone.
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
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from "vue";
import { XIcon, ThumbsUpIcon } from "lucide-vue-next";
import {
	CogIcon,
	CameraIcon,
	EnvelopeIcon,
	GlobeAltIcon,
	UserIcon,
	PhotoIcon,
	TrophyIcon,
	ArrowLeftIcon,
} from "@heroicons/vue/24/outline";
import axiosClient from "../axios";

import axios from "axios";
import moment from "moment";
import { useRouter, useRoute } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();
const store = useStore();
const router = useRouter();

const hasContentCreator = ref(false);
const hasGuideGuru = ref(false);
const hasLikeLeader = ref(false);
const hasShareStar = ref(false);
const hasCommentConnoisseur = ref(false);
const hasExplorerExtraordinaire = ref(false);
const hasKnowledgeSeeker = ref(false);
const hasTrendsetter = ref(false);
const hasCulturaContributor = ref(false);

const showModal = ref(false);
const profile = reactive({
	username: "",
	user_photo: "",
	fullname: "",
	email: "",
	password: "",
	country: "",
});

const posts = ref([]);
const followers = ref([]);

const activeTab = ref("posts");
const tabs = [
	{ id: "posts", name: "Posts", icon: PhotoIcon },
	{ id: "follower_tab", name: "Followers", icon: UserIcon },
	{ id: "achievements", name: "Achievements", icon: TrophyIcon },
];

const setActiveTab = (tabId) => {
	activeTab.value = tabId;
};

const selectedPost = ref([]);
const reply = ref("");
const replied_to = ref("");
const post_id = ref("");

const comments = ref([]);
const comments_in_post = ref([]);

const modalDeleteActive = ref(false);
const isMenuOpen = ref(false);
const openedPost_id = ref(null);

const selectedImageUrl = ref("/default_profile.png");

const changingPhoto = ref(false);
const picture = ref(null);
const checkedAfterDelay = ref(false);
const isLoading = ref(true);

const token = sessionStorage.getItem("TOKEN");

const client = axios.create({
	baseURL: "http://127.0.0.1:8000",
	withCredentials: true,
	timeout: 5000,
	xsrfCookieName: "csrftoken",
	xsrfHeaderName: "X-Csrftoken",
	headers: {
		Authorization: `Token ${token}`,
		"Content-Type": "application/json",
	},
});

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

onMounted(() => {
	fetchData();
});

const fetchData = async () => {
	try {
		await fetchUser();
		await fetchPosts();
	} catch (error) {
		console.error("Error fetching data:", error);
	} finally {
		console.log("Data fetched, setting isLoading to false");
		isLoading.value = false;
	}
};

const goToViewItinerary = (itineraryId) => {
	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};

const follow = (userId) => {
	console.log("The user", userId);
	axiosClient
		.post(`/follow/${userId}/follow/`)
		.then((response) => {
			console.log(response.data);
			fetchPosts();
		})
		.catch((error) => {
			console.error("Error following the user:", error);
		});
};

const fetchUser = async () => {
	try {
		const { data } = await axiosClient.get("/user");
		const { user, profile: userProfile } = data;
		Object.assign(profile, {
			username: user.username,
			fullname: userProfile.fullname,
			country: userProfile.country,
			user_photo: userProfile.user_photo,
			email: userProfile.email,
		});
		changingPhoto.value = false;

		hasContentCreator.value = userProfile.content_creator >= 5;
		hasGuideGuru.value = userProfile.guide_guru >= 1;
		hasLikeLeader.value = userProfile.like_leader >= 10;
		hasShareStar.value = userProfile.share_star >= 10;
		hasCommentConnoisseur.value = userProfile.comment_connoisseur >= 5;
		hasExplorerExtraordinaire.value =
			userProfile.explorer_extraordinaire >= 10;
		hasKnowledgeSeeker.value = userProfile.knowledge_seeker >= 15;
		hasTrendsetter.value = userProfile.trend_setter >= 50;
		hasCulturaContributor.value =
			userProfile.content_creator >= 20 && userProfile.guide_guru >= 10;

		console.log("USER", userProfile);
	} catch (error) {
		console.log("ERROR", error);
		throw error;
	}
};

const handleFileSelection = (event) => {
	console.log("Image : TRIGERRED");
	const file = event.target.files[0];

	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		picture.value = file;
		changingPhoto.value = true;
		console.log("Image :", picture.value);
	}
};

const cancelProfile = () => {
	changingPhoto.value = false;
	document.getElementById("imgSelect").value = "";
};

const changeProfile = () => {
	let formData = new FormData();

	if (picture.value && picture.value instanceof File) {
		formData.append("image", picture.value, picture.value.name);
	}
	console.log("FORM :", formData);
	axiosClient
		.post("/change-profile", formData, {
			headers: {
				"Content-Type": "multipart/form-data",
			},
		})
		.then((response) => {
			console.log("CHANGE PROFILE !!");
			fetchUser();
		})
		.catch((error) => {
			console.error(error);
		});
};

const likePost = (post_id) => {
	axiosClient
		.post(`/like-posts/${post_id}/like_post/`)
		.then((response) => {
			console.log(response.data);
			fetchPosts();
		})
		.catch((error) => {
			console.error("Error liking the post:", error);
		});
};

const toggleMenu = (postId) => {
	isMenuOpen.value = isMenuOpen.value === postId ? null : postId;
	openedPost_id.value = postId;
};

const editItem = () => {
	alert("Edit action triggered");
	isMenuOpen.value = false;
};

const deleteItem = () => {
	modalDeleteActive.value = !modalDeleteActive.value;
	isMenuOpen.value = null;
	console.log("the opened : ", openedPost_id.value);
};

const deletePost = () => {
	axiosClient
		.post("/delete-post", {
			post_id: openedPost_id.value,
		})
		.then((response) => {
			console.log(response.data);
			fetchPosts();
			modalDeleteActive.value = false;
		})
		.catch((error) => {
			console.error(error);
		});
};

const submitReply = () => {
	axiosClient
		.post("/commenting", {
			post_id: post_id.value,
			replied_to: replied_to.value,
			body: reply.value,
		})
		.then((response) => {
			console.log(response.data);
			reply.value = "";
			fetchPosts();
		})
		.catch((error) => {
			console.error(error);
		});
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const selectPost = (post) => {
	// showModal.value = true;
	selectedPost.value = [post];
	// console.log("GET POST", selectedPost.value[0]._id);
	const _id = selectedPost.value[0]._id;
	// replied_to.value = selectedPost.value[0].author;
	// comments_in_post.value =
	// 	posts.value.find((p) => p._id === post_id.value)?.comments || [];
	// console.log("the id : ", comments_in_post.value);
	router.push({
		name: "view-post",
		params: { post: _id },
		query: { n: "" },
	});
};

const edit_post = (post_data) => {
	router.push({
		name: "editpost",
		params: {
			user: JSON.stringify(post_data),
		},
	});
};

const view_user = (user_data) => {
	router.push({
		name: "user-profile",
		params: {
			username: user_data[0].username,
			user: JSON.stringify(user_data[0]),
		},
	});
};

const fetchPosts = async () => {
	try {
		const response = await axiosClient.get(`/profile-posts`);
		posts.value = response.data.posts.reverse();

		if (posts.value.length > 0) {
			const itineraries_frompost = posts.value[0].itinerary_in_post;
			comments_in_post.value =
				posts.value.find((p) => p._id === post_id.value)?.comments ||
				[];
		}
		followers.value = response.data.followers;
		console.log("Followers", followers.value);
	} catch (error) {
		console.log(error);
		throw error;
	}
};

const activeTooltip = ref(null);

const achievements = computed(() => [
	{
		name: "Welcome Wanderer",
		image: "/achievements/welcome-wanderer.png",
		description: "First steps into CulturaLink",
		achieved: true, // Always achieved as they're using the app
		encouragement: "Join CulturaLink!",
	},
	{
		name: "Content Creator",
		image: "/achievements/content-creator.png",
		description: "Create 5+ engaging posts",
		achieved: hasContentCreator.value,
		encouragement: "Keep creating!",
	},
	{
		name: "Guide Guru",
		image: "/achievements/guide-guru.png",
		description: "Create your first travel guide",
		achieved: hasGuideGuru.value,
		encouragement: "Start guiding!",
	},
	{
		name: "Like Leader",
		image: "/achievements/like-leader.png",
		description: "Receive 10+ likes on your content",
		achieved: hasLikeLeader.value,
		encouragement: "Keep sharing quality content!",
	},
	{
		name: "Share Star",
		image: "/achievements/share-star.png",
		description: "Share content 10+ times",
		achieved: hasShareStar.value,
		encouragement: "Start sharing!",
	},
	{
		name: "Comment Connoisseur",
		image: "/achievements/comment-connoisseur.png",
		description: "Make 5+ thoughtful comments",
		achieved: hasCommentConnoisseur.value,
		encouragement: "Join the conversation!",
	},
	{
		name: "Explorer Extraordinaire",
		image: "/achievements/explorer-extraordinaire.png",
		description: "Explore 10+ different locations",
		achieved: hasExplorerExtraordinaire.value,
		encouragement: "Keep exploring!",
	},
	{
		name: "Knowledge Seeker",
		image: "/achievements/knowledge-seeker.png",
		description: "Complete 15+ learning activities",
		achieved: hasKnowledgeSeeker.value,
		encouragement: "Keep learning!",
	},
	{
		name: "Trend Setter",
		image: "/achievements/trend-setter.png",
		description: "Get 50+ trending posts",
		achieved: hasTrendsetter.value,
		encouragement: "Create trending content!",
	},
	{
		name: "Cultura Contributor",
		image: "/achievements/cultura-contributor.png",
		description: "Elite status: 20+ content & 10+ guides",
		achieved: hasCulturaContributor.value,
		encouragement: "Become an elite contributor!",
	},
]);

const showTooltip = (index) => {
	activeTooltip.value = index;
};

const hideTooltip = () => {
	activeTooltip.value = null;
};

const goBack = () => {
	router.go(-1);
};
</script>

<style scoped>
/* Your existing styles */
</style>
