<template lang="">
	<div
		class="post-container flex flex-col items-center align-middle w-full sm:px-11 md:px-24 lg:px-20 py-5 overflow-y-auto scroll-smooth h-screen sm:pt-3 bg-field dark:bg-dark-notif px-2"
		@scroll="onScroll"
	>
		<div
			class="z-10 crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
		>
			<div class="flex justify-between items-center w-full">
				<div class="w-1/2">
					<div v-if="isEditing" class="relative w-full">
						<input
							v-model="postTitle"
							@blur="handleTitleChange"
							@keyup.enter="handleTitleChange"
							@input="checkForBadWords('title')"
							class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-3xl rounded-lg border-field dark:bg-dark-field p-[.23rem] px-2 w-full ring-1 ring-gray-600 outline-[.5px] outline-none"
							placeholder="POST TITLE"
							autofocus
						/>
						<span
							class="absolute right-1 top-1 mt-1 material-icons-outlined text-field"
						>
							edit_note
						</span>
					</div>
					<h1
						v-else
						@click="isEditing = true"
						class="font-bebas-neue p-[.23rem] text-lg w-full text-prime dark:text-dark-prime sm:text-3xl"
					>
						{{ postTitle }}
					</h1>
				</div>
				<div class="w-1/2 sm:w-1/4 font-montserrat">
					<div class="relative">
						<select
							id="category-option"
							v-model="categoryOption"
							class="appearance-none w-full bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-gray-100 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 pr-8"
						>
							<option value="" disabled selected>
								Select a Category
							</option>
							<option
								v-for="category in categories"
								:key="category"
								:value="category"
							>
								{{ category }}
							</option>
						</select>
						<div
							class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 dark:text-gray-300"
						>
							<ChevronDownIcon class="h-4 w-4" />
						</div>
					</div>
				</div>
			</div>
			<div class="for-content flex flex-col w-full mt-3">
				<div class="flex sm:space-x-2">
					<div class="hidden sm:flex size-14 rounded-full">
						<span
							v-if="!post_profile_display"
							class="flex items-center"
						>
							<svg
								class="animate-spin h-5 w-5 mr-3 dark:text-white"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
							>
								<circle
									class="opacity-25"
									cx="12"
									cy="12"
									r="10"
									stroke="currentColor"
									stroke-width="4"
								></circle>
								<path
									class="opacity-75"
									fill="currentColor"
									d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
								></path>
							</svg>
						</span>
						<img
							v-else
							:src="post_profile_display"
							alt="Profile"
							class="object-cover rounded-full cursor-pointer"
						/>
					</div>
					<textarea
						class="w-full rounded-lg resize-none p-4 outline-none ring-1 ring-gray-600 dark:bg-dark-field dark:text-dark-prime"
						name=""
						id="post-content"
						v-model="postContent"
						@input="checkForBadWords('content')"
						cols="30"
						rows=""
						placeholder="What do you want to share?"
					></textarea>
				</div>
				<div class="mt-4 space-y-4">
					<!-- Image preview -->
					<div v-if="selectedImageUrl" class="relative group">
						<img
							:src="selectedImageUrl"
							alt="Post Image"
							class="w-auto h-28 sm:h-40 object-cover rounded-lg shadow-md transition-all duration-300 group-hover:brightness-75"
						/>
						<button
							@click="removeImage"
							class="absolute top-2 left-2 bg-red-500 text-white p-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
						>
							<XMarkIcon class="h-5 w-5" />
						</button>
					</div>

					<!-- Itinerary preview -->
					<div
						v-if="selectedItinerary"
						class="bg-gray-100 dark:bg-gray-700 rounded-lg p-4 shadow-md"
					>
						<div class="flex items-center justify-between">
							<h3
								class="text-lg font-semibold text-gray-800 dark:text-white truncate"
							>
								{{ selectedItinerary.main_title }}
							</h3>
							<button
								@click="removeItinerary"
								class="text-gray-500 hover:text-red-500 transition-colors duration-200"
							>
								<XMarkIcon class="h-5 w-5" />
							</button>
						</div>
						<p
							class="mt-2 text-sm text-gray-600 dark:text-gray-300 line-clamp-2"
						>
							{{ selectedItinerary.main_description }}
						</p>
					</div>
				</div>
			</div>
			<div
				class="about-country font-montserrat flex my-3 items-center sm:justify-between border-b-2 dark:border-dark-field"
			>
				<p
					class="hidden sm:flex text-sm text-prime dark:text-dark-prime"
				>
					What country is your post about?
				</p>
				<!-- <p
					class="text-sm text-prime dark:text-dark-prime"
				>
					Country
				</p> -->
				<input
					id="country-post"
					v-model="countryPost"
					@input="checkForBadWords('country')"
					type="text"
					ref="autocompletecountry"
					placeholder="Country"
					class="bg-field dark:bg-dark-second-dark dark:text-dark-prime text-xs rounded-full pl-4 sm:ml-2 h-9 w-full sm:w-1/2 outline-none"
				/>

				<div class="hidden sm:flex sm:w-1/5"></div>
			</div>
			<div class="flex my-3 items-center justify-between">
				<div class="flex">
					<label for="imgSelect">
						<span
							class="material-icons-outlined text-second text-3xl cursor-pointer"
							>image</span
						>
					</label>
					<input
						type="file"
						name=""
						id="imgSelect"
						class="hidden"
						@change="handleFileSelection"
					/>
					<span
						class="material-icons-outlined text-second text-3xl pl-2 cursor-pointer"
						@click="addItineraryModal = true"
						>explore</span
					>
				</div>

				<button
					type="submit"
					class="font-montserrat text-base bg-second text-interface p-2 rounded-full w-36 h-8 sm:h-10 hover:bg-second-light cursor-pointer flex items-center justify-center"
					@click.prevent="submitPost"
					:disabled="isPosting"
				>
					<span v-if="!isPosting">Post</span>
					<span v-else class="flex items-center">
						<svg
							class="animate-spin h-5 w-5 mr-3 text-white"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
						>
							<circle
								class="opacity-25"
								cx="12"
								cy="12"
								r="10"
								stroke="currentColor"
								stroke-width="4"
							></circle>
							<path
								class="opacity-75"
								fill="currentColor"
								d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
							></path>
						</svg>
						Posting
					</span>
				</button>
			</div>
		</div>

		<section class="w-full mb-10 sm:mb-0">
			<div>
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
									:src="post.cultura_user.user_photo"
									alt="Profile"
									class="w-full h-full object-cover"
								/>
							</div>
							<div class="flex flex-col space-y-1">
								<div class="flex items-center space-x-2">
									<router-link
										v-if="
											post.author === user.user.username
										"
										:to="{ name: 'profile' }"
										class="font-medium text-xs text-gray-900 dark:text-white hover:underline"
									>
										@{{ post.author }}
									</router-link>
									<span
										v-else
										@click="gotoUser(post.cultura_user)"
										class="font-medium text-xs text-gray-900 dark:text-white cursor-pointer hover:underline"
									>
										@{{ post.author }}
									</span>
									<span
										class="text-sm text-gray-500 dark:text-gray-400"
										>•</span
									>
									<span
										class="text-xs text-gray-500 dark:text-gray-400"
									>
										{{ timesince(post.date_posted) }}
									</span>
								</div>
								<div
									class="text-xs text-gray-500 dark:text-gray-400"
								>
									{{ post.category }} | {{ post.country }}
								</div>
							</div>
						</div>

						<div class="flex items-center">
							<router-link
								:to="{
									name: 'report',
									query: {
										post_id: post._id,
										user_id: auth_user,
									},
								}"
								class="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-full transition-colors duration-200"
							>
								<i
									class="fa-solid fa-circle-exclamation text-gray-400 hover:text-red-500 text-xl"
								></i>
							</router-link>
						</div>
					</div>

					<!-- Title Section -->
					<h1
						class="font-bebas-neue text-2xl font-bold text-second mb-3 leading-4 tracking-wider"
					>
						{{ post.title }}
					</h1>

					<!-- Content Section -->
					<div class="space-y-4">
						<p
							v-if="!post.isEditing"
							class="text-gray-600 dark:text-gray-300 leading-relaxed"
						>
							{{ post.content }}
						</p>

						<textarea
							v-else
							v-model="post.editedContent"
							class="w-full p-4 rounded-lg border border-gray-200 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							rows="4"
						></textarea>

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
										<i
											class="fas fa-search-plus text-4xl"
										></i>
									</span>
								</div>
							</div>
							<div
								v-if="post.itinerary_in_post"
								v-for="itinerary in post.itinerary_in_post"
								:key="itinerary.id"
								class="rounded-xl w-full overflow-hidden border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-200 cursor-pointer"
								@click="goToViewItinerary(itinerary.id)"
							>
								<img
									v-if="itinerary.main_image"
									:src="itinerary.main_image"
									alt=""
									class="w-full h-48 object-cover"
								/>
								<div class="p-4 bg-gray-50 dark:bg-gray-800">
									<h3
										class="text-sm sm:text-xl font-bold text-gray-900 dark:text-white mb-2"
									>
										{{ itinerary.main_title }}
									</h3>
									<p
										class="text-gray-600 dark:text-gray-300 text-sm line-clamp-2"
									>
										{{ itinerary.main_description }}
									</p>
								</div>
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
							<ChatBubbleLeftIcon class="size-4" />
							<span class="text-sm">{{
								post.comments?.length || 0
							}}</span>
						</button>

						<div class="relative group">
							<button
								@click="likePost(post._id)"
								class="flex items-center space-x-1"
								:class="
									post.is_liked
										? 'text-second'
										: 'text-gray-500 hover:text-second'
								"
							>
								<HeartIcon
									v-if="post.is_liked"
									class="size-4"
								/>
								<HeartIcon v-else class="size-4" />
								<span>{{
									formatLikeCount(post.like_count)
								}}</span>
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
				<!-- <div v-if="loading" class="loading">Loading...</div> -->
				<div
					v-if="loading"
					class="loading border border-gray-500 dark:border-blue-300 shadow rounded-md p-4 mb-3 max-w-sm sm:max-w-none w-full mx-auto mt-10"
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
				class="comments-modal fixed z-50 inset-0 overflow-y-auto"
				aria-labelledby="modal-title"
				role="dialog"
				aria-modal="true"
				v-if="showModal"
			>
				<div class="flex min-h-screen items-center justify-center p-4">
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
											<span class="text-gray-500 text-sm"
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
									<div class="flex items-center space-x-2">
										<span class="text-white font-medium">{{
											comment.author
										}}</span>
										<span class="text-gray-500">to</span>
										<span class="text-blue-400">{{
											comment.replied_to
										}}</span>
										<span class="text-gray-500 text-sm">{{
											timesince(comment.date_posted)
										}}</span>
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
									:src="post_profile_display"
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
				v-if="addItineraryModal"
				class="fixed inset-0 z-50 overflow-hidden bg-black/70 backdrop-blur-sm"
				aria-labelledby="modal-title"
				role="dialog"
				aria-modal="true"
			>
				<div class="h-screen px-4 text-center">
					<!-- Background overlay -->
					<div
						class="fixed inset-0 transition-opacity"
						aria-hidden="true"
					></div>

					<!-- Modal panel -->
					<div
						class="inline-block w-full max-w-2xl my-8 text-left align-middle transition-all transform"
					>
						<div
							class="relative bg-white dark:bg-gray-900 rounded-xl shadow-2xl"
						>
							<!-- Header -->
							<div
								class="flex items-center justify-between p-6 border-b border-gray-200 dark:border-gray-800"
							>
								<h2
									class="text-2xl font-bold text-gray-900 dark:text-white"
								>
									Select Itinerary
								</h2>
								<button
									@click="addItineraryModal = false"
									class="p-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
								>
									<span class="sr-only">Close</span>
									<XIcon class="w-6 h-6" />
								</button>
							</div>

							<!-- Create new itinerary button -->
							<div
								class="p-6 border-b border-gray-200 dark:border-gray-800"
							>
								<button
									@click="createNewItinerary"
									class="flex items-center w-full px-4 py-3 text-left text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors group"
								>
									<div
										class="flex items-center justify-center w-10 h-10 rounded-full bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400"
									>
										<PlusIcon class="w-6 h-6" />
									</div>
									<div class="ml-4">
										<p
											class="font-medium text-gray-900 dark:text-white"
										>
											Create New Itinerary
										</p>
										<p
											class="text-sm text-gray-500 dark:text-gray-400"
										>
											Start planning a new travel
											experience
										</p>
									</div>
								</button>
							</div>

							<!-- Itinerary list -->
							<div class="p-6 max-h-[60vh] overflow-y-auto">
								<div
									v-if="itineraries.length === 0"
									class="text-center py-12"
								>
									<DocumentIcon
										class="mx-auto h-12 w-12 text-gray-400"
									/>
									<h3
										class="mt-2 text-lg font-medium text-gray-900 dark:text-white"
									>
										No itineraries
									</h3>
									<p
										class="mt-1 text-sm text-gray-500 dark:text-gray-400"
									>
										Get started by creating a new itinerary
									</p>
								</div>

								<div v-else class="space-y-4">
									<button
										v-for="itinerary in itineraries"
										:key="itinerary.id"
										@click="selectItinerary(itinerary)"
										class="w-full group"
									>
										<div
											class="flex items-start p-4 rounded-lg border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800/50 transition-colors"
											:class="{
												'bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800':
													selectedItinerary?.id ===
													itinerary.id,
											}"
										>
											<!-- Itinerary image -->
											<div class="flex-shrink-0">
												<img
													:src="itinerary.main_image"
													:alt="itinerary.main_title"
													class="w-20 h-20 rounded-lg object-cover"
												/>
											</div>

											<!-- Itinerary details -->
											<div
												class="ml-4 flex-1 flex flex-col items-start justify-start min-w-0"
											>
												<div
													class="flex items-center justify-between w-full"
												>
													<h3
														class="text-xs sm:text-base font-medium text-gray-900 dark:text-white truncate"
														:class="{
															'text-blue-600 dark:text-blue-400':
																selectedItinerary?.id ===
																itinerary.id,
														}"
													>
														{{
															itinerary.main_title
														}}
													</h3>
													<span
														class="text-xs text-gray-500 dark:text-gray-400"
													>
														{{
															formatDate(
																itinerary.date_posted
															)
														}}
													</span>
												</div>
												<p
													class="mt-1 text-sm text-gray-500 dark:text-gray-400 line-clamp-2"
												>
													{{
														itinerary.main_description
													}}
												</p>
												<div
													class="mt-2 flex items-center text-sm text-gray-500 dark:text-gray-400"
												>
													<CurrencyDollarIcon
														class="flex-shrink-0 mr-1.5 h-4 w-4"
													/>
													{{ itinerary.currency }}
													{{
														itinerary.total_budget.toLocaleString()
													}}
													<span class="mx-2">•</span>
													<StarIcon
														class="flex-shrink-0 mr-1.5 h-4 w-4"
													/>
													{{
														calculateAverageRating(
															itinerary.rating
														)
													}}
												</div>
											</div>
										</div>
									</button>
								</div>
							</div>

							<!-- Footer -->
							<div
								class="flex items-center justify-end gap-3 px-6 py-4 border-t border-gray-200 dark:border-gray-800"
							>
								<button
									@click="addItineraryModal = false"
									class="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
								>
									Cancel
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
		<transition
			enter-active-class="transition ease-out duration-300"
			enter-from-class="opacity-0 translate-y-10"
			enter-to-class="opacity-100 translate-y-0"
			leave-active-class="transition ease-in duration-300"
			leave-from-class="opacity-100 translate-y-0"
			leave-to-class="opacity-0 translate-y-10"
		>
			<button
				v-show="showScrollTop"
				@click="scrollToTop"
				class="fixed bottom-5 right-5 bg-second hover:bg-second-light text-white p-2 rounded-full shadow-lg transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-second"
				aria-label="Scroll to top"
			>
				<ChevronUpIcon class="h-6 w-6" />
			</button>
		</transition>
	</div>
	<Snackbar
		:show="showSnackbar"
		:message="snackbarMessage"
		:type="snackbarType"
		@close="showSnackbar = false"
	/>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useDark, useToggle } from "@vueuse/core";
import axios from "axios";
import axiosClient from "../axios";
import moment from "moment";
import { clean } from "profanity-cleaner";
import { XIcon, ThumbsUpIcon } from "lucide-vue-next";
import {
	ChatBubbleLeftIcon,
	HeartIcon,
	PencilSquareIcon,
	XMarkIcon,
	CheckIcon,
	PhotoIcon,
	FaceSmileIcon,
	PaperAirplaneIcon,
	ArrowLeftIcon,
	ChevronDownIcon,
	ChevronUpIcon,
} from "@heroicons/vue/24/solid";

import {
	PlusIcon,
	DocumentIcon,
	CurrencyDollarIcon,
	StarIcon,
} from "@heroicons/vue/24/outline";

import filipinoBadWords from "../custom-badwords";

const store = useStore();
const router = useRouter();
const isDark = useDark();
const toggleDark = useToggle(isDark);
const user = computed(() => store.state.user.data);

const posts = computed(() => store.getters.getPosts); // Reactive array to store posts
const post_profile_display = ref(null);
const selectedImageUrl = ref(null);
const picture = ref(null);
const auth_user = ref(0);
const isEditing = ref(true);
const postTitle = ref("");
const addItineraryModal = ref(false);
const showModal = ref(false);
const categoryOption = ref("");
const categories = [
	"Food",
	"Traditions",
	"History",
	"Art",
	"Music",
	"Literature",
	"Fashion",
	"Festivals",
	"Language",
	"Architecture",
	"Sports",
	"Religion",
	"Mythology",
	"Crafts",
	"Dance",
	"Cinema",
	"Technology",
	"Education",
	"Cuisine",
	"Folklore",
];
const postContent = ref("");
const countryPost = ref("");
const selectedPost = ref([]);
const reply = ref("");
const replied_to = ref("");
const post_id = ref("");
const comments_in_post = ref([]);
const itineraries = ref([]);
const selectedItinerary = ref(null);
const id_of_selected = ref("");
const isFullTextShown = ref({});

const showImageModal = ref(false);
const modalImage = ref("");

import Snackbar from "./snackbars/Snackbar.vue";
const hasBadWords = ref({
	title: false,
	content: false,
	country: false,
});

const englishBadWords = [
	"fuck",
	"shit",
	"ass",
	"bitch",
	"cunt",
	"damn",
	"hell",
	"whore",
	"dick",
	"piss",
	"pussy",
	"slut",
	// Add more English bad words as needed
];

const allBadWords = [...filipinoBadWords, ...englishBadWords];
// Snackbar state
const showSnackbar = ref(false);
const snackbarMessage = ref("");
const snackbarType = ref("error");
const showMessage = (message, type = "error") => {
	snackbarMessage.value = message;
	snackbarType.value = type;
	showSnackbar.value = true;
	setTimeout(() => {
		showSnackbar.value = false;
	}, 5000); // Hide after 5 seconds
};

const checkForBadWords = (field) => {
	const text =
		field === "title"
			? postTitle.value
			: field === "content"
			? postContent.value
			: countryPost.value;

	const words = text.toLowerCase().split(/\s+/);
	const hasBad = words.some((word) => allBadWords.includes(word));

	hasBadWords.value[field] = hasBad;

	if (hasBad) {
		// showSnackbar.value = true;
		// snackbarMessage.value = `Please remove inappropriate language from the ${field}.`;
		showMessage(
			`Please remove inappropriate language from the ${field}.`,
			"error"
		);
	}
};
const isPostInvalid = computed(() => {
	return (
		hasBadWords.value.title ||
		hasBadWords.value.content ||
		hasBadWords.value.country ||
		!categoryOption.value ||
		!postTitle.value ||
		postTitle.value.toLowerCase == "post title" ||
		!postContent.value ||
		!countryPost.value
	);
});
// functions for image modal
const openImageModal = (imageUrl) => {
	modalImage.value = imageUrl;
	showImageModal.value = true;
};

const closeImageModal = () => {
	showImageModal.value = false;
};

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleDateString("en-US", {
		year: "numeric",
		month: "short",
		day: "numeric",
	});
};

const calculateAverageRating = (ratings) => {
	if (!ratings || ratings.length === 0) return "No ratings";
	const validRatings = ratings.filter((r) => r.rating && r.user_id);
	if (validRatings.length === 0) return "No ratings";

	const average =
		validRatings.reduce((acc, curr) => acc + curr.rating, 0) /
		validRatings.length;
	return average.toFixed(1);
};

const createNewItinerary = () => {
	addItineraryModal.value = false;
	router.push({ name: "create-itinerary" });
};

const confirmSelection = () => {
	if (selectedItinerary.value) {
		// Emit selected itinerary to parent component
		addItineraryModal.value = false;
	}
};

const fetchUser = async () => {
	try {
		const res = await store.dispatch("fetchUserData");

		post_profile_display.value = res.profile?.user_photo;
		auth_user.value = res.user.id;
	} catch (error) {
		console.error("Error fetching user:", error);
	}
};

// const displayedPosts = ref([]);
// const postsPerPage = 5;
// const currentPage = ref(1);

const hasMorePosts = computed(() => {
	return displayedPosts.value.length < posts.value.length;
});
const page = ref(1); // Current page number
const perPage = 5; // Items per page
const loading = ref(false); // Loading state
const hasMore = ref(true); // Whether more data is available

// Fetch posts from the API
const fetchPosts = async () => {
	if (!hasMore.value || loading.value) return; // Avoid multiple calls

	loading.value = true;
	try {
		const morePosts = await store.dispatch("fetchPosts", {
			page: page.value,
			perPage,
		});
		console.log("MORE POSTS : ", store.getters.getPosts);

		if (!morePosts) {
			hasMore.value = false; // No more data available
		}
		page.value++;
	} catch (error) {
		console.error("Error fetching posts:", error);
	} finally {
		loading.value = false;
	}
};

// Handle scroll event
const onScroll = (event) => {
	const container = event.target;
	if (
		container.scrollTop + container.clientHeight >=
		container.scrollHeight - 10
	) {
		fetchPosts(); // Load more data when scrolled to the bottom
	}
};
const updateDisplayedPosts = () => {
	const start = 0;
	const end = currentPage.value * postsPerPage;
	displayedPosts.value = posts.value.slice(start, end);
};

const loadMorePosts = () => {
	currentPage.value++;
	updateDisplayedPosts();
};

const formatLikeCount = (count) => {
	return count >= 1000 ? (count / 1000).toFixed(1) + "k" : count;
};
const handleFileSelection = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		picture.value = file;
	}
};

const handleTitleChange = () => {
	if (postTitle.value.trim() === "") {
		isEditing.value = true;
	} else {
		isEditing.value = false;
	}
};

const initializeAutocompleteCountry = () => {
	const inputElement = document.getElementById("country-post");
	if (
		inputElement &&
		window.google &&
		window.google.maps &&
		window.google.maps.places
	) {
		const autocomplete = new google.maps.places.Autocomplete(inputElement, {
			types: ["(regions)"],
		});
		autocomplete.addListener("place_changed", () => {
			const place = autocomplete.getPlace();
			if (place && place.formatted_address) {
				countryPost.value = place.formatted_address;
			}
		});
	}
};

const timesince = (date) => {
	return moment(date).fromNow();
};

const likePost = async (postId) => {
	try {
		await store.dispatch("likePost", postId);
		await fetchPosts();
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
const isPosting = ref(false);
const submitPost = async () => {
	if (isPostInvalid.value) {
		showMessage(`Please fill all fields correctly.`, "error");
	} else {
		const formData = new FormData();
		formData.append("title", postTitle.value);
		formData.append("category", categoryOption.value);
		formData.append("body", postContent.value);
		formData.append("country", countryPost.value);
		if (id_of_selected.value) {
			formData.append("itinerary_id", id_of_selected.value);
		}
		if (picture.value instanceof File) {
			formData.append("image", picture.value, picture.value.name);
		}
		isPosting.value = true;

		try {
			await axiosClient.post("/posting", formData, {
				headers: { "Content-Type": "multipart/form-data" },
			});
			postTitle.value = "POST TITLE";
			categoryOption.value = "";
			postContent.value = "";
			countryPost.value = "";
			selectedImageUrl.value = null;
			picture.value = null;
			selectedItinerary.value = null;
			id_of_selected.value = "";
			await fetchPosts();
		} catch (error) {
			console.error("Error submitting post:", error);
		} finally {
			isPosting.value = false;
		}
	}
};
const removeImage = () => {
	selectedImageUrl.value = null;
	// Reset the file input if needed
	if (document.getElementById("imgSelect")) {
		document.getElementById("imgSelect").value = "";
	}
};
const removeItinerary = () => {
	id_of_selected.value = "";
	selectedItinerary.value = null;
};

const submitReply = async () => {
	try {
		await axiosClient.post("/commenting", {
			post_id: post_id.value,
			replied_to: replied_to.value,
			body: reply.value,
		});
		reply.value = "";
		await fetchPosts();
		const updatedPost = posts.value.find((p) => p._id === post_id.value);
		if (updatedPost) {
			comments_in_post.value = updatedPost.comments || [];
		}
	} catch (error) {
		console.error("Error submitting reply:", error);
	}
};

const fetchSavedItineraries = async () => {
	try {
		await store.dispatch("fetchItineraries");
		itineraries.value = store.getters.getItineraries;
		// console.log("ITINERARIES: ", itineraries.value);
	} catch (error) {
		console.error("Error fetching saved itineraries:", error);
	}
};

const selectItinerary = (itinerary) => {
	selectedItinerary.value = itinerary;
	id_of_selected.value = itinerary.id;
	addItineraryModal.value = false;
};

const goToViewItinerary = (itineraryId) => {
	router.push({ name: "view-itinerary", query: { id: itineraryId } });
};

const toggleEdit = (post) => {
	if (post.isEditing) {
		post.content = post.editedContent;
		if (post.previewImage) {
			post.image = post.previewImage;
		}
	} else {
		post.editedContent = post.content;
		post.previewImage = post.image;
	}
	post.isEditing = !post.isEditing;
};

const handleImageUpload = (event, post) => {
	const file = event.target.files[0];
	if (file) {
		const reader = new FileReader();
		reader.onload = (e) => {
			post.previewImage = e.target.result;
		};
		reader.readAsDataURL(file);
	}
};
const showScrollTop = ref(false);

const checkScroll = () => {
	showScrollTop.value = window.scrollY > 100;
};

const scrollToTop = () => {
	window.scrollTo({
		top: 0,
		behavior: "smooth",
	});
};

// onMounted(() => {});

onUnmounted(() => {
	window.removeEventListener("scroll", checkScroll);
});
onMounted(async () => {
	window.addEventListener("scroll", checkScroll);
	nextTick(() => {
		checkScroll(); // Check scroll position after initial render
	});
	await fetchUser();
	await fetchPosts();
	await fetchSavedItineraries();
	initializeAutocompleteCountry();
	setInterval(fetchSavedItineraries, 5000);
});
</script>

<style scoped>
/* Add any scoped styles here if needed */
</style>
