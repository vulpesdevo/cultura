<template>
	<div
		class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4"
	>
		<div class="bg-white dark:bg-gray-800 rounded-lg w-full max-w-md">
			<div class="p-6">
				<h3
					class="text-xl font-bold mb-4 text-gray-800 dark:text-white"
				>
					Comments
				</h3>
				<div class="max-h-60 overflow-y-auto mb-4">
					<div
						v-for="comment in post.comments"
						:key="comment._id"
						class="mb-2 p-2 bg-gray-100 dark:bg-gray-700 rounded"
					>
						<p class="text-sm text-gray-800 dark:text-gray-200">
							{{ comment.body }}
						</p>
						<small class="text-xs text-gray-500 dark:text-gray-400"
							>By {{ comment.author }} |
							{{ formatDate(comment.date_posted) }}</small
						>
					</div>
				</div>
				<form @submit.prevent="submitComment">
					<textarea
						v-model="newComment"
						class="w-full p-2 mb-4 border rounded dark:bg-gray-700 dark:text-white"
						placeholder="Add a comment..."
						rows="3"
					></textarea>
					<div class="flex justify-end">
						<button
							type="button"
							@click="$emit('close')"
							class="mr-2 px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400"
						>
							Cancel
						</button>
						<button
							type="submit"
							class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
						>
							Submit
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from "vue";
import moment from "moment";

const props = defineProps(["post"]);
const emit = defineEmits(["close", "comment-submitted"]);

const newComment = ref("");

const formatDate = (date) => moment(date).fromNow();

const submitComment = () => {
	if (!newComment.value.trim()) return;

	const commentData = {
		post_id: props.post._id,
		body: newComment.value,
		replied_to: props.post.author,
	};

	emit("comment-submitted", commentData);
	newComment.value = "";
};
</script>
