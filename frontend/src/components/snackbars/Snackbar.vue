<template>
	<transition name="snackbar">
		<div
			v-if="show"
			class="fixed sm:bottom-4 left-1/2 transform -translate-x-1/2 z-50 w-full sm:w-auto"
		>
			<div
				:class="[
					'px-4 py-3 rounded-lg shadow-sm flex items-center gap-2 min-w-[320px]',
					type === 'success'
						? 'bg-green-50 text-green-700'
						: 'bg-red-50 text-red-700',
				]"
			>
				<CheckIcon v-if="type === 'success'" class="h-5 w-5" />
				<AlertTriangleIcon v-else class="h-5 w-5" />

				<span class="flex-grow text-sm font-medium">{{ message }}</span>

				<button
					@click="$emit('close')"
					class="hover:opacity-70 transition-opacity focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-green-50 focus-visible:ring-green-600"
					:class="{
						'focus-visible:ring-offset-red-50 focus-visible:ring-red-600':
							type !== 'success',
					}"
				>
					<XIcon class="h-5 w-5" />
				</button>
			</div>
		</div>
	</transition>
</template>

<script setup>
import { CheckIcon, AlertTriangleIcon, XIcon } from "lucide-vue-next";

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
	transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.snackbar-enter-from,
.snackbar-leave-to {
	opacity: 0;
	transform: translateY(20px) translateX(-50%);
}
</style>
