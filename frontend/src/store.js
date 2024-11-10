import { createStore } from "vuex";
import axiosClient from "./axios";
import { clean } from "profanity-cleaner";
import filipinoBadWords from "./custom-badwords";

const store = createStore({
	state: {
		user: {
			data: {},
			token: sessionStorage.getItem("TOKEN"),
		},
		otpData: null,
		unreadCount: 0,
		searchResults: [],
		posts: [],
		itineraries: [],
		itineraryDetails: {},
	},
	getters: {
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
		getLikeNotifications(state) {
			return state.likeNotifications;
		},
		getFollowNotifications(state) {
			return state.followNotifications;
		},
	},
	mutations: {
		setUser(state, userData) {
			state.user.data = userData.user;
			state.user.token = userData.token;
			sessionStorage.setItem("TOKEN", userData.token);
		},

		setPosts(state, posts) {
			state.posts = posts;
		},
		setItineraries(state, itineraries) {
			state.itineraries = itineraries;
		},
		setItineraryDetails(state, itineraryDetails) {
			state.itineraryDetails = itineraryDetails;
		},

		setOtpData(state, otpData) {
			state.otpData = otpData;
		},
		logout(state) {
			state.user.data = {};
			state.user.token = null;
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
	},
	actions: {
		// Notifications
		//
		async fetchLikeNotifications({ commit }) {
			try {
				const response = await axiosClient.get(
					"/like-notification-list"
				);
				commit("setLikeNotifications", response.data);
			} catch (error) {
				console.error("Error fetching like notifications:", error);
			}
		},
		async fetchFollowNotifications({ commit }) {
			try {
				const response = await axiosClient.get(
					"/follow-notification-list"
				);
				commit("setFollowNotifications", response.data);
			} catch (error) {
				console.error("Error fetching follow notifications:", error);
			}
		},
		// dashboards actions
		//
		async fetchPosts({ commit, state }) {
			try {
				const response = await axiosClient.get("/posts-list", {});
				const cleanedPosts = response.data.reverse().map((post) => {
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
				commit("setPosts", cleanedPosts);
			} catch (error) {
				console.error("Error fetching posts:", error);
			}
		},
		async fetchItineraries({ commit, state }) {
			try {
				const response = await axiosClient.get("/saved-itinerary", {});
				commit("setItineraries", response.data);
			} catch (error) {
				console.error("Error fetching itineraries:", error);
			}
		},
		async fetchSavedItineraries({ commit, state }, itineraryId) {
			try {
				if (!itineraryId) {
					throw new Error("Itinerary ID is required");
				}

				const response = await axiosClient.get(
					`/viewing-itinerary/${itineraryId}`,
					{}
				);
				const itineraries = response.data;

				if (itineraries.length > 0) {
					const itinerary = itineraries[0];
					const itineraryDetails = {
						creator_name: itinerary.creator_name,
						user_photo: itinerary.user_photo,
						date_posted: itinerary.date_posted,
						gen_tips: itinerary.gen_tips,
						id: itinerary.id,
						main_description: itinerary.main_description,
						main_image: itinerary.main_image,
						main_title: itinerary.main_title,
						owner: itinerary.owner,
						status: itinerary.status,
						currency: itinerary.currency,
						total_budget: itinerary.total_budget,
						list_itineraries: itinerary.itineraries,
						allRatings: itinerary.rating.map((item) => item.rating),
						paragraphs: itinerary.gen_tips.split(/\n+/),
					};

					commit("setItineraryDetails", itineraryDetails);
				}

				console.log("ITINERARIES", itineraries);
			} catch (error) {
				console.error("Error fetching saved itineraries:", error);
			}
		},
		async likePost({ state }, post_id) {
			try {
				await axiosClient.post(
					`/like-posts/${post_id}/like_post/`,
					null,
					{}
				);
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
		async submitPost({ state }, formData) {
			try {
				await axiosClient.post("/posting", formData, {});
			} catch (error) {
				console.error("Error submitting post:", error);
			}
		},

		async fetchLikenotification({ commit, state }) {
			return axiosClient
				.get("like-notification-list", {})
				.then((response) => {
					commit("SET_UNREAD_COUNT", response.data.unreadCount);
					return response.data;
				})
				.catch((error) => {
					console.error("Error fetching notifications:", error);
					throw error;
				});
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

		async verifyForgotPasswordOTP({ commit, state }, otp) {
			return axiosClient
				.post("/verify-fp-otp", {
					otp,
					email: state.otpData.email, // Assuming we stored the email when sending OTP
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
					console.log("setUser", response.data);
					commit("setUser", response.data);
					return response.data;
				})
				.catch((error) => {
					console.error(error);
					throw error;
				});
		},

		async fetchUserData({ commit, state }) {
			if (state.user.token) {
				return axiosClient
					.get("/user", {})
					.then((response) => {
						return response.data;
					})
					.catch((error) => {
						console.error("Error fetching user data:", error);
						throw error;
					});
			}
		},

		async logout({ commit, state }) {
			console.log("", state.user.token);
			return axiosClient
				.post("/logout", {})
				.then(() => {
					commit("logout");
				})
				.catch((error) => {
					console.log("Error logging out:", error);
					console.error(error);
					throw error;
				});
		},
		async search({ commit }, query) {
			return axiosClient
				.get("search", {
					params: {
						title: query,
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
