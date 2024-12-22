<template>
	<div
		class="min-h-full flex items-center justify-center px-4 sm:px-6 lg:px-8"
	>
		<div class="w-full max-w-md rounded-lg overflow-hidden">
			<div class="p-6 sm:p-8">
				<div class="flex justify-center mb-6">
					<DocumentMagnifyingGlassIcon
						class="h-20 w-20 text-gray-400 dark:text-gray-200"
					/>
				</div>
				<h2
					class="text-center text-2xl font-extrabold text-gray-900 dark:text-white mb-4"
				>
					Post Not Found
				</h2>
				<p
					class="text-center text-sm text-gray-600 dark:text-gray-300 mb-6"
				>
					Oops! The post you're looking for has been deleted or
					doesn't exist.
				</p>
				<div
					class="flex flex-col sm:flex-row justify-center space-y-3 sm:space-y-0 sm:space-x-4"
				>
					<button
						@click="goBack"
						class="inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition duration-150 ease-in-out"
					>
						<ArrowLeftIcon class="h-5 w-5 mr-2" />
						Go Back
					</button>
					<button
						@click="goToHome"
						class="inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-blue-600 bg-blue-100 hover:bg-blue-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition duration-150 ease-in-out"
					>
						<HomeIcon class="h-5 w-5 mr-2" />
						Go to Home
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import {
	DocumentMagnifyingGlassIcon,
	ArrowLeftIcon,
	HomeIcon,
} from "@heroicons/vue/24/outline";
import { useRouter } from "vue-router";

const router = useRouter();

const goBack = () => {
	router.go(-1);
};

const goToHome = () => {
	router.push({ name: "dashboard" });
};
</script>
