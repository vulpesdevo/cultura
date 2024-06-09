<template>
	<div
		class="flex flex-col items-center align-middle w-full px-5 sm:px-28 py-5 sm:ml-64 overflow-auto"
	>
		<div
			class="crate-post-container w-full pt-3 px-6 mb-3 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
		>
			<div class="flex justify-between items-center">
				<h1 class="font-bebas-neue text-lg text-prime sm:text-3xl">
					POST TITLE
				</h1>
				<div
					class="drop-down-categ w-1/2 flex items-center justify-end font-montserrat"
				>
					<select
						name=""
						id=""
						class=" sm:w-1/2 rounded-full bg-field outline-none p-1"
					>
						<option value="" disabled selected>Category</option>
						<option value="Food">Food</option>
						<option value="Traditions">Traditions</option>
						<option value="History">History</option>
					</select>
				</div>
			</div>
			<div class="for-content flex w-full mt-4">
				<div class="hidden sm:flex w-14 h-14 mr-4">
					<img
						src="/sample_img/mark.png"
						alt="Profile"
						class="rounded-full cursor-pointer"
					/>
				</div>
				<textarea
					class="w-full rounded-lg resize-none p-4 outline-none"
					name=""
					id=""
					cols="30"
					rows=""
					placeholder="What do you want to share?"
				></textarea>
			</div>
			<div
				class="about-country font-montserrat flex my-3 items-center justify-between border-b-2 p-1"
			>
				<p class=" hidden sm:flex text-prime">
					What coutry is your post about?
				</p>
				<p class="flex sm:hidden text-prime">Country</p>
				<input
					type="text"
					class="bg-field rounded-full pl-3 h-9 w-1/2 outline-none"
					placeholder=""
				/>

				<div class="hidden sm:flex sm:w-1/5"></div>
			</div>
			<div class="flex my-3 items-center justify-between">
				<div class="flex">
					<label for="imgSelect">
						<span
							class="material-icons-outlined text-second text-3xl"
							>image</span
						>
					</label>
					<input type="file" name="" id="imgSelect" class="hidden" />
					<span
						class="material-icons-outlined text-second text-3xl pl-2"
						>explore</span
					>
				</div>
				<input
					type="submit"
					value="Post"
					class="font-montserrat text-xl bg-second text-interface p-2 rounded-full w-36 h-12 hover:bg-second-light "
				/>
			</div>
		</div>
		<section class="posts">
			<div
				class="post-contents w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
			>
				<div class="post-title flex justify-between items-center">
					<h1 class="font-bebas-neue text-lg text-prime sm:text-2xl">
						BEST PULLED NOODLES IN BINONDO
					</h1>
					<p class="text-second">10mins ago</p>
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
							<p class="font-montserrat text-prime pr-5">
								@mark0
							</p>
							<p class="about-post font-montserrat">
								Food | Philippines
							</p>
						</div>
						<p
							class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify "
						>
							Slurp-worthy satisfaction awaits at Lan-Zhou Lamien,
							where every strand of their hand-pulled noodles
							tells a tale of culinary mastery. Taste the
							tradition, savor the excellence, and discover why
							they're Manila's noodle maestros.
						</p>
					</div>
				</div>
				<div class="flex items-center justify-end">
					<i
						class="fa-regular fa-comment text-second text-2xl pr-2" @click.prevent="showModal = true"
					></i>
					<span class="material-icons-outlined text-second text-2xl"
						>favorite_border</span
					>
				</div>
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
							class="absolute top-0 right-0 m-2 mr-3 text-prime text-2xl"
							@click="showModal = false"
						>
							&times;
						</button>
						<div
							class="post-contents bg-interface w-full pt-3 px-6 sm:pt-6 sm:px-9 rounded-lg shadow-lg"
						>
							<div
								class="post-title flex justify-between items-center"
							>
								<h1
									class="font-bebas-neue text-lg text-prime sm:text-2xl"
								>
									BEST PULLED NOODLES IN BINONDO
								</h1>
								
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
										<p
											class="font-montserrat text-prime pr-5"
										>
											@mark0
										</p>
										<p class="about-post font-montserrat">
											Food | Philippines
										</p>
									</div>
									<p
										class="font-montserrat w-full rounded-lg resize-none p-4 text-sm text-justify "
									>
										Slurp-worthy satisfaction awaits at
										Lan-Zhou Lamien, where every strand of
										their hand-pulled noodles tells a tale
										of culinary mastery. Taste the
										tradition, savor the excellence, and
										discover why they're Manila's noodle
										maestros.
									</p>
								</div>
							</div>
                            <div class="reply-post flex w-full mt-4">
                                <div class="w-14 h-14 mr-4">
									<img
										src="/sample_img/mark.png"
										alt="Profile"
										class="rounded-full cursor-pointer"
									/>
								</div>
                                <textarea
                                    class="w-full rounded-lg resize-none p-4 outline-none"
                                    name=""
                                    id=""
                                    cols="30"
                                    rows=""
                                    placeholder="Replying to @mark0"
                                ></textarea>
                            </div>
							<div class="flex py-3 items-center justify-between border-t-2 mt-2">
								<div class="flex">
									<label for="imgSelect">
										<span
											class="material-icons-outlined text-second text-3xl"
											>image</span
										>
									</label>
									<input
										type="file"
										name=""
										id="imgSelect"
										class="hidden"
									/>
									<span
										class="material-icons-outlined text-second text-3xl pl-2"
										>explore</span
									>
								</div>
								<input
									type="submit"
									value="Reply"
									class="font-montserrat text-xl bg-second text-interface rounded-full w-28 h-10 hover:bg-second-light"
								/>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</div>
</template>

<script>
export default {
    data() {
        return {
            showModal: false,
        };
    },
    
}
</script>
<style scoped></style>
