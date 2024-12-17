<template lang="">
	<transition
		name="page"
		mode="out-in"
		@before-leave="beforeLeave"
		@enter="enter"
		@after-enter="afterEnter"
	>
		<!-- Landing Page Content -->
		<div
			v-if="!showLogin"
			key="landing"
			class="relative h-screen sm:overflow-hidden bg-white dark:bg-gray-700 transition-colors duration-300"
		>
			<!-- Navigation -->
			<nav class="px-4 sm:px-6">
				<div class="mx-auto flex justify-between items-center">
					<div class="flex items-center">
						<a href="/" class="flex items-center">
							<img
								:src="
									isDarkMode
										? '/ULTURALINK-DMLong.png'
										: '/culturalink_brand_logo.png'
								"
								alt="CulturalLink Logo"
								class="h-32"
							/>
						</a>
					</div>
					<div class="flex items-center space-x-4">
						<button
							@click="toggleDarkMode"
							class="p-2 rounded-full bg-gray-200 dark:bg-gray-800 text-gray-800 dark:text-gray-200 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors duration-200"
							aria-label="Toggle dark mode"
						>
							<SunIcon v-if="isDarkMode" class="h-5 w-5" />
							<MoonIcon v-else class="h-5 w-5" />
						</button>
						<button
							@click="showLogin = true"
							class="px-8 py-4 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-600 text-navy-900 dark:text-white rounded-full font-semibold transition-colors duration-200 sm:flex hidden"
						>
							SIGN IN
						</button>
					</div>
				</div>
			</nav>
			<!-- Hero Section -->
			<div class="mx-auto px-4 sm:px-10 pt-8 sm:pt-5 sm:pb-8">
				<div class="relative grid lg:grid-cols-2 gap-12 items-center">
					<!-- Left Column -->
					<div class="">
						<h1
							class="text-4xl sm:text-5xl lg:text-6xl font-bold text-navy-900 dark:text-white leading-tight mb-6"
						>
							Share. Learn. Connect.
						</h1>
						<p
							class="text-base text-gray-600 dark:text-gray-300 mb-16 leading-relaxed"
						>
							CulturalLink connects you to the world's diverse
							cultures, bridging gaps, celebrating diversity, and
							fostering meaningful connections. Join us in uniting
							cultures—one connection at a time!
						</p>
						<button
							@click.prevent="showModal = true"
							class="w-full sm:w-auto px-8 py-4 bg-second hover:bg-indigo-600 text-white rounded-full text-lg font-semibold transition-colors duration-200 mb-4"
						>
							CREATE ACCOUNT
						</button>
						<button
							@click.prevent="showLogin = true"
							class="w-full sm:w-auto px-8 py-4 bg-gray-200 hover:bg-gray-600 text-prime rounded-full text-center text-lg font-semibold transition-colors duration-200 mb-4 sm:hidden block"
						>
							SIGN IN
						</button>
						<p
							class="text-xs text-gray-500 dark:text-gray-400 pb-10 sm:pb-0"
						>
							By signing up, you agree to the
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Terms of Service</a
							>
							and
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Privacy Policy</a
							>, including
							<a
								href="#"
								class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300"
								>Cookie Use</a
							>.
						</p>
					</div>

					<!-- Right Column - Device Mockups -->
					<div
						class="absolute -bottom-24 right-0 w-[50rem] sm:flex hidden"
					>
						<img
							src="/mock_up.png"
							alt="CulturalLink App Interface"
							class="w-full h-auto rounded-lg drop-shadow-lg"
						/>
					</div>
				</div>
			</div>

			<!-- Features Section -->
			<div
				class="bg-second dark:bg-gray-800 transition-colors duration-300"
			>
				<div class="max-w-full mx-auto px-4 sm:px-14 py-14">
					<div class="grid md:grid-cols-3 gap-8">
						<!-- Feature 1 -->
						<div
							class="flex items-center space-x-4 p-6 rounded-lg shadow-sm"
						>
							<div class="flex-shrink-0">
								<div
									class="size-20 rounded-full bg-prime dark:bg-indigo-900 flex items-center justify-center"
								>
									<UsersIcon
										class="size-9 text-second dark:text-indigo-400"
									/>
								</div>
							</div>
							<div>
								<p
									class="text-prime text-sm dark:text-gray-300"
								>
									Share ideas and connect with a global
									community.
								</p>
							</div>
						</div>

						<!-- Feature 2 -->
						<div
							class="flex items-center space-x-4 p-6 rounded-lgshadow-sm"
						>
							<div class="flex-shrink-0">
								<div
									class="size-20 rounded-full bg-prime dark:bg-indigo-900 flex items-center justify-center"
								>
									<MapPinIcon
										class="size-9 text-second dark:text-indigo-400"
									/>
								</div>
							</div>
							<div>
								<p
									class="text-prime text-sm dark:text-gray-300"
								>
									Plan cultural experiences with a
									customizable itinerary feature.
								</p>
							</div>
						</div>

						<!-- Feature 3 -->
						<div
							class="flex items-center space-x-4 p-6 rounded-lg shadow-sm"
						>
							<div class="flex-shrink-0">
								<div
									class="size-20 rounded-full bg-prime dark:bg-indigo-900 flex items-center justify-center"
								>
									<ChatBubbleOvalLeftIcon
										class="size-9 text-second dark:text-indigo-400"
									/>
								</div>
							</div>
							<div>
								<p
									class="text-prime text-sm dark:text-gray-300"
								>
									Get fun and informative cultural trivia with
									our chatbot, "Cura".
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Actual Login Form (Unchanged UI) -->
		<section
			v-else
			key="login"
			class="bg-interface dark:bg-dark-notif h-screen w-full flex flex-col justify-center items-center sm:flex-row p-0 sm:p-20"
		>
			<button
				@click="showLogin = false"
				class="absolute top-4 left-4 px-4 py-2 text-sm dark:text-white hover:bg-gray-300 rounded-full dark:hover:bg-gray-600 transition-colors duration-300 flex items-center"
			>
				<ArrowLeftIcon class="h-5 w-5 inline-block mr-2" />
				Return
			</button>
			<div
				class="logo-container sm:w-1/2 flex justify-center items-center align-middle pt-10 sm:pt-1"
			>
				<img
					class="h-52 sm:w-screen sm:h-auto"
					:src="isDark ? '/logo1Light.png' : '/culturalink_logo.png'"
					alt="cultura-logo"
				/>
			</div>
			<div
				class="flex flex-col justify-center items-center sm:w-1/2 align-middle text-center"
			>
				<h3
					class="sm:pl-0 flex text-center text-prime dark:text-dark-prime text-2xl sm:text-5xl mb-3 w-auto"
					@click="test"
				>
					Share. Learn. Connect.
				</h3>
				<h1
					class="font-bebas-neue text-6xl text-prime dark:text-dark-prime text-center mb-6 tracking-widest sm:text-9xl"
				>
					Culturalink
				</h1>
				<form
					class="flex flex-col justify-center align-middle items-center m-12 mx-10"
					@submit.prevent="submitLogin"
				>
					<div v-if="errorMessage" class="text-red-500 mb-4">
						{{ errorMessage }}
					</div>

					<input
						type="text"
						placeholder="Username"
						name="lusername"
						v-model="username"
						:class="[
							'pl-5 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second rounded-full mb-4 w-80 sm:w-96 h-14',
							{ 'ring-2 ring-red-500': errorMessage },
						]"
					/>
					<input
						type="password"
						name="lpassword"
						v-model="password"
						placeholder="Password"
						class="pl-5 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second rounded-full mb-2 w-80 sm:w-96 h-14"
					/>
					<a
						class="text-center text-second mb-10 cursor-pointer"
						@click="fpmodalActive = true"
						>Forgot passsword?</a
					>
					<input
						type="submit"
						value="Log in"
						class="font-bebas-neue text-3xl bg-second text-interface p-2 rounded-full w-52 h-14 mb-6 hover:bg-second-light cursor-pointer"
					/>
					<span class="flex"
						><p class="text-black dark:text-dark-prime">
							Don't have an account?
						</p>
						<a
							href=""
							class="pl-3 text-second"
							@click.prevent="showModal = true"
							>Sign Up Now!</a
						></span
					>
				</form>
			</div>

			<!-- Forgot Password Modal -->
			<div
				v-show="fpmodalActive"
				class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
			>
				<div
					v-if="fpmodalActive"
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface self-start mt-36"
				>
					<div class="w-full flex justify-end items-end">
						<span
							@click="fpmodalActive = false"
							class="flex material-icons-outlined justify-end cursor-pointer dark:text-interface"
							>close</span
						>
					</div>
					<h1
						class="flex text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-5 justify-center"
					>
						reset your password
					</h1>
					<p
						class="flex text-center text-xs sm:text-[1rem] my-5 mb-7 sm:my-7 px-7 sm:px-20 font-montserrat dark:text-interface"
					>
						A one-time PIN will be emailed to you to help reset your
						password.
					</p>
					<form class="flex justify-center w-full sm:px-24">
						<div class="relative text-left mb-4 w-full">
							<label
								for=""
								class="hidden sm:flex dark:text-interface"
								>Email</label
							>

							<div
								class="absolute inset-y-0 start-0 flex sm:mt-6 items-center ps-3.5 pointer-events-none"
							>
								<svg
									class="w-4 h-4 text-gray-500 dark:text-gray-400"
									aria-hidden="true"
									xmlns="http://www.w3.org/2000/svg"
									fill="currentColor"
									viewBox="0 0 20 16"
								>
									<path
										d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"
									/>
									<path
										d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"
									/>
								</svg>
							</div>
							<input
								type="email"
								id="email"
								v-model="fpemail"
								:class="{
									'ring-2 ring-red-500 ring-inset': error,
									'ring-2 ring-green-500 ring-inset':
										isGmailEmail,
								}"
								required
								class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second"
								placeholder="name@gmail.com"
							/>
						</div>
						<!-- <div class="flex-col mb-6 px-5 sm:px-28">
						<label
							for="email"
							class="flex ms-3 mb-2 text-sm font-bold text-prime dark:text-interface justify-start"
							>Email</label
						>
						<input
							type="email"
							id="email"
							v-model="fpemail"
							class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field outline-none"
							:class="{
								'outline-red-500': error, // add this line
							}"
							required
							placeholder="christina.tecson@sdca.edu.ph"
						/>
					</div> -->
					</form>
					<div class="flex justify-center">
						<button
							@click="sendOTPfp"
							class="rounded-full text-xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue justify-center"
						>
							Send OTP
						</button>
					</div>
				</div>
			</div>

			<div
				v-if="modalOTPActive"
				class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8 z-50"
			>
				<div
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface self-start mt-36"
				>
					<div class="flex justify-end">
						<span
							@click="modalOTPActive = false"
							class="material-icons-outlined justify-items-center dark:text-interface"
							>close</span
						>
					</div>
					<h1
						class="flex justify-center text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-5"
					>
						ENTER ONE TIME PIN
					</h1>
					<p
						class="flex justify-center text-xs sm:text-[1rem] dark:text-interface my-5 mb-7 sm:my-7 px-7 sm:px-20 font-montserrat text-center"
					>
						Enter the pin sent to your email for verification
					</p>
					<form>
						<div
							class="flex mb-6 text-4xl text-center justify-evenly sm:px-28"
						>
							<input
								v-for="(input, index) in inputs"
								:key="index"
								type="text"
								maxlength="1"
								class="w-12 sm:w-16 h-16 text-center text-2xl font-extrabold text-slate-900 bg-slate-200 border border-transparent hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100"
								:class="{
									'outline-red-500': error,
									'outline-none': input !== '', // add this line
								}"
								v-model="inputs[index]"
								@keyup="moveFocus($event, index)"
								@input="
									inputs[index] = $event.target.value.replace(
										/[^0-9]/g,
										''
									)
								"
								:ref="(el) => (inputsRefs[index] = el)"
							/>
						</div>
					</form>
					<div class="flex justify-center">
						<button
							@click="verifyOTP('register')"
							class="rounded-full text-2xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue"
						>
							Verify
						</button>
					</div>
				</div>
			</div>
			<div
				v-if="fpmodalOTPActive"
				class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8 z-50"
			>
				<div
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-36"
				>
					<div class="flex justify-end">
						<span
							@click="fpmodalOTPActive = false"
							class="material-icons-outlined justify-items-center"
							>close</span
						>
					</div>
					<h1
						class="flex justify-center text-4xl sm:text-7xl text-prime font-bebas-neue my-5"
					>
						ENTER ONE TIME PIN
					</h1>
					<p
						class="flex justify-center text-sm sm:text-lg my-5 mb-7 sm:my-7 px-7 sm:px-20 font-montserrat text-center"
					>
						Enter the pin sent to your email for verification
					</p>
					<form>
						<div
							class="flex mb-6 text-4xl text-center justify-evenly sm:px-28"
						>
							<input
								v-for="(input, index) in inputs"
								:key="index"
								type="text"
								maxlength="1"
								class="w-12 sm:w-16 h-16 text-center text-2xl font-extrabold text-slate-900 bg-slate-200 border border-transparent hover:border-slate-200 appearance-none rounded p-4 outline-none focus:bg-white focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100"
								:class="{
									'outline-red-500': error,
									'outline-none': input !== '', // add this line
								}"
								v-model="inputs[index]"
								@keyup="moveFocus($event, index)"
								@input="
									inputs[index] = $event.target.value.replace(
										/[^0-9]/g,
										''
									)
								"
								:ref="(el) => (inputsRefs[index] = el)"
							/>
						</div>
					</form>
					<div class="flex justify-center">
						<button
							@click="verifyOTP('forgot-password')"
							class="rounded-full text-2xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue"
						>
							Verify
						</button>
					</div>
				</div>
			</div>
			<div
				v-show="modalChangeActive"
				class="fixed flex bg-black bg-opacity-30 h-screen w-screen items-start justify-center px-8"
			>
				<div
					v-if="modalChangeActive"
					class="flex-col w-full sm:w-1/2 rounded-lg p-4 bg-interface dark:bg-dark-interface mt-36"
				>
					<div class="w-full flex justify-end items-end">
						<span
							@click="modalChangeActive = false"
							class="flex material-icons-outlined justify-end dark:text-interface cursor-pointer"
							>close</span
						>
					</div>
					<h1
						class="flex text-4xl sm:text-7xl text-prime dark:text-interface font-bebas-neue my-5 justify-center"
					>
						Change Password
					</h1>
					<form method="POST">
						<div class="flex-col mb-6 px-5 sm:px-28">
							<div
								class="sm:mb-2 flex flex-col justify-between items-start"
							>
								<label
									for="newpassword"
									class="hidden sm:flex ms-3 mb-2 text-sm font-bold text-prime dark:text-interface justify-start"
									>New Password</label
								>
								<div class="relative w-full px-1">
									<input
										:type="
											showPassword ? 'text' : 'password'
										"
										id="fp_newpassword"
										v-model="fp_newpassword"
										:class="{
											'outline-red-500': error, // add this line
										}"
										class="text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-second"
										placeholder="New Password"
										required
									/>
									<button
										class="absolute right-5 top-2"
										@click.prevent="
											showPassword = !showPassword
										"
									>
										<i
											class="fas text-gray-500 dark:text-gray-400"
											:class="
												showPassword
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>

							<div
								class="flex flex-col justify-end items-start mt-0 mb-2"
							>
								<div
									class="flex w-full sm:w-3/4 h-20 dark:text-dark-second-dark"
								>
									<div
										class="flex flex-col items-end justify-evenly w-5 h-full"
									>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasCapitalLetter"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasSymbol"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasNumber"
											>
												check_circle
											</span>
										</div>
										<div class="h-3">
											<span
												class="material-icons-outlined text-green-700 text-sm"
												v-if="hasMinLength"
											>
												check_circle
											</span>
										</div>
									</div>
									<div
										class="flex flex-col justify-evenly h-20 items-start pt-[.45rem]"
									>
										<label
											for="has-capital-letter"
											class="ml-2 text-xs h-4"
											>has capital letter</label
										>

										<label
											for="has-symbol"
											class="ml-2 text-xs h-4"
											>has symbol</label
										>

										<label
											for="has-number"
											class="ml-2 text-xs h-4"
											>has number</label
										>

										<label
											for="has-min-length"
											class="ml-2 text-xs h-4"
											>has at least 8 characters</label
										>
									</div>
								</div>
							</div>

							<div
								class="mb-6 flex flex-col justify-between items-start"
							>
								<label
									for="newpassword"
									class="hidden sm:flex ms-3 mb-2 text-sm font-bold text-prime dark:text-interface justify-start"
									>Confirm Password</label
								>
								<div class="relative w-full px-1">
									<input
										:type="
											showRePassword ? 'text' : 'password'
										"
										id="fp_confirmpassword"
										v-model="fp_confirmpassword"
										:class="[
											!isValidNewPassword
												? 'cursor-not-allowed'
												: 'cursor-pointer',
											error ? 'outline-red-500' : '',
										]"
										class="text-prime text-sm rounded-3xl w-full h-10 pl-6 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface outline-second"
										placeholder="Confirm New Password"
										:disabled="!isValidNewPassword"
										required
									/>
									<button
										:disabled="!isValidNewPassword"
										:class="[
											!isValidNewPassword
												? 'cursor-not-allowed'
												: 'cursor-pointer',
										]"
										class="absolute right-5 top-2"
										@click.prevent="
											showRePassword = !showRePassword
										"
									>
										<i
											class="fas text-gray-500 dark:text-gray-400"
											:class="
												showRePassword
													? 'fa-eye'
													: 'fa-eye-slash'
											"
										></i>
									</button>
								</div>
							</div>
						</div>
					</form>
					<div class="flex justify-center">
						<button
							@click="confirmPassword"
							:class="[
								!isValidNewPassword || !isValidConfirmPassword
									? 'cursor-not-allowed'
									: 'cursor-pointer',
							]"
							class="rounded-full text-xl text-white mt-3 mb-6 bg-second py-3 px-7 font-bebas-neue justify-center"
							:disabled="!isValidNewPassword"
						>
							Confirm
						</button>
					</div>
				</div>
			</div>
			<div
				v-show="modalInvalidActive"
				class="absolute w-full bg-black bg-opacity-30 h-screen top-0 left-0 flex justify-center px-8"
			>
				<div
					v-if="modalInvalidActive"
					class="flex-col sm:w-1/2 rounded-lg p-4 bg-interface self-start mt-52"
				>
					<span
						@click="modalInvalidActive = false"
						class="flex material-icons-outlined justify-end cursor-pointer dark:text-interface"
						>close</span
					>
					<h1
						class="flex text-4xl sm:text-7xl text-prime font-bebas-neue my-5 justify-center"
					>
						invalid one time pin
					</h1>
					<p
						class="flex justify-center text-sm sm:text-lg my-5 mb-20 sm:my-7 px-7 sm:px-28 font-montserrat text-center"
					>
						It seems like you entered the wrong pin. Please try
						again.
					</p>
				</div>
			</div>
		</section>
	</transition>
	<transition name="modal">
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
					class="fixed inset-0 bg-black bg-opacity-70 transition-opacity w-full"
					aria-hidden="true"
				></div>
				<span
					class="hidden sm:inline-block sm:align-middle sm:h-screen"
					aria-hidden="true"
					>&#8203;</span
				>
				<div
					class="inline-block align-center rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:align-middle sm:w-1/2"
				>
					<!-- <button
						class="absolute top-0 right-0 m-2 text-prime text-2xl"
						@click="showModal = false"
					>
						&times;
					</button> -->
					<span
						@click="showModal = false"
						class="flex material-icons-outlined justify-end absolute top-0 right-0 m-2 text-prime dark:text-dark-prime text-2xl"
						>close</span
					>
					<div
						class="bg-interface dark:bg-dark-notif px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<h3
							class="font-bebas-neue text-5xl pt-5 sm:text-7xl leading-6 font-medium text-prime tracking-widest dark:text-dark-prime"
							id="modal-title"
						>
							SIGN UP
						</h3>
						<p
							class="font-montserrat text-prime dark:text-dark-prime pt-2 pb-5 text-sm sm:text-lg"
						>
							Create your own account
						</p>
						<form class="mt-2" @submit.prevent="submitRegistration">
							<div class="flex flex-wrap sm:flex-nowrap">
								<div
									class="w-full sm:w-1/2 md:w-1/2 xl:w-1/2 px-3"
								>
									<div class="relative text-left mb-4">
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Full Name</label
										>
										<input
											type="text"
											placeholder="Full Name"
											name="name"
											v-model="rname"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second"
											required
										/>
									</div>
									<div class="relative text-left mb-4">
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Country</label
										>
										<input
											type="text"
											placeholder="Country"
											name="country"
											v-model="rcountry"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second"
											required
										/>
									</div>
								</div>
								<div
									class="w-full sm:w-1/2 md:w-1/2 xl:w-1/2 px-3"
								>
									<div class="relative text-left mb-4">
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Email</label
										>

										<div
											class="absolute inset-y-0 start-0 flex sm:mt-6 items-center ps-3.5 pointer-events-none"
										>
											<svg
												class="w-4 h-4 text-gray-500 dark:text-gray-400"
												aria-hidden="true"
												xmlns="http://www.w3.org/2000/svg"
												fill="currentColor"
												viewBox="0 0 20 16"
											>
												<path
													d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"
												/>
												<path
													d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"
												/>
											</svg>
										</div>
										<input
											type="email"
											id="input-group-1"
											name="email"
											v-model="email"
											required
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second"
											:class="{
												'ring-2 ring-red-500 ring-inset':
													error_email,
												'ring-2 ring-green-500 ring-inset':
													isGmailEmail &&
													!error_email,
											}"
											placeholder="name@gmail.com"
										/>
									</div>
									<div class="relative text-left mb-4">
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Username</label
										>
										<input
											type="text"
											placeholder="Username"
											name="rusername"
											v-model="rusername"
											:class="{
												'ring-2 ring-red-500 ring-inset':
													error_user,
												'ring-2 ring-green-500 ring-inset':
													usernameValid &&
													!error_user,
											}"
											class="border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:border-gray-600 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 mt-2 sm:mt-0 pl-5 rounded-full h-11 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second"
											required
										/>
									</div>
								</div>
							</div>
							<div class="w-full flex flex-wrap sm:flex-nowrap">
								<div
									class="w-full flex flex-col sm:flex-row px-3"
								>
									<div
										class="relative sm:w-1/2 text-left mb-4"
									>
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Password</label
										>
										<div class="relative w-full">
											<input
												:type="
													showPassword
														? 'text'
														: 'password'
												"
												id="password"
												v-model="rpassword"
												:class="[
													'text-prime text-sm rounded-3xl w-full h-10 pl-10 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface border-green-400',
													{
														'outline-second':
															!error && !match,
														'ring-2 ring-red-500 ring-inset':
															error,
														'ring-2 ring-green-500 ring-inset':
															match,
													},
												]"
												placeholder="Password"
												required
												:autofocus="error"
											/>
											<button
												class="absolute right-5 top-2"
												@click.prevent="
													showPassword = !showPassword
												"
											>
												<i
													class="fas text-gray-500 dark:text-gray-400"
													:class="
														showPassword
															? 'fa-eye'
															: 'fa-eye-slash'
													"
												></i>
											</button>
										</div>
										<div class="flex">
											<div
												class="flex flex-col justify-start items-start mt-0 mb-2"
											>
												<div
													class="flex w-full sm:w-dull h-12 dark:text-dark-second-dark"
												>
													<div
														class="flex flex-col items-start justify-evenly w-5 h-full"
													>
														<div class="h-2">
															<span
																class="material-icons-outlined text-green-700 text-sm"
																v-if="
																	hasCapitalLetter
																"
															>
																check_circle
															</span>
														</div>
														<div class="h-2">
															<span
																class="material-icons-outlined text-green-700 text-sm"
																v-if="hasSymbol"
															>
																check_circle
															</span>
														</div>
													</div>
													<div
														class="flex flex-col justify-evenly h-12 items-start pt-[.45rem]"
													>
														<label
															for="has-capital-letter"
															class="ml-2 text-xs h-2"
															>has capital
															letter</label
														>
														<label
															for="has-symbol"
															class="ml-2 text-xs h-2"
															>has symbol</label
														>
													</div>
												</div>
											</div>
											<div
												class="flex flex-col justify-end items-start mt-0 mb-2 ml-2"
											>
												<div
													class="flex w-full sm:w-full h-12 dark:text-dark-second-dark"
												>
													<div
														class="flex flex-col items-end justify-evenly w-5 h-full"
													>
														<div class="h-2">
															<span
																class="material-icons-outlined text-green-700 text-sm"
																v-if="hasNumber"
															>
																check_circle
															</span>
														</div>
														<div class="h-2">
															<span
																class="material-icons-outlined text-green-700 text-sm"
																v-if="
																	hasMinLength
																"
															>
																check_circle
															</span>
														</div>
													</div>
													<div
														class="flex flex-col justify-evenly h-12 items-start pt-[.45rem]"
													>
														<label
															for="has-number"
															class="ml-2 text-xs h-2"
															>has number</label
														>

														<label
															for="has-min-length"
															class="ml-2 text-xs h-2"
															>has at least 8
															characters</label
														>
													</div>
												</div>
											</div>
										</div>
									</div>
									<div
										class="relative sm:w-1/2 text-left mb-4 sm:ml-7"
									>
										<label
											for=""
											class="hidden sm:flex text-sm dark:text-dark-prime"
											>Re-enter Password</label
										>
										<div class="relative w-full">
											<input
												:type="
													showRePassword
														? 'text'
														: 'password'
												"
												id="re-password"
												v-model="repassword"
												:class="[
													'text-prime text-sm rounded-3xl w-full h-10 pl-10 pr-14 bg-field dark:bg-dark-second-dark dark:text-interface',
													{
														'outline-second':
															!error && !match,
														'ring-2 ring-red-500 ring-inset':
															error,
														'ring-2 ring-green-500 ring-inset':
															match,
													},
												]"
												placeholder="Re-enter Password"
												:disabled="!isValidPassword"
												required
											/>
											<button
												class="absolute right-5 top-2"
												@click.prevent="
													showRePassword =
														!showRePassword
												"
												:disabled="!isValidPassword"
											>
												<i
													class="fas text-gray-500 dark:text-gray-400"
													:class="
														showRePassword
															? 'fa-eye'
															: 'fa-eye-slash'
													"
												></i>
											</button>
										</div>
									</div>
								</div>
							</div>
							<div class="flex justify-center mt-4">
								<input
									type="submit"
									value="SIGN UP"
									class="font-bebas-neue text-interface text-3xl bg-second p-2 rounded-full w-52 h-14 mb-6 hover:bg-second-light cursor-pointer"
								/>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</transition>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { useDark, useToggle } from "@vueuse/core";
import axiosClient from "../axios";
import {
	UsersIcon,
	MapPinIcon,
	ChatBubbleOvalLeftIcon,
	SunIcon,
	MoonIcon,
	ArrowLeftIcon,
} from "@heroicons/vue/24/outline";
const router = useRouter();
const store = useStore();
const isDark = useDark();

const toggleDark = useToggle(isDark);
const isDarkMode = ref(false);

const toggleDarkMode = () => {
	isDarkMode.value = !isDarkMode.value;
	document.documentElement.classList.toggle("dark");
};

// State variables
const showLogin = ref(false);
const showModal = ref(false);
const modalActive = ref(false);
const modalOTPActive = ref(false);
const fpmodalActive = ref(false);
const fpmodalOTPActive = ref(false);
const modalChangeActive = ref(false);
const modalInvalidActive = ref(false);
const showRePassword = ref(false);
const showPassword = ref(false);
const inputs = ref(new Array(6).fill(""));
const inputsRefs = ref([]);
const error = ref(false);
const error_user = ref(false);
const error_email = ref(false);
const hasCapitalLetter = ref(false);
const hasSymbol = ref(false);
const hasNumber = ref(false);
const hasMinLength = ref(false);
const usernameValid = ref(false);

// Form data
const username = ref("");
const password = ref("");
const email = ref("");
const rname = ref("");
const rcountry = ref("");
const rusername = ref("");
const rpassword = ref("");
const repassword = ref("");
const fpemail = ref("");
const fp_newpassword = ref("");
const fp_confirmpassword = ref("");

// Computed properties
const isGmailEmail = computed(() => {
	error_email.value = false;
	const emailRegex = /^[A-Za-z0-9._%+-]+@gmail\.com$/;
	return emailRegex.test(email.value);
});

const match = computed(
	() => rpassword.value === repassword.value && rpassword.value !== ""
);

const isValidNewPassword = computed(() => {
	const password = fp_newpassword.value;
	hasCapitalLetter.value = /[A-Z]/.test(password);
	hasSymbol.value = /[!@#$%^&*(),.?":{}|<>]/.test(password);
	hasNumber.value = /\d/.test(password);
	hasMinLength.value = password.length >= 8;
	return (
		hasCapitalLetter.value &&
		hasSymbol.value &&
		hasNumber.value &&
		hasMinLength.value
	);
});

const isValidConfirmPassword = computed(
	() => fp_confirmpassword.value === fp_newpassword.value
);

const isValidPassword = computed(() => {
	const password = rpassword.value;
	hasCapitalLetter.value = /[A-Z]/.test(password);
	hasSymbol.value = /[!@#$%^&*(),.?":{}|<>]/.test(password);
	hasNumber.value = /\d/.test(password);
	hasMinLength.value = password.length >= 8;
	return (
		hasCapitalLetter.value &&
		hasSymbol.value &&
		hasNumber.value &&
		hasMinLength.value
	);
});

const isValidRePassword = computed(() => repassword.value === rpassword.value);

// Methods
const createToast = (message, type) => {
	// Toast creation logic (unchanged)
};

const sendOTPfp = async () => {
	if (fpemail.value !== "") {
		try {
			const response = await store.dispatch(
				"sendForgotPasswordOTP",
				fpemail.value
			);
			console.log("OTP send successful:", response);
			fpmodalOTPActive.value = true;
			fpmodalActive.value = false;
		} catch (error) {
			console.log("ERROR: ", error);
		}
	} else {
		error.value = true;
		console.log("put email");
	}
};

const verifyOTP = async (modal) => {
	try {
		if (modal === "register") {
			await store.dispatch(
				"verifyRegistrationOTP",
				parseInt(inputs.value.join(""))
			);
			// Handle successful verification
			router.push({ name: "dashboard" });
		} else if (modal === "forgot-password") {
			const verified = await store.dispatch(
				"verifyForgotPasswordOTP",
				parseInt(inputs.value.join(""))
			);
			if (verified) {
				fpmodalOTPActive.value = false;
				modalChangeActive.value = true;
			} else {
				error.value = true;
				createToast("Wrong one-time password", "error");
			}
		}
	} catch (error) {
		console.error("OTP verification error:", error);
		error.value = true;
	}
};

const confirmPassword = async () => {
	if (fp_newpassword.value === fp_confirmpassword.value) {
		try {
			await store.dispatch("changePassword", {
				email: fpemail.value,
				password: fp_newpassword.value,
			});
			modalChangeActive.value = false;
			createToast(
				`${fpemail.value}\nPassword changed successfully`,
				"success"
			);
		} catch (error) {
			console.error("Password change error:", error);
		}
	} else {
		error.value = true;
		console.log("Password does not match");
	}
};

const submitRegistration = async () => {
	if (rpassword.value === repassword.value) {
		try {
			// await store.dispatch("register", {
			// 	email: email.value,
			// 	fullname: rname.value,
			// 	country: rcountry.value,
			// 	username: rusername.value,
			// 	password: rpassword.value,
			// });
			const response = await store.dispatch("sendOtp", {
				email: email.value,
				username: rusername.value,
			});

			console.log("Otp send successful:", response);
			// Navigate to OTP verification or dashboard based on your flow
			router.push({
				name: "otp",
				query: {
					email: email.value,
					rname: rname.value,
					rcountry: rcountry.value,
					rusername: rusername.value,
					rpassword: rpassword.value,
				},
			});

			error.value = false;
		} catch (error) {
			console.error("Registration error:", error);
			if (error.email_error) {
				error_email.value = true;
			}
			if (error.username_error) {
				error_user.value = true;
			}
		}
	} else {
		error.value = true;
		console.log("Password does not match");
	}
};
const errorMessage = ref("");

const submitLogin = async () => {
	try {
		await store.dispatch("login", {
			username: username.value,
			password: password.value,
		});
		router.push({ name: "dashboard" });
	} catch (error) {
		console.error("Login error:", error);
		errorMessage.value = "Incorrect creadentials. Please try again.";

		// Handle login error (e.g., show error message)
	}
};

const moveFocus = (event, index) => {
	if (event.key.match(/^[0-9]$/)) {
		if (index < inputs.value.length - 1) {
			inputsRefs.value[index + 1].focus();
		}
	} else if (event.keyCode === 8) {
		if (index > 0) {
			inputsRefs.value[index - 1].focus();
		}
	}
};

// Lifecycle hooks
// onMounted(async () => {
// 	try {
// 		await store.dispatch("fetchUserData");
// 		router.push({ name: "dashboard" });
// 	} catch (error) {
// 		console.log("User not authenticated or error fetching user data");
// 	}
// });

// Watchers
watch(rpassword, (newVal) => {
	// Password validation logic (unchanged)
});

watch(repassword, (newVal) => {
	error.value = rpassword.value !== newVal;
});

watch(rusername, (newVal) => {
	if (newVal !== "") {
		error_user.value = false;
		usernameValid.value = true;
	} else {
		usernameValid.value = false;
	}
});

const beforeLeave = (el) => {
	const mockup = el.querySelector('img[src="/mock_up.png"]');
	const features = el.querySelector(".bg-second");
	const otherElements = el.querySelectorAll(
		'*:not(img[src="/mock_up.png"]):not(.bg-second)'
	);

	if (mockup) {
		mockup.style.transition = "transform 0.5s ease-in-out";
		mockup.style.transform = "translateX(-100%)";
	}

	if (features) {
		features.style.transition = "transform 0.5s ease-in-out";
		features.style.transform = "translateY(100%)";
	}

	otherElements.forEach((element) => {
		element.style.transition = "opacity 0.5s ease-in-out";
		element.style.opacity = "0";
	});
};

const enter = (el, done) => {
	const elements = el.querySelectorAll("*");
	elements.forEach((element, index) => {
		element.style.opacity = "0";
		element.style.transform = "translateY(20px)";
		element.style.transition = `opacity 0.5s ease-in-out ${
			index * 0.1
		}s, transform 0.5s ease-in-out ${index * 0.1}s`;
	});

	setTimeout(() => {
		elements.forEach((element) => {
			element.style.opacity = "1";
			element.style.transform = "translateY(0)";
		});
		done();
	}, 50);
};

const afterEnter = (el) => {
	const elements = el.querySelectorAll("*");
	elements.forEach((element) => {
		element.style.transition = "";
		element.style.transform = "";
	});
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

.page-enter-active,
.page-leave-active {
	transition: opacity 0.5s ease;
}

.page-enter-from,
.page-leave-to {
	opacity: 0;
}

/* Add new transition styles */
.page-enter-active,
.page-leave-active {
	transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.page-enter-from,
.page-leave-to {
	opacity: 0;
	transform: translateY(50px);
}

/* Modal transition */
.modal-enter-active,
.modal-leave-active {
	transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
	opacity: 0;
}

.modal-enter-active .modal-container,
.modal-leave-active .modal-container {
	transition: transform 0.3s ease;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
	transform: translateY(-50px);
}
</style>
