import { createStore } from "vuex";
import axiosClient from "./axios";
import { clean } from "profanity-cleaner";
import filipinoBadWords from "./custom-badwords";

const store = createStore({
	state: {
		user: {
			data: {},
			token: sessionStorage.getItem("TOKEN"),
			is_admin: null,
		},
		surveys: [],

		otpData: null,
		unreadCount: 0,
		searchResults: [],
		posts: [],
		postIds: new Set(),
		itineraries: [],
		itineraryIds: new Set(), // Track itinerary IDs to avoid duplicates

		itineraryDetails: {},
		likeNotifications: [],
		followNotifications: [],
		viewed_user: null,
		admin: {
			reports: [],
			report: null,

			culturaUsers: [],
			culturaUser: null,
		},

		list_itineraries: [],
		editingItinerary: null,
		showModal: false,
		showDeleteConfirmation: false,
	},
	getters: {
		// getItineraries: (state) => state.itineraries,

		surveys: (state) => state.surveys,

		singleCulturaUser: (state) => state.viewed_user,
		isAdmin(state) {
			return state.user.is_admin;
		},
		isAuthenticated: (state) => !!state.user.token,
		currentUser: (state) => state.user.data,
		getUser(state) {
			return state.user;
		},
		getPosts(state) {
			return state.posts;
		},
		getItineraries(state) {
			return state.itineraries;
		},

		getItineraryDetails(state) {
			return state.itineraryDetails;
		},

		getUnreadCount(state) {
			return state.unreadCount;
		},
		hasOtp: (state) => !!state.otpData,
		getSearchResults(state) {
			return state.searchResults;
		},
		getLikeNotifications: (state) => state.likeNotifications,
		getFollowNotifications: (state) => state.followNotifications,
		getTotalUnreadNotificationsCount(state) {
			const likeUnreadCount = state.likeNotifications.filter(
				(n) => !n.is_read
			).length;
			const followUnreadCount = state.followNotifications.filter(
				(n) => !n.is_read
			).length;
			return likeUnreadCount + followUnreadCount;
		},
	},
	mutations: {
		updatePostLikes(state, { postId, newIsLiked, newLikeCount, newLikes }) {
			const postIndex = state.posts.findIndex(
				(post) => post._id === postId
			);
			if (postIndex !== -1) {
				state.posts[postIndex] = {
					...state.posts[postIndex],
					is_liked: newIsLiked,
					like_count: newLikeCount,
					likes: newLikes,
				};
			}
		},
		SET_SURVEYS(state, surveys) {
			state.surveys = surveys;
		},
		SET_CULTURAUSER(state, culturauser) {
			state.viewed_user = culturauser;
		},
		setReports(state, reports) {
			state.admin.reports = reports;
		},
		setReport(state, report) {
			state.admin.report = report;
		},
		setCulturaUsers(state, users) {
			state.admin.culturaUsers = users;
		},
		setCulturaUser(state, user) {
			state.admin.culturaUser = user;
		},

		setUser(state, userData) {
			state.user.data = userData.profile;
			state.user.token = userData.token;
			state.user.is_admin = userData.profile?.is_admin;

			sessionStorage.setItem("TOKEN", userData.token);
		},

		setPosts(state, posts) {
			state.posts = posts;
			state.postIds = new Set(posts.map((post) => post._id));
		},
		appendPosts(state, posts) {
			posts.forEach((post) => {
				if (!state.postIds.has(post._id)) {
					state.posts.push(post);
					state.postIds.add(post._id);
				}
			});
		},

		setItineraries(state, itineraries) {
			state.itineraries = itineraries;
			state.itineraryIds = new Set(
				itineraries.map((itinerary) => itinerary.id)
			);
		},
		appendItineraries(state, itineraries) {
			itineraries.forEach((itinerary) => {
				if (!state.itineraryIds.has(itinerary.id)) {
					state.itineraries.push(itinerary);
					state.itineraryIds.add(itinerary.id);
				}
			});
		},
		setItineraryDetails(state, itineraryDetails) {
			state.itineraryDetails = itineraryDetails;
		},
		setSearchResults(state, results) {
			state.searchResults = results;
		},

		setOtpData(state, otpData) {
			state.otpData = otpData;
		},
		logout(state) {
			state.user.token = "";
			state.user.data = {};
			sessionStorage.removeItem("TOKEN");
		},
		SET_UNREAD_COUNT(state, count) {
			state.unreadCount = count;
		},
		SET_SEARCH_RESULTS(state, results) {
			state.searchResults = results;
		},
		setLikeNotifications(state, notifications) {
			state.likeNotifications = notifications;
		},
		setFollowNotifications(state, notifications) {
			state.followNotifications = notifications;
		},
		SET_LIKE_NOTIFICATIONS(state, notifications) {
			state.likeNotifications = notifications;
		},
		SET_FOLLOW_NOTIFICATIONS(state, notifications) {
			state.followNotifications = notifications;
		},
		UPDATE_NOTIFICATION_READ_STATUS(
			state,
			{ notificationType, notificationId, isRead }
		) {
			const notifications =
				notificationType === "like"
					? state.likeNotifications
					: state.followNotifications;
			const notification = notifications.find(
				(n) => n.id === notificationId || n._id === notificationId
			);
			if (notification) {
				notification.is_read = isRead;
			}
		},

		SET_ITINERARIES(state, itineraries) {
			state.list_itineraries = itineraries;
		},
		SET_EDITING_ITINERARY(state, itinerary) {
			state.editingItinerary = itinerary;
		},
		TOGGLE_MODAL(state, value) {
			state.showModal = value;
		},
		TOGGLE_DELETE_CONFIRMATION(state, value) {
			state.showDeleteConfirmation = value;
		},
		REMOVE_ITINERARY(state, id) {
			state.list_itineraries = state.list_itineraries.filter(
				(itinerary) => itinerary.id !== id
			);
		},
		UPDATE_ITINERARY(state, updatedItinerary) {
			const index = state.list_itineraries.findIndex(
				(itinerary) => itinerary.id === updatedItinerary.id
			);
			if (index !== -1) {
				state.list_itineraries[index] = updatedItinerary;
			}
		},
	},
	actions: {
		// ADMIN  USER    MANAGEMENT
		async fetchCulturaUsers({ commit, state }) {
			return axiosClient
				.get("culturausers/all", {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setCulturaUsers", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error("Error fetching CulturaUsers:", error);
				});
		},
		async fetchCulturaUser({ commit, state }, id) {
			return axiosClient
				.get(`culturauser/${id}/`, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					// commit("setCulturaUser", response.data);

					return response.data;
				})
				.catch((error) => {
					console.error("Error fetching CulturaUser:", error);
				});
		},
		async viewCulturaUser({ commit }, id) {
			try {
				const response = await axiosClient.get(`/view_user/${id}/`);

				commit("SET_CULTURAUSER", response.data);
				return response.data;
			} catch (error) {
				console.error("Error fetching culturauser:", error);
			}
		},
		async updatePrivacy({ commit }, is_private) {
			try {
				const response = await axiosClient.put(
					"/user/update-privacy/",
					{ is_private }
				);

				return response.data;
			} catch (error) {
				console.error("Error updating privacy:", error);
			}
		},
		async fetchPublicProfilePosts({ commit }, userID) {
			try {
				const response = await axiosClient.get(
					"/public-profile-posts/",
					{
						params: {
							user_id: userID,
						},
					}
				);
				// console.log("POSTS::", response.data);
				return response.data;
				// commit("SET_POSTS", response.data.reverse());
			} catch (error) {
				console.error("Error fetching posts:", error);
			}
		},
		async createCulturaUser({ commit, state }, userData) {
			return axiosClient
				.post("culturausers/", userData, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setCulturaUser", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error("Error creating CulturaUser:", error);
					throw error;
				});
		},
		async updateCulturaUser({ commit, state }, { id, userData }) {
			return axiosClient
				.put(`culturausers/${id}/`, userData, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setCulturaUser", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error("Error updating CulturaUser:", error);
					throw error;
				});
		},
		async deleteCulturaUser({ commit, state }, id) {
			return axiosClient
				.delete(`culturauser/${id}/`, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then(() => {
					// commit("setCulturaUser", null);
				})
				.catch((error) => {
					console.error("Error deleting CulturaUser:", error);
					throw error;
				});
		},
		// Reports
		async fetchReports({ commit, state }) {
			return axiosClient
				.get("reports/", {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setReports", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async fetchReport({ commit, state }, id) {
			return axiosClient
				.get(`/reports/${id}/`, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setReport", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async createReport({ commit, state }, reportData) {
			return axiosClient
				.post("reports/", reportData, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setReport", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},
		async warnReport(
			{ commit, state },
			{ id, post_id, mark_as_warned, mark_as_reported }
		) {
			return axiosClient
				.put(
					`/reports/${id}/`,
					{
						post_id: post_id,
						mark_as_warned,
						mark_as_reported,
					},
					{
						headers: { Authorization: `Token ${state.user.token}` },
					}
				)
				.then((response) => {
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},
		async updateReport({ commit, state }, { id }) {
			return axiosClient
				.delete(`/reports/${id}/`, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async deleteReport({ commit, state }, id) {
			return axiosClient
				.delete(`/reports/${id}/`, {
					headers: { Authorization: `Token ${state.user.token}` },
				})
				.then((response) => {
					commit("setReport", null);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		// Notifications

		async fetchLikeNotifications({ commit }) {
			try {
				const response = await axiosClient.get(
					"/like-notification-list"
				);
				commit("SET_LIKE_NOTIFICATIONS", response.data);
			} catch (error) {
				console.error("Error fetching like notifications:", error);
				throw error;
			}
		},
		async fetchFollowNotifications({ commit }) {
			try {
				const response = await axiosClient.get(
					"/follow-notification-list"
				);
				commit("SET_FOLLOW_NOTIFICATIONS", response.data);
			} catch (error) {
				console.error("Error fetching follow notifications:", error);
				throw error;
			}
		},
		async updateNotificationReadStatus(
			{ commit },
			{ notificationType, notificationId, isRead }
		) {
			try {
				// Assuming your API endpoint is something like this:
				await axiosClient.post("/update-notification-status", {
					notification_type: notificationType,
					notification_id: notificationId,
					is_read: isRead,
				});
				commit("UPDATE_NOTIFICATION_READ_STATUS", {
					notificationType,
					notificationId,
					isRead,
				});
			} catch (error) {
				console.error("Error updating notification status:", error);
				throw error;
			}
		},
		async markAllNotificationsAsRead({ commit }) {
			try {
				const response = await axiosClient.post(
					"/mark-all-notifications-read/"
				);
				console.log("Notifications marked as read:", response.data);
			} catch (error) {
				console.error(
					"Error marking all notifications as read:",
					error
				);
			}
		},
		//
		// Survey
		async fetchSurveys({ commit, state }) {
			// commit("SET_LOADING", true);
			try {
				const response = await axiosClient.get("/surveys", {
					headers: {
						Authorization: `Token ${state.user.token}`,
					},
				});
				commit("SET_SURVEYS", response.data);
				return response.data;
			} catch (error) {
				console.log("Survey Error", error);
			}
		},
		// dashboards actions
		//
		async fetchPosts({ commit, state }, { page = 1, perPage = 5 }) {
			try {
				const response = await axiosClient.get(
					`/posts-list?page=${page}&page_size=${perPage}`
				);

				const cleanedPosts = response.data.results.map((post) => {
					return {
						...post,
						title: clean(post.title, {
							customMatch: (word) => word.length % 2 !== 0,
							customBadWords: filipinoBadWords,
						}),
						content: clean(post.content, {
							customMatch: (word) => word.length % 2 !== 0,
							customBadWords: filipinoBadWords,
						}),
					};
				});
				// commit("setPosts", cleanedPosts);
				commit("appendPosts", cleanedPosts);
				return response.data !== null; // Return whether there are more posts to load
			} catch (error) {
				// console.error("Error fetching posts:", error);
				return false;
			}
		},
		async fetchItineraries({ commit, state }, { page = 1, perPage = 10 }) {
			try {
				const response = await axiosClient.get(
					`/saved-itinerary?page=${page}&page_size=${perPage}`
				);
				// console.log("ITINERARIES::", response.data);

				const cleanedItineraries = response.data.results.map(
					(itinerary) => {
						return {
							...itinerary,
							main_title: clean(itinerary.main_title, {
								customMatch: (word) => word.length % 2 !== 0,
								customBadWords: filipinoBadWords,
							}),
							main_description: clean(
								itinerary.main_description,
								{
									customMatch: (word) =>
										word.length % 2 !== 0,
									customBadWords: filipinoBadWords,
								}
							),
						};
					}
				);

				commit("appendItineraries", cleanedItineraries);
				return response.data.next !== null; // Return whether there are more itineraries to load
			} catch (error) {
				console.error("Error fetching itineraries:", error);
				return false;
			}
		},
		async updateItineraryDetails({ commit, state }, { id, data }) {
			try {
				const response = await axiosClient.put(
					`/update/${id}/itinerary`,
					data
				);
				// commit("SET_ITINERARY_DETAILS", response.data);
				return response.data;
			} catch (error) {
				console.error("Error updating itinerary details:", error);
			}
		},
		async deleteItinerary({ commit, state }, { id, viewed_it_id = 0 }) {
			try {
				const response = await axiosClient.delete(
					`/delete-itinerary/${id}/${viewed_it_id}`,
					{
						headers: {
							Authorization: `Token ${state.user.token}`,
						},
					}
				);
				commit("REMOVE_ITINERARY", id);
				return response.data;
			} catch (error) {
				console.error("Error deleting itinerary:", error);
			}
		},
		async submitItinerary({ commit, state }, { formData, itineraryId }) {
			const url = itineraryId
				? `/itinerary-stop/${itineraryId}`
				: "/create-itinerary";
			const method = itineraryId ? "put" : "post";

			try {
				const response = await axiosClient[method](url, formData, {
					headers: {
						Authorization: `Token ${state.user.token}`,
					},
				});

				return response.data;
			} catch (error) {
				console.error("Error submitting itinerary:", error);
			}
		},
		async saveMainItinerary({ commit, state }, formData) {
			try {
				const response = await axiosClient.post(
					"/save-itinerary",
					formData,
					{
						headers: {
							Authorization: `Token ${state.user.token}`,
							"Content-Type": "multipart/form-data",
						},
					}
				);
				// Reset form fields and navigate to itinerary page
				return response.data;
			} catch (error) {
				console.error("Error saving itinerary:", error);
			}
		},
		async updateSavedItinerary(
			{ commit, state },
			{ id, id_in_saved_itinerary }
		) {
			try {
				const response = await axiosClient.put(
					`/update-save-itinerary/${id}/saved-itinerary/${id_in_saved_itinerary}/`,

					{
						headers: {
							Authorization: `Token ${state.user.token}`,
						},
					}
				);
				// Reset form fields and navigate to itinerary page
				return response.data;
			} catch (error) {
				console.error("Error saving itinerary:", error);
			}
		},
		async fetchSavedItineraries({ commit, state }, itineraryId) {
			try {
				if (!itineraryId) {
					throw new Error("Itinerary ID is required");
				}

				const response = await axiosClient.get(
					`/viewing-itinerary/${itineraryId}`,
					{ headers: { Authorization: `Token ${state.user.token}` } }
				);
				const itineraries = response.data;

				// if (itineraries.length > 0) {
				// 	const itinerary = itineraries[0];
				// 	const itineraryDetails = {
				// 		creator_name: itinerary.creator_name,
				// 		user_photo: itinerary.user_photo,
				// 		date_posted: itinerary.date_posted,
				// 		gen_tips: itinerary.gen_tips,
				// 		id: itinerary.id,
				// 		main_description: itinerary.main_description,
				// 		main_image: itinerary.main_image,
				// 		main_title: itinerary.main_title,
				// 		owner: itinerary.owner,
				// 		status: itinerary.status,
				// 		currency: itinerary.currency,
				// 		total_budget: itinerary.total_budget,
				// 		list_itineraries: itinerary.itineraries,
				// 		allRatings: itinerary.rating.map((item) => item.rating),
				// 		paragraphs: itinerary.gen_tips.split(/\n+/),
				// 	};

				// 	commit("setItineraryDetails", itineraryDetails);
				// }

				return response.data;
			} catch (error) {
				console.error("Error fetching saved itineraries:", error);
			}
		},
		async likePost({ commit, state }, postId) {
			try {
				const response = await axiosClient.post(
					`/like-posts/${postId}/like_post/`,
					null,
					{}
				);

				return response.data;
			} catch (error) {
				console.error("Error liking the post:", error);
			}
		},
		async submitReply({ state }, replyData) {
			try {
				await axiosClient.post("/commenting", replyData, {});
			} catch (error) {
				console.error("Error submitting reply:", error);
			}
		},
		async deleteComment({ commit, state }, { _id, audience }) {
			try {
				const response = await axiosClient.delete(
					`/delete/${_id}/comment`,
					{
						params: {
							audience: audience,
						},
						headers: {
							Authorization: `Token ${state.user.token}`,
						},
					}
				);
				return response.data;
			} catch (error) {
				console.error("Error deleting comment:", error);
			}
		},
		async submitPost({ state }, formData) {
			try {
				await axiosClient.post("/posting", formData, {});
			} catch (error) {
				console.error("Error submitting post:", error);
			}
		},

		async sendForgotPasswordOTP({ commit }, email) {
			return axiosClient
				.post("/fp-otp", { email })
				.then((response) => {
					commit("setOtpData", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},
		async sendOtp({ commit }, { email, username }) {
			return axiosClient
				.post("/send-otp", { email, username })
				.then((response) => {
					commit("setOtpData", response.data.otp);
					return response.data;
				})
				.catch((error) => {
					console.error("Error sending OTP:", error);
					throw error;
				});
		},

		async verifyRegistrationOTP({ commit }, otp) {
			return axiosClient
				.post("/verify-registration-otp", { otp })
				.then((response) => {
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async verifyForgotPasswordOTP({ commit, state }, { email, otp }) {
			// console.log("OTP DATA:", otp, email);

			return axiosClient
				.post("/fp-otp", {
					otp,
					email: email, // Assuming we stored the email when sending OTP
				})
				.then((response) => {
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async changePassword({ commit }, { email, password }) {
			return axiosClient
				.post("/fp-change", { email, password })
				.then((response) => {
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async register({ commit }, userData) {
			return axiosClient
				.post("/registration", userData)
				.then((response) => {
					commit("setUser", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async login({ commit }, credentials) {
			return axiosClient
				.post("/login", credentials)
				.then((response) => {
					// console.log("setUser", response.data);
					commit("setUser", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async fetchUserData({ commit, state }) {
			return axiosClient
				.get("/user", {
					headers: {
						Authorization: `Token ${state.user.token}`,
					},
				})
				.then((response) => {
					commit("setUser", response.data);
					state.user.is_admin = response.data.profile.is_admin;
					return response.data;
				})
				.catch((error) => {
					console.error("Error fetching user data:", error);
					throw error;
				});
		},

		async logout({ commit, state }) {
			// console.log("Logging out user with token:", state.user.token);
			try {
				const response = await axiosClient.post(
					"/logout",

					{
						headers: { Authorization: `Token ${state.user.token}` },
					}
				);
				commit("logout");
				return response;
			} catch (error) {
				throw error;
			}
		},
		async search({ commit }, query) {
			return axiosClient
				.get("search", {
					params: {
						title: query,
					},
					headers: {
						Authorization:
							"Bearer " + sessionStorage.getItem("TOKEN"),
					},
				})
				.then((response) => {
					commit("SET_SEARCH_RESULTS", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error("Error searching:", error);
					throw error;
				});
		},
	},
});

export default store;
