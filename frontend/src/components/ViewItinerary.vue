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
				<img
					:src="itineraryDetails.main_image"
					alt="Itinerary Cover"
					class="w-full h-full object-cover"
				/>
				<div
					class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"
				>
					<div class="absolute bottom-0 left-0 p-6">
						<h1
							class="text-5xl font-bold text-white font-['BebasNeue'] tracking-wide"
						>
							{{ itineraryDetails.main_title }}
						</h1>
						<div class="flex items-center mt-2">
							<div class="flex items-center">
								<StarIcon
									class="w-5 h-5 sm:w-6 sm:h-6 text-yellow-400 mr-1"
								/>
								<span
									class="text-white font-semibold text-sm sm:text-base"
									>{{ avgRating.toFixed(1) }} / 5</span
								>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Rating Section -->
			<div
				class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm mb-6"
			>
				<div class="flex justify-end items-center space-x-2">
					<span class="text-sm text-gray-600 dark:text-gray-300">
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
								class="w-6 h-6 transition-colors"
							/>
						</button>
					</div>
				</div>
			</div>
			<!-- Author Profile and Description -->
			<div class="flex items-start space-x-4 p-4">
				<img
					:src="itineraryDetails.user_photo"
					alt="Author profile"
					class="w-12 h-12 rounded-full object-cover flex-shrink-0"
				/>
				<div class="flex-1">
					<div class="flex items-center text-sm space-x-2 mb-1">
						<h2 class="text-gray-900 dark:text-white">
							@{{ itineraryDetails.creator_name }}
						</h2>
						<span class="text-gray-500">{{
							new Date(
								itineraryDetails.date_posted
							).toLocaleDateString("en-US", {
								month: "long",
								day: "numeric",
								year: "numeric",
							})
						}}</span>
					</div>
					<p class="text-gray-900 dark:text-white leading-relaxed">
						{{ itineraryDetails.main_description }}
					</p>
				</div>
			</div>

			<!-- General Tips Section -->
			<div class="p-6 rounded-lg shadow-sm mb-6">
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white w-full border-b border-gray-300 dark:border-gray-700 pb-2"
				>
					General Tips
				</h2>
				<div class="w-full sm:w-[83%] mx-auto">
					<p
						v-for="(paragraph, index) in paragraphs"
						:key="index"
						class="text-gray-600 dark:text-gray-300 text-sm mb-4"
						v-html="formatText(paragraph)"
					></p>
				</div>
			</div>
			<!-- Budget Section -->
			<div class="p-6 rounded-lg shadow-sm mb-6">
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
							{{ selectedSymbol }}{{ total_budget }}
						</div>
					</div>
					<div class="bg-prime dark:bg-gray-700 p-4 rounded-lg">
						<div class="text-sm text-gray-500 dark:text-gray-400">
							Currency
						</div>
						<select
							ref="toDropDown"
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
			<div class="rounded-lg shadow-sm mb-6">
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Itinerary Stops
				</h2>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
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
									{{ String.fromCharCode(65 + index) }}
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
						</div>
					</div>
				</div>
			</div>

			<!-- Suggested Places -->
			<div
				class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm mb-6"
			>
				<h2
					class="text-xl font-semibold mb-4 text-gray-900 dark:text-white"
				>
					Suggested Places
				</h2>
				<p class="text-sm text-gray-600 dark:text-gray-300 mb-4">
					The following are CulturaLink's suggested stops along your
					itinerary, offering travelers more opportunities to explore
					the cultural, historical, and traditional insights of the
					place you're visiting.
				</p>
				<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
					<div
						v-for="place in suggested_places"
						:key="place.place_id"
						@click="locateSuggestedPlace(place.geometry)"
						class="bg-gray-50 dark:bg-gray-700 rounded-lg overflow-hidden cursor-pointer transition-transform hover:scale-[1.02]"
						:class="{ 'h-28': !hasPhoto(place) }"
					>
						<img
							v-if="hasPhoto(place)"
							:src="place.photos[0].getUrl()"
							:alt="place.name"
							class="w-full h-48 object-cover"
						/>
						<div class="p-4">
							<div class="flex justify-between items-center mb-2">
								<h3
									class="text-lg font-semibold text-gray-900 dark:text-white"
								>
									{{ place.name }}
								</h3>
								<div class="flex items-center">
									<StarIcon
										class="w-5 h-5 text-yellow-400 mr-1"
									/>
									<span
										class="text-sm text-gray-600 dark:text-gray-300"
									>
										{{ place.rating }}
									</span>
								</div>
							</div>
							<div class="flex flex-wrap gap-2">
								<span
									v-for="type in place.types.slice(0, 3)"
									:key="type"
									class="px-2 py-1 text-xs rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300"
								>
									{{ type.replace("_", " ") }}
								</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Desktop Map Section -->
		<div class="hidden lg:block w-1/2 h-screen relative top-0">
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
</template>

<script setup>
import { ref, reactive, nextTick, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { StarIcon, MapIcon, XIcon } from "lucide-vue-next";
import axios from "axios";

const router = useRouter();
const route = useRoute();

const user_id = ref("");
const rating = ref(0); // Current user's rating
const tempRating = ref(0); // Used for hover effect
const hasSubmitted = ref(false);
const allRatings = ref([]); // Initial ratings from the backend

const suggested_places = ref([]);
const paragraphs = ref([]);

const isEditing = ref(true);
const main_title = ref("ITINERARY TITLE");

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
const selectedSymbol = ref("");
const currency_save = ref("");
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

const itinerary_id = ref(route.query.itinerarydata);
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

// Computed properties
const isMobile = computed(() => window.innerWidth < 640);

const avgRating = computed(() => {
	if (allRatings.value.length === 0) return 0;
	const total = allRatings.value.reduce((sum, current) => sum + current, 0);
	return total / allRatings.value.length;
});
const fetchUser = async () => {
	try {
		const res = await client.value.get("api/user");
		username.value = res.data.user.username;
	} catch (error) {
		console.log("ERROR", error.message);
	}
};

onMounted(() => {
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
		})
		.catch((error) => {
			console.log("ERROR", error.message);
		});

	console.log("FROM OTHER", route.params.itinerarydata);

	fetchSavedItineraries();
	fetchUser();

	populateDropdown();
	initializeAutocomplete();
	// trackUserLocation();
	findNearestTouristAttractions();
	initializeMaps();
	// checkArrival(destination);
});
const initializeMaps = async () => {
	const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

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

		// Call showLocationOnMap after initializing both maps
		showLocationOntheMap();
	}
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

const fetchItineraries = async () => {
	try {
		itineraryIds.value = list_itineraries.value.map(
			(itinerary) => itinerary.id
		);
		console.log("itineraryIds:", itineraryIds.value);
		checkCode();
		console.log("Total Budget:", budget.value);
		let symbol = currency_list.value.find(
			(currency) => currency[0] === currency_save.value
		)[2];
		selectedSymbol.value = symbol;
		// this.convertedBudget = `${symbol}${total_budget.value}`;
		// // Sort the itineraries by proximity before showing them on the map
		console.log("enter :::", symbol);
		toDropDown.value.value = currency_save.value;
		await sortItinerariesByProximity();
		showLocationOntheMap();
	} catch (error) {
		console.log(error);
	}
};

const fetchSavedItineraries = async () => {
	try {
		if (itinerary_id.value == null) {
			router.push({ name: "itinerary" });
		} else {
			const response = await client.value.get(
				`/api/viewing-itinerary/${itinerary_id.value}`
			);
			itineraries.value = response.data;
			console.log("ITINERARIES", itineraries.value);
			itineraries.value.forEach((itinerary) => {
				itineraryDetails.creator_name = itinerary.creator_name;
				itineraryDetails.user_photo = itinerary.user_photo;
				currency_save.value = itinerary.currency;
				itineraryDetails.date_posted = itinerary.date_posted;
				itineraryDetails.gen_tips = itinerary.gen_tips;
				itineraryDetails.id = itinerary.id;
				list_itineraries.value = itinerary.itineraries;
				itineraryDetails.main_description = itinerary.main_description;
				itineraryDetails.main_image = itinerary.main_image;
				itineraryDetails.main_title = itinerary.main_title;
				itineraryDetails.owner = itinerary.owner;
				itineraryDetails.status = itinerary.status;
				total_budget.value = itinerary.total_budget;
				allRatings.value = itinerary.rating.map((item) => item.rating);
			});
			fetchItineraries();
			paragraphs.value = itineraryDetails.gen_tips.split(/\n+/);
			console.log("this is the paragraph", list_itineraries.value);
		}
	} catch (error) {
		console.error(error);
	}
};
const checkCode = () => {
	const toCurrency = toDropDown.value.value;
	selectedCurrency.value = toCurrency;
	console.log("Selected currency code:", toCurrency);
	selectedSymbol.value = currency_list.value.find(
		(currency) => currency[0] === toCurrency
	)[2];
	let newvalue = 0;
	list_itineraries.value.forEach((itinerary) => {
		console.log("the code ", itinerary);
		if (itinerary.code != toCurrency) {
			if (itinerary.budget.length !== 0) {
				console.log("convert the value to what selected currency");
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
						console.log("in check code if", newvalue.toFixed(2));
						total_budget.value = newvalue.toFixed(2);
						console.log("total_budget == ", total_budget.value);
					});
			}
		} else {
			console.log("do not convert the value to what selected currency");
			newvalue += itinerary.budget;
			total_budget.value = newvalue;
			console.log("in check code else", newvalue);
		}
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
					// this.findNearestTouristAttractions();
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
	const map = new google.maps.Map(document.getElementById("the-map"), {
		center: { lat: latitude, lng: longitude },
		zoom: 8,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
	});

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

const autocomplete = ref(null);

const initializeAutocomplete = () => {
	nextTick(() => {
		// Ensures the DOM is updated
		const inputElement = autocomplete.value;

		const autocompleteInstance = new google.maps.places.Autocomplete(
			inputElement
		);

		autocompleteInstance.addListener("place_changed", () => {
			// Get the place object from the autocomplete widget
			const place = autocompleteInstance.getPlace();

			// Check if the place has a geometry property
			if (place.geometry) {
				// Extract the latitude and longitude from the place's geometry
				latitude.value = place.geometry.location.lat();
				longitude.value = place.geometry.location.lng();
				location.value = place.formatted_address;
				// Now you can use the latitude and longitude for whatever you need
			} else {
				console.log("Selected place does not have a geometry");
			}
		});
	});
};

const findNearestTouristAttractions = async () => {
	const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
	try {
		const location = await getCurrentLocation();

		if (mobileMap.value) {
			const service = new google.maps.places.PlacesService(
				mobileMap.value
			);

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
					console.log("RESULTS Suggested", results);

					results.forEach((place) => {
						const name = place.name;
						const description = place.vicinity;
						let photoUrl = "No photo available";
						if (place.photos && place.photos.length > 0) {
							photoUrl = place.photos[0].getUrl({
								maxWidth: 400,
							});
						} else {
							console.log(`Place: ${place}`);
						}
						const latlngStr = String(place.geometry.location);

						// Extract lat and lng from the string format "(lat, lng)"
						const match = latlngStr.match(/\(([^,]+),\s*([^)]+)\)/);
						if (match) {
							const lat = parseFloat(match[1]);
							const lng = parseFloat(match[2]);

							console.log("latlong::::::", lat, lng);

							// Check if lat and lng are valid numbers
							if (!isNaN(lat) && !isNaN(lng)) {
								// Initialize map
								const map = new google.maps.Map(
									document.getElementById("the-map"),
									{
										center: { lat: lat, lng: lng },
										zoom: 15,
									}
								);
								// Add a marker to the new center using AdvancedMarkerElement
								new google.maps.marker.AdvancedMarkerElement({
									position: { lat: lat, lng: lng },
									map: map,
									title: "Suggested Place Marker",
								});
							} else {
								console.error(
									"Invalid latitude or longitude values"
								);
							}
						} else {
							console.error("Invalid latlng format");
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

const closeModal = () => {
	showModal.value = false;
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
	console.log(`User selected rating: ${star}`); // Log the user input rating
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

	console.log("Submit rating to backend:", data);
	hasSubmitted.value = true;
	// ADD SUBMIT RATING TO BACKEND HERE
	try {
		const response = await client.value.put("api/ratings/", data);
		console.log("Rating submitted successfully:", response.data);
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
const locateSuggestedPlace = (latlng) => {
	const latlngStr = String(geometry.location);
	const match = latlngStr.match(/$$([^,]+),\s*([^)]+)$$/);

	if (match) {
		const lat = parseFloat(match[1]);
		const lng = parseFloat(match[2]);

		if (!isNaN(lat) && !isNaN(lng)) {
			const center = { lat, lng };
			desktopMap.value.setCenter(center);
			desktopMap.value.setZoom(15);
			mobileMap.value.setCenter(center);
			mobileMap.value.setZoom(15);

			new google.maps.marker.AdvancedMarkerElement({
				position: center,
				map: desktopMap.value,
				title: "Suggested Place",
			});
			new google.maps.marker.AdvancedMarkerElement({
				position: center,
				map: mobileMap.value,
				title: "Suggested Place",
			});

			if (!showMap.value) {
				toggleMap();
			}
		} else {
			console.error("Invalid latitude or longitude values");
		}
	} else {
		console.error("Invalid latlng format");
	}
};
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
