import axios from "axios";
import store from "./store";

const axiosClient = axios.create({
	baseURL: "http://127.0.0.1:8000/api",
	xsrfCookieName: "csrftoken",
	timeout: 5000,
	withCredentials: true,
	xsrfHeaderName: "X-Csrftoken",

	headers: {
		"Content-Type": "application/json",
	},
});

axiosClient.interceptors.request.use(
	(config) => {
		const token = sessionStorage.getItem("TOKEN");
		if (
			token &&
			!config.url.includes("/send-otp") &&
			!config.url.includes("/registration") &&
			!config.url.includes("/login")
		) {
			config.headers.Authorization = `Token ${token}`;
		}
		return config;
	},
	(error) => {
		return Promise.reject(error);
	}
);

export default axiosClient;
