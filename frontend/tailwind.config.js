/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: ["class"],
	content: ["./index.html", "./src/**/*.{html,vue,js,ts,jsx,tsx}"],
	theme: {
		extend: {
			screens: {
				xs: "412px",
			},
			colors: {
				interface: "#F7F7F7",
				prime: "#1A193F",
				second: "#6A7FDB",
				field: "#D1D0D0",
				"second-light": "#7589E1",
				notif: "#1E1E1E",
				dark: {
					interface: "#2D313D",
					prime: "#F7F7F7",
					second: "#6A7FDB",
					field: "#2D313D",
					"second-dark": "#5B606F",
					notif: "#1E1E1E",
				},
				light: {
					interface: "#F7F7F7",
					prime: "#1A193F",
					second: "#6A7FDB",
					field: "#D1D0D0",
					"second-light": "#7589E1",
					notif: "#1E1E1E",
				},
			},
		},
	},
	plugins: [],
};
