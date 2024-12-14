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
					class="w-full h-full flex items-center justify-center bg-gray-200 dark:bg-gray-700 cursor-pointer"
				>
					<img
						v-if="selectedImageUrl"
						:src="selectedImageUrl"
						class="w-full h-full object-cover"
						alt="Selected image"
					/>
					<div
						v-else
						class="text-gray-500 dark:text-gray-400 text-xl"
					>
						+ Add Image
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
						class="text-5xl font-bold text-white bg-transparent w-full font-bebas-neue tracking-wide"
						placeholder="Enter title"
						maxlength="30"
					/>
				</div>
			</div>

			<!-- Author Profile and Description -->
			<div
				class="flex items-start space-x-4 p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm mb-6"
			>
				<img
					:src="user_photo"
					alt="Author profile"
					class="w-12 h-12 rounded-full object-cover flex-shrink-0"
				/>
				<div class="flex-1">
					<div class="flex items-center text-sm space-x-2 mb-1">
						<h2 class="text-gray-900 dark:text-white">
							@{{ username }}
						</h2>
					</div>
					<textarea
						v-model="setAboutMe"
						@blur="isEditingAboutMe = false"
						class="w-full text-gray-900 dark:text-white leading-relaxed bg-transparent resize-none outline-none"
						placeholder="Tell us about yourself"
						rows="3"
					></textarea>
				</div>
			</div>

			<!-- General Tips Section -->
			<div
				class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm mb-6"
			>
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white w-full border-b border-gray-300 dark:border-gray-700 pb-2"
				>
					General Tips
				</h2>
				<div class="w-full sm:w-[83%] mx-auto">
					<textarea
						v-model="setTips"
						@blur="isEditingTips = false"
						class="w-full text-gray-600 dark:text-gray-300 text-sm bg-transparent resize-none outline-none"
						placeholder="What do you want to share?"
						rows="4"
					></textarea>
				</div>
			</div>

			<!-- Budget Section -->
			<div
				class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm mb-6"
			>
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Budgeting
				</h2>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<div class="bg-prime dark:bg-gray-700 p-4 rounded-lg">
						<div class="text-sm text-gray-500 dark:text-gray-400">
							Total Budget
						</div>
						<div
							class="text-2xl font-bold text-gray-200 dark:text-white"
						>
							{{ selectedSymbol }}
							<input
								v-model="total_budget"
								type="number"
								class="bg-transparent w-24 focus:outline-none"
							/>
						</div>
					</div>
					<div class="bg-prime dark:bg-gray-700 p-4 rounded-lg">
						<div class="text-sm text-gray-500 dark:text-gray-400">
							Currency
						</div>
						<select
							v-model="selectedCurrency"
							@change="checkCode"
							class="w-full bg-transparent border-0 text-gray-200 dark:text-white focus:ring-0 text-sm sm:text-base"
						>
							<option
								v-for="[code, name] in currency_list"
								:key="code"
								:value="code"
								class="text-gray-900 dark:text-white focus:ring-0 dark:bg-gray-800 text-xs sm:text-sm"
							>
								{{ code }} - {{ name }}
							</option>
						</select>
					</div>
				</div>
			</div>

			<!-- Itinerary List -->
			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm mb-6">
				<h2
					class="text-xl font-semibold p-6 text-gray-900 dark:text-white"
				>
					Itinerary Stops
				</h2>
				<div class="p-6 flex gap-3">
					<button
						@click="showModal = true"
						class="w-full bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600 transition-colors"
					>
						Add New Stop
					</button>
					<button
						@click="saveMainItinerary"
						class="w-full bg-green-500 text-white p-2 rounded-lg hover:bg-green-600 transition-colors"
					>
						Save Itinerary
					</button>
				</div>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 p-6">
					<div
						v-for="(itinerary, index) in list_itineraries"
						:key="itinerary.id"
						class="bg-gray-50 dark:bg-gray-700 rounded-lg overflow-hidden transition-transform hover:scale-[1.02]"
					>
						<img
							:src="itinerary.place_image"
							:alt="itinerary.title"
							class="w-full h-48 object-cover"
						/>
						<div class="p-4">
							<div class="flex items-center space-x-2 mb-2">
								<div
									class="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-semibold"
								>
									{{ String.fromCharCode(66 + index) }}
								</div>
								<h3
									class="text-lg font-semibold text-gray-900 dark:text-white"
								>
									{{ itinerary.title }}
								</h3>
							</div>
							<p class="text-gray-600 dark:text-gray-300 mb-4">
								{{ itinerary.description }}
							</p>
							<div class="flex justify-between items-center">
								<span
									class="text-sm text-gray-500 dark:text-gray-400"
									>Budget:</span
								>
								<span
									class="font-semibold text-gray-900 dark:text-white"
								>
									{{ getSymbol(itinerary.code)
									}}{{ itinerary.budget.toFixed(2) }}
								</span>
							</div>
							<div
								class="mt-2 text-sm text-gray-500 dark:text-gray-400"
							>
								Arrival: {{ checkArrival(itinerary) }}
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
				<h3
					class="text-3xl sm:text-4xl font-bold mb-6 text-gray-900 dark:text-white text-center"
				>
					Add New Stop
				</h3>
				<form @submit.prevent="submitItinerary" class="space-y-6">
					<!-- Image Upload -->
					<div class="group relative">
						<label
							for="imgSelectIn"
							class="block w-full h-48 sm:h-64 rounded-xl overflow-hidden cursor-pointer transition-all duration-300 ease-in-out"
							:class="{
								'bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600':
									!selectedImageUrlIn,
							}"
						>
							<img
								v-if="selectedImageUrlIn"
								:src="selectedImageUrlIn"
								class="w-full h-full object-cover transition-all duration-300 ease-in-out group-hover:scale-105"
								alt="Selected image"
							/>
							<div
								v-else
								class="flex flex-col items-center justify-center h-full"
							>
								<PhotoIcon
									class="h-16 w-16 text-gray-400 group-hover:text-gray-500 dark:text-gray-500 dark:group-hover:text-gray-400 transition-colors duration-300 ease-in-out"
								/>
								<span
									class="mt-2 text-sm text-gray-500 dark:text-gray-400"
									>Click to upload image</span
								>
							</div>
						</label>
						<input
							type="file"
							id="imgSelectIn"
							class="hidden"
							@change="handleFileSelectionIn"
							accept="image/*"
						/>
					</div>

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
							<div
								class="absolute inset-y-0 right-0 flex items-center"
							>
								<label for="currency" class="sr-only"
									>Currency</label
								>
								<select
									id="currency"
									v-model="selectedSymbol"
									class="h-full py-0 pl-2 pr-7 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md focus:ring-blue-500 focus:border-blue-500"
								>
									<option>$</option>
									<option>€</option>
									<option>£</option>
								</select>
							</div>
						</div>
					</div>

					<div
						class="flex flex-col sm:flex-row justify-end space-y-3 sm:space-y-0 sm:space-x-3 mt-8"
					>
						<button
							type="button"
							@click="showModal = false"
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
	</div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeMount, nextTick } from "vue";
import { Loader } from "@googlemaps/js-api-loader";

import axios from "axios";
import * as Dropdown from "primevue/dropdown";
import router from "../routes";
import { PhotoIcon, MapPinIcon, GlobeAltIcon } from "@heroicons/vue/24/outline";

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
	"https://v6.exchangerate-api.com/v6/14L4SCh7Me4KaDH1xLnMmw==wik53BlNsvI2cN3k/latest/USD";
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
const selectedCurrency = ref("PHP");
const selectedSymbol = ref("");
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

const showLocationOntheMap = () => {
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
const deleteItinerary = (itineraryId) => {
	client.value
		.post("/api/delete-itinerary", {
			itinerary_id: itineraryId,
		})
		.then(() => {
			fetchItineraries();
			checkCode();
		})
		.catch((error) => {
			console.error(error);
		});
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
		console.log("Image :", picture.value);
		isEditingTitle.value = true;
	}
};

const handleFileSelectionIn = (event) => {
	const file = event.target.files[0];
	if (file) {
		selectedImageUrlIn.value = URL.createObjectURL(file);
		pictureIn.value = file;
		console.log("Image IN:", pictureIn.value);
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
		let formData = new FormData();
		formData.append("main_image", null);
		formData.append("main_title", main_title.value);
		formData.append("main_description", setAboutMe.value);
		formData.append("gen_tips", setTips.value);
		formData.append("total_budget", total_budget.value);
		formData.append("currency", currency_save.value);
		formData.append("itineraries", itineraryIds.value);
		if (picture.value && picture.value instanceof File) {
			formData.append("image", picture.value, picture.value.name);
		}
		client.value
			.post("/api/save-itinerary", formData, {
				headers: {
					"Content-Type": "multipart/form-data",
				},
			})
			.then((response) => {
				console.log(response.data);
				main_title.value = "ITINERARY TITLE";
				setAboutMe.value = "";
				setTips.value = "";
				selectedImageUrl.value = null;
				selectedImageUrlIn.value = null;
				window.scrollTo(0, 0);
				router.push({ name: "itinerary" }).then(() => {
					window.location.reload();
				});
			})
			.catch((error) => {
				// Handle error
				console.error("Error saving itinerary:", error);
			});
	}
};

const submitItinerary = () => {
	const formData = new FormData();

	formData.append("longitude", longitude.value);
	formData.append("latitude", latitude.value);
	formData.append("budget", budget.value);
	formData.append("code", selectedCurrency.value);

	if (pictureIn.value && pictureIn.value instanceof File) {
		formData.append("image", pictureIn.value, pictureIn.value.name);
	}

	client.value
		.post("/api/create-itinerary", formData, {
			headers: {
				"Content-Type": "multipart/form-data",
			},
		})
		.then((response) => {
			console.log(response.data);
			showModal.value = false;
			location.value = "";
			budget.value = "";
			fetchItineraries();
			checkCode();
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
		const response = await client.get("/api/itinerary");
		list_itineraries.value = response.data;
		console.log("list_itineraries:", list_itineraries.value);
		itineraryIds.value = list_itineraries.value.map(
			(itinerary) => itinerary.id
		);
		checkCode();
		console.log("itineraryIds:", itineraryIds.value);

		await sortItinerariesByProximity();
		showLocationOntheMap();
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
		// autocomplete.addListener("place_changed", () => {
		// 	const place = autocomplete.getPlace();
		// 	console.log("Selected place:", place);
		// });
		// const inputElement = autocompleteRef.value;
		// if (
		// 	inputElement &&
		// 	window.google &&
		// 	window.google.maps &&
		// 	window.google.maps.places
		// ) {
		// 	const autocomplete = new google.maps.places.Autocomplete(
		// 		inputElement
		// 	);

		// 	});
		// } else {
		// 	console.error(
		// 		"Autocomplete input element not found or Google Maps API not loaded"
		// 	);
		// }
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

// Lifecycle hooks
onBeforeMount(() => {
	const token = sessionStorage.getItem("TOKEN");
	const headers = {
		Authorization: `Token ${token}`,
		"Content-Type": "application/json",
	};
	client.value = axios.create({
		baseURL: "http://127.0.0.1:8000",
		withCredentials: true,
		timeout: 5000,
		xsrfCookieName: "csrftoken",
		xsrfHeaderName: "X-Csrftoken",
		headers: headers,
	});
	client.value
		.get("api/user")
		.then((res) => {
			username.value = res.data.user.username;
			user_photo.value = res.data.profile.user_photo;
			// console.log("HALAAA", user_photo.value);
		})
		.catch((error) => {
			console.log("ERROR", error.message);
		});
	isEditingTitle.value = true;
	fetchItineraries();
});

onMounted(() => {
	initializeAutocomplete();
	initializeMaps();
});
</script>
<style scoped></style>
