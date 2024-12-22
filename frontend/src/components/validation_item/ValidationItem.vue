<template>
	<div class="flex items-center space-x-2 sm:space-x-0 group">
		<div class="w-5 h-5 flex items-center justify-center">
			<span
				class="material-icons-outlined text-sm transition-colors duration-200"
				:class="
					isValid
						? 'text-green-500'
						: 'text-gray-400 group-hover:text-gray-500'
				"
			>
				{{ isValid ? "check_circle" : "radio_button_unchecked" }}
			</span>
		</div>
		<label
			class="text-sm text-gray-600 dark:text-gray-400 group-hover:text-gray-700 dark:group-hover:text-gray-300 transition-colors duration-200 whitespace-nowrap"
		>
			{{ label }}
		</label>
	</div>
</template>

<script setup>
defineProps({
	isValid: {
		type: Boolean,
		required: true,
	},
	label: {
		type: String,
		required: true,
	},
});
</script>
