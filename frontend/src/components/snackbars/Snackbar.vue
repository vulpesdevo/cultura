<template>
	<transition name="snackbar">
		<div
			v-if="show"
			class="fixed sm:bottom-4 left-1/2 transform -translate-x-1/2 z-50 w-full sm:w-auto"
		>
			<div
				:class="[
					'px-4 py-2 rounded-lg shadow-lg flex items-center ',
					type === 'success' ? 'bg-green-500' : 'bg-rose-500',
				]"
			>
				<span class="mr-2">
					<svg
						v-if="type === 'success'"
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6 text-white"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M5 13l4 4L19 7"
						/>
					</svg>
					<svg
						v-else
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6 text-white"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
						/>
					</svg>
				</span>
				<span class="flex-grow text-white">{{ message }}</span>
				<button
					@click="$emit('close')"
					class="ml-2 focus:outline-none text-white"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M6 18L18 6M6 6l12 12"
						/>
					</svg>
				</button>
			</div>
		</div>
	</transition>
</template>

<script setup>
defineProps({
	show: Boolean,
	message: String,
	type: {
		type: String,
		default: "error",
		validator: (value) => ["success", "error"].includes(value),
	},
});

defineEmits(["close"]);
</script>

<style scoped>
.snackbar-enter-active,
.snackbar-leave-active {
	transition: all 0.5s ease;
}
.snackbar-enter-from,
.snackbar-leave-to {
	opacity: 0;
	transform: translateY(20px) translateX(-50%);
}
</style>
