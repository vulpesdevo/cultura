<script>
export default {
	data() {
		return {
			showModal: false,
		};
	},
};
</script>

<template>
	<section
		class="login-section h-screen flex flex-col justify-center sm:flex-row p-24"
	>
		<div
			class="logo-container sm:pl-20 flex justify-center items-center align-middle"
		>
			<img
				class="img-logo sm:w-auto sm:h-auto"
				src="/login/culturalink_logo.png"
				alt="cultura-logo"
			/>
		</div>
		<div
			class="flex flex-col justify-center items-center w-full align-middle sm:ml-20"
		>
			<h3
				class="slc pl-2 sm:pl-0 flex text-center text-white text-2xl w-72 sm:text-5xl mb-3 sm:w-auto"
			>
				Share. Learn. Connect.
			</h3>
			<h1
				class="cultura-text text-6xl text-white text-center mb-6 tracking-widest sm:text-9xl"
			>
				Culturalink
			</h1>
			<form
				class="flex flex-col justify-center align-middle items-center m-12 mx-10"
			>
				<input
					type="text"
					placeholder="Username"
					class="pl-5  color-purple rounded-full mb-4  w-80 sm:w-96 h-14"
				/>
				<input
					type="password"
					placeholder="Password"
					class="pl-5  color-purple rounded-full mb-2  w-80 sm:w-96 h-14"
				/>
				<a href="" class="text-center text-white mb-10 hover:underline"
					>Forgot passsword?</a
				>
				<input
					type="submit"
					value="Log in"
					class="buttons text-3xl bg-gray-300 text-purple p-2 rounded-full w-52 h-14 mb-6 hover:bg-gray-400"
				/>

				<span class="flex"
					><p class="text-white">Don't have an account?</p>
					<a
						href=""
						class="pl-3 text-blue-300"
						@click.prevent="showModal = true"
						>Sign Up Now!</a
					></span
				>
			</form>
		</div>
		<div
			class="fixed z-10 inset-0 overflow-y-auto"
			aria-labelledby="modal-title"
			role="dialog"
			aria-modal="true"
			v-if="showModal"
		>
			<div
				class="flex items-center justify-center h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
			>
				<div
					class="fixed inset-0 bg-black bg-opacity-70 transition-opacity"
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
					<button
						class="absolute top-0 right-0 m-2 mr-3 text-white text-2xl"
						@click="showModal = false"
					>
						&times;
					</button>
					<div
						class="modal-bg px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-center"
					>
						<h3
							class="text-bebas text-4xl sm:text-7xl leading-6 font-medium text-white"
							id="modal-title"
						>
							SIGN UP
						</h3>
						<p class="text-mont text-white pt-1 pb-5 text-2xl">
							Create your account
						</p>
						<form class="mt-2">
							<div class="flex flex-wrap">
								<div class="w-full md:w-1/2 px-3">
									<input
										type="text"
										placeholder="Username"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
									<input
										type="email"
										placeholder="Email"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
									<input
										type="text"
										placeholder="Name"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
								</div>
								<div class="w-full md:w-1/2 px-3">
									<input
										type="text"
										placeholder="Country"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
									<input
										type="password"
										placeholder="Password"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
									<input
										type="password"
										placeholder="Re-enter Password"
										class="mt-2 pl-5 w-full rounded-full h-14 color-purple"
									/>
								</div>
							</div>

							<div
								class="flex flex-col items-center align-middle text-center"
							>
								<p class="py-5 text-white text-mont text-xs">
									By signing up, you agree to the Terms of
									Service and Privacy Policy, including Cookie
									Use.
								</p>
								<input
									type="submit"
									value="SIGN UP"
									class="buttons text-3xl bg-gray-300 text-purple-800 p-2 rounded-full w-52 h-14 mb-6 hover:bg-gray-400"
								/>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</section>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

.modal-bg {
	background-color: var(--dark-bg-theme);
}

.login-section {
	background-color: var(--dark-bg-theme);
}

</style>
