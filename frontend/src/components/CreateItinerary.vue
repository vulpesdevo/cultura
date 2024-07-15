<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto h-screen bg-field dark:bg-notif pt-14 sm:pt-3"
	>
		<div
			class="field-editable flex flex-col justify-start items-center w-full bg-field sm:bg-white dark:bg-notif rounded-2xl p-1"
		>
			<div
				class="fixed sm:relative flex flex-col justify-between title-image h-[20rem] sm:h-96 w-screen sm:w-full rounded-2xl bg-field dark:bg-dark-interface sm:bg-transparent z-10"
			>
				<div
					class="flex items-center justify-center w-screen h-[70%] sm:w-full sm:h-[87%] bg-field dark:bg-notif hover:bg-gray-300 sm:rounded-2xl cursor-pointer z-10"
				>
					<label
						for="imgSelect"
						class="w-screen sm:w-full h-full flex items-center justify-center bg-field dark:bg-gray-900 cursor-pointer rounded-xl"
					>
						<img
							:class="{ hidden: !selectedImageUrl }"
							:src="selectedImageUrl"
							class="w-full h-full object-cover rounded-xl z-0"
							alt="Selected image"
						/>
						<div
							:class="{ hidden: selectedImageUrl }"
							class="flex items-center justify-center font-montserrat w-full h-full text-prime dark:text-dark-prime text-xl z-0"
						>
							<span>+ Add Image</span>
						</div>
					</label>
				</div>
				<input
					type="file"
					id="imgSelect"
					class="hidden"
					@change="handleFileSelection"
				/>
				<div
					class="flex absolute left-[3.2rem] bottom-[4rem] sm:bottom-0 sm:left-[7.7rem] bg-prime w-3/4 h-16 sm:h-24 z-30 rounded-md text-center items-center justify-center cursor-pointer"
				>
					<div class="w-full mx-5 z-30">
						<!-- Text Field for Editing -->
						<div v-if="isEditing" class="w-full">
							<input
								v-model="main_title"
								@blur="handleTitleChange"
								@keyup.enter="handleTitleChange"
								class="font-bebas-neue text-lg text-interface text-center bg-prime sm:text-5xl rounded-md w-full px-2 z-20"
								autofocus
								maxlength="30"
							/>
							<!-- Example using FontAwesome -->
						</div>
						<!-- Text Display -->
						<h1
							v-else
							@click="isEditing = true"
							autofocus
							class="font-bebas-neue text-lg text-interface sm:text-5xl z-20"
						>
							{{ main_title }}
						</h1>
					</div>
				</div>
				<div
					class="sm:hidden flex items-center justify-center h-14 w-full"
					id="navs"
				>
					<div
						class="w-3/4 justify-center items-center font-montserrat"
					>
						<button
							class="bg-second h-9 w-1/2 rounded-full"
							:class="{
								'bg-second text-interface':
									currentView === 'overview',
								'bg-transparent text-black':
									currentView !== 'overview',
							}"
							@click="showItinerary('overview')"
						>
							<a href="#overview-section" class="h-full w-full"
								>Overview</a
							>
						</button>
						<button
							class="h-9 w-1/2 rounded-full"
							:class="{
								'bg-second text-interface':
									currentView === 'itinerary',
								'bg-transparent text-black':
									currentView !== 'itinerary',
							}"
							@click="showItinerary('itinerary')"
						>
							<a href="#itinerary-section" class="h-full w-full"
								>Itinerary</a
							>
						</button>
					</div>
				</div>
			</div>

			<section
				class="mt-80 itinerary-1 flex flex-col items-center sm:mt-10 px-16 w-full dark:bg-notif"
				id="overview-section"
			>
				<button
					@click="saveMainItinerary"
					class="bg-second w-full h-10 rounded-lg mb-3"
				>
					Save
				</button>
				<div class="post-content flex w-screen sm:w-full">
					<div
						class="hidden w-[9.2%] sm:flex items-start justify-center"
					>
						<img
							src="/sample_img/mark.png"
							alt="Profile"
							class="w-12 h-12 rounded-full cursor-pointer"
						/>
					</div>
					<div class="w-full mx-3 mt-3 sm:m-0">
						<div class="flex">
							<small
								class="hidden sm:flex items-center justify-center font-montserrat text-prime dark:text-interface text-base pb-3"
							>
								@{{ username }}
							</small>
							<p
								class="font-montserrat sm:hidden pb-1 text-lg text-prime dark:text-interface"
							>
								Description
							</p>
						</div>
						<div>
							<!-- Editable Textarea -->
							<!-- For setAboutMe -->
							<textarea
								v-if="!setAboutMe || isEditingAboutMe"
								class="w-full sm:w-[90.5%] rounded-lg resize-none p-4 outline-none bg-gray-200 dark:text-interface dark:bg-dark-interface dark:ring-notif ring-1"
								v-model="setAboutMe"
								@blur="isEditingAboutMe = false"
								@keyup.tab="isEditingAboutMe = false"
								placeholder="Tell us about yourself"
								autofocus
							>
							</textarea>
							<p
								v-else
								@click="isEditingAboutMe = true"
								class="w-full sm:w-[90.5%] p-4"
								v-html="formatText(setAboutMe)"
							></p>
						</div>
					</div>
				</div>
				<div
					class="flex flex-col items-center justify-center w-screen sm:mx-0 sm:mt-4 sm:w-full"
				>
					<p
						class="font-montserrat text-prime dark:text-interface w-full px-3 mb-2 text-lg sm:text-xl sm:font-semibold"
					>
						General Tips
					</p>
					<div
						class="flex flex-col items-start justify-center w-full px-3 sm:px-0 sm:w-[83%]"
					>
						<textarea
							v-if="!setTips || isEditingTips"
							class="w-full rounded-lg resize-none p-4 outline-none bg-gray-200 dark:text-interface dark:bg-dark-interface dark:ring-notif ring-1"
							v-model="setTips"
							@blur="isEditingTips = false"
							@keyup.enter="
								setTips.split(/\n+/);
								isEditingTips = false;
							"
							placeholder="What do you want to share?"
							autofocus
						>
						</textarea>
						<p
							v-else
							@click="isEditingTips = true"
							class="w-full sm:w-[90.5%] p-4 text-prime dark:text-interface"
							v-html="formatText(setTips)"
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
							<p class="text-2xl">
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
								class="w-full text-white pb-1 text-xl bg-transparent outline-none"
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
						<button
							class="font-montserrat text-interface h-10 sm:h-[7%] w-auto mb-2 bg-second rounded-lg"
							@click.prevent="showModal = true"
							@click="initializeAutocomplete"
						>
							Add place
						</button>
						<div
							class="sm:overflow-auto h-screen rounded-lg p-3"
							style="scrollbar-width: none"
						>
							<div
								class="flex-col justify-center items-center w-full h-[13.5rem] sm:h-[17rem] font-montserrat text-prime dark:bg-dark-second-dark bg-interface drop-shadow-md mb-3 rounded-lg"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-normal sm:justify-evenly items-center dark:text-interface"
								>
									<h1 class="text-2xl py-3 text-center">
										Lucky Chinatown Mall
									</h1>
									<p
										class="text-justify text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16"
									>
										Lucky Chinatown offers a unique blend of
										history, tradition and modern shopping
										and world-class leisure experience.
									</p>
									<div
										class="flex w-full h-8 text-center items-center justify-end sm:justify-center"
									>
										<p class="bg-second w-24 rounded-full">
											P2000
										</p>
									</div>
								</div>
							</div>
							<div
								class="flex-col justify-center items-center w-full h-[13rem] sm:h-[17rem] font-montserrat text-prime bg-white sm:bg-interface dark:bg-dark-second-dark drop-shadow-md mb-3 rounded-lg"
								v-for="(itinerary, index) in list_itineraries"
								:key="index"
							>
								<img
									class="w-full object-cover h-2/5 rounded-lg"
									src="/sample_img/binondo.webp"
									alt=""
								/>
								<div
									class="px-4 flex flex-col justify-normal sm:justify-evenly items-center"
								>
									<h1
										class="text-2xl px-4 dark:text-interface py-3 text-center"
									>
										{{ itinerary.title }}
									</h1>
									<p
										class="text-justify text-sm px-4 overflow-hidden whitespace-nowrap sm:whitespace-normal text-ellipsis w-full h-10 sm:h-16 dark:text-interface"
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

		<div
			class="fixed z-50 inset-0 overflow-y-auto"
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
		>
			<div
				class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0 w-screen"
			>
				<div
					class="fixed inset-0 bg-black bg-opacity-70 transition-opacity w-screen"
					aria-hidden="true"
				></div>
				<span
					class="hidden sm:inline-block sm:align-middle sm:h-screen"
					aria-hidden="true"
					>&#8203;</span
				>
				<div
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle w-screen sm:w-[35%]"
				>
					<div
						class="bg-interface dark:bg-dark-interface px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<div
							class="flex items-center justify-center w-screen h-[70%] sm:w-full sm:h-[10rem] bg-field dark:bg-notif hover:bg-gray-300 sm:rounded-2xl cursor-pointer z-10"
						>
							<label
								for="imgSelect"
								class="w-screen sm:w-full h-full flex items-center justify-center bg-field dark:bg-gray-900 cursor-pointer rounded-xl"
							>
								<img
									:class="{ hidden: !selectedImageUrl }"
									:src="selectedImageUrl"
									class="w-full h-full object-cover rounded-xl z-0"
									alt="Selected image"
								/>
								<div
									:class="{ hidden: selectedImageUrl }"
									class="flex items-center justify-center font-montserrat w-full h-full text-prime dark:text-dark-prime text-xl z-0"
								>
									<span>+ Add Image</span>
								</div>
							</label>
						</div>
						<input
							type="file"
							id="imgSelect"
							class="hidden"
							@change="handleFileSelection"
						/>
						<h3
							class="font-bebas-neue text-2xl pt-5 sm:text-3xl leading-6 font-medium text-prime  dark:text-interface"
							id="modal-title"
						>
							add place
						</h3>

						<form class="mt-2" @submit.prevent="submitItinerary">
							<div class="flex">
								<div
									class="w-full px-3 text-start text-sm font-montserrat dark:text-interface"
								>
									<div class="">
										<label for="it-title">Title</label>
										<input
											type="text"
											placeholder="Title"
											name="it-title"
											id="it-title"
											v-model="title"
											class="mt-2 pl-5 w-full rounded-full h-12 bg-field dark:bg-dark-second-dark outline-none "
											required
										/>
									</div>
									<div class="mt-2">
										<label for="it-location"
											>Set Location's Pin</label
										>
										<div
											class="flex relative justify-center items-center"
										>
											<input
												type="text"
												placeholder="Location"
												name="auto-complete"
												ref="autocomplete"
												id="autocomplete"
												v-model="location"
												class="mt-2 pl-5 w-full rounded-full h-12 bg-field dark:bg-dark-second-dark outline-none"
											required
											/>
											<span
												class="flex justify-center items-center material-icons-outlined absolute right-0 bottom-0 text-prime text-center bg-gray-500 hover:bg-gray-400 dark:text-interface w-12 h-12 rounded-full cursor-pointer"
												@click="locatorBtn"
											>
												location_searching
											</span>
										</div>
									</div>
									<div class="mt-2">
										<label for="it-budget"
											>Set a Budget</label
										>
										<div class="relative">
											<span class="absolute bottom-[.72rem] text-lg font-semibold left-4">{{ selectedSymbol }}</span>
											<input
												type="text"
												placeholder="Budget"
												name="it-budget"
												id="it-budget"
												v-model="budget"
												class="mt-2 pl-12 w-full rounded-full h-12 bg-field dark:bg-dark-second-dark outline-none"
												required
											/>

										</div>
									</div>
									<div class="flex flex-col mt-2">
										<label for="it-description "
											>Add description</label
										>
										<textarea
											class="rounded-lg resize-none mt-2 p-4 outline-none bg-field dark:bg-dark-second-dark "
											required
											name=""
											id="it-description"
											v-model="description"
											cols="30"
											rows="4"
											pattern="^[A-Z][a-zA-Z\s]*[.]$"
											placeholder="Add notes, links, descriptions or whatever you want your fellow travelers to know about this place!"
										></textarea>
									</div>
									<div class="hidden">
										<input type="text" v-model="latitude" />
										<input
											type="text"
											v-model="longitude"
										/>
									</div>
								</div>
							</div>

							<div
								class="flex flex-col items-center align-middle text-center mt-5"
							>
								<div class="flex font-montserrat">
									<button
										class="text-interface text-lg bg-gray-500 p-2 rounded-3xl w-32 h-14 mb-3 hover:bg-gray-400 mr-5"
										@click="showModal = false"
									>
										Cancel
									</button>
									<input
										type="submit"
										value="Save"
										class="text-interface text-lg bg-second p-2 rounded-3xl w-32 h-14 mb-3 hover:bg-second-light"
									/>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
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
import * as Dropdown from "primevue/dropdown";
import router from "../routes";
export default {
	components: {
		Dropdown,
	},
	data() {
		return {
			isEditingTips: true,
			isEditingTitle: true,
			isEditingAboutMe: true,
			main_title: "ITINERARY TITLE",
			selectedImageUrl: null,
			picture: null,

			setTips: "",
			setAboutMe: "",
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

			selectedPera: null,
			list_budget: [],

			selectedCurrency: "",
			selectedSymbol: "",
			currency_save: "",
			converted: 0,
			paragraphs: [],

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

			// This property controls which view is currently visible
			currentView: "itinerary", // 'overview' or 'itinerary'
			showMap: false,
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
	created() {
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
		this.isEditing = true;
		this.fetchItineraries();
	},
	mounted() {
		this.populateDropdown();
		this.initializeAutocomplete();
	},
	methods: {
		handleFileSelection(event) {
			const file = event.target.files[0];
			if (file) {
				this.selectedImageUrl = URL.createObjectURL(file);
				this.picture = file;
				console.log("Image :", this.picture);
				this.isEditing = true;
			}
		},
		processTips() {
			this.paragraphs = this.setTips.split(/\n+/);
		},
		formatText(text) {
			let paragraphs = text.split(/\n+/);
			return paragraphs
				.map((paragraph) => {
					return paragraph.replace(
						/\*\*(.*?)\*\*/g,
						"<strong>$1</strong>"
					);
				})
				.join("<br><br>");
		},
		populateDropdown() {
			const toDropDown = this.$refs.toDropDown;
			this.currency_list.forEach((currency) => {
				const [code, countryName] = currency;
				const option = document.createElement("option");
				option.value = code; // Assuming 'sysmbol' was a typo and should be 'code'
				option.textContent = `${code} - ${countryName}`;
				option.classList.add(
					"text-prime",
					"bg-interface",
					"appearance-none"
				);

				toDropDown.add(option);
			});
			// this.checkCode();
			// Assuming you want to set the default selected value
		},
		// getSelectedCurrencyCode() {

		// 	// this.currency_save = toCurrency;
		// 	console.log("Selected currency code:", this.selectedCurrency); // This returns the code of the selected currency
		// },
		// indivConvert(to, from) {
		// 	const fromCurrency = this.currency_save;
		// 	const toCurrency = this.$refs.toDropDown.value;
		// 	this.currency_save = toCurrency;

		// 	if (this.total_budget.length !== 0) {
		// 		fetch(this.api) // Assuming 'this.api' is your API URL
		// 			.then((resp) => resp.json())
		// 			.then((data) => {
		// 				let fromExchangeRate =
		// 					data.conversion_rates[fromCurrency];
		// 				// let toExchangeRate = data.conversion_rates[toCurrency];
		// 				this.list_itineraries.forEach((itinerary) => {
		// 					const convertedAmount =
		// 						(itinerary.budget / from) * to;

		// 					// Find the symbol for the target currency
		// 					let symbol = this.currency_list.find(
		// 						(currency) => currency[0] === toCurrency
		// 					)[2];

		// 					itinerary.budget = convertedAmount.toFixed(2);
		// 					itinerary.convertedBudget = `${symbol} ${convertedAmount.toFixed(
		// 						2
		// 					)}`;
		// 					console.log("Converted budgets:", to, " ", from);
		// 				});

		// 				// console.log(
		// 				// 	"Converted budgets:",
		// 				// 	this.list_itineraries
		// 				// );
		// 			});
		// 	}
		// },
		// 		convertCurrency() {
		// 			const fromCurrency = this.currency_save;
		// 			const toCurrency = this.$refs.toDropDown.value;
		// 			this.currency_save = toCurrency;
		// 			this.selectedCurrency = toCurrency;

		// console.log("Selected currency code:", this.selectedCurrency);
		// 			if (this.total_budget.length !== 0) {
		// 				fetch(this.api) // Assuming 'this.api' is your API URL
		// 					.then((resp) => resp.json())
		// 					.then((data) => {
		// 						let fromExchangeRate =
		// 							data.conversion_rates[fromCurrency];
		// 						let toExchangeRate = data.conversion_rates[toCurrency];
		// 						const convertedAmount =
		// 							(this.total_budget / fromExchangeRate) *
		// 							toExchangeRate;

		// 						// Find the symbol for the target currency
		// 						let symbol = this.currency_list.find(
		// 							(currency) => currency[0] === toCurrency
		// 						)[2];

		// 						const finalAmount = `${symbol} ${convertedAmount.toFixed(
		// 							2
		// 						)}`;
		// 						this.total_budget += convertedAmount;
		// 						// this.total_budget = convertedAmount.toFixed(2);

		// 						// console.log(total_budget);
		// 						// this.convertedBudget = finalAmount;
		// 						// this.indivConvert(toExchangeRate, fromExchangeRate);
		// 						// Assuming 'result' is a reference to an element for displaying the result
		// 						// this.$refs.result.innerHTML = `${this.total_budget} ${fromCurrency} = ${convertedAmount.toFixed(
		// 						// 	2
		// 						// )} ${toCurrency}`;
		// 					});
		// 			}
		// 		},
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
			this.currency_save = toCurrency;
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
		saveMainItinerary() {
			// this.client
			// 	.post("/api/save-itinerary", {
			// 		main_image: null,
			// 		main_title: this.main_title,
			// 		main_description: this.setAboutMe,
			// 		gen_tips: this.setTips,
			// 		total_budget: this.total_budget,
			// 		currency: this.currency_save,
			// 		itineraries: this.itineraryIds,
			// 	})
			// 	.then((response) => {})
			// 	.catch((error) => {
			// 		console.error(error);
			// 	});

			if (
				!this.main_title.trim() ||
				!this.setAboutMe.trim() ||
				!this.setTips.trim() ||
				this.main_title === "ITINERARY TITLE"
			) {
				alert("Please fill all fields correctly."); // Inform the user (consider using a more user-friendly notification system)
				return; // Exit the method
			} else {
				let formData = new FormData();
				formData.append("main_image", null);
				formData.append("main_title", this.main_title);
				formData.append("main_description", this.setAboutMe);
				formData.append("gen_tips", this.setTips);
				formData.append("total_budget", this.total_budget);
				formData.append("currency", this.currency_save);
				formData.append("itineraries", this.itineraryIds);
				if (this.picture && this.picture instanceof File) {
					formData.append("image", this.picture, this.picture.name);
				}
				this.client
					.post("/api/save-itinerary", formData, {
						headers: {
							"Content-Type": "multipart/form-data",
						},
					})
					.then((response) => {
						console.log(response.data);
						this.main_title = "ITINERARY TITLE";
						this.setAboutMe = "";
						this.setTips = "";

						this.selectedImageUrl = null;
						window.scrollTo(0, 0);
						router.push({ name: "itinerary" }).then(() => {
							window.location.reload();
						});
					})
					.catch((error) => {
						// Handle error
					});
			}
		},
		submitItinerary() {
			this.client
				.post("/api/create-itinerary", {
					title: this.title,
					place_name: this.location,
					longitude: this.longitude,
					latitude: this.latitude,
					budget: this.budget,
					code: this.selectedCurrency,
					description: this.description,
				})
				.then((response) => {
					console.log(response.data);
					this.showModal = false;
					this.fetchItineraries();
				})
				.catch((error) => {
					console.error(error);
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
			const token = localStorage.getItem("token");
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
				this.list_itineraries = response.data;
				console.log("list_itineraries:", this.list_itineraries);
				this.itineraryIds = this.list_itineraries.map(
					(itinerary) => itinerary.id
				);
				this.checkCode();
				console.log("itineraryIds:", this.itineraryIds);

				// this.total_budget = this.list_itineraries.reduce(
				// 	(sum, itinerary) => sum + itinerary.budget,
				// 	0
				// );
				// console.log("Total Budget:", this.total_budget);
				// let symbol = this.currency_list.find(
				// 	(currency) => currency[0] === this.currency_save
				// )[2];
				// this.convertedBudget = `${symbol}${this.total_budget}`;
				// Sort the itineraries by proximity before showing them on the map

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
