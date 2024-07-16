<template>
	<section
		class="bg-interface dark:bg-dark-notif h-screen w-screen flex flex-col justify-center items-center sm:flex-row p-0 sm:p-20"
	>
		<div
			class="logo-container sm:w-1/2 flex justify-center items-center align-middle pt-10 sm:pt-1"
		>
			<img
				class="h-56 sm:w-screen sm:h-auto"
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
				<input
					type="text"
					placeholder="Username"
					name="lusername"
					v-model="username"
					class="pl-5 bg-field dark:bg-dark-second-dark dark:text-dark-prime outline-second rounded-full mb-4 w-80 sm:w-96 h-14"
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
						<label for="" class="hidden sm:flex dark:text-interface"
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
				<form>
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
									:type="showPassword ? 'text' : 'password'"
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
									:type="showRePassword ? 'text' : 'password'"
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
					It seems like you entered the wrong pin. Please try again.
				</p>
			</div>
		</div>
	</section>
</template>

<script>
import axios from "axios";
import { useDark, useToggle } from "@vueuse/core";
import { ref } from "vue";
import router from "../routes";
// import emailjs from "emailjs-com";

export default {
	name: "register-login",
	data() {
		return {
			// showLoginModal: null, // Comment: Controls the visibility of the login modal
			// loginSuccess: null, // Comment: Indicates whether the login was successful or not
			object: null, // Comment: Placeholder for any object data
			showModal: false, // Comment: Controls the visibility of a generic modal
			// // Data property for showing/hiding the OTP modal
			// showOtpModal: false, // Comment: Controls the visibility of the OTP modal
			modalActive: false, // Comment: Controls the visibility of a specific modal
			modalOTPActive: false, // Comment: Controls the visibility of the OTP modal
			fpmodalActive: false, // Comment: Controls the visibility of the forgot password modal
			fpmodalOTPActive: false, // Comment: Controls the visibility of the OTP modal in the forgot password flow
			modalChangeActive: false, // Comment: Controls the visibility of the password change modal
			modalInvalidActive: false, // Comment: Controls the visibility of the invalid modal
			input1: "", // Comment: Placeholder for the first input field
			input2: "", // Comment: Placeholder for the second input field
			input3: "", // Comment: Placeholder for the third input field
			input4: "", // Comment: Placeholder for the fourth input field
			input5: "", // Comment: Placeholder for the fifth input field
			input6: "", // Comment: Placeholder for the sixth input field
			
			showRePassword: false, // Comment: Controls the visibility of the re-enter password field
			showPassword: false, // Comment: Controls the visibility of the password field

			// inputs: ["", "", "", "", "", ""], // Comment: Placeholder for an array of input values
			inputs: new Array(6).fill(""), // Comment: Placeholder for an array of input values with a length of 6
			inputsRefs: [], // Comment: Placeholder for an array of input field references

			error: false, // Comment: Indicates whether an error occurred
			error_user: false, // Comment: Indicates whether there is an error related to the user
			error_email: false, // Comment: Indicates whether there is an error related to the email

			hasCapitalLetter: false, // Comment: Indicates whether the password has at least one capital letter
			hasSymbol: false, // Comment: Indicates whether the password has at least one symbol
			hasNumber: false, // Comment: Indicates whether the password has at least one number
			hasMinLength: false, // Comment: Indicates whether the password has a minimum length

			email: "", // Comment: Placeholder for the email input value
			rname: "", // Comment: Placeholder for the full name input value
			rcountry: "", // Comment: Placeholder for the country input value
			rusername: "", // Comment: Placeholder for the username input value
			rpassword: "", // Comment: Placeholder for the password input value
			repassword: "", // Comment: Placeholder for the re-enter password input value

			usernameValid: false, // Comment: Indicates whether the username is valid

			fpemail: "", // Comment: Placeholder for the forgot password email input value
			fp_newpassword: "", // Comment: Placeholder for the new password input value in the forgot password flow
			fp_confirmpassword: "", // Comment: Placeholder for the confirm password input value in the forgot password flow
			url: null, // Comment: Placeholder for the axios instance
		};
	},
	watch: {
		rpassword() {
			this.isValidPassword = this.rpassword.length >= 8;
		},
		repassword() {
			this.error = this.rpassword !== this.repassword;
		},
		rusername(newVal) {
			if (newVal !== "") {
				this.error_user = false;
				this.usernameValid = true;
			} else {
				this.usernameValid = false;
			}
		},
	},
	computed: {
		isGmailEmail() {
			this.error_email = false;
			const emailRegex = /^[A-Za-z0-9._%+-]+@gmail\.com$/;
			return emailRegex.test(this.email) ;
		},
		match() {
			return this.rpassword === this.repassword && this.rpassword !== "";
		},
		isValidNewPassword() {
			const password = this.fp_newpassword;
			this.hasCapitalLetter = /[A-Z]/.test(password);
			this.hasSymbol = /[!@#$%^&*(),.?":{}|<>]/.test(password);
			this.hasNumber = /\d/.test(password);
			this.hasMinLength = password.length >= 8;
			return (
				this.hasCapitalLetter &&
				this.hasSymbol &&
				this.hasNumber &&
				this.hasMinLength
			);
		},
		isValidConfirmPassword() {
			return this.fp_confirmpassword === this.fp_newpassword;
		},
		isValidPassword() {
			const password = this.rpassword;
			this.hasCapitalLetter = /[A-Z]/.test(password);
			this.hasSymbol = /[!@#$%^&*(),.?":{}|<>]/.test(password);
			this.hasNumber = /\d/.test(password);
			this.hasMinLength = password.length >= 8;
			return (
				this.hasCapitalLetter &&
				this.hasSymbol &&
				this.hasNumber &&
				this.hasMinLength
			);
		},
		isValidRePassword() {
			return this.repassword === this.rpassword;
		},
	},
	created() {
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
		});
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};

		this.url = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});
		client
			.get("api/user", { headers: headers })
			.then((res) => {
				window.scrollTo(0, 0);
				router.push({ name: "dashboard" }).then(() => {
					window.location.reload();
				});
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
	setup() {
		const isDark = useDark();
		const toggleDark = useToggle(isDark);

		const username = ref("");
		const password = ref("");

		// const modalOTPActive = ref(false);

		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});

		const submitLogin = () => {
			//console.log(email.value, password.value);
			client
				.post("/api/login", {
					username: username.value,
					password: password.value,
				})
				.then((response) => {
					console.log("Login successful:", response.data);
					// Redirect to home page
					const token = response.data.token; // Replace with your token
					localStorage.setItem("token", token);

					window.scrollTo(0, 0);

					router.push({ name: "dashboard" }).then(() => {
						window.location.reload();
					});
				})
				.catch((error) => {});
		};

		const submitLogout = () => {
			client.post("/api/logout").then((res) => {
				console.log("Logged out user:", res.data);
			});
		};

		return {
			//login
			username,
			password,

			//registration
			// email,
			// rcountry,
			// rname,
			// rusername,
			// rpassword,
			// repassword,
			//funstions
			// submitRegistration,
			submitLogin,
			submitLogout,

			isDark,
			toggleDark,
		};
	},

	methods: {
		test() {
			this.createToast("Wrong one-time password", "error");
		},
		createToast(message, type) {
			const toast = document.createElement("div");
			toast.id = "toast-simple";
			toast.className = `
	flex items-center justify-center w-full max-w-xs p-4 space-x-4 rtl:space-x-reverse
	text-interface
	bg-white divide-x rtl:divide-x-reverse divide-gray-200 rounded-lg shadow
	dark:divide-gray-700 dark:bg-gray-600
  `;
			toast.setAttribute("role", "alert");

			const messageElement = document.createElement("div");
			messageElement.className = "text-sm text-center font-normal";
			messageElement.textContent = message;

			toast.appendChild(messageElement);

			const toastContainer = document.createElement("div");
			toastContainer.className = `
    fixed bottom-16 right-4 sm:bottom-4 sm:right-[37%] sm:transform sm:-translate-x-1/2
    ${
		window.innerWidth <= 641
			? "bottom-20 left-1/2 transform -translate-x-1/2"
			: ""
	}
  `;

			toastContainer.appendChild(toast);
			document.body.appendChild(toastContainer);

			setTimeout(() => {
				toastContainer.remove();
			}, 5000);
		},
		onlyNumbers(event) {
			const charCode = event.which ? event.which : event.keyCode;
			if ((charCode < 48 || charCode > 57) && charCode !== 46) {
				event.preventDefault();
			}
		},
		sendOTPfp() {
			if (this.fpemail != "") {
				this.url
					.post("/api/fp-otp", {
						email: this.fpemail,
					})
					.then((response) => {
						console.log("Otp send successful:", response.data);
						this.fpmodalOTPActive = true;
						this.fpmodalActive = false;
						this.otp = response.data.otp;
					})
					.catch((error) => {
						console.log("ERROR: ", error);
					});
			} else {
				this.error = true;
				console.log("put email");
			}
		},
		verifyOTP(modal) {
			console.log(modal);
			if (modal == "register") {
				if (this.otp === parseInt(this.inputs.join(""))) {
					this.url
						.post("/api/registration", {
							email: this.email,
							fullname: this.rname,
							country: this.rcountry,
							username: this.rusername,
							password: this.rpassword,
						})
						.then((response) => {
							this.url
								.post("/api/login", {
									username: this.rusername,
									password: this.rpassword,
								})
								.then((response) => {
									this.showModal = false;
									this.modalOTPActive = false;
									const token = response.data.token; // Replace with your token
									localStorage.setItem("token", token);
									// localStorage.setItem(
									//  "username",
									//  response.data.user.username
									// );
									document.cookie =
										"name=value; SameSite=Lax; Secure";
									console.log("logged in!");
									window.scrollTo(0, 0);
									this.$router
										.push({ name: "dashboard" })
										.then(() => {
											window.location.reload();
										});
								});
							this.createToast(
								`Logged in as\n${this.rusername}`,
								"success"
							);
						})
						.catch((error) => {
							console.log("ERROR: ", error);
							// showRegisterModal.value = true;
							// registerSuccess.value = false;
						});
				} else {
					this.error = true;
					console.log(
						this.otp,
						" failed to verify the ",
						parseInt(this.inputs.join(""))
					);
				}
			}
			if (modal == "forgot-password") {
				console.log(parseInt(this.inputs.join("")));
				if (this.otp === parseInt(this.inputs.join(""))) {
					this.fpmodalOTPActive = false;
					this.modalChangeActive = true;
				} else {
					this.error = true;
					this.createToast("Wrong one-time password", "error");
				}
			}
		},
		confirmPassword() {
			if (this.fp_newpassword === this.fp_confirmpassword) {
				this.url
					.post("/api/fp-change", {
						email: this.fpemail,
						password: this.fp_newpassword,
					})
					.then((response) => {
						console.log(
							"Password changed successfully:",
							response.data
						);
						this.modalChangeActive = false;
						this.createToast(
							`${this.fpemail}\nPassword changed successfully`,
							"success"
						);
					})
					.catch((error) => {
						console.log("ERROR: ", error);
					});
			} else {
				this.error = true;
				console.log("Password does not match");
			}
		},
		submitRegistration() {
			if (this.rpassword === this.repassword) {
				this.url
					.post("/api/send-otp", {
						email: this.email,
						username: this.rusername,
					})
					.then((response) => {
						console.log("Otp send successful:", response.data);
						this.otp = response.data.otp;
						this.modalActive = true;
						this.modalOTPActive = true;
						this.error = false;
					})
					.catch((error) => {
						console.log("ERROR: ", error);
						if (error.response.data.email_error) {
							this.error_email = true;
						}
						if (error.response.data.username_error) {
							this.error_user = true;
						}
					});
			} else {
				this.error = true;
				console.log("Password does not match");
			}
		},
		toggleModal() {
			this.modalActive = !this.modalActive;
		},
		toggleChangeModal() {
			this.modalChangeActive = !this.modalChangeActive;
		},
		moveFocus(event, index) {
			if (event.key.match(/^[0-9]$/)) {
				if (index < this.inputs.length - 1) {
					this.inputsRefs[index + 1].focus();
				}
			} else if (event.keyCode === 8) {
				// backspace key
				if (index > 0) {
					this.inputsRefs[index - 1].focus();
				}
			}
		},
		// moveFocus(event, nextInput) {
		// 	if (event.target.value.length === 1) {
		// 		this.$refs[nextInput].focus();
		// 	}
		// },
		moveBack(event, prevInput) {
			if (event.target.value.length === 0 && prevInput !== "input1") {
				this.$refs[prevInput].focus();
			}
		},
	},
	mounted() {},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");
</style>
