/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./index.html", "./src/**/*.{html,vue,js,ts,jsx,tsx}"],
	theme: {
		extend: {
			screens: {
				xs: "412px",
			},
		},
	},
	plugins: [],
}
