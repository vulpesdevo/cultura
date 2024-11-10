<template>
	<div
		class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface dark:bg-dark-interface"
	>
		<div class="flex justify-between items-center w-full">
			<div class="w-1/2">
				<div v-if="isEditing" class="relative w-full">
					<input
						v-model="postTitle"
						@blur="handleTitleChange"
						@keyup.enter="handleTitleChange"
						class="font-bebas-neue text-lg text-prime dark:text-dark-prime sm:text-3xl rounded-lg border-field dark:bg-dark-field p-[.23rem] px-2 w-full ring-1 ring-gray-600 outline-[.5px] outline-none"
						placeholder="POST TITLE"
						autofocus
					/>
					<span
						class="absolute right-1 top-1 mt-1 material-icons-outlined text-field"
					>
						edit_note
					</span>
				</div>
				<h1
					v-else
					@click="isEditing = true"
					class="font-bebas-neue p-[.23rem] text-lg w-full text-prime dark:text-dark-prime sm:text-3xl"
				>
					{{ postTitle }}
				</h1>
			</div>
			<div
				class="drop-down-categ w-1/2 flex items-center justify-end font-montserrat"
			>
				<select
					id="category-option"
					v-model="categoryOption"
					class="appearance-none outline-none bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg ring-1 ring-gray-600 block w-3/4 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
				>
					<option class="mb-2" value="" disabled selected>
						Category
					</option>
					<option value="Food">Food</option>
					<option value="Traditions">Traditions</option>
					<option value="History">History</option>
				</select>
			</div>
		</div>
		<div class="for-content flex flex-col w-full mt-3">
			<div class="flex">
				<div class="hidden sm:flex w-14 h-14 mr-5 rounded-full">
					<img
						:src="postProfileDisplay"
						alt="Profile"
						class="size-full object-cover rounded-full cursor-pointer"
					/>
				</div>
				<textarea
					class="w-full rounded-lg resize-none p-4 outline-none dark:bg-dark-field dark:text-dark-prime"
					id="post-content"
					v-model="postContent"
					placeholder="What do you want to share?"
				></textarea>
			</div>
			<div
				class="added-img-container flex h-20 sm:ml-[4.5rem] mt-2 rounded-lg"
				v-if="selectedImageUrl"
			>
				<img
					:src="selectedImageUrl"
					alt="Post Image"
					class="object-cover w-32 h-full rounded-lg mr-1"
				/>
			</div>
			<div
				class="added-itinerary-container flex items-center justify-between bg-field dark:bg-dark-second-dark h-10 w-1/3 p-3 sm:ml-[4.5rem] mt-2 rounded-lg"
				v-if="selectedItinerary"
			>
				<p class="">{{ selectedItinerary.main_title }}</p>
				<span
					class="material-icons-outlined text-second text-2xl cursor-pointer"
					@click="removeItinerary"
					>close</span
				>
			</div>
		</div>
		<div
			class="about-country font-montserrat flex my-3 items-center justify-between border-b-2 dark:border-dark-field p-1"
		>
			<p class="hidden sm:flex text-prime dark:text-dark-prime">
				What country is your post about?
			</p>
			<p class="flex sm:hidden text-prime dark:text-dark-prime">
				Country
			</p>
			<input
				v-model="countryPost"
				type="text"
				ref="autocompletecountry"
				id="autocompletecountry"
				placeholder="Enter country"
				class="bg-field dark:bg-dark-second-dark dark:text-dark-prime rounded-full pl-4 ml-2 h-9 w-1/2 outline-none"
			/>
			<div class="hidden sm:flex sm:w-1/5"></div>
		</div>
		<div class="flex my-3 items-center justify-between">
			<div class="flex">
				<label for="imgSelect">
					<span
						class="material-icons-outlined text-second text-3xl cursor-pointer"
						>image</span
					>
				</label>
				<input
					type="file"
					id="imgSelect"
					class="hidden"
					@change="handleFileSelection"
				/>
				<span
					class="material-icons-outlined text-second text-3xl pl-2 cursor-pointer"
					@click="$emit('open-itinerary-modal')"
					>explore</span
				>
			</div>
			<input
				@click.prevent="submitPost"
				type="submit"
				value="Post"
				class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-10 sm:h-12 hover:bg-second-light cursor-pointer"
			/>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
const store = useStore();
const props = defineProps({
	postProfileDisplay: {
		type: String,
		required: true,
	},
	selectedItinerary: {
		type: Object,
		default: null,
	},
});

const emit = defineEmits([
	"submit-post",
	"open-itinerary-modal",
	"remove-itinerary",
	"file-selected",
]);

const isEditing = ref(true);
const postTitle = ref("POST TITLE");
const categoryOption = ref("");
const postContent = ref("");
const countryPost = ref("");
const selectedImageUrl = ref(null);
const id_of_selected = ref(null);
const handleTitleChange = () => {
	if (postTitle.value.trim() === "") {
		isEditing.value = true;
	} else {
		isEditing.value = false;
	}
};

const handleFileSelection = (event) => {
	const file = event.target.files[0];

	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		emit("file-selected", file);
	}
};

const removeItinerary = () => {
	emit("remove-itinerary");
};
console.log("selectedItinerary", props.selectedItinerary);

const submitPost = async () => {
	if (
		!categoryOption.value.trim() ||
		!postContent.value.trim() ||
		!countryPost.value.trim() ||
		postTitle.value === "POST TITLE"
	) {
		alert("Please fill all fields correctly.");
		return;
	} else {
		let formData = new FormData();
		formData.append("title", postTitle.value);
		formData.append("category", categoryOption.value);
		formData.append("body", postContent.value);
		formData.append("country", countryPost.value);
		formData.append("itinerary_id", id_of_selected.value);
		if (selectedImageUrl.value && selectedImageUrl.value instanceof File) {
			formData.append(
				"image",
				selectedImageUrl.value,
				selectedImageUrl.value.name
			);
		}
		try {
			await store.dispatch("submitPost", formData);
			postTitle.value = "POST TITLE";
			categoryOption.value = "";
			postContent.value = "";
			countryPost.value = "";
			selectedImageUrl.value = null;
			store.dispatch("fetchPosts").then(() => {
				posts.value = store.getters.getPosts;
			});
		} catch (error) {
			console.log("Error submitting post:", error);
		}
	}
};

onMounted(() => {
	const inputElement = document.getElementById("autocompletecountry");
	if (inputElement && window.google) {
		const autocomplete = new window.google.maps.places.Autocomplete(
			inputElement,
			{
				types: ["(regions)"],
			}
		);

		autocomplete.addListener("place_changed", () => {
			const place = autocomplete.getPlace();
			if (place && place.formatted_address) {
				countryPost.value = place.formatted_address;
			}
		});
	}
});
</script>
