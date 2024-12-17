<template lang="">
	<!-- Viewing  of  Itinerary -->
	<div
		class="flex flex-col lg:flex-row h-screen bg-gray-100 dark:bg-gray-900"
	>
		<!-- Main Content -->

		<div class="w-full lg:w-7/12 overflow-y-auto px-4 lg:px-8 py-6">
			<!-- Hero Image and Title -->

			<div
				class="relative w-full h-[250px] rounded-lg overflow-hidden mb-6"
			>
				<img
					:src="itineraryDetails.main_image"
					alt="Itinerary Cover"
					class="w-full h-full object-cover"
				/>
				<div
					class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"
				>
					<div class="absolute bottom-0 left-0 p-6 w-full">
						<div class="flex items-center justify-between">
							<div class="flex-1">
								<input
									v-if="editingField === 'main_title'"
									v-model="tempEditValue"
									@blur="saveEdit('main_title')"
									@keyup.enter="saveEdit('main_title')"
									class="text-3xl font-bold px-1.5 py-1 text-white font-bebas-neue tracking-wide bg-black/30 border-b border-white w-full focus:outline-none focus:ring-2 focus:ring-white/50 rounded"
									:ref="
										(el) => {
											if (el) el.focus();
										}
									"
									placeholder="Enter title"
								/>
								<h1
									v-else
									class="text-3xl font-bold text-white font-bebas-neue tracking-wide"
									@click="isOwner && toggleEdit('main_title')"
								>
									{{
										itineraryDetails.main_title ||
										"Untitled Itinerary"
									}}
								</h1>
							</div>
							<button
								v-if="isOwner"
								@click="toggleEdit('main_title')"
								class="ml-2 text-white hover:text-gray-200 transition-colors duration-200"
								:aria-label="
									editingField === 'main_title'
										? 'Save title'
										: 'Edit title'
								"
							>
								<PencilIcon
									v-if="editingField !== 'main_title'"
									class="size-4"
								/>
								<div
									v-else
									class="flex items-center justify-between space-x-1 text-xs border border-second hover:border-blue-700 px-1.5 p-1 rounded-lg"
								>
									<CheckIcon class="size-3 font-bold" />
									<span>Save</span>
								</div>
							</button>
						</div>
					</div>
				</div>
			</div>

			<!-- Rating Section -->
			<div
				class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm mb-6"
			>
				<div class="flex justify-end items-center space-x-2">
					<span class="text-xs text-gray-600 dark:text-gray-300">
						{{
							hasSubmitted
								? "Rating Submitted"
								: "Rate this Itinerary"
						}}
					</span>
					<div class="flex items-center">
						<button
							v-for="star in 5"
							:key="star"
							@mouseover="!hasSubmitted && hoverRating(star)"
							@mouseleave="!hasSubmitted && resetRating()"
							@click="!hasSubmitted && setRating(star)"
							class="focus:outline-none"
							:disabled="hasSubmitted"
						>
							<StarIcon
								:class="{
									'text-second':
										star <= (tempRating || rating),
									'text-gray-300':
										star > (tempRating || rating),
								}"
								class="size-4 transition-colors"
							/>
						</button>
					</div>
				</div>
			</div>

			<!-- Author Profile and Description -->
			<div
				class="flex items-start space-x-4 p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm mb-6"
			>
				<img
					:src="itineraryDetails.user_photo"
					alt="Author profile"
					class="size-9 rounded-full object-cover flex-shrink-0"
				/>
				<div class="flex-1">
					<div class="flex items-center justify-between">
						<div class="flex items-center text-xs space-x-2 mb-1">
							<h2 class="text-gray-900 dark:text-white">
								@{{ itineraryDetails.creator_name }}
							</h2>
							<span class="text-gray-500">
								{{ formatDate(itineraryDetails.date_posted) }}
							</span>
						</div>
						<button
							v-if="isOwner"
							@click="toggleEdit('main_description')"
							class="text-blue-500 hover:text-blue-700 transition-colors duration-200"
							:aria-label="
								editingField === 'main_description'
									? 'Save description'
									: 'Edit description'
							"
						>
							<PencilIcon
								v-if="editingField !== 'main_description'"
								class="h-4 w-4"
							/>
							<div
								v-else
								class="flex items-center justify-between space-x-1 text-xs border border-second hover:border-blue-700 px-1.5 p-1 rounded-lg"
							>
								<CheckIcon class="size-3 font-bold" />
								<span>Save</span>
							</div>
						</button>
					</div>

					<div class="relative">
						<textarea
							v-if="editingField === 'main_description'"
							v-model="tempEditValue"
							@blur="saveEdit('main_description')"
							class="w-full text-xs pt-2 bg-transparent border rounded text-gray-900 dark:text-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							rows="3"
							:ref="
								(el) => {
									if (el) el.focus();
								}
							"
							placeholder="Enter description"
						></textarea>
						<p
							v-else
							class="text-gray-900 text-xs pt-2 dark:text-gray-300 leading-relaxed"
							@click="isOwner && toggleEdit('main_description')"
						>
							{{
								itineraryDetails.main_description ||
								"No description provided"
							}}
						</p>
					</div>
				</div>
			</div>

			<!-- General Tips Section -->
			<div class="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-sm">
				<div class="flex items-center justify-between mb-4">
					<h2
						class="text-base font-semibold text-gray-900 dark:text-white"
					>
						General Tips
					</h2>
					<button
						v-if="isOwner"
						@click="toggleEdit('gen_tips')"
						class="text-blue-500 hover:text-blue-700 transition-colors duration-200"
						:aria-label="
							editingField === 'gen_tips'
								? 'Save tips'
								: 'Edit tips'
						"
					>
						<PencilIcon
							v-if="editingField !== 'gen_tips'"
							class="h-4 w-4"
						/>
						<div
							v-else
							class="flex items-center justify-between space-x-1 text-xs border border-second hover:border-blue-700 px-1.5 p-1 rounded-lg"
						>
							<CheckIcon class="size-3 font-bold" />
							<span>Save</span>
						</div>
					</button>
				</div>
				<div class="w-full sm:w-[83%] mx-auto">
					<div v-if="editingField === 'gen_tips'" class="relative">
						<textarea
							v-model="tempEditValue"
							@blur="saveEdit('gen_tips')"
							class="w-full text-xs bg-transparent border rounded p-2 dark:text-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-200"
							rows="6"
							:ref="
								(el) => {
									if (el) el.focus();
								}
							"
							placeholder="Enter general tips"
						></textarea>
					</div>
					<div v-else @click="isOwner && toggleEdit('gen_tips')">
						<p
							v-for="(paragraph, index) in paragraphs"
							:key="index"
							class="text-gray-600 dark:text-gray-300 text-xs mb-4"
							v-html="formatText(paragraph)"
						></p>
						<p
							v-if="paragraphs.length === 0"
							class="text-gray-500 dark:text-gray-400 text-xs italic"
						>
							No general tips provided
						</p>
					</div>
				</div>
			</div>
			<!-- Budget Section -->
			<div class="pb-6 px-6 rounded-lg shadow-sm mb-6 mt-4">
				<h2
					class="text-base font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Suggeted Budget
				</h2>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<div class="bg-prime dark:bg-gray-700 p-4 rounded-lg">
						<div class="text-xs text-gray-500 dark:text-gray-400">
							Total Budget
						</div>
						<div
							class="text-lg font-bold text-gray-200 dark:text-white"
						>
							{{ selectedSymbol }}{{ total_budget }}
						</div>
					</div>
					<div class="bg-prime dark:bg-gray-700 p-4 rounded-lg">
						<div class="text-xs text-gray-500 dark:text-gray-400">
							Currency
						</div>
						<select
							v-model="selectedCurrency"
							@change="updateCurrency"
							class="w-full bg-transparent border-0 text-gray-200 dark:text-white focus:ring-0 text-xs sm:text-sm"
						>
							<option
								v-for="[code, name, symbol] in currency_list"
								:key="code"
								:value="{ code, symbol }"
								class="text-gray-900 dark:text-white focus:ring-0 dark:bg-gray-800 text-xs sm:text-sm"
							>
								{{ code }} - {{ name }}
							</option>
						</select>
					</div>
				</div>
			</div>

			<!-- Itinerary List -->
			<div
				class="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-4 sm:p-6 mb-6"
			>
				<div class="flex items-center justify-between mb-6">
					<h2
						class="text-xl font-semibold text-gray-900 dark:text-white"
					>
						Itinerary Stops
					</h2>
				</div>

				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<!-- Add New Stop Card -->
					<button
						v-if="isOwner"
						@click="openEditModal(null)"
						class="group relative sm:h-[400px] h-[200px] border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg overflow-hidden transition-all duration-300 hover:border-blue-500 dark:hover:border-blue-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
					>
						<div
							class="absolute inset-0 flex flex-col items-center justify-center p-6"
						>
							<div
								class="rounded-full bg-gray-100 dark:bg-gray-700 p-3 mb-3 group-hover:bg-blue-100 dark:group-hover:bg-blue-900 transition-colors duration-300"
							>
								<PlusIcon
									class="h-8 w-8 text-gray-500 dark:text-gray-400 group-hover:text-blue-600 dark:group-hover:text-blue-400"
								/>
							</div>
							<span
								class="text-sm font-medium text-gray-600 dark:text-gray-300 group-hover:text-blue-600 dark:group-hover:text-blue-400"
							>
								Add New Stop
							</span>
						</div>
					</button>
					<div
						v-for="(itinerary, index) in list_itineraries"
						:key="itinerary.id"
						class="relative bg-gray-50 dark:bg-gray-700 rounded-lg overflow-hidden transition-transform hover:scale-[1.02] h-auto sm:h-[400px]"
					>
						<button
							v-if="isOwner"
							@click="openEditModal(itinerary)"
							class="absolute top-2 right-2 bg-gray-800 hover:bg-gray-900 text-white rounded-full p-2 shadow-xl drop-shadow-xl shadow-black transition-colors duration-200 ease-in-out z-20"
						>
							<PencilIcon class="size-4" />
						</button>
						<img
							v-if="itinerary.photos"
							:src="itinerary.photos[0].getUrl()"
							:alt="itinerary.name"
							class="w-full h-48 object-cover"
						/>
						<div
							v-else
							class="w-full h-48 flex items-center justify-center bg-gray-700"
						>
							<span class="text-gray-500"
								>No image available</span
							>
						</div>
						<div class="p-4">
							<div class="flex items-center space-x-2 mb-2">
								<div
									class="flex-shrink-0 w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold"
								>
									{{ String.fromCharCode(66 + index) }}
								</div>
								<h3
									class="flex-1 text-base font-semibold text-gray-900 dark:text-white truncate"
								>
									{{ itinerary.name }}
								</h3>
							</div>
							<p class="text-gray-600 text-xs dark:text-gray-300">
								{{ itinerary.description }}
							</p>

							<div class="py-3">
								<div class="flex flex-wrap gap-1">
									<span
										v-for="type in itinerary?.types
											? itinerary.types.slice(0, 3)
											: []"
										:key="type"
										class="px-2 py-1 text-xs rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300"
									>
										{{ type.replace("_", " ") }}
									</span>
								</div>
							</div>
							<div class="flex justify-between items-center">
								<div class="flex justify-between items-center">
									<div class="flex items-center">
										<StarIcon
											class="size-4 text-yellow-400 mr-1"
										/>
										<span
											class="text-xs text-gray-600 dark:text-gray-300"
										>
											{{ itinerary.rating || 0 }}
										</span>
									</div>
								</div>
								<div>
									<span
										class="text-xs text-gray-500 dark:text-gray-400"
										>Budget:</span
									>
									<span
										class="ml-3 font-semibold text-gray-900 dark:text-white text-sm"
									>
										{{ selectedSymbol
										}}{{
											convertCurrency(
												itinerary.budget,
												"PHP"
											)
										}}
									</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Suggested Places -->
			<div class="bg-white dark:bg-transparent rounded-lg shadow-sm mb-6">
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Suggested Places
				</h2>
				<p class="text-sm text-gray-600 dark:text-gray-300 mb-5">
					The following are CulturaLink's suggested stops along your
					itinerary, offering travelers more opportunities to explore
					the cultural, historical, and traditional insights of the
					place you're visiting.
				</p>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<div
						v-for="place in suggested_places"
						:key="place.place_id"
						@click="locateSuggestedPlace(place)"
						class="bg-gray-50 dark:bg-gray-700 rounded-lg overflow-hidden cursor-pointer transition-transform hover:scale-[1.02]"
					>
						<img
							v-if="hasPhoto(place)"
							:src="place.photos[0].getUrl()"
							:alt="place.name"
							class="w-full h-48 object-cover"
						/>
						<div
							v-else
							class="w-full h-48 flex items-center justify-center bg-gray-700"
						>
							<span class="text-gray-500"
								>No image available</span
							>
						</div>
						<div class="p-4">
							<div class="flex justify-between items-center mb-2">
								<h3
									class="text-base font-semibold text-gray-900 dark:text-white"
								>
									{{ place.name }}
								</h3>
							</div>
							<div class="flex flex-wrap gap-2">
								<span
									v-for="type in place?.types.slice(0, 3)"
									:key="type"
									class="px-2 py-1 text-xs rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300"
								>
									{{ type.replace("_", " ") }}
								</span>
							</div>
							<div class="flex items-center mt-2">
								<StarIcon class="size-4 text-yellow-400 mr-1" />
								<span
									class="text-xs text-gray-600 dark:text-gray-300"
								>
									{{ place?.rating }}
								</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Desktop Map Section -->
		<div class="hidden lg:block w-5/12 h-screen relative top-0">
			<div class="absolute inset-0 bg-white dark:bg-gray-800">
				<div ref="desktopMapRef" class="w-full h-full"></div>
			</div>
		</div>

		<!-- Mobile Map Section -->
		<div
			:class="{
				'translate-y-0': showMap,
				'translate-y-full': !showMap,
				'duration-300': true,
				'ease-in-out': true,
			}"
			class="lg:hidden fixed inset-0 bg-white dark:bg-gray-800 transition-transform duration-300 ease-in-out z-50"
		>
			<div ref="mobileMapRef" class="w-full h-full"></div>
		</div>

		<!-- Mobile Map Toggle Button -->
		<button
			@click="toggleMap"
			class="lg:hidden fixed bottom-24 right-4 bg-blue-500 text-white p-4 rounded-full shadow-lg z-50"
		>
			<MapIcon v-if="!showMap" class="w-6 h-6" />
			<XIcon v-else class="w-6 h-6" />
		</button>
	</div>
	<!-- Add the edit modal -->

	<!-- Add New Stop Modal -->
	<div
		v-if="showModal"
		class="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm flex items-center justify-center z-50 p-4"
	>
		<div
			class="bg-white dark:bg-gray-800 rounded-2xl p-6 sm:p-8 w-full max-w-lg shadow-2xl transform transition-all duration-300 ease-in-out"
		>
			<div class="flex justify-between items-center mb-6">
				<h3
					class="text-3xl sm:text-4xl font-bold text-gray-500 font-bebas-neue tracking-wider dark:text-white"
				>
					{{ isEditMode ? "Edit Stop" : "Add New Stop" }}
				</h3>
				<button
					v-if="isEditMode"
					@click="showDeleteConfirmation = true"
					class="text-red-500 hover:text-red-700 focus:outline-none"
					aria-label="Delete stop"
				>
					<TrashIcon class="h-6 w-6" />
				</button>
			</div>
			<form @submit.prevent="submitItinerary" class="space-y-6">
				<!-- Location -->
				<div>
					<label
						for="autocomplete"
						class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
					>
						Set Location's Pin
					</label>
					<div class="relative">
						<MapPinIcon
							class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400"
						/>
						<input
							type="text"
							placeholder="Enter location"
							name="auto-complete"
							ref="autocompleteRef"
							id="autocomplete"
							v-model="location"
							@focus="initializeAutocomplete"
							class="w-full pl-10 pr-12 py-3 rounded-full bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 focus:outline-none transition-all duration-300 ease-in-out"
							required
						/>
						<button
							type="button"
							@click="locatorBtn"
							class="absolute right-2 top-1/2 transform -translate-y-1/2 p-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all duration-300 ease-in-out"
							aria-label="Use current location"
						>
							<GlobeAltIcon class="h-5 w-5" />
						</button>
					</div>
				</div>

				<!-- Budget -->
				<div>
					<label
						for="it-budget"
						class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
					>
						Budget
					</label>
					<div class="relative rounded-full shadow-sm">
						<div
							class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
						>
							<span class="text-gray-500 sm:text-sm">{{
								selectedSymbol
							}}</span>
						</div>
						<input
							type="number"
							id="it-budget"
							v-model="budget"
							class="block w-full pl-10 pr-12 py-3 rounded-full border-gray-300 dark:border-gray-600 bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 focus:border-blue-500 dark:focus:border-blue-400 transition-all duration-300 ease-in-out appearance-none"
							placeholder="Enter budget"
							required
						/>
					</div>
				</div>

				<div
					class="flex flex-col sm:flex-row justify-end space-y-3 sm:space-y-0 sm:space-x-3 mt-8"
				>
					<button
						type="button"
						@click="closeModal"
						class="w-full sm:w-auto px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-full text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 ease-in-out"
					>
						Cancel
					</button>
					<button
						type="submit"
						class="w-full sm:w-auto px-4 py-2 border border-transparent rounded-full text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 ease-in-out"
					>
						Save
					</button>
				</div>
			</form>
		</div>
	</div>
	<!-- Delete Confirmation Modal -->
	<div
		v-if="showDeleteConfirmation"
		class="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm flex items-center justify-center z-50 p-4"
	>
		<div
			class="bg-white dark:bg-gray-800 rounded-2xl p-6 sm:p-8 w-full max-w-md shadow-2xl"
		>
			<h3 class="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
				Confirm Deletion
			</h3>
			<p class="text-gray-600 dark:text-gray-300 mb-6">
				Are you sure you want to delete this stop? This action cannot be
				undone.
			</p>
			<div class="flex justify-end space-x-3">
				<button
					@click="showDeleteConfirmation = false"
					class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-all duration-300 ease-in-out"
				>
					Cancel
				</button>
				<button
					@click="deleteItinerary"
					class="px-4 py-2 border border-transparent rounded-md text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-all duration-300 ease-in-out"
				>
					Delete
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { StarIcon, MapIcon, XIcon } from "lucide-vue-next";
import { PencilIcon } from "@heroicons/vue/24/solid";
import {
	PhotoIcon,
	MapPinIcon,
	GlobeAltIcon,
	PlusIcon,
	CheckIcon,
	TrashIcon,
	ArrowDownOnSquareIcon,
} from "@heroicons/vue/24/outline";
import axiosClient from "../axios";

import axios from "axios";
import { useStore } from "vuex";
const store = useStore();
const router = useRouter();
const route = useRoute();

const user_id = ref("");

const rating = ref(0); // Current user's rating
const tempRating = ref(0); // Used for hover effect
const hasSubmitted = ref(false);
const allRatings = ref([]); // Initial ratings from the backend

const suggested_places = ref([]);
const paragraphs = ref([]);

const showDeleteConfirmation = ref(false);
const isEditing = ref(true);
const main_title = ref("ITINERARY TITLE");
const selectedImageUrlIn = ref("");

const total_budget = ref(0);
const convertedBudget = ref("");
const api =
	"https://v6.exchangerate-api.com/v6/eab4e81875a8acd578c8d5c1/latest/USD";
const currency_list = ref([
	["AED", "United Arab Emirates Dirhams", "د.إ"],
	["AFN", "Afghan Afghani", "؋"],
	["ALL", "Albanian Lek", "L"],
	["AMD", "Armenian Dram", "֏"],
	["ANG", "Netherlands Antillean Guilder", "ƒ"],
	["AOA", "Angolan Kwanza", "Kz"],
	["ARS", "Argentine Peso", "$"],
	["AUD", "Australian Dollar", "$"],
	["AWG", "Aruban Florin", "ƒ"],
	["AZN", "Azerbaijani Manat", "₼"],
	["BAM", "Bosnia Herzegovina Convertible Mark", "KM"],
	["BBD", "Barbadian Dollar", "$"],
	["BGN", "Bulgarian Lev", "лв"],
	["BHD", "Bahraini Dinar", ".د.ب"],
	["BIF", "Burundian Franc", "FBu"],
	["BMD", "Bermudan Dollar", "$"],
	["BOB", "Bolivian Boliviano", "Bs."],
	["BRL", "Brazilian Real", "R$"],
	["BSD", "Bahamian Dollar", "$"],
	["BWP", "Botswanan Pula", "P"],
	["BYN", "Belarusian Ruble", "Br"],
	["BZD", "Belize Dollar", "$"],
	["CDF", "Congolese Franc", "FC"],
	["CHF", "Swiss Franc", "CHF"],
	["CLP", "Chilean Peso", "$"],
	["CNY", "Chinese Yuan", "¥"],
	["COP", "Colombian Peso", "$"],
	["CRC", "Costa Rican Colón", "₡"],
	["CUP", "Cuban Peso", "$"],
	["CZK", "Czech Koruna", "Kč"],
	["DJF", "Djiboutian Franc", "Fdj"],
	["DKK", "Danish Krone", "kr"],
	["DOP", "Dominican Peso", "$"],
	["DZD", "Algerian Dinar", "دج"],
	["EGP", "Egyptian Pound", "£"],
	["ERN", "Eritrean Nakfa", "Nfk"],
	["EUR", "Euro", "€"],
	["FJD", "Fijian Dollar", "$"],
	["FKP", "Falkland Islands Pound", "£"],
	["GBP", "British Pound", "£"],
	["GEL", "Georgian Lari", "₾"],
	["GHS", "Ghanaian Cedi", "₵"],
	["GIP", "Gibraltar Pound", "£"],
	["GMD", "Gambian Dalasi", "D"],
	["GNF", "Guinean Franc", "FG"],
	["GTQ", "Guatemalan Quetzal", "Q"],
	["GYD", "Guyanaese Dollar", "$"],
	["HKD", "Hong Kong Dollar", "$"],
	["HNL", "Honduran Lempira", "L"],
	["HRK", "Croatian Kuna", "kn"],
	["HTG", "Haitian Gourde", "G"],
	["HUF", "Hungarian Forint", "Ft"],
	["IDR", "Indonesian Rupiah", "Rp"],
	["ILS", "Israeli New Shekel", "₪"],
	["INR", "Indian Rupee", "₹"],
	["IQD", "Iraqi Dinar", "ع.د"],
	["IRR", "Iranian Rial", "﷼"],
	["ISK", "Icelandic Króna", "kr"],
	["JMD", "Jamaican Dollar", "$"],
	["JOD", "Jordanian Dinar", "د.ا"],
	["JPY", "Japanese Yen", "¥"],
	["KES", "Kenyan Shilling", "Sh"],
	["KGS", "Kyrgystani Som", "с"],
	["KHR", "Cambodian Riel", "៛"],
	["KMF", "Comorian Franc", "CF"],
	["KRW", "South Korean Won", "₩"],
	["KWD", "Kuwaiti Dinar", "د.ك"],
	["KYD", "Cayman Islands Dollar", "$"],
	["KZT", "Kazakhstani Tenge", "₸"],
	["LAK", "Laotian Kip", "₭"],
	["LBP", "Lebanese Pound", "ل.ل"],
	["LKR", "Sri Lankan Rupee", "Rs"],
	["LRD", "Liberian Dollar", "$"],
	["LSL", "Lesotho Loti", "M"],
	["LYD", "Libyan Dinar", "ل.د"],
	["MAD", "Moroccan Dirham", "د.م."],
	["MDL", "Moldovan Leu", "L"],
	["MGA", "Malagasy Ariary", "Ar"],
	["MKD", "Macedonian Denar", "ден"],
	["MMK", "Myanmar Kyat", "K"],
	["MNT", "Mongolian Tugrik", "₮"],
	["MOP", "Macanese Pataca", "MOP$"],
	["MRU", "Mauritanian Ouguiya", "UM"],
	["MUR", "Mauritian Rupee", "₨"],
	["MVR", "Maldivian Rufiyaa", "ރ."],
	["MWK", "Malawian Kwacha", "MK"],
	["MXN", "Mexican Peso", "$"],
	["MYR", "Malaysian Ringgit", "RM"],
	["MZN", "Mozambican Metical", "MT"],
	["NAD", "Namibian Dollar", "$"],
	["NGN", "Nigerian Naira", "₦"],
	["NIO", "Nicaraguan Córdoba", "C$"],
	["NOK", "Norwegian Krone", "kr"],
	["NPR", "Nepalese Rupee", "रु"],
	["NZD", "New Zealand Dollar", "$"],
	["OMR", "Omani Rial", "ر.ع."],
	["PAB", "Panamanian Balboa", "B/"],
	["PGK", "Papua New Guinean Kina", "K"],
	["PHP", "Philippine Peso", "₱"],
	["PKR", "Pakistani Rupee", "₨"],
	["PLN", "Polish Zloty", "zł"],
	["PYG", "Paraguayan Guarani", "₲"],
	["QAR", "Qatari Riyal", "ر.ق"],
	["RON", "Romanian Leu", "lei"],
	["RSD", "Serbian Dinar", "дин"],
	["RUB", "Russian Ruble", "₽"],
	["RWF", "Rwandan Franc", "FRw"],
	["SAR", "Saudi Riyal", "ر.س"],
	["SBD", "Solomon Islands Dollar", "$"],
	["SCR", "Seychellois Rupee", "₨"],
	["SDG", "Sudanese Pound", "ج.س."],
	["SEK", "Swedish Krona", "kr"],
	["SGD", "Singapore Dollar", "$"],
	["SHP", "St. Helena Pound", "£"],
	["SLL", "Sierra Leonean Leone (1964—2022)", "Le"],
	["SOS", "Somali Shilling", "Sh"],
	["SRD", "Surinamese Dollar", "$"],
	["SSP", "South Sudanese Pound", "£"],
	["STN", "São Tomé Príncipe Dobra", "Db"],
	["SYP", "Syrian Pound", "£"],
	["SZL", "Swazi Lilangeni", "E"],
	["THB", "Thai Baht", "฿"],
	["TJS", "Tajikistani Somoni", "SM"],
	["TMT", "Turkmenistani Manat", "T"],
	["TND", "Tunisian Dinar", "د.ت"],
	["TOP", "Tongan Paanga", "T$"],
	["TRY", "Turkish Lira", "₺"],
	["TTD", "Trinidad Tobago Dollar", "$"],
	["TWD", "New Taiwan Dollar", "$"],
	["TZS", "Tanzanian Shilling", "Sh"],
	["UAH", "Ukrainian Hryvnia", "₴"],
	["UGX", "Ugandan Shilling", "Sh"],
	["USD", "US Dollar", "$"],
	["UYU", "Uruguayan Peso", "$"],
	["UZS", "Uzbekistani Som", "soʻm"],
	["VES", "Venezuelan Bolívar", "Bs.S."],
	["VND", "Vietnamese Dong", "₫"],
	["VUV", "Vanuatu Vatu", "VT"],
	["WST", "Samoan Tala", "T"],
	["XAF", "Central African CFA Franc", "FCFA"],
	["XCD", "East Caribbean Dollar", "$"],
	["XOF", "West African CFA Franc", "CFA"],
	["XPF", "CFP Franc", "F"],
	["YER", "Yemeni Rial", "﷼"],
	["ZAR", "South African Rand", "R"],
	["ZMW", "Zambian Kwacha", "ZK"],
	["ZWL", "Zimbabwean Dollar (2009)", "$"],
]);

const selectedCurrency = ref("");

const currency_save = ref("PHP");
const converted = ref(0);

const username = ref("");

const location = ref("");
const title = ref("");
const budget = ref("");
const description = ref("");
const latitude = ref(0);
const longitude = ref(0);
const showModal = ref(false);
const client = ref(null); // Initialize axios client later

const list_itineraries = ref([]);
const itineraryIds = ref([]);
const itinerariesfrom = ref([]);

// This property controls which view is currently visible
const currentView = ref("itinerary"); // 'overview' or 'itinerary'
const showMap = ref(false);
const desktopMap = ref(null);
const mobileMap = ref(null);
const desktopMapRef = ref(null);
const mobileMapRef = ref(null);

const itinerary_id = ref(route.query.id);
const itineraries = ref([]);
const itineraryDetails = reactive({
	creator_name: null,
	currency: null,
	date_posted: null,
	gen_tips: "",
	user_photo: null,
	id: null,
	itineraries: [],
	main_description: "",
	main_image: null,
	main_title: null,
	owner: null,
	status: null,
});
const nearestTouristInterest = ref(null);
const map = ref(null);
const userMarker = ref(null);
const userLocation = ref(null);
const arrivalMessage = ref("");

const formatDate = (dateString) => {
	return new Date(dateString).toLocaleDateString("en-US", {
		month: "long",
		day: "numeric",
		year: "numeric",
	});
};
// Computed properties
const isMobile = computed(() => window.innerWidth < 640);

const avgRating = computed(() => {
	if (allRatings.value.length === 0) return 0;
	const total = allRatings.value.reduce((sum, current) => sum + current, 0);
	return total / allRatings.value.length;
});
const fetchUser = async () => {
	try {
		const res = await axiosClient.get("/user");
		username.value = res.data.user.username;
	} catch (error) {
		console.log("ERROR", error.message);
	}
};
const isOwner = computed(() => itineraryDetails.owner === user.value.user?.id);
const isEditMode = ref(false);
const editingItinerary = ref(null);
const editingField = ref(null);
const tempEditValue = ref("");
const toggleEditMode = () => {
	isEditMode.value = !isEditMode.value;
};

const toggleEdit = (field) => {
	if (editingField.value === field) {
		saveEdit(field);
	} else {
		tempEditValue.value = itineraryDetails[field] || "";
		editingField.value = field;
	}
};

const saveEdit = async (field) => {
	if (itineraryDetails) {
		itineraryDetails[field] = tempEditValue.value;
		if (field === "gen_tips") {
			paragraphs.value = itineraryDetails.gen_tips.split(/\n+/);
		}
		editingField.value = null;
		const data = { [field]: tempEditValue.value };
		await store.dispatch("updateItineraryDetails", {
			id: itinerary_id.value,
			data,
		});
		// Here you would typically call an API to save the changes
		// For example: await updateItineraryDetails(itineraryDetails.id, { [field]: tempEditValue.value });
	} else {
		console.error("itineraryDetails is undefined");
	}
};

const openEditModal = (itinerary) => {
	if (itinerary !== null) {
		isEditMode.value = true;
		editingItinerary.value = { ...itinerary };
		location.value = itinerary.name;
		budget.value = itinerary.budget;
	} else {
		isEditMode.value = false;
		editingItinerary.value = null;
		location.value = "";
		budget.value = "";
	}
	// console.log("Editing itinerary:", editingItinerary.value);

	showModal.value = true;
};

const closeModal = () => {
	showModal.value = false;
	editingItinerary.value = null;
};

const handleFileSelectionIn = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrlIn.value = URL.createObjectURL(file);
	}
};
const deleteItinerary = async () => {
	const id = editingItinerary.value ? editingItinerary.value.id : null;
	console.log("ID", id);

	const viewed_it_id = itinerary_id.value;
	if (editingItinerary.value) {
		try {
			await store.dispatch("deleteItinerary", {
				id,
				viewed_it_id,
			});
			const index = list_itineraries.value.findIndex(
				(i) => i.id === editingItinerary.value.id
			);
			if (index !== -1) {
				list_itineraries.value.splice(index, 1);
			}
		} catch (error) {
			console.error("Error deleting itinerary:", error);
		}
	}
	showDeleteConfirmation.value = false;
	closeModal();
};
const locatorBtn = () => {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				latitude.value = position.coords.latitude;
				longitude.value = position.coords.longitude;
				console.log("Current position:", position.coords);
				getAddressFrom(latitude.value, longitude.value);
			},
			(error) => {
				console.error("Geolocation error:", error.message);
				locationError.value = `Error: ${error.message}`;
			},
			{
				enableHighAccuracy: true,
				timeout: 5000,
				maximumAge: 0,
			}
		);
	} else {
		console.error("Geolocation is not supported by this browser.");
		locationError.value = "Geolocation is not supported by this browser.";
	}
};
const submitItinerary = () => {
	const formData = new FormData();

	formData.append("longitude", longitude.value);
	formData.append("latitude", latitude.value);
	formData.append("budget", budget.value);
	formData.append("code", selectedCurrency.value);

	const isEditMode = editingItinerary.value !== null;
	const itineraryId = editingItinerary.value
		? editingItinerary.value.id
		: null;

	store
		.dispatch("submitItinerary", { formData, itineraryId })
		.then(async (response) => {
			if (itineraryId) {
				const index = list_itineraries.value.findIndex(
					(i) => i.id === editingItinerary.value.id
				);
				if (index !== -1) {
					list_itineraries.value[index] = {
						...list_itineraries.value[index],
						...response,
					};
					console.log("LIST OF ITINERARIES", list_itineraries.value);
				}
				await letDetails();
				await showLocationOntheMap();
				showModal.value = false;
			} else {
				list_itineraries.value.push(response);
				console.log("CREATEDD NEW in VIEWING: ", response);
				const id = response.id;
				const id_in_saved_itinerary = itinerary_id.value;
				await store
					.dispatch("updateSavedItinerary", {
						id,
						id_in_saved_itinerary,
					})
					.then(async (response) => {
						console.log("UPDATED ITINERARY", response);
						await fetchItineraries();
					})
					.catch((error) => {
						console.error(error);
					});
			}

			showModal.value = false;
		})
		.catch((error) => {
			console.error(error);
		});
};
const editItineraryDetails = async (field) => {
	if (editingField.value === field) {
		// Save changes
		const formData = new FormData();
		formData.append(field, tempEditValue.value);

		try {
			const response = await axiosClient.put(
				`/itinerary/${itineraryDetails.id}`,
				formData
			);
			if (response.data) {
				itineraryDetails[field] = response.data[field];
				if (field === "gen_tips") {
					paragraphs.value = itineraryDetails.gen_tips.split(/\n+/);
				}
			}
		} catch (error) {
			console.error(`Error updating ${field}:`, error);
		}

		editingField.value = null;
		tempEditValue.value = "";
	} else {
		// Start editing
		editingField.value = field;
		tempEditValue.value = itineraryDetails[field];
	}
};
const user = ref({});
onMounted(async () => {
	await store.dispatch("fetchUserData");
	user.value = store.getters.getUser.data;

	// console.log("FROM OTHER", route.params.itinerarydata);
	initializeAutocomplete();
	await fetchSavedItineraries();
	fetchUser();
	initializeMaps();
	// checkArrival(destination);
});
const initializeMaps = async () => {
	nextTick(() => {
		if (desktopMapRef.value && mobileMapRef.value) {
			desktopMap.value = new google.maps.Map(desktopMapRef.value, {
				center: { lat: 0, lng: 0 },
				zoom: 2,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				mapId: "2c9b57c42de97202",
			});

			mobileMap.value = new google.maps.Map(mobileMapRef.value, {
				center: { lat: 0, lng: 0 },
				zoom: 2,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				mapId: "2c9b57c42de97202",
			});
		}
		showLocationOntheMap();
	});
};

const toDropDown = ref(null);

const populateDropdown = () => {
	if (toDropDown.value) {
		currency_list.value.forEach((currency) => {
			const [code, countryName] = currency;
			const option = document.createElement("option");
			option.value = code;
			option.textContent = `${code} - ${countryName}`;
			option.classList.add("text-prime", "bg-interface");
			toDropDown.value.add(option);
		});
	} else {
		console.error("Dropdown element not found");
	}
};

const getPlaceDetails = async (lat, lng) => {
	if (!lat || !lng || isNaN(lat) || isNaN(lng)) {
		console.error("Invalid latitude or longitude values");
		return null;
	}

	try {
		const response = await axios.get(
			"https://maps.googleapis.com/maps/api/geocode/json",
			{
				params: {
					latlng: `${lat},${lng}`,
					key: "AIzaSyAGNh44Urq3R3CJWtWYcAsvtRiwwupo-5s",
				},
			}
		);
		if (response.data.status === "OK") {
			const placeDetails = response.data.results[0];

			return placeDetails;
		} else {
			console.error("Geocoding API error:", response.data.status);
			return null;
		}
	} catch (error) {
		console.error("Error fetching place details:", error);
		return null;
	}
};
const googleMapsApiKey = "AIzaSyAGNh44Urq3R3CJWtWYcAsvtRiwwupo-5s"; // Replace with your actual API key
const getPlacePhoto = (photoReference) => {
	if (!photoReference) return null;
	return `https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=${photoReference}&key=${googleMapsApiKey}`;
};

const getMorePlaceDetails = async (placeId) => {
	try {
		const { PlacesService } = await google.maps.importLibrary("places");
		const service = new PlacesService(document.createElement("div"));

		return new Promise((resolve, reject) => {
			service.getDetails(
				{
					placeId: placeId,
				},
				(place, status) => {
					if (status === google.maps.places.PlacesServiceStatus.OK) {
						// console.log("More place details:", place);
						resolve(place);
					} else {
						console.error("Places API error:", status);
						reject(new Error(`Places API error: ${status}`));
					}
				}
			);
		});
	} catch (error) {
		console.error("Error fetching more place details:", error);
		throw error;
	}
};

// Modify the letDetails function to use the new getMorePlaceDetails
const letDetails = async () => {
	for (const itinerary of list_itineraries.value) {
		const placeDetails = await getPlaceDetails(
			itinerary.latitude,
			itinerary.longitude
		);
		if (placeDetails) {
			// console.log("Place details:", placeDetails);
			itinerary.description =
				placeDetails.formatted_address || placeDetails.name;

			// Get more details using the place ID
			try {
				const morePlaceDetails = await getMorePlaceDetails(
					placeDetails.place_id
				);
				if (morePlaceDetails) {
					Object.assign(itinerary, morePlaceDetails);
				}
			} catch (error) {
				console.error("Error getting more place details:", error);
			}
		}
	}
	// console.log("List of itineraries with details:", list_itineraries.value);
};
const fetchItineraries = async () => {
	// showModal.value = false;
	try {
		itineraryIds.value = list_itineraries.value.map(
			(itinerary) => itinerary.id
		);
		// console.log("itineraryIds:", itineraryIds.value);

		let symbol = currency_list.value.find(
			(currency) => currency[0] === currency_save.value
		)[2];
		// selectedSymbol.value = symbol;
		// this.convertedBudget = `${symbol}${total_budget.value}`;
		// // Sort the itineraries by proximity before showing them on the map
		toDropDown.value = currency_save.value;
		await sortItinerariesByProximity();
		showLocationOntheMap();
		letDetails();
		// checkCode();
	} catch (error) {
		console.log(error);
	}
};
function selectSymbol(symbol) {
	selectedSymbol.value = symbol;
}

const fetchSavedItineraries = async () => {
	try {
		if (itinerary_id.value == null) {
			router.push({ name: "itinerary" });
		} else {
			const response = await store.dispatch(
				"fetchSavedItineraries",
				itinerary_id.value
			);

			itineraries.value = response;
			console.log("ITINERARIES", itineraries.value);

			itineraryDetails.creator_name = response.creator_name;
			itineraryDetails.user_photo = response.cultura_user.user_photo;
			currency_save.value = response.currency;
			itineraryDetails.date_posted = response.date_posted;
			itineraryDetails.gen_tips = response.gen_tips;
			itineraryDetails.id = response.id;
			list_itineraries.value = response.itineraries;
			itineraryDetails.main_description = response.main_description;
			itineraryDetails.main_image = response.main_image;
			itineraryDetails.main_title = response.main_title;
			itineraryDetails.owner = response.owner;
			itineraryDetails.status = response.status;
			total_budget.value = response.total_budget;
			allRatings.value = response.rating.map((item) => item.rating);
			console.log("ITINERARY ID: " + list_itineraries.value);
			await letDetails();
			await fetchItineraries();
			paragraphs.value = itineraryDetails.gen_tips.split(/\n+/);
			// console.log("this is the paragraph", list_itineraries.value);
			// Fetch place details for each itinerary and update main_description
		}
	} catch (error) {
		console.error(error);
	}
};
const checkCode = () => {
	const toCurrency = toDropDown.value.value;
	selectedCurrency.value = toCurrency;
	// console.log("Selected currency code:", toCurrency);
	selectedSymbol.value = currency_list.value.find(
		(currency) => currency[0] === selectedCurrency.value
	)[2];
	// console.log("Selected symbol:", selectedSymbol.value);
	let newvalue = 0;
	list_itineraries.value.forEach((itinerary) => {
		// console.log("the code ", itinerary);
		if (itinerary.code != toCurrency) {
			if (itinerary.budget.length !== 0) {
				// console.log("convert the value to what selected currency");
				fetch(api) // Assuming 'api' is your API URL
					.then((resp) => resp.json())
					.then((data) => {
						let fromExchangeRate =
							data.conversion_rates[itinerary.code];
						let toExchangeRate = data.conversion_rates[toCurrency];
						const convertedAmount =
							(itinerary.budget / fromExchangeRate) *
							toExchangeRate;

						newvalue += parseFloat(convertedAmount.toFixed(2));

						total_budget.value = newvalue.toFixed(2);
					});
			}
		} else {
			// console.log("do not convert the value to what selected currency");
			newvalue += itinerary.budget;
			total_budget.value = newvalue;
		}
	});
};

const getCurrentLocation = async () => {
	return new Promise((resolve, reject) => {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(resolve, reject);
		} else {
			reject(new Error("Geolocation is not supported by this browser."));
		}
	});
};
const deg2rad = (deg) => {
	return deg * (Math.PI / 180);
};

const calculateDistance = (lat1, lon1, lat2, lon2) => {
	const R = 6371; // Radius of the earth in km
	const dLat = deg2rad(lat2 - lat1);
	const dLon = deg2rad(lon2 - lon1);
	const a =
		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(deg2rad(lat1)) *
			Math.cos(deg2rad(lat2)) *
			Math.sin(dLon / 2) *
			Math.sin(dLon / 2);
	const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	const distance = R * c; // Distance in km
	return distance;
};

const sortItinerariesByProximity = async () => {
	try {
		const currentLocation = await getCurrentLocation();
		list_itineraries.value.forEach((itinerary) => {
			itinerary.distance = calculateDistance(
				currentLocation.latitude,
				currentLocation.longitude,
				itinerary.latitude,
				itinerary.longitude
			);
		});

		list_itineraries.value.sort((a, b) => a.distance - b.distance);
		list_itineraries.value.forEach((itinerary, index) => {
			itinerary.order = String.fromCharCode(66 + index); // Start with 'B'
		});

		// After sorting, you can now update the map
		showLocationOntheMap();
	} catch (error) {
		console.error(error);
	}
};

const initializeMap = (latitude, longitude) => {
	// const map = new google.maps.Map(document.getElementById("the-map"), {
	// 	center: { lat: latitude, lng: longitude },
	// 	zoom: 8,
	// 	mapTypeId: google.maps.MapTypeId.ROADMAP,
	// });

	// Add a marker at the user's location
	new google.maps.Marker({
		position: { lat: latitude, lng: longitude },
		map: map,
		title: "Your Location",
	});
};
const updateMaps = async (center) => {
	const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

	if (desktopMap.value && mobileMap.value) {
		desktopMap.value.setCenter(center);
		mobileMap.value.setCenter(center);

		new AdvancedMarkerElement({
			position: center,
			map: desktopMap.value,
			title: "Your Location",
		});

		new AdvancedMarkerElement({
			position: center,
			map: mobileMap.value,
			title: "Your Location",
		});
	}
};
const showLocationOntheMap = async () => {
	if (list_itineraries.value.length === 0) {
		// If list_itineraries is empty, use the user's current location or a default location
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				updateMaps({ lat: latitude, lng: longitude });
			},
			async () => {
				// Fallback to a default location if unable to get the user's location
				const defaultLat = 37.7749; // Example default latitude
				const defaultLng = -122.4194; // Example default longitude
				await updateMaps({ lat: defaultLat, lng: defaultLng });
			}
		);
	} else {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				const bounds = new google.maps.LatLngBounds();
				const directionsService = new google.maps.DirectionsService();
				const directionsRendererDesktop =
					new google.maps.DirectionsRenderer({
						map: desktopMap.value,
					});
				const directionsRendererMobile =
					new google.maps.DirectionsRenderer({
						map: mobileMap.value,
					});

				const start = new google.maps.LatLng(latitude, longitude);
				const end = new google.maps.LatLng(
					list_itineraries.value[
						list_itineraries.value.length - 1
					].latitude,
					list_itineraries.value[
						list_itineraries.value.length - 1
					].longitude
				);

				const waypoints = list_itineraries.value
					.slice(0, -1)
					.map((itinerary) => ({
						location: new google.maps.LatLng(
							itinerary.latitude,
							itinerary.longitude
						),
						stopover: true,
					}));

				const request = {
					origin: start,
					destination: end,
					waypoints: waypoints,
					travelMode: google.maps.TravelMode.DRIVING,
					optimizeWaypoints: false,
				};

				directionsService.route(request, (result, status) => {
					if (status === google.maps.DirectionsStatus.OK) {
						directionsRendererDesktop.setDirections(result);
						directionsRendererMobile.setDirections(result);
					} else {
						console.error(
							"Directions request failed due to " + status
						);
					}
				});

				bounds.extend(start);
				bounds.extend(end);
				desktopMap.value.fitBounds(bounds);
				mobileMap.value.fitBounds(bounds);

				// Check arrival at destination
				checkArrival(
					list_itineraries.value[list_itineraries.value.length - 1]
				);
			},
			() => {
				console.error("Unable to retrieve current location");
			}
		);
	}
	// Optional: adjust the zoom level after fitting bounds if the zoom is too close or too far
	// This is a workaround because fitBounds does not let you specify max zoom level
};

const autocomplete = ref(null);
import { Loader } from "@googlemaps/js-api-loader";

const getAddressFrom = async (lat, long) => {
	try {
		const response = await axios.get(
			`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${long}&key=AIzaSyAGNh44Urq3R3CJWtWYcAsvtRiwwupo-5s
`
		);

		if (response.data.results && response.data.results.length > 0) {
			const address = response.data.results[0].formatted_address;
			console.log("Reverse geocoded address:", address);
			location.value = address;
			// You can update a ref here to display the address in your component
		} else {
			console.error("No results found");
		}
	} catch (error) {
		console.error("Error in reverse geocoding:", error);
	}
};
const initializeAutocomplete = () => {
	nextTick(async () => {
		const loader = new Loader({
			apiKey: "AIzaSyAGNh44Urq3R3CJWtWYcAsvtRiwwupo-5s",
			version: "weekly",
		});

		const Places = await loader.importLibrary("places");
		const input = document.getElementById("autocomplete");

		const autocomplete = new Places.Autocomplete(input);
		autocomplete.addListener("place_changed", () => {
			const place = autocomplete.getPlace();
			if (place.geometry) {
				latitude.value = place.geometry.location.lat();
				longitude.value = place.geometry.location.lng();
				location.value = place.formatted_address;
				console.log("Selected place:", location.value);
			} else {
				console.log("Selected place does not have a geometry");
			}
		});
	});
};

const findNearestTouristAttractions = async () => {
	const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
	try {
		if (mobileMap.value) {
			// const location = await getCurrentLocation();
			// const service = new google.maps.places.PlacesService(
			// 	mobileMap.value
			// );
			const position = await getCurrentLocation();
			const location = {
				latitude: position.coords.latitude,
				longitude: position.coords.longitude,
			};
			const { PlacesService } = await google.maps.importLibrary("places");
			const service = new PlacesService(mobileMap.value);

			const request = {
				location: new google.maps.LatLng(
					location.latitude,
					location.longitude
				),
				radius: "3000",
				type: ["tourist_attraction"],
			};

			service.nearbySearch(request, (results, status) => {
				if (status === google.maps.places.PlacesServiceStatus.OK) {
					suggested_places.value = results;
					console.log("Suggested places:", results);

					results.forEach((place) => {
						const name = place.name;
						const description = place.vicinity;
						let photoUrl = "No photo available";
						if (place.photos && place.photos.length > 0) {
							photoUrl = place.photos[0].getUrl({
								maxWidth: 400,
							});
						}
					});
				} else {
					console.error("Error finding tourist attractions:", status);
				}
			});
		}
	} catch (error) {
		console.error("Error finding nearest tourist attractions:", error);
	}
};

const openModal = (message) => {
	arrivalMessage.value = message;
	showModal.value = true;
};

const checkArrival = (destination) => {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition((position) => {
			const userLat = position.coords.latitude;
			const userLng = position.coords.longitude;
			const destinationLat = destination.latitude;
			const destinationLng = destination.longitude;

			const distance = calculateDistance(
				userLat,
				userLng,
				destinationLat,
				destinationLng
			);
			if (distance < 0.1) {
				// Adjust the threshold as needed
				openModal(`You have arrived at ${destination.name}`);
			}
		});
	}
};
const formatText = (text) => {
	return text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>"); // replace **text** with <strong>text</strong>
};
const getSymbol = (code) => {
	for (let i = 0; i < currency_list.value.length; i++) {
		if (currency_list.value[i][0] === code) {
			return currency_list.value[i][2];
		}
	}
	return null; // or some default value if code is not found
};

// Reset the rating display when hover ends
const resetRating = () => {
	tempRating.value = 0;
};

// Set and submit the rating
const setRating = (star) => {
	rating.value = star;
	// console.log(`User selected rating: ${star}`); // Log the user input rating
	allRatings.value.push(star); // Add the rating to the array
	submitRating(); // Call method to send data to the backend
};
const hoverRating = (star) => {
	tempRating.value = star;
};

// Method to send the new rating to the backend
const submitRating = async () => {
	if (hasSubmitted.value) return;
	const data = {
		user_id: user_id.value,
		itinerary_id: itinerary_id.value, // Include the postId
		rating: rating.value,
	};

	// console.log("Submit rating to backend:", data);
	hasSubmitted.value = true;
	// ADD SUBMIT RATING TO BACKEND HERE
	try {
		const response = await axiosClient.put("/ratings/", data);
		// console.log("Rating submitted successfully:", response.data);
	} catch (error) {
		console.error("Error submitting rating:", error);
		// Handle error response (e.g., show an error message)
		hasSubmitted.value = false; // Allow retrying the submission
	}
};

const handleTitleChange = () => {
	if (main_title.value.trim() === "") {
		main_title.value = "ITINERARY TITLE";
	}
	isEditing.value = false;
};

const toggleMap = () => {
	showMap.value = !showMap.value;
};

const showItinerary = (view) => {
	currentView.value = view;
	nextTick(() => {
		const navHeight = document.querySelector("#navs")
			? document.querySelector("#navs").offsetHeight
			: 0;
		let targetSection;

		if (view === "itinerary") {
			targetSection = document.getElementById("itinerary-section");
		} else {
			// Default to overview-section or handle other cases
			targetSection = document.getElementById("overview-section");
		}

		if (targetSection) {
			const offsetTop = targetSection.offsetTop - navHeight;

			window.scrollTo({
				top: offsetTop,
				behavior: "smooth",
			});
		}
	});
};
const hasPhoto = (place) => {
	return place.photos && place.photos.length > 0;
};
const currentInfoWindow = ref(null); // Define currentInfoWindow as a ref

const locateSuggestedPlace = (place) => {
	// console.log("Locating suggested place  with its descriptions:", place);

	try {
		const lat = place.geometry.location.lat();
		const lng = place.geometry.location.lng();

		// console.log("Locating suggested place:", latlngArray);

		if (!isNaN(lat) && !isNaN(lng)) {
			const center = { lat, lng };

			nextTick(() => {
				if (desktopMap.value && mobileMap.value) {
					desktopMap.value.setCenter(center);
					desktopMap.value.setZoom(15);
					mobileMap.value.setCenter(center);
					mobileMap.value.setZoom(15);

					const createInfoWindowContent = () => {
						const photoUrl =
							place.photos && place.photos.length > 0
								? place.photos[0].getUrl({})
								: "/placeholder.svg?height=200&width=320";

						return `
              <div style="
                width: 300px;

                border-radius: 8px;

                font-family: Arial, sans-serif;
                color: #FFFFFF;
                overflow: hidden;

				margin-right: 10px;
				margin-bottom: 10px;

              ">
                <div style="
                  height: 150px;
                  overflow: hidden;

                ">
                  <img
                    src="${photoUrl}"
                    alt="${place.name}"
                    style="
                      width: 100%;
                      height: 100%;
                      object-fit: cover;
                    "
                  >
                </div>

                <div style="margin-block: 1rem; margin-bottom:2rem;">
                  <h1 style="
                    margin: 0 0 8px 0;
                    font-size: 15px;
                    font-weight: 600;
                  ">${place.name}</h1>

                  <p style="
                    margin: 0 0 12px 0;
                    font-size: 12px;
                    color: #B0B0B0;
                  ">${place.vicinity}</p>

                  <div style="
                    display: flex;
                    gap: 16px;
                    margin-bottom: 12px;
                    color: #B0B0B0;
                    font-size: 13px;
                  ">
                    ${
						place.rating
							? `
                      <div style="display: flex; align-items: center; gap: 4px;">
                        <span style="color: #fbbf24;">★</span>
                        <span>${place.rating.toFixed(1)}</span>
                      </div>
                    `
							: ""
					}
                    ${
						place.user_ratings_total
							? `
                      <div>${place.user_ratings_total} reviews</div>
                    `
							: ""
					}
                  </div>

                  <div style="
                    display: flex;
                    gap: 8px;
                    flex-wrap: wrap;
                  ">
                    ${
						place.types
							? place.types
									.slice(0, 2)
									.map(
										(type) => `
                      <span style="
                        background: #444857;
                        padding: 4px 8px;
                        border-radius: 4px;
                        font-size: 12px;
                        color: #FFFFFF;
                      ">${type.replace(/_/g, " ")}</span>
                    `
									)
									.join("")
							: ""
					}
                  </div>
                </div>
              </div>
            `;
					};

					const infoWindow = new google.maps.InfoWindow({
						content: createInfoWindowContent(),
						maxWidth: 400,

						pixelOffset: new google.maps.Size(0, -5),
					});

					// Close any existing info window
					if (currentInfoWindow.value) {
						currentInfoWindow.value.close();
					}

					const createCustomMarkerIcon = () => ({
						path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
						fillColor: "#4f46e5",
						fillOpacity: 1,
						strokeColor: "#ffffff",
						strokeWeight: 2,
						scale: 10,
						labelOrigin: new google.maps.Point(0, -4),
					});
					// console.log(google.maps.SymbolPath);

					const createMarker = (map) => {
						return new google.maps.Marker({
							position: center,
							map: map,
							title: place.name,
							icon: createCustomMarkerIcon(),
							animation: google.maps.Animation.DROP,
							label: {
								text: "📍",
								fontSize: "32px",
								color: "#ffffff",
							},
						});
					};

					const desktopMarker = createMarker(desktopMap.value);
					const mobileMarker = createMarker(mobileMap.value);

					const handleMarkerClick = (map, marker) => {
						if (currentInfoWindow.value) {
							currentInfoWindow.value.close();
						}
						infoWindow.open(map, marker);
						currentInfoWindow.value = infoWindow;
					};

					desktopMarker.addListener("click", () => {
						handleMarkerClick(desktopMap.value, desktopMarker);
					});

					mobileMarker.addListener("click", () => {
						handleMarkerClick(mobileMap.value, mobileMarker);
					});

					if (!showMap.value) {
						toggleMap();
					}

					// Add click listener to map to close info window when clicking elsewhere
					desktopMap.value.addListener("click", () => {
						if (currentInfoWindow.value) {
							currentInfoWindow.value.close();
						}
					});

					mobileMap.value.addListener("click", () => {
						if (currentInfoWindow.value) {
							currentInfoWindow.value.close();
						}
					});
				}
			});
		} else {
			console.error("Invalid latitude or longitude values");
		}
	} catch (error) {
		console.error("Error locating suggested place:", error);
	}
};

const exchangeRates = ref({});

const selectedSymbol = computed(() => selectedCurrency.value.symbol);

const fetchExchangeRates = async () => {
	try {
		const response = await fetch(api);
		const data = await response.json();
		exchangeRates.value = data.conversion_rates;
	} catch (error) {
		console.error("Error fetching exchange rates:", error);
	}
};

const convertCurrency = (amount, fromCurrency) => {
	if (!amount || isNaN(amount)) return 0;

	const toCurrency = selectedCurrency.value.code;

	if (
		!exchangeRates.value[fromCurrency] ||
		!exchangeRates.value[toCurrency]
	) {
		console.warn(
			`Exchange rate not available for ${fromCurrency} or ${toCurrency}`
		);
		return amount;
	}

	const amountInBaseCurrency = amount / exchangeRates.value[fromCurrency];
	const convertedAmount =
		amountInBaseCurrency * exchangeRates.value[toCurrency];
	// console.log(
	// 	`Converting ${amount} ${fromCurrency} to ${convertedAmount} ${toCurrency}`
	// );
	return parseFloat(convertedAmount.toFixed(2));
};

const calculateTotalBudget = () => {
	total_budget.value = list_itineraries.value.reduce((total, itinerary) => {
		const budget = parseFloat(itinerary.budget) || 0;
		const code = itinerary.code || "PHP";
		const convertedBudget = convertCurrency(budget, code);

		return total + convertedBudget;
	}, 0);
	// console.log(`Total budget: ${total_budget.value}`);
};

const updateCurrency = () => {
	calculateTotalBudget();
};

onMounted(async () => {
	await fetchExchangeRates();
	if (typeof google !== "undefined" && google.maps) {
		await findNearestTouristAttractions();
	} else {
		console.error("Google Maps API is not loaded");
	}
	// Set initial currency based on the saved currency
	const savedCurrency = currency_list.value.find(
		([code]) => code === currency_save.value
	);
	if (savedCurrency) {
		selectedCurrency.value = {
			code: savedCurrency[0],
			symbol: savedCurrency[2],
		};
	}

	calculateTotalBudget();
});

watch(list_itineraries, calculateTotalBudget, { deep: true });
watch(selectedCurrency, calculateTotalBudget);
</script>

<style scoped>
select {
	/* Reset default select styles */
	-webkit-appearance: none;
	-moz-appearance: none;
	appearance: none;
}

/* Style the options specifically for mobile */
select option {
	padding: 0.75rem 1rem;
	font-size: 0.875rem;
	line-height: 1.25rem;
}

/* Dark mode styles for options */
@media (prefers-color-scheme: dark) {
	select option {
		background-color: #1f2937;
		color: white;
	}
}

/* Ensure dropdown stays within viewport on mobile */
@media (max-width: 640px) {
	select {
		max-height: 60vh;
	}
}
</style>
