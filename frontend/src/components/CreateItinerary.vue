<template>
	<div
		class="flex flex-col lg:flex-row h-screen bg-gray-100 dark:bg-gray-900"
	>
		<!-- Main Content -->
		<div class="w-full lg:w-2/3 overflow-y-auto px-4 lg:px-8 py-6">
			<!-- Hero Image and Title -->
			<div
				class="relative w-full h-[300px] rounded-lg overflow-hidden mb-6"
			>
				<label
					for="imgSelect"
					class="w-full h-full flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-800 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg cursor-pointer transition-all duration-300 hover:bg-gray-200 dark:hover:bg-gray-700"
				>
					<div
						class="flex flex-col items-center justify-center pt-5 pb-6"
					>
						<PhotoIcon
							v-if="!selectedImageUrl"
							class="w-12 h-12 mb-3 text-gray-400"
						/>
						<img
							v-else
							:src="selectedImageUrl"
							class="w-full h-full object-cover rounded-lg"
							alt="Selected image"
						/>
						<p
							v-if="!selectedImageUrl"
							class="mb-2 text-sm text-gray-500 dark:text-gray-400"
						>
							<span class="font-semibold">Click to upload</span>
							or drag and drop
						</p>
						<p
							v-if="!selectedImageUrl"
							class="text-xs text-gray-500 dark:text-gray-400"
						>
							SVG, PNG, JPG or GIF (MAX. 800x400px)
						</p>
					</div>
				</label>
				<input
					type="file"
					id="imgSelect"
					class="hidden"
					@change="handleFileSelection"
				/>
				<div class="absolute bottom-0 left-0 p-6 w-full">
					<input
						v-model="main_title"
						@blur="handleTitleChange"
						@keyup.enter="handleTitleChange"
						class="text-5xl px-2 font-bold text-prime dark:text-white bg-transparent w-full font-bebas-neue tracking-wide rounded-lg"
						placeholder="Enter title"
						maxlength="30"
					/>
				</div>
			</div>

			<!-- Author Profile and Description -->
			<div class="flex items-start sm:space-x-4 rounded-lg shadow-sm">
				<img
					:src="user.user_photo"
					alt="Author profile"
					class="w-12 h-12 rounded-full object-cover hidden sm:flex flex-shrink-0"
				/>
				<div class="flex-1">
					<div
						class="hidden sm:flex items-center text-sm space-x-2 mb-2"
					>
						<h2 class="text-gray-900 dark:text-white font-semibold">
							@{{ user.user?.username }}
						</h2>
					</div>
					<textarea
						v-model="setAboutMe"
						@blur="isEditingAboutMe = false"
						class="w-full text-gray-700 dark:text-gray-300 text-sm leading-relaxed bg-gray-50 dark:bg-gray-700 rounded-md p-3 resize-none outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out"
						placeholder="Tell us about yourself"
						rows="3"
					></textarea>
				</div>
			</div>
			<!-- General Tips Section -->
			<div class="rounded-lg shadow-sm mb-3 pt-3">
				<h2
					class="text-base font-semibold mb-4 text-gray-900 dark:text-white w-full border-b border-gray-300 dark:border-gray-700 pb-2"
				>
					General Tips
				</h2>
				<div class="w-full mx-auto">
					<textarea
						v-model="setTips"
						@blur="isEditingTips = false"
						class="w-full text-gray-700 dark:text-gray-300 text-sm bg-gray-50 dark:bg-gray-700 rounded-md p-3 resize-none outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out"
						placeholder="What do you want to share?"
						rows="4"
					></textarea>
				</div>
			</div>

			<!-- Budget Section -->
			<div class="pb-6 rounded-lg shadow-sm mb-6">
				<h2
					class="text-base font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Budgeting
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
					<button
						@click.prevent="saveMainItinerary"
						class="inline-flex items-center px-4 py-2 bg-second text-white text-sm font-medium rounded-md hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-300"
					>
						<ArrowDownOnSquareIcon class="h-5 w-5 mr-2" />
						Save
					</button>
				</div>

				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<!-- Add New Stop Card -->
					<button
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
						class="relative bg-gray-50 dark:bg-gray-700 rounded-lg overflow-hidden transition-transform hover:scale-[1.02] h-auto"
					>
						<button
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
									class="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold"
								>
									{{ String.fromCharCode(66 + index) }}
								</div>
								<h3
									class="text-base font-semibold text-gray-900 dark:text-white"
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
		</div>

		<!-- Desktop Map Section -->
		<div class="hidden lg:block w-1/2 h-screen relative">
			<div class="absolute inset-0 bg-white dark:bg-gray-800">
				<div ref="desktopMapRef" class="w-full h-full"></div>
			</div>
		</div>

		<!-- Mobile Map Section -->
		<div
			:class="{
				'translate-y-0': showMap,
				'translate-y-full': !showMap,
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
				<h3
					class="text-2xl font-bold mb-4 text-gray-900 dark:text-white"
				>
					Confirm Deletion
				</h3>
				<p class="text-gray-600 dark:text-gray-300 mb-6">
					Are you sure you want to delete this stop? This action
					cannot be undone.
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
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeMount, nextTick, watch } from "vue";
import { Loader } from "@googlemaps/js-api-loader";
import axiosClient from "../axios";

import axios from "axios";
import * as Dropdown from "primevue/dropdown";
import router from "../routes";

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
import { useStore } from "vuex";
const store = useStore();
// Reactive variables
const isEditingTips = ref(true);
const isEditingTitle = ref(true);
const isEditingAboutMe = ref(true);
const main_title = ref("ITINERARY TITLE");
const selectedImageUrl = ref(null);
const picture = ref(null);
const selectedImageUrlIn = ref(null);
const pictureIn = ref(null);
const setTips = ref("");
const setAboutMe = ref("");
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

const selectedPera = ref(null);
const list_budget = ref([]);
const selectedCurrency = ref("");
const selectedSymbol = computed(() => selectedCurrency.value.symbol);
const currency_save = ref("");
const converted = ref(0);
const paragraphs = ref([]);
const username = ref("");
const user_photo = ref(null);
const location = ref("");
const title = ref("");
const budget = ref("");
const description = ref("");
const latitude = ref("");
const longitude = ref("");
const showModal = ref(false);
const client = ref(null);
const list_itineraries = ref([]);
const itineraryIds = ref([]);
const currentView = ref("itinerary");

const showMap = ref(false);
const desktopMap = ref(null);
const mobileMap = ref(null);
const desktopMapRef = ref(null);
const mobileMapRef = ref(null);
onMounted(async () => {
	await fetchExchangeRates();
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
	initializeAutocomplete();
	initializeMaps();
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
			() => {
				// Fallback to a default location if unable to get the user's location
				const defaultLat = 37.7749; // Example default latitude
				const defaultLng = -122.4194; // Example default longitude
				updateMaps({ lat: defaultLat, lng: defaultLng });
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
const fetchExchangeRates = async () => {
	try {
		const response = await fetch(api);
		const data = await response.json();
		exchangeRates.value = data.conversion_rates;
	} catch (error) {
		console.error("Error fetching exchange rates:", error);
	}
};
const exchangeRates = ref({});
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
	console.log(
		`Converting ${amount} ${fromCurrency} to ${convertedAmount} ${toCurrency}`
	);

	return parseFloat(convertedAmount.toFixed(2));
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
const calculateTotalBudget = () => {
	total_budget.value = list_itineraries.value.reduce((total, itinerary) => {
		const budget = parseFloat(itinerary.budget) || 0;
		const code = itinerary.code || "PHP";
		const convertedBudget = convertCurrency(budget, code);
		console.log(
			`Converting ${budget} ${code} to ${convertedBudget} ${selectedCurrency.value.code}`
		);

		return total + convertedBudget;
	}, 0);
	// console.log(`Total budget: ${total_budget.value}`);
};
const updateCurrency = () => {
	calculateTotalBudget();
};
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
const showDeleteConfirmation = ref(false);

const isEditMode = ref(false);
const editingItinerary = ref(null);
const editingField = ref(null);
const tempEditValue = ref("");
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

const checkArrival = (itinerary) => {
	const now = new Date();
	const arrivalDate = new Date(itinerary.arrival_date);
	const timeDiff = arrivalDate.getTime() - now.getTime();
	const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));

	if (daysDiff < 0) {
		return "Past";
	} else if (daysDiff === 0) {
		return "Today";
	} else if (daysDiff === 1) {
		return "Tomorrow";
	} else {
		return `In ${daysDiff} days`;
	}
};

// Methods
const deleteItinerary = async () => {
	if (editingItinerary.value) {
		try {
			await store.dispatch("deleteItinerary", {
				id: editingItinerary.value.id,
				viewed_it_id: 0,
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

const scrollToElement = () => {
	const targetElement = document.getElementById("target-element");
	targetElement.scrollIntoView({
		behavior: "smooth",
		block: "center",
	});
};

const handleFileSelection = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrl.value = URL.createObjectURL(file);
		picture.value = file;
		console.log("Image :", file);
		isEditingTitle.value = true;
	}
};

const handleFileSelectionIn = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrlIn.value = URL.createObjectURL(file);
		picture.value = file;
		console.log("Image IN:", picture.value);
		isEditingTitle.value = true;
	}
};

const processTips = () => {
	paragraphs.value = setTips.value.split(/\n+/);
};

const formatText = (text) => {
	let paragraphs = text.split(/\n+/);
	return paragraphs
		.map((paragraph) => {
			return paragraph.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
		})
		.join("<br><br>");
};

const getSymbol = (code) => {
	for (let i = 0; i < currency_list.value.length; i++) {
		if (currency_list.value[i][0] === code) {
			return currency_list.value[i][2];
		}
	}
	return null;
};

const checkCode = () => {
	const toCurrency = selectedCurrency.value;
	currency_save.value = toCurrency;
	console.log("Selected currency code:", toCurrency);
	selectedSymbol.value = currency_list.value.find(
		(currency) => currency[0] === toCurrency
	)[2];
	let newvalue = 0;
	list_itineraries.value.forEach((itinerary) => {
		if (itinerary.code != toCurrency) {
			if (itinerary.budget.length !== 0) {
				fetch(api.value)
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
			newvalue += itinerary.budget;
			total_budget.value = newvalue;
		}
	});
};

const handleTitleChange = () => {
	if (main_title.value.trim() === "") {
		main_title.value = "ITINERARY TITLE";
	}
	isEditingTitle.value = false;
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

const saveMainItinerary = () => {
	if (
		!main_title.value.trim() ||
		!setAboutMe.value.trim() ||
		!setTips.value.trim() ||
		main_title.value === "ITINERARY TITLE"
	) {
		alert("Please fill all fields correctly.");
		return;
	} else {
		const formData = new FormData();
		formData.append("main_title", main_title.value);
		formData.append("main_description", setAboutMe.value);
		formData.append("gen_tips", setTips.value);
		formData.append("total_budget", total_budget.value);
		formData.append("currency", currency_save.value);
		formData.append("itineraries", itineraryIds.value);
		if (picture.value instanceof File) {
			formData.append("image", picture.value, picture.value.name);
		}

		store
			.dispatch("saveMainItinerary", formData)
			.then((response) => {
				console.log(response.data);
				main_title.value = "ITINERARY TITLE";
				setAboutMe.value = "";
				setTips.value = "";
				selectedImageUrl.value = null;
				selectedImageUrlIn.value = null;

				router.push({ name: "itinerary" });
			})
			.catch((error) => {
				console.error("Error saving itinerary:", error);
			});
	}
};

const submitItinerary = () => {
	const formData = new FormData();

	formData.append("longitude", longitude.value);
	formData.append("latitude", latitude.value);
	formData.append("budget", budget.value);
	formData.append("code", currency_save.value);

	if (pictureIn.value && pictureIn.value instanceof File) {
		formData.append("image", pictureIn.value, pictureIn.value.name);
	}

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
				// await store.dispatch("fetchItineraries");
				fetchItineraries();
			}

			showModal.value = false;
		})
		.catch((error) => {
			console.error(error);
		});
};

const getCurrentLocation = () => {
	return new Promise((resolve, reject) => {
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(
				(position) => {
					resolve({
						latitude: position.coords.latitude,
						longitude: position.coords.longitude,
					});
				},
				(error) => {
					reject(error);
				}
			);
		} else {
			reject(new Error("Geolocation is not supported by this browser."));
		}
	});
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
			itinerary.order = String.fromCharCode(65 + index);
		});
		console.log("ORDER", list_itineraries.value);
		showLocationOntheMap();
	} catch (error) {
		console.error(error);
	}
};

const calculateDistance = (lat1, lon1, lat2, lon2) => {
	const R = 6371;
	const dLat = deg2rad(lat2 - lat1);
	const dLon = deg2rad(lon2 - lon1);
	const a =
		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(deg2rad(lat1)) *
			Math.cos(deg2rad(lat2)) *
			Math.sin(dLon / 2) *
			Math.sin(dLon / 2);
	const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	const distance = R * c;
	return distance;
};

const deg2rad = (deg) => {
	return deg * (Math.PI / 180);
};

const fetchItineraries = async () => {
	const token = sessionStorage.getItem("TOKEN");
	const headers = {
		Authorization: `Token ${token}`,
		"Content-Type": "application/json",
	};
	const client = axios.create({
		baseURL: "http://127.0.0.1:8000",
		withCredentials: true,
		timeout: 5000,
		xsrfCookieName: "csrftoken",
		xsrfHeaderName: "X-Csrftoken",
		headers: headers,
	});
	try {
		const response = await axiosClient.get("/itinerary");
		list_itineraries.value = response.data;
		console.log("list_itineraries:", list_itineraries.value);
		itineraryIds.value = list_itineraries.value.map(
			(itinerary) => itinerary.id
		);
		// checkCode();
		console.log("itineraryIds:", itineraryIds.value);

		await sortItinerariesByProximity();
		showLocationOntheMap();
		letDetails();
	} catch (error) {
		console.log(error);
	}
};

const initializeMap = (latitude, longitude) => {
	new google.maps.Map(document.getElementById("the-map"), {
		center: { lat: latitude, lng: longitude },
		zoom: 8,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
	});
};

const autocompleteRef = ref(null);

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
			} else {
				console.log("Selected place does not have a geometry");
			}
		});
	});
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
const user = ref({});
// Lifecycle hooks
onBeforeMount(async () => {
	await store.dispatch("fetchUserData");
	user.value = store.getters.getUser.data;
	// username.value = user.username;
	console.log("user:", user.value);

	isEditingTitle.value = true;
	fetchItineraries();
});

watch(list_itineraries, calculateTotalBudget, { deep: true });
watch(selectedCurrency, calculateTotalBudget);
</script>
<style scoped></style>
