<template>
	<div
		class="min-h-screen w-screen bg-[#F8F7FF] flex flex-col items-center justify-center p-4"
	>
		<!-- Main Content -->
		<div class="text-center max-w-md mx-auto">
			<!-- 3D Illustration -->
			<div class="relative mb-12">
				<img
					src="/illustrations/undraw_page_not_found_re_e9o6.svg"
					alt="404 illustration"
					class="mx-auto h-[300px] w-auto"
				/>
				<!-- Decorative Elements -->
				<div class="absolute bottom-0 left-0 -translate-x-full">
					<TreePineIcon class="h-12 w-12 text-[#9F8FEF]" />
					<TreePineIcon class="h-8 w-8 text-[#9F8FEF] mt-2" />
				</div>
			</div>
			<h2
				class="text-xl text-[#424867] mb-2 flex items-center justify-center gap-2"
			>
				Page Not Found
			</h2>
			<p class="text-gray-600 mb-12">
				we couldn't find the page you are looking for
			</p>

			<!-- Action Buttons -->
			<div
				class="flex flex-col sm:flex-row items-center justify-center gap-4"
			>
				<router-link
					to="/"
					class="px-6 py-2.5 bg-[#9F8FEF] text-white rounded-full hover:bg-[#8A7AD8] transition-colors duration-200 flex items-center gap-2"
				>
					<HomeIcon class="h-4 w-4" />
					Back To Home
				</router-link>
			</div>
		</div>
	</div>
</template>

<script setup>
import { HomeIcon, TreePineIcon, FrownIcon, CrownIcon } from "lucide-vue-next";
</script>

<style scoped>
/* Optional: Add any component-specific styles here */
</style>
