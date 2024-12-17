<template>
	<div
		class="min-h-screen bg-white dark:bg-gray-900 transition-colors duration-300"
	>
		<!-- Navigation -->
		<nav class="px-4 sm:px-6 lg:px-8 py-4">
			<div class="max-w-7xl mx-auto flex justify-between items-center">
				<div class="flex items-center">
					<a href="/" class="flex items-center">
						<span
							class="text-2xl font-bold text-navy-900 dark:text-white"
						>
							<img src="/ULTURALINK-DMLong.png" alt=""
						/></span>
					</a>
				</div>
				<div class="flex items-center space-x-4">
					<button
						@click="toggleDarkMode"
						class="p-2 rounded-full bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200"
						aria-label="Toggle dark mode"
					>
						<SunIcon v-if="isDarkMode" class="h-5 w-5" />
						<MoonIcon v-else class="h-5 w-5" />
					</button>
					<button
						class="px-6 py-2 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 text-navy-900 dark:text-white rounded-full font-semibold transition-colors duration-200"
					>
						SIGN IN
					</button>
				</div>
			</div>
		</nav>

		<!-- Hero Section -->
		<div class="relative overflow-hidden">
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-20">
				<div class="grid lg:grid-cols-2 gap-12 items-center">
					<!-- Left Column -->
					<div>
						<h1
							class="text-4xl sm:text-5xl lg:text-6xl font-bold text-navy-900 dark:text-white leading-tight mb-6"
						>
							Share. Learn. Connect.
						</h1>
						<p
							class="text-lg text-gray-600 dark:text-gray-300 mb-8 leading-relaxed"
						>
							CulturalLink connects you to the world's diverse
							cultures, bridging gaps, celebrating diversity, and
							fostering meaningful connections. Join us in uniting
							cultures—one connection at a time!
						</p>
						<button
							class="w-full sm:w-auto px-8 py-4 bg-indigo-500 hover:bg-indigo-600 text-white rounded-full text-lg font-semibold transition-colors duration-200 mb-4"
						>
							CREATE ACCOUNT
						</button>
						<p class="text-sm text-gray-500 dark:text-gray-400">
							By signing up, you agree to the
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Terms of Service</a
							>
							and
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Privacy Policy</a
							>, including
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Cookie Use</a
							>.
						</p>
					</div>

					<!-- Right Column - Device Mockups -->
					<div class="relative lg:ml-auto">
						<img
							src="/mock_up.png"
							alt="CulturalLink App Interface"
							class="w-full h-auto rounded-lg shadow-2xl"
						/>
					</div>
				</div>
			</div>
		</div>

		<!-- Features Section -->
		<div
			class="bg-indigo-100 dark:bg-gray-800 transition-colors duration-300"
		>
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
				<div class="grid md:grid-cols-3 gap-8">
					<!-- Feature 1 -->
					<div
						class="flex items-start space-x-4 p-6 rounded-lg bg-white dark:bg-gray-700 shadow-sm"
					>
						<div class="flex-shrink-0">
							<div
								class="w-12 h-12 rounded-full bg-indigo-100 dark:bg-indigo-900 flex items-center justify-center"
							>
								<UsersIcon
									class="w-6 h-6 text-indigo-600 dark:text-indigo-400"
								/>
							</div>
						</div>
						<div>
							<h3
								class="text-lg font-semibold text-navy-900 dark:text-white mb-2"
							>
								Share ideas and connect
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Share ideas and connect with a global community.
							</p>
						</div>
					</div>

					<!-- Feature 2 -->
					<div
						class="flex items-start space-x-4 p-6 rounded-lg bg-white dark:bg-gray-700 shadow-sm"
					>
						<div class="flex-shrink-0">
							<div
								class="w-12 h-12 rounded-full bg-indigo-100 dark:bg-indigo-900 flex items-center justify-center"
							>
								<MapPinIcon
									class="w-6 h-6 text-indigo-600 dark:text-indigo-400"
								/>
							</div>
						</div>
						<div>
							<h3
								class="text-lg font-semibold text-navy-900 dark:text-white mb-2"
							>
								Plan cultural experiences
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Plan cultural experiences with a customizable
								itinerary feature.
							</p>
						</div>
					</div>

					<!-- Feature 3 -->
					<div
						class="flex items-start space-x-4 p-6 rounded-lg bg-white dark:bg-gray-700 shadow-sm"
					>
						<div class="flex-shrink-0">
							<div
								class="w-12 h-12 rounded-full bg-indigo-100 dark:bg-indigo-900 flex items-center justify-center"
							>
								<ChatBubbleOvalLeftIcon
									class="w-6 h-6 text-indigo-600 dark:text-indigo-400"
								/>
							</div>
						</div>
						<div>
							<h3
								class="text-lg font-semibold text-navy-900 dark:text-white mb-2"
							>
								Get fun and informative
							</h3>
							<p class="text-gray-600 dark:text-gray-300">
								Get fun and informative cultural trivia with our
								chatbot, "Cura".
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import {
	UsersIcon,
	MapPinIcon,
	ChatBubbleOvalLeftIcon,
	SunIcon,
	MoonIcon,
} from "@heroicons/vue/24/outline";

const isDarkMode = ref(false);

const toggleDarkMode = () => {
	isDarkMode.value = !isDarkMode.value;
	document.documentElement.classList.toggle("dark");
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap");

:root {
	--navy-900: #1a1f36;
}

body {
	font-family: "Inter", sans-serif;
}

.text-navy-900 {
	color: var(--navy-900);
}

/* Dark mode styles */
.dark .text-navy-900 {
	color: white;
}
</style>
