<template>
	<div
		class="relative w-full h-48 bg-gray-100 dark:bg-gray-800 rounded-lg overflow-hidden"
	>
		<!-- Main Image -->
		<img
			v-if="constructedUrl && !error"
			:src="constructedUrl"
			:alt="alt"
			@error="handleError"
			@load="handleLoad"
			class="w-full h-full object-cover transition-all duration-300"
			:class="{ 'opacity-0': loading, 'opacity-100': !loading }"
		/>

		<!-- Loading State -->
		<div
			v-if="loading"
			class="absolute inset-0 flex items-center justify-center bg-gray-100 dark:bg-gray-800"
		>
			<div
				class="animate-spin rounded-full h-8 w-8 border-2 border-gray-300 border-t-blue-600"
			></div>
		</div>

		<!-- Error State -->
		<div
			v-if="error"
			class="absolute inset-0 flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-800 p-4"
		>
			<ExclamationTriangleIcon class="h-8 w-8 text-gray-400 mb-2" />
			<p class="text-sm text-gray-500 dark:text-gray-400 text-center">
				Unable to load image
			</p>
		</div>

		<!-- Attribution -->
		<div
			v-if="!error && !loading && attribution"
			class="absolute bottom-0 left-0 right-0 px-3 py-2 bg-black/60 text-xs text-white"
			v-html="attribution"
		></div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { ExclamationTriangleIcon } from "@heroicons/vue/24/outline";

const props = defineProps({
	photoReference: {
		type: String,
		required: true,
	},
	maxWidth: {
		type: Number,
		default: 400,
	},
	maxHeight: {
		type: Number,
		default: null,
	},
	apiKey: {
		type: String,
		required: true,
	},
	alt: {
		type: String,
		default: "Location photo",
	},
	attribution: {
		type: String,
		default: "",
	},
});

const loading = ref(true);
const error = ref(false);

const constructedUrl = computed(() => {
	const baseUrl = "https://maps.googleapis.com/maps/api/place/photo";
	const params = new URLSearchParams({
		key: props.apiKey,
		photo_reference: props.photoReference,
		...(props.maxWidth ? { maxwidth: props.maxWidth } : {}),
		...(props.maxHeight ? { maxheight: props.maxHeight } : {}),
	});
	return `${baseUrl}?${params.toString()}`;
});

const handleError = () => {
	error.value = true;
	loading.value = false;
};

const handleLoad = () => {
	loading.value = false;
};

onMounted(() => {
	// Preload image
	const img = new Image();
	img.onload = handleLoad;
	img.onerror = handleError;
	img.src = constructedUrl.value;
});
</script>
