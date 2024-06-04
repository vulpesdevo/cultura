<template>
	<div
		class="w-full sm:w-64 h-16 sm:min-h-screen dark-bg-color text-white p-0 sm:p-4 fixed bottom-0 sm:relative sm:bottom-auto"
	>
		<div class="hidden sm:flex flex-col items-center mb-6 p-5">
			<img
				src="/login/culturalink_logo.png"
				alt="Logo"
				class="mr-3 sm:w-32 sm:h-32"
			/>
			<h1
				class="text-cl-purple font-bebas-neue text-4xl text-center mb-3 py-3 tracking-widest"
			>
				CULTURALINK
			</h1>
			<div class="relative">
				<input
					type="search"
					placeholder="Search..."
					class="ml-auto pl-10 h-10 outline-none text-black rounded-full"
				/>
				<span
					class="material-icons-outlined absolute left-0 pl-3 pt-2 text-gray-600"
					>search</span
				>
			</div>
		</div>
		<ul class="flex justify-evenly h-full sm:h-72 sm:block">
			<li
				class="flex mb-0 sm:mb-4 justify-between"
				v-for="(link, index) in links"
				:key="index"
			>
				<router-link
					active-class="active"
					:to="link.path"
					class="flex flex-col sm:flex-row align-middle items-center text-white sm:h-12 w-20 sm:w-full"
				>
					<span
						:class="{ active: $route.path === link.path }"
						class="left-border w-full h-[4px] sm:w-[4px] sm:h-full top-0 left-0 mr-0 mb-5 sm:mb-0 sm:mr-3 z-50"
					></span
					><span class="material-icons-outlined sm:pr-3">{{
						link.label
					}}</span>
					<span class="hidden sm:flex">{{
						link.name
					}}</span></router-link
				>
			</li>
		</ul>
		<div
		
			class="hidden sm:flex absolute bottom-0 left-0 w-16 h-16 m-4 p-1 rounded-full border hover:border-purple-900 transition-all duration-500"
			:class="{ 'border-purple-900': showPopup }"
			@click.self="showPopup = false"
		>
			<img
				src="/sample_img/mark.png"
				alt="Profile"
				class="rounded-full cursor-pointer"
				@click="togglePopup"
			/>
		</div>
		<div
			v-if="showPopup"
			class="hidden sm:flex popup-opt absolute bottom-16 left-20 rounded-lg p-4 w-36 h-40 transition-all duration-500"
			@click.self="showPopup = false"
		>
			<ul class="">
				<div class="flex flex-col h-20 mb-2">
					<li>
						<router-link
							to="/profile"
							class="flex align-middle items-start pb-3"
							><span class="material-icons-outlined pr-2"
								>account_circle</span
							>
							<p>Profile</p></router-link
						>
					</li>
					<li>
						<router-link
							to="/settings"
							class="flex align-middle items-start"
							><span class="material-icons-outlined pr-2"
								>settings</span
							>
							<p>Settings</p></router-link
						>
					</li>
				</div>
				<li>
					<router-link
						to="/logout"
						class="flex align-middle items-start border-t border-gray-500 pt-2"
						><span class="material-icons-outlined pr-2"
							>logout</span
						>
						<p>Logout</p></router-link
					>
				</li>
			</ul>
		</div>
	</div>
</template>

<script>
export default {
	name: "Sidebar",
	data() {
		return {
			showPopup: false,
			isHovered: false,
			links: [
				{
					name: "Home",
					path: "/home",
					// showIcon: true,
					label: "home",
				},
				{
					name: "Notification",
					path: "/",
					// showIcon: true,
					label: "notifications",
				},
				{
					name: "Itinerary",
					path: "/itinerary",
					// showIcon: true,
					label: "explore",
				},
			],
		};
	},
	methods: {
		togglePopup() {
			this.showPopup = !this.showPopup;
		},
	},
};
</script>

<style scoped>
a {
	text-decoration: none;
}
a:hover {
	color: var(--text-color-b);
}
a.active {
	color: var(--text-color-b);
}
.left-border {
	transition: all 0.3s ease;
	border-radius: 15px;
	background: transparent;
}

.left-border.active {
	transition: all 0.3s ease;
	background: var(--text-color-b);
}

input::placeholder {
	color: gray;
}
.popup-opt {
	background: var(--purple);
	color: var(--text-color-a);
}
</style>
