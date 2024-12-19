<template>
	<div class="w-full mx-auto">
		<h2
			class="text-lg font-semibold text-gray-700 dark:text-gray-300 mb-2 text-center"
		>
			Response Summary
		</h2>
		<div class="grid grid-cols-3 size-full justify-center items-center">
			<div class="col-span-1 flex justify-center" style="">
				<svg class="h-32" viewBox="0 0 100 100">
					<circle
						cx="50"
						cy="50"
						:r="radius"
						fill="transparent"
						class="stroke-gray-200 dark:stroke-gray-700"
						stroke-width="10"
					/>
					<circle
						v-for="(segment, index) in segments"
						:key="index"
						cx="50"
						cy="50"
						:r="radius"
						fill="transparent"
						:stroke="segment.color"
						stroke-width="10"
						:stroke-dasharray="`${segment.length} ${circumference}`"
						:stroke-dashoffset="segment.offset"
						class="transition-all duration-500 ease-in-out"
					/>
					<text
						x="50"
						y="50"
						text-anchor="middle"
						dy=".3em"
						class="text-lg font-bold fill-gray-700 dark:fill-gray-300"
					>
						{{ averageScore.toFixed(1) }}
					</text>
				</svg>
			</div>
			<div class="col-span-2 grid grid-cols-2 gap-3 text-xs w-full">
				<div
					v-for="(count, response) in responseCounts"
					:key="response"
					class="flex items-center"
				>
					<div
						:class="[
							'w-2 h-2 rounded-full mr-1',
							colorClasses[response],
						]"
					></div>
					<span class="text-gray-600 dark:text-gray-400"
						>{{ response }}: {{ count }}</span
					>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
	surveys: {
		type: Array,
		required: true,
	},
});

const radius = 40;
const circumference = 2 * Math.PI * radius;

const responseCounts = computed(() => {
	const counts = {
		"Strongly Disagree": 0,
		Disagree: 0,
		Neutral: 0,
		Agree: 0,
		"Strongly Agree": 0,
	};
	props.surveys.forEach((survey) => {
		Object.values(survey).forEach((response) => {
			if (counts.hasOwnProperty(response)) {
				counts[response]++;
			}
		});
	});
	return counts;
});

const totalResponses = computed(() =>
	Object.values(responseCounts.value).reduce((sum, count) => sum + count, 0)
);

const colorClasses = {
	"Strongly Disagree": "bg-red-300",
	Disagree: "bg-orange-300",
	Neutral: "bg-yellow-300",
	Agree: "bg-green-300",
	"Strongly Agree": "bg-blue-300",
};

const strokeColors = {
	"Strongly Disagree": "stroke-red-300",
	Disagree: "stroke-orange-300",
	Neutral: "stroke-yellow-300",
	Agree: "stroke-green-300",
	"Strongly Agree": "stroke-blue-300",
};
const segments = computed(() => {
	let offset = 0;
	return Object.entries(responseCounts.value)
		.filter(([, count]) => count > 0) // Only include segments with non-zero count
		.map(([response, count]) => {
			const length = (count / totalResponses.value) * circumference;
			const segment = {
				response,
				color: colorClasses[response],
				length,
				offset: -offset,
			};
			offset += length;
			return segment;
		});
});

const averageScore = computed(() => {
	const scoreMap = {
		"Strongly Disagree": 1,
		Disagree: 2,
		Neutral: 3,
		Agree: 4,
		"Strongly Agree": 5,
	};
	let totalScore = 0;
	Object.entries(responseCounts.value).forEach(([response, count]) => {
		totalScore += scoreMap[response] * count;
	});
	return totalResponses.value > 0 ? totalScore / totalResponses.value : 0;
});
</script>
