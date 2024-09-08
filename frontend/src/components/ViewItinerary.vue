<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field dark:bg-notif pt-14 sm:pt-3"
	>
		<!-- Header -->

		<div
			class="field-editable flex flex-col justify-start items-center w-full bg-fiel sm:bg-white dark:sm:bg-dark-interface dark:bg-notif rounded-2xl p-1"
		>
			<div
				class="fixed sm:relative flex flex-col justify-between title-image h-[20rem] sm:h-96 w-screen sm:w-full rounded-2xl dark:bg-notif bg-field sm:bg-transparent z-10"
			>
				<div
					class="w-screen sm:w-full sm:h-[87%] h-[14rem] bg-second sm:rounded-2xl"
				>
					<img
						:src="itineraryDetails.main_image"
						alt=""
						class="w-full h-full object-cover sm:rounded-2xl"
					/>
				</div>
				<div
					class="flex absolute left-[3.2rem] bottom-[4rem] sm:bottom-0 sm:left-[7.7rem] bg-prime w-3/4 h-16 sm:h-24 z-10 rounded-md text-center items-center justify-center"
				>
					<div class="w-full mx-5">
						<!-- Text Field for Editing -->

						<!-- Text Display -->
						<h1
							class="font-bebas-neue text-lg text-interface sm:text-5xl"
						>
							{{ itineraryDetails.main_title }}
						</h1>
					</div>
				</div>
				<div
					class="sm:hidden flex items-center justify-center h-14 w-full"
					id="navs"
				></div>
			</div>

			<section
				class="mt-80 itinerary-1 flex flex-col items-center sm:mt-10 px-16 w-full"
				id="overview-section"
			>
				<div class="post-content flex w-screen sm:w-full">
					<div
						class="hidden w-[9.2%] sm:flex items-start justify-center"
					>
						<img
							:src="itineraryDetails.user_photo"
							alt="Profile"
							class="w-14 h-14 rounded-full cursor-pointer"
						/>
					</div>
					<div class="w-full mx-3 mt-3 sm:m-0">
						<div class="flex flex-col items-start border-b-2">
							<small
								class="hidden sm:flex items-center justify-center font-montserrat text-prime dark:text-interface text-base pb-1"
							>
								@{{ itineraryDetails.creator_name }}
							</small>
							<small class="hidden sm:flex pl-5 pb-3 text-second"
								>date here</small
							>
							<p
								class="font-montserrat sm:hidden pb-1 text-lg text-prime dark:text-interface"
							>
								Description
							</p>
						</div>
						<p
							class="w-full sm:w-[90.5%] p-4 text-justify dark:text-interface"
						>
							{{ itineraryDetails.main_description }}
						</p>
					</div>
				</div>
				<div
					class="flex flex-col items-center justify-center w-screen sm:mx-0 sm:mt-4 sm:w-full"
				>
					<p
						class="font-montserrat text-prime dark:text-interface w-full px-3 mb-1 text-lg sm:text-xl sm:font-semibold border-b"
					>
						General Tips
					</p>

					<div
						class="flex flex-col items-start justify-center w-full px-3 sm:px-0 sm:w-[83%]"
					>
						<p
							class="w-full text-justify p-4 dark:text-interface"
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
						class="text-prime dark:text-interface text-lg sm:text-xl sm:font-semibold m-3 pl-3 sm:px-2 w-full text-left"
					>
						Budgeting
					</p>

					<div
						class="flex sm:justify-between w-full px-3 sm:p-0 sm:w-[83%] h-20 text-interface"
					>
						<div
							class="flex flex-col justify-center items-center bg-prime w-1/2 mr-2 rounded-lg"
						>
							<p class="">Total Budget</p>
							<p class="text-sm sm:text-2xl">
								<span class="font-bold">{{
									selectedSymbol
								}}</span
								>{{ total_budget }}
							</p>
						</div>
						<div
							class="flex flex-col justify-center bg-prime w-3/4 rounded-lg p-3"
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
				class="itinerary-2 pt-10 sm:pt-0 flex flex-col h-[45rem] w-screen sm:w-full my-5"
				id="itinerary-section"
			>
				<h1
					class="hidden sm:flex items-center justify-center text-center text-prime dark:text-interface text-xl mb-4"
				>
					Main Itinerary
				</h1>
				<div
					id="the-itineraries"
					class="flex justify-center w-full h-auto sm:h-[700px] px-3 pb-5 sm:px-16"
				>
					<div
						class="flex flex-col justify-center-center w-full sm:w-1/2 m-0 sm:mr-5 pb-5 sm:pb-0"
					>
						<div
							class="sm:overflow-auto h-screen rounded-lg px-3"
							style="scrollbar-width: none"
						>
							<div
								class="flex-col justify-center items-center w-full h-56 sm:h-80 font-montserrat text-prime bg-white dark:bg-dark-second-dark sm:bg-interface drop-shadow-md mb-3 rounded-lg"
								v-for="(itinerary, index) in list_itineraries"
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
																		fill="#6A7FDB"
																	></path>
																	<circle
																		id="Oval"
																		fill="#6A7FDB"
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
									class="px-4 flex flex-col justify-normal sm:justify-evenly items-left"
								>
									<h1
										class="text-2xl px-4 py-3 text-left dark:text-interface"
									>
										{{ itinerary.title }}
									</h1>
									<p
										class="text-left text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16 dark:text-interface"
									>
										{{ itinerary.description }}
									</p>
									<div
										class="flex w-full h-8 text-center items-center justify-end sm:justify-center"
									>
										<p
											class="flex justify-start items-center font-montserrat font-semibold h-full text-sm text-interface bg-second w-28 rounded-full"
										>
											<span class="pr-2 mr-2 ml-3">{{
												getSymbol(itinerary.code)
											}}</span>
											{{ itinerary.budget.toFixed(2) }}
										</p>
									</div>
									<!-- <p class="rounded-full bg-second text-center inline-block py-1 px-2"
										:style="{ width: `${text.length * 10}px` }"
									>{{ text }}</p> -->
								</div>
							</div>
						</div>
					</div>
					<div
						:class="{
							'translate-y-0': showMap,
							'translate-y-full': !showMap,

							'duration-500': true,
							'ease-in-out': true,
						}"
						class="absolute sm:static sm:flex h-full items-center w-screen sm:w-1/2 rounded-lg bottom-0 left-0 transform sm:transform-none z-20 bg-interface overflow-hidden sm:overflow-visible"
					>
						<div
							id="the-map"
							class="the-map h-full w-full rounded-lg"
						></div>
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
</template>

<script>
import axios from "axios";
import { ref } from "vue";
// import { Loader } from "@googlemaps/js-api-loader";
import router from "../routes";
export default {
	data() {
		return {
			paragraphs: [],

			isEditing: true,
			main_title: "ITINERARY TITLE",

			total_budget: 0,
			convertedBudget: "",
			api: "https://v6.exchangerate-api.com/v6/dfbd57179cf6a5ebcd1a6b59/latest/USD",
			currency_list: [
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
			],
			selectedCurrency: "",
			selectedSymbol: "",
			currency_save: "",
			converted: 0,

			username: "",

			location: "",
			title: "",
			budget: "",
			description: "",
			latitude: "",
			longitude: "",
			showModal: false,
			client: null, // Initialize axios client later

			showModal: false,
			latitude: 0,
			longitude: 0,
			location: null,
			list_itineraries: [],
			itineraryIds: [],
			itinerariesfrom: [],

			// This property controls which view is currently visible
			currentView: "itinerary", // 'overview' or 'itinerary'
			showMap: false,

			itinerary_id: this.$route.params.itinerarydata,
			itineraryDetails: {
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
			},
			nearestTouristInterest: null,
		};
	},
	computed: {
		// Define isMobile as a computed property
		isMobile() {
			// This example uses 768px as the threshold for mobile devices
			return window.innerWidth < 768;
		},
	},
	// watch: {
	// 	total_budget(newVal, oldVal) {
	// 		if (newVal !== oldVal) {
	// 			this.convertCurrency();
	// 		}
	// 	},
	// 	selectedCurrency(newVal, oldVal) {
	// 		if (newVal !== oldVal) {
	// 			this.convertCurrency();
	// 		}
	// 	},
	// },
	// props: {
	// 	// Define props here. For example, if you want to pass an itinerary, you can define it like this:
	// 	itineraryid: {
	// 		type: Object,
	// 		required: true,
	// 	},
	// 	// Add other props as needed
	// },
	created() {
		// this.itineraryfrom = this.$route.params.itinerarydata;
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		this.client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: headers,
		});
		this.client
			.get("api/user")
			.then((res) => {
				this.username = res.data.user.username;
			})
			.catch((error) => {
				console.log("ERROR", error.message);
			});
		console.log("FROM  OTHER", this.itineraryfrom);

		this.fetchSavedItineraries();
	},
	mounted() {
		this.populateDropdown();
		this.fetchSavedItineraries();
		this.initializeAutocomplete();
	},
	filters: {},
	methods: {
		async fetchSavedItineraries() {
			try {
				if (this.itinerary_id == null) {
					//
				} else {
					const response = await this.client.get(
						`/api/viewing-itinerary/${this.itinerary_id}`
					);
					this.itineraries = response.data;
					console.log("ITINERARIES", this.itineraries);
					this.itineraries.forEach((itinerary) => {
						this.itineraryDetails.creator_name =
							itinerary.creator_name;
						this.itineraryDetails.user_photo = itinerary.user_photo;
						this.currency_save = itinerary.currency;
						this.itineraryDetails.date_posted =
							itinerary.date_posted;
						this.itineraryDetails.gen_tips = itinerary.gen_tips;
						this.itineraryDetails.id = itinerary.id;
						this.list_itineraries = itinerary.itineraries;
						this.itineraryDetails.main_description =
							itinerary.main_description;
						this.itineraryDetails.main_image = itinerary.main_image;
						this.itineraryDetails.main_title = itinerary.main_title;
						this.itineraryDetails.owner = itinerary.owner;
						this.itineraryDetails.status = itinerary.status;
						this.total_budget = itinerary.total_budget;
					});
					this.fetchItineraries();
					// this.convertCurrency()
					this.paragraphs =
						this.itineraryDetails.gen_tips.split(/\n+/);
					console.log("this is the paragraph", this.list_itineraries);
				}
			} catch (error) {
				console.error(error);
			}
		},
		formatText(text) {
			return text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>"); // replace **text** with <strong>text</strong>
		},
		populateDropdown() {
			this.toDropDown = this.$refs.toDropDown;
			this.currency_list.forEach((currency) => {
				const [code, countryName] = currency;
				const option = document.createElement("option");
				option.value = code;
				option.textContent = `${code} - ${countryName}`;

				option.classList.add("text-prime", "bg-interface");
				this.toDropDown.add(option);
			});

			// this.getSelectedCurrencyCode();
			// this.convertCurrency(); // Assuming you want to set the default selected value
		},
		getSymbol(code) {
			for (let i = 0; i < this.currency_list.length; i++) {
				if (this.currency_list[i][0] === code) {
					return this.currency_list[i][2];
				}
			}
			return null; // or some default value if code is not found
		},
		checkCode() {
			const toCurrency = this.$refs.toDropDown.value;
			this.selectedCurrency = toCurrency;
			console.log("Selected currency code:", toCurrency);
			this.selectedSymbol = this.currency_list.find(
				(currency) => currency[0] === toCurrency
			)[2];
			let newvalue = 0;
			this.list_itineraries.forEach((itinerary) => {
				// Your code here
				console.log("the code ", itinerary);
				if (itinerary.code != toCurrency) {
					//convert to selected currency
					// this.indivConvert(this.selectedCurrency, itinerary.code);
					if (itinerary.budget.length !== 0) {
						console.log(
							"convert the value to what selected currency"
						);
						fetch(this.api) // Assuming 'this.api' is your API URL
							.then((resp) => resp.json())
							.then((data) => {
								let fromExchangeRate =
									data.conversion_rates[itinerary.code];
								let toExchangeRate =
									data.conversion_rates[toCurrency];
								const convertedAmount =
									(itinerary.budget / fromExchangeRate) *
									toExchangeRate;

								// Find the symbol for the target currency

								// const finalAmount = `${symbol} ${convertedAmount.toFixed(
								// 	2
								// )}`;
								// this.total_budget = convertedAmount.toFixed(2);

								newvalue += parseFloat(
									convertedAmount.toFixed(2)
								);
								console.log(
									"in check code if",
									newvalue.toFixed(2)
								);
								this.total_budget = newvalue.toFixed(2);
								console.log(
									"total_budget == ",
									this.total_budget
								);
								// this.convertedBudget = finalAmount;
								// this.indivConvert(toExchangeRate, fromExchangeRate);
								// Assuming 'result' is a reference to an element for displaying the result
								// this.$refs.result.innerHTML = `${this.total_budget} ${fromCurrency} = ${convertedAmount.toFixed(
								// 	2
								// )} ${toCurrency}`;
							});
					}
				} else {
					//add to total budget

					console.log(
						"do not convert the value to what selected currency"
					);
					newvalue += itinerary.budget;
					this.total_budget = newvalue;
					console.log("in check code else", newvalue);
				}
			});
		},
		handleTitleChange() {
			if (this.main_title.trim() === "") {
				this.main_title = "ITINERARY TITLE";
			}
			this.isEditing = false;
		},
		toggleMap() {
			this.showMap = !this.showMap;
		},
		showItinerary(view) {
			this.currentView = view;

			this.$nextTick(() => {
				const navHeight = document.querySelector("#navs")
					? document.querySelector("#navs").offsetHeight
					: 0;
				let targetSection;

				if (view === "itinerary") {
					targetSection =
						document.getElementById("itinerary-section");
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
		},

		getCurrentLocation() {
			return new Promise((resolve, reject) => {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(
						(position) => {
							resolve({
								latitude: position.coords.latitude,
								longitude: position.coords.longitude,
							});
							this.findNearestTouristAttractions();
						},
						(error) => {
							reject(error);
						}
					);
				} else {
					reject(
						new Error(
							"Geolocation is not supported by this browser."
						)
					);
				}
			});
		},

		//search nearby tourist attractions
		async findNearestTouristAttractions() {
			const { AdvancedMarkerElement } = await google.maps.importLibrary(
				"marker"
			);
			try {
				const location = await this.getCurrentLocation();
				const map = new google.maps.Map(
					document.getElementById("the-map")
				);
				const service = new google.maps.places.PlacesService(map);

				const request = {
					location: new google.maps.LatLng(
						location.latitude,
						location.longitude
					),
					radius: "1500",
					type: ["tourist_attraction"],
				};

				service.nearbySearch(request, (results, status) => {
					if (status === google.maps.places.PlacesServiceStatus.OK) {
						results.forEach((place) => {
							const name = place.name;
							const description = place.vicinity;
							let photoUrl = "No photo available";
							if (place.photos && place.photos.length > 0) {
								const photoUrl = place.photos[0].getUrl({
									maxWidth: 400,
								});
								console.log(
									`Place: ${place.geometry.location}, Photo URL: ${photoUrl}`
								);
							} else {
								console.log(
									`Place: ${place.name}, No photo available`
								);
							}

							const marker = new AdvancedMarkerElement({
								map: map,
								position: place.geometry.location,
								title: place.name,
							});

							// Add an info window for each marker
							const infoWindow = new google.maps.InfoWindow({
								content: `<div><strong>${name}</strong><br>${description}<br><img src="${photoUrl}" alt="${name}" style="max-width: 100px;"></div>`,
							});

							marker.addListener("click", () => {
								infoWindow.open(
									new google.maps.Map(
										document.getElementById("the-map")
									),
									marker
								);
							});
						});
					} else {
						console.error(
							"Error finding tourist attractions:",
							status
						);
					}
				});
			} catch (error) {
				console.error(
					"Error finding nearest tourist attractions:",
					error
				);
			}
		},

		// Step 2 & 3: Calculate Distances and Sort Itineraries
		async sortItinerariesByProximity() {
			try {
				const currentLocation = await this.getCurrentLocation();
				this.list_itineraries.forEach((itinerary) => {
					itinerary.distance = this.calculateDistance(
						currentLocation.latitude,
						currentLocation.longitude,
						itinerary.latitude,
						itinerary.longitude
					);
				});

				this.list_itineraries.sort((a, b) => a.distance - b.distance);
				this.list_itineraries.forEach((itinerary, index) => {
					itinerary.order = String.fromCharCode(65 + index);
				});

				// After sorting, you can now update the map
				this.showLocationOntheMap();
			} catch (error) {
				console.error(error);
			}
		},

		// Helper Method: Calculate Distance Between Two Coordinates
		calculateDistance(lat1, lon1, lat2, lon2) {
			const R = 6371; // Radius of the earth in km
			const dLat = this.deg2rad(lat2 - lat1);
			const dLon = this.deg2rad(lon2 - lon1);
			const a =
				Math.sin(dLat / 2) * Math.sin(dLat / 2) +
				Math.cos(this.deg2rad(lat1)) *
					Math.cos(this.deg2rad(lat2)) *
					Math.sin(dLon / 2) *
					Math.sin(dLon / 2);
			const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
			const distance = R * c; // Distance in km
			return distance;
		},

		// Helper Method: Convert Degrees to Radians
		deg2rad(deg) {
			return deg * (Math.PI / 180);
		},
		async fetchItineraries() {
			try {
				this.itineraryIds = this.list_itineraries.map(
					(itinerary) => itinerary.id
				);
				console.log("itineraryIds:", this.itineraryIds);
				this.checkCode();
				console.log("Total Budget:", this.budget);
				let symbol = this.currency_list.find(
					(currency) => currency[0] === this.currency_save
				)[2];
				this.selectedSymbol = symbol;
				// this.convertedBudget = `${symbol}${this.total_budget}`;
				// // Sort the itineraries by proximity before showing them on the map
				console.log("enter :::", symbol);
				this.$refs.toDropDown.value = this.currency_save;
				await this.sortItinerariesByProximity();
				this.showLocationOntheMap();
			} catch (error) {
				console.log(error);
			}
		},
		initializeMap(latitude, longitude) {
			new google.maps.Map(document.getElementById("the-map"), {
				center: { lat: latitude, lng: longitude },
				zoom: 8,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
			});

			// Optionally, add a marker at the location
		},
		showLocationOntheMap() {
			// const lat = 37.7749;
			// const lng = -122.4194;
			if (this.list_itineraries.length === 0) {
				// If list_itineraries is empty, use the user's current location or a default location
				navigator.geolocation.getCurrentPosition(
					(position) => {
						const { latitude, longitude } = position.coords;
						this.initializeMap(latitude, longitude);
					},
					() => {
						// Fallback to a default location if unable to get the user's location
						const defaultLat = 37.7749; // Example default latitude
						const defaultLng = -122.4194; // Example default longitude
						this.initializeMap(defaultLat, defaultLng);
					}
				);
			} else {
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
				const start = this.list_itineraries[0];
				const end =
					this.list_itineraries[this.list_itineraries.length - 1];
				const waypoints = this.list_itineraries
					.slice(1, -1)
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
			}
			// Optional: adjust the zoom level after fitting bounds if the zoom is too close or too far
			// This is a workaround because fitBounds does not let you specify max zoom level
		},
		initializeAutocomplete() {
			this.$nextTick(() => {
				// Ensures the DOM is updated
				const inputElement = this.$refs.autocomplete;

				// Define the bounds for the Cavite area

				const autocomplete = new google.maps.places.Autocomplete(
					inputElement
				);

				autocomplete.addListener("place_changed", () => {
					// Get the place object from the autocomplete widget
					const place = autocomplete.getPlace();

					// Check if the place has a geometry property
					if (place.geometry) {
						// Extract the latitude and longitude from the place's geometry
						this.latitude = place.geometry.location.lat();
						this.longitude = place.geometry.location.lng();
						this.location = place.formatted_address;
						// Now you can use the latitude and longitude for whatever you need
					} else {
						console.log("Selected place does not have a geometry");
					}
				});
			});
		},
		locatorBtn() {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition(
					(position) => {
						const { latitude, longitude } = position.coords;
						this.getAddressFrom(latitude, longitude);
					},
					(error) => {
						console.log(error.message);
					}
				);
			}
		},
		getAddressFrom(lat, long) {
			axios
				.get(
					`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${long}&key=AIzaSyAlo4jqabMxIygmvXtD-K0tm1HJEecnrEA`
				)
				.then((response) => {
					const address = response.data.error_message
						? response.data.error_message
						: response.data.results[0].formatted_address;

					console.log(address);
					const inputElement = this.$refs.autocomplete;
					inputElement.value = address;
				})
				.catch((error) => {
					console.log(error.message);
				});
		},
	},
};
</script>

<style scoped></style>
