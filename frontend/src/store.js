import { createStore } from "vuex";

export default createStore({
	state: {
		otp: null,
	},
	mutations: {
		setOtp(state, otp) {
			state.otp = otp;
		},
	},
	actions: {
		saveOtp({ commit }, otp) {
			commit("setOtp", otp);
		},
	},
});
