<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-8 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-5 sm:pt-7"
	>
		<div
			class="profile-1 w-full pt-3 px-3 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface"
		>
			<div class="profile-edit w-full flex justify-end">
				<span class="material-icons-outlined text-4xl"> edit </span>
			</div>
			<div
				class="profile-img flex flex-col items-center align-middle mb-10"
			>
				<img
					class="rounded-full shadow-2xl drop-shadow-xl w-60 mb-8"
					src="/sample_img/mark.png"
					alt=""
				/>
				<h1
					class="font-bebas-neue profile-name text-5xl sm:text-7xl drop-shadow-lg shadow-black text-prime"
				>
					Mark Francis
				</h1>
			</div>
			<div class="profile-details flex justify-center align-middle mb-10">
				<div
					class="profile-desc text-xm sm:text-2xl flex items-start flex-col me-7 sm:me-32"
				>
					<h1 class="font-montserrat text-prime mb-5">Username:</h1>
					<h1 class="font-montserrat text-prime mb-5">Email:</h1>
					<h1 class="font-montserrat text-prime mb-5">Password:</h1>
					<h1 class="font-montserrat text-prime mb-5">Country:</h1>
				</div>
				<div class="profile-info text-xm sm:text-2xl flex flex-col">
					<h1 class="font-montserrat text-prime mb-5">mark0</h1>
					<h1 class="font-montserrat text-prime mb-5">
						mark.galan@sdca.edu.ph
					</h1>
					<h1 class="font-montserrat text-prime mb-5">**********</h1>
					<h1 class="font-montserrat text-prime mb-5">Bermuda</h1>
				</div>
			</div>
		</div>
		<div class="profile-tabs flex justify-center w-full mt-5 -ms-5">
			<button
				class="font-montserrat text-white rounded-3xl h-10 sm:h-14 w-40 sm:w-60 text-xl sm:text-3xl bg-second"
			>
				Posts
			</button>
			<button
				class="font-montserrat text-prime rounded-3xl h-10 sm:h-14 w-40 sm:w-60 text-xl sm:text-3xl ms-5 sm:ms-10"
			>
				Achievements
			</button>
		</div>

		<div
			class="post-contents w-full h-full sm:h-full pt-3 pb-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg bg-interface mt-5 mb-14 sm:mt-10"
		>
			<div class="post-title flex justify-between items-center">
				<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
					BEST PULLED NOODLES IN BINONDO
				</h1>
				<small class="text-second">10mins ago</small>
			</div>
			<div class="post-content flex w-full mt-4">
				<div class="w-14 h-14 mr-4">
					<img
						src="/sample_img/mark.png"
						alt="Profile"
						class="rounded-full cursor-pointer"
					/>
				</div>
				<div class="w-full">
					<div class="flex border-b-2">
						<small class="font-montserrat text-prime pr-5">
							@mark0
						</small>
						<small class="about-post font-montserrat">
							Food | Philippines
						</small>
					</div>
					<p
						class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify"
					>
						Slurp-worthy satisfaction awaits at Lan-Zhou Lamien,
						where every strand of their hand-pulled noodles tells a
						tale of culinary mastery. Taste the tradition, savor the
						excellence, and discover why they're Manila's noodle
						maestros.
					</p>
				</div>
			</div>
			<div class="flex items-center justify-end">
				<i
					class="fa-regular fa-comment text-second text-2xl pr-2"
					@click.prevent="showModal = true"
				></i>
				<span class="material-icons-outlined text-second text-2xl"
					>favorite_border</span
				>
			</div>
		</div>
	</div>
</template>

<script></script>

<style></style>
