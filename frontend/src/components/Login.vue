<script>
export default {};
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
					class="pl-5 border border-blue-300 rounded-full mb-4 bg-blue-300 w-80 sm:w-96 h-14"
				/>
				<input
					type="password"
					placeholder="Password"
					class="pl-5 border border-blue-300 rounded-full mb-2 bg-blue-300 w-80 sm:w-96 h-14"
				/>
				<a href="" class="text-center text-white mb-10 hover:underline"
					>Forgot passsword?</a
				>
				<button
					class="text-3xl bg-gray-900 text-white p-2 rounded-full w-52 h-14 mb-6 hover:bg-gray-800"
				>
					Log in
				</button>

				<span class="flex"
					><p class="text-white">Don't have an account?</p>
					<a href="" class="pl-3 text-blue-300">Sign Up Now!</a></span
				>
			</form>
		</div>
	</section>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

.login-section {
	background-color: var(--bg-main-color);
}

.cultura-text,
button {
	font-family: "Bebas Neue";
}

.slc,
input {
	font-family: "Montserrat";
}
input::placeholder {
	color: #6c6c6e;
}
</style>
