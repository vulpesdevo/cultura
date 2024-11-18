<template>
	<div class="flex sm:w-full">
		<div
			class="flex flex-col items-center align-middle sm:w-[65%] px-5 sm:px-12 overflow-auto h-screen bg-field dark:bg-notif sm:pt-0"
		>
			<!-- Header -->
			<div
				class="field-editable flex flex-col justify-start items-center w-full bg-fiel sm:bg-white dark:bg-notif rounded-2xl sm:rounded-none px-1"
			>
				<div
					class="fixed sm:relative flex flex-col justify-between title-image h-[15rem] sm:h-72 w-screen sm:w-full rounded-2xl dark:bg-notif bg-field sm:bg-transparent z-10"
				>
					<img
						:src="itineraryDetails.main_image"
						alt=""
						class="w-full h-full object-cover brightness-[.25]"
					/>
					<h1
						class="absolute bottom-0 left-5 font-bebas-neue text-3xl text-interface sm:text-5xl"
					>
						{{ itineraryDetails.main_title }}
					</h1>

					<!-- RATING DISPLAY CONTAINER -->
					<div
						class="flex items-center absolute bottom-0 right-5 mb-2"
					>
						<i
							class="fa-solid fa-star sm:text-3xl text-xl text-second"
						></i>
						<div
							class="sm:text-2xl ml-2 font-montserrat text-lg text-white"
						>
							{{ avgRating.toFixed(1) }} / 5
						</div>
					</div>
				</div>
				<section
					class="mt-64 itinerary-1 flex flex-col items-center sm:mt-10 px-10 w-full"
					id="overview-section"
				>
					<div
						class="flex flex-col w-screen sm:w-full sm:-mt-7 items-end sm:-mb-10 -mb-8"
					>
						<!-- Disable button if the user has already submitted their rating -->
						<button
							@click="submitRating"
							class="text-white flex mr-5 font-montserrat"
							:disabled="hasSubmitted"
						>
							{{
								hasSubmitted
									? "Rating Submitted"
									: "Submit a Rating"
							}}
						</button>
						<div class="flex">
							<div
								v-for="star in 5"
								:key="star"
								class="relative flex items-center"
								@mouseover="!hasSubmitted && hoverRating(star)"
								@mouseleave="!hasSubmitted && resetRating"
								@click="!hasSubmitted && setRating(star)"
							>
								<!-- Full star when hovered or rated -->
								<i
									:class="{
										'fa-solid fa-star text-second':
											star <= (tempRating || rating),
										'fa-regular fa-star text-gray-300':
											star > (tempRating || rating),
									}"
									class="text-2xl cursor-pointer mr-2"
								></i>

								<input
									type="radio"
									:id="'star' + star"
									:value="star"
									v-model="rating"
									class="hidden"
								/>
							</div>
						</div>
					</div>
					<div class="post-content flex w-screen sm:w-full">
						<button @click="showLocationOntheMap()">
							Optimize
						</button>
						<div
							class="hidden w-[9.2%] sm:flex items-start justify-center"
						>
							<img
								:src="itineraryDetails.user_photo"
								alt="Profile"
								class="size-10 rounded-full cursor-pointer"
							/>
						</div>
						<div class="w-full mx-3 mt-3 sm:m-0">
							<div
								class="flex flex-row items-start border-b-2 border-gray-700 justify-between"
							>
								<div class="">
									<small
										class="hidden sm:flex items-center justify-center font-montserrat text-prime dark:text-interface text-sm pb-1"
									>
										@{{ itineraryDetails.creator_name }}
									</small>
									<small
										class="hidden sm:flex pl-5 pb-3 text-second"
										>{{
											new Date(
												itineraryDetails.date_posted
											).toLocaleDateString("en-US", {
												month: "long",
												day: "numeric",
												year: "numeric",
											})
										}}</small
									>

									<p
										class="font-montserrat sm:hidden pb-1 text-lg text-prime dark:text-interface"
									>
										Description
									</p>
								</div>
							</div>
							<p
								class="w-full sm:w-[90.5%] p-4 text-justify text-sm dark:text-interface font-montserrat"
							>
								{{ itineraryDetails.main_description }}
							</p>
						</div>
					</div>
					<div
						class="flex flex-col items-center justify-center w-screen sm:mx-0 sm:mt-4 sm:w-full"
					>
						<p
							class="font-montserrat text-prime dark:text-interface w-full px-1 mb-1 text-lg sm:text-lg sm:font-medium tracking-wide border-b border-gray-700"
						>
							General Tips
						</p>
						<div
							class="flex flex-col items-start justify-center w-full px-3 sm:px-0 sm:w-[83%]"
						>
							<p
								class="w-full text-justify text-sm p-4 dark:text-interface font-montserrat"
								v-for="(paragraph, index) in paragraphs"
								:key="index"
								v-html="formatText(paragraph)"
							></p>
						</div>
					</div>
					<div
						class="font-montserrat flex flex-col justify-center items-center w-screen sm:w-full py-3"
					>
						<p
							class="text-prime dark:text-interface text-lg sm:text-xl sm:font-medium tracking-wide m-3 pl-3 sm:px-2 w-full text-left font-montserrat"
						>
							Budgeting
						</p>
						<div
							class="flex sm:justify-between w-full px-3 sm:p-0 sm:w-[83%] h-20 text-interface"
						>
							<div
								class="flex flex-col justify-center items-center bg-prime dark:bg-dark-interface w-1/2 mr-2 rounded-lg"
							>
								<p
									class="font-montserrat text-center sm:text-start"
								>
									Suggested Budget
								</p>
								<p class="text-sm sm:text-2xl">
									<span class="font-bold">{{
										selectedSymbol
									}}</span
									>{{ total_budget }}
								</p>
							</div>
							<div
								class="flex flex-col justify-center bg-prime dark:bg-dark-interface w-3/4 rounded-lg p-3"
							>
								<p class="">Currency</p>
								<select
									ref="toDropDown"
									@change="checkCode"
									class="w-full text-white pb-1 text-sm sm:text-xl bg-transparent outline-none"
								>
									<!-- Options will be populated by the method -->
								</select>
							</div>
						</div>
					</div>
				</section>
				<section
					class="itinerary-2 pt-10 sm:pt-0 flex flex-col h-auto w-screen sm:w-full my-5"
					id="itinerary-section"
				>
					<h1
						class="sm:flex items-center justify-center text-center text-prime dark:text-interface tracking-wider text-xl mb-4"
					>
						Main Itinerary
					</h1>
					<div
						id="the-itineraries"
						class="flex justify-center w-full h-auto px-3 pb-5 sm:px-5"
					>
						<div
							class="flex flex-col justify-center-center w-full sm:w-full m-0 pb-3 sm:pb-0"
						>
							<div
								class="sm:overflow-auto grid grid-cols-1 sm:grid-cols-2 gap-2 h-auto rounded-lg"
								style="scrollbar-width: none"
							>
								<div
									class="flex-col justify-center items-center w-full h-56 sm:h-80 font-montserrat text-prime bg-white dark:bg-dark-interface sm:bg-interface drop-shadow-md mb-3 rounded-lg"
									v-for="(
										itinerary, index
									) in list_itineraries"
									:key="index"
								>
									<div
										class="absolute w-full marker-container flex items-start justify-between p-4"
									>
										<svg
											width="64px"
											height="64px"
											viewBox="-4 0 36 36"
											version="1.1"
											xmlns="http://www.w3.org/2000/svg"
											xmlns:xlink="http://www.w3.org/1999/xlink"
											fill="#000000"
										>
											<defs>
												<filter
													id="icon-shadow"
													x="-50%"
													y="-50%"
													width="200%"
													height="200%"
												>
													<feDropShadow
														dx="0"
														dy="2"
														stdDeviation="3"
														flood-color="rgba(0,0,0,0.5)"
													/>
												</filter>
											</defs>
											<g filter="url(#icon-shadow)">
												<g
													id="SVGRepo_bgCarrier"
													stroke-width="0"
												></g>
												<g
													id="SVGRepo_tracerCarrier"
													stroke-linecap="round"
													stroke-linejoin="round"
												></g>
												<g id="SVGRepo_iconCarrier">
													<title>
														{{ itinerary.title }}
													</title>
													<desc>
														Created with Sketch.
													</desc>
													<g
														id="Vivid.JS"
														stroke="none"
														stroke-width="1"
														fill="none"
														fill-rule="evenodd"
													>
														<g
															id="Vivid-Icons"
															transform="translate(-125.000000, -643.000000)"
														>
															<g
																id="Icons"
																transform="translate(37.000000, 169.000000)"
															>
																<g
																	id="map-marker"
																	transform="translate(78.000000, 468.000000)"
																>
																	<g
																		transform="translate(10.000000, 6.000000)"
																	>
																		<path
																			d="M14,0 C21.732,0 28,5.641 28,12.6 C28,23.963 14,36 14,36 C14,36 0,24.064 0,12.6 C0,5.641 6.268,0 14,0 Z"
																			id="Shape"
																			fill="#1A193F"
																		></path>
																		<circle
																			id="Oval"
																			fill="#1A193F"
																			fill-rule="nonzero"
																			cx="14"
																			cy="14"
																			r="7"
																		></circle>
																		<!-- Adding the letter A -->
																		<text
																			x="11"
																			y="20"
																			font-family="Arial"
																			font-size="10"
																			fill="#FFFFFF"
																		>
																			{{
																				itinerary.order
																			}}
																		</text>
																	</g>
																</g>
															</g>
														</g>
													</g>
												</g>
											</g>
										</svg>
									</div>
									<img
										class="w-full object-cover h-2/5 rounded-lg"
										:src="itinerary.place_image"
										alt=""
									/>
									<div
										class="font-montserrat px-4 flex flex-col justify-normal sm:justify-between items-left"
									>
										<h1
											class="text-2xl px-4 py-3 text-left dark:text-interface truncate"
										>
											{{ itinerary.title }}
										</h1>
										<p
											class="text-left text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16 dark:text-interface"
										>
											{{ itinerary.description }}
										</p>
										<div
											class="fixed bottom-0 left-0 mb-2 flex w-full h-8 text-center items-center justify-end sm:justify-center"
										>
											<p
												class="flex justify-start items-center font-montserrat font-semibold h-full text-sm text-interface bg-second w-28 rounded-full"
											>
												<span class="pr-2 mr-2 ml-3">{{
													getSymbol(itinerary.code)
												}}</span>
												{{
													itinerary.budget.toFixed(2)
												}}
											</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</section>
				<section
					class="itinerary-2 pt-10 sm:pt-0 flex flex-col h-[45rem] w-screen sm:w-full my-5"
					id="itinerary-section"
				>
					<h1
						class="sm:flex items-center justify-center text-center text-prime dark:text-interface tracking-wider text-xl mb-4"
					>
						Suggested Places
					</h1>
					<p
						class="font-montserrat hidden sm:flex items-center justify-center text-justify text-prime dark:text-interface tracking-wider text-xs mb-4 mx-5"
					>
						The following are CulturaLink's suggested stops along
						your itinerary, offering travelers more opportunities to
						explore the cultural, historical, and traditional
						insights of place you're visiting.
					</p>
					<div
						id="the-itineraries"
						class="flex justify-center w-full h-auto px-3 pb-5 sm:px-5"
					>
						<div
							class="flex flex-col justify-center-center w-full sm:w-full m-0 pb-5 sm:pb-0"
						>
							<div
								class="sm:overflow-auto grid grid-cols-1 sm:grid-cols-2 gap-2 h-auto rounded-lg"
								style="scrollbar-width: none"
							>
								<div
									class="flex-col justify-center items-center w-full h-32 sm:h-60 font-montserrat text-prime bg-white dark:bg-dark-interface sm:bg-interface drop-shadow-md mb-3 rounded-lg cursor-pointer z-20"
									v-for="(place, index) in suggested_places"
									:key="index"
									@click="
										locateSuggestedPlace(place.geometry)
									"
								>
									<img
										v-if="place?.photos?.length > 0"
										class="w-full object-cover h-2/5 rounded-lg"
										:src="place.photos[0].getUrl()"
										alt=""
									/>
									<div
										class="font-montserrat px-2 flex flex-col justify-normal sm:justify-between items-left"
									>
										<div
											class="text-end text-xs px-4 py-3 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full dark:text-interface"
										>
											rating: {{ place.rating }}
										</div>

										<h1
											class="text-sm px-4 py-3 text-left dark:text-interface truncate"
										>
											{{ place.name }}
										</h1>

										<div class="w-full px-5">
											<ul
												class="w-full grid grid-cols-2 list-disc justify-end"
											>
												<li
													class="text-xs text-prime dark:text-interface text-wrap"
													v-for="(
														type, index
													) in place.types"
													:key="index"
												>
													{{ type }}
												</li>
											</ul>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</section>
			</div>

			<!-- Floating Action Button -->
			<button
				class="flex sm:hidden items-center justify-center fixed bottom-20 right-5 bg-second active:bg-prime text-white font-bold rounded-full h-16 w-16 z-40"
				@click="toggleMap"
			>
				<span class="material-icons-outlined"> map </span>
				<!-- Icon or text for your button -->
			</button>
		</div>
		<div
			:class="{
				'translate-y-0': showMap,
				'translate-y-full': !showMap,
				'duration-500': true,
				'ease-in-out': true,
			}"
			class="absolute sm:fixed sm:flex h-full items-center w-screen sm:w-1/3 rounded-lg sm:rounded-none bottom-0 right-0 transform sm:transform-none z-20 bg-interface overflow-hidden sm:overflow-visible"
		>
			<div id="the-map" class="the-map h-full w-full rounded-lg"></div>
		</div>
		<div
			v-if="showModal"
			class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50"
		>
			<div class="bg-white rounded-lg shadow-lg p-6 w-4/5 sm:w-1/2">
				<span
					class="text-gray-500 float-right text-2xl font-bold cursor-pointer"
					@click="closeModal"
					>&times;</span
				>
				<p class="mt-4">{{ arrivalMessage }}</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, reactive, nextTick, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

const route = useRoute();

const user_id = ref("");
const rating = ref(0); // Current user's rating
const tempRating = ref(0); // Used for hover effect
const hasSubmitted = ref(false);
// Uncomment this line to use the initial ratings from the backend
// const allRatings = ref([4, 3.5, 5, 4.2]); // Simulated ratings from different users
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
const isMobile = computed(() => window.innerWidth < 768);

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
	// checkArrival(destination);
});
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

const showLocationOntheMap = () => {
	if (list_itineraries.value.length === 0) {
		// If list_itineraries is empty, use the user's current location or a default location
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				initializeMap(latitude, longitude);
			},
			() => {
				// Fallback to a default location if unable to get the user's location
				const defaultLat = 37.7749; // Example default latitude
				const defaultLng = -122.4194; // Example default longitude
				initializeMap(defaultLat, defaultLng);
			}
		);
	} else {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				const map = new google.maps.Map(
					document.getElementById("the-map"),
					{
						mapTypeId: google.maps.MapTypeId.ROADMAP,
						mapId: "2c9b57c42de97202",
					}
				);

				let bounds = new google.maps.LatLngBounds();
				const directionsService = new google.maps.DirectionsService();
				const directionsRenderer = new google.maps.DirectionsRenderer({
					map: map,
				});

				// Assuming the first item is the start, the last is the end, and the rest are waypoints
				const start = { latitude, longitude }; // Use current location as start
				const end =
					list_itineraries.value[list_itineraries.value.length - 1];
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
					origin: new google.maps.LatLng(
						start.latitude,
						start.longitude
					),
					destination: new google.maps.LatLng(
						end.latitude,
						end.longitude
					),
					waypoints: waypoints,
					travelMode: google.maps.TravelMode.DRIVING,
					optimizeWaypoints: false, // Set to true if you want Google to reorder the waypoints for the shortest route
				};

				directionsService.route(request, (result, status) => {
					if (status == google.maps.DirectionsStatus.OK) {
						directionsRenderer.setDirections(result);
					} else {
						console.error(
							"Directions request failed due to " + status
						);
					}
				});

				// Extend bounds to include start and end
				bounds.extend(
					new google.maps.LatLng(start.latitude, start.longitude)
				);
				bounds.extend(
					new google.maps.LatLng(end.latitude, end.longitude)
				);
				map.fitBounds(bounds);

				// Check arrival at destination
				checkArrival(end);
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
		const mapId = "2c9b57c42de97202";
		const map1 = new google.maps.Map(document.getElementById("the-map"));

		const service = new google.maps.places.PlacesService(map1);

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
						photoUrl = place.photos[0].getUrl({ maxWidth: 400 });
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
									mapId: mapId,
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
</script>

<style scoped></style>
