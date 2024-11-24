<template>
	<div class="h-screen bg-gray-900 p-6">
		<div class="max-w-7xl mx-auto">
			<h1 class="text-3xl font-bold text-white mb-8">
				Cultura Users Management
			</h1>

			<!-- Users List -->
			<div class="space-y-4">
				<div
					v-for="user in culturaUsers"
					:key="user.id"
					class="relative bg-gray-800 rounded-lg overflow-hidden transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/10 hover:translate-y-[-2px]"
				>
					<div class="p-6">
						<!-- User Header -->
						<div class="flex items-start justify-between">
							<div class="flex items-start space-x-4">
								<img
									:src="
										user.user_photo ||
										'/placeholder.svg?height=48&width=48'
									"
									class="w-12 h-12 rounded-full object-cover"
									alt=""
								/>
								<div>
									<h3
										class="text-lg font-semibold text-white"
									>
										{{ user.fullname }}
									</h3>
									<p class="text-gray-400">
										{{ user.email }}
									</p>
									<p class="text-sm text-gray-500">
										{{ user.country }}
									</p>
								</div>
							</div>
							<div class="flex flex-col items-end">
								<span
									:class="[
										'px-2 py-1 rounded-full text-xs font-medium',
										user.is_active
											? 'bg-green-100 text-green-800'
											: 'bg-red-100 text-red-800',
									]"
								>
									{{ user.is_active ? "Active" : "Inactive" }}
								</span>
								<span class="text-sm text-gray-500 mt-1"
									>ID: {{ user.id }}</span
								>
							</div>
						</div>

						<!-- Achievements -->
						<div class="mt-4 flex flex-wrap gap-2">
							<div
								v-if="user.like_leader > 0"
								class="inline-flex items-center px-2.5 py-1 rounded-md bg-pink-500/10 text-pink-400 text-xs"
							>
								<span class="mr-1">❤️</span>
								Like Leader: {{ user.like_leader }}
							</div>
							<div
								v-if="user.guide_guru > 0"
								class="inline-flex items-center px-2.5 py-1 rounded-md bg-blue-500/10 text-blue-400 text-xs"
							>
								<span class="mr-1">🎓</span>
								Guide Guru: {{ user.guide_guru }}
							</div>
							<div
								v-if="user.content_creator > 0"
								class="inline-flex items-center px-2.5 py-1 rounded-md bg-green-500/10 text-green-400 text-xs"
							>
								<span class="mr-1">✍️</span>
								Content Creator: {{ user.content_creator }}
							</div>
							<div
								v-if="user.comment_connoisseur > 0"
								class="inline-flex items-center px-2.5 py-1 rounded-md bg-yellow-500/10 text-yellow-400 text-xs"
							>
								<span class="mr-1">💭</span>
								Comment Connoisseur:
								{{ user.comment_connoisseur }}
							</div>
						</div>

						<!-- Actions -->
						<div class="mt-4 flex justify-end space-x-2">
							<button
								@click="openEditModal(user)"
								class="px-4 py-2 text-sm font-medium text-white bg-blue-500/10 rounded-md hover:bg-blue-500/20 transition-colors duration-200"
							>
								Edit
							</button>
							<button
								@click="confirmDelete(user.id)"
								class="px-4 py-2 text-sm font-medium text-white bg-red-500/10 rounded-md hover:bg-red-500/20 transition-colors duration-200"
							>
								Delete
							</button>
						</div>

						<!-- Hover Details -->
						<div
							class="absolute inset-0 w-3/4 bg-gray-800/95 opacity-0 group-hover:opacity-100 group-hover:visible transition-all duration-300 flex items-center justify-center p-6 z-10"
							:class="{
								'opacity-100 ': activeUserId === user.id,
							}"
							@mouseenter="activeUserId = user.id"
							@mouseleave="activeUserId = null"
						>
							<div
								class="flex flex-col justify-start items-start w-full"
							>
								<h4
									class="text-lg font-semibold text-white mb-4"
								>
									Additional Information
								</h4>
								<div class="grid grid-cols-2 gap-6">
									<!-- Stats -->
									<div>
										<h5
											class="text-sm font-medium text-gray-400 mb-2"
										>
											Statistics
										</h5>
										<div class="space-y-2">
											<p class="text-sm text-white">
												Followers:
												{{ user.follow_count }}
											</p>
											<p class="text-sm text-white">
												Trend Setter:
												{{ user.trend_setter }}
											</p>
											<p class="text-sm text-white">
												Share Star:
												{{ user.share_star }}
											</p>
											<p class="text-sm text-white">
												Knowledge Seeker:
												{{ user.knowledge_seeker }}
											</p>
										</div>
									</div>
									<!-- Followers -->
									<div>
										<h5
											class="text-sm font-medium text-gray-400 mb-2"
										>
											Followers
										</h5>
										<div
											class="space-y-1 max-h-32 overflow-y-auto"
										>
											<p
												v-for="follower in user.followers"
												:key="follower.id"
												class="text-sm text-white"
											>
												{{ follower.username }}
											</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Modals -->
			<div
				v-if="showModal"
				class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50"
			>
				<div
					class="bg-gray-800 rounded-lg w-full max-w-md p-6"
					@click.stop
				>
					<h3 class="text-xl font-semibold text-white mb-4">
						{{ editingUser ? "Edit User" : "Create New User" }}
					</h3>
					<form @submit.prevent="submitUser" class="space-y-4">
						<div>
							<label
								class="block text-sm font-medium text-gray-300 mb-1"
								>Full Name</label
							>
							<input
								v-model="userForm.fullname"
								type="text"
								required
								class="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>
						<div>
							<label
								class="block text-sm font-medium text-gray-300 mb-1"
								>Email</label
							>
							<input
								v-model="userForm.email"
								type="email"
								required
								class="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>
						<div>
							<label
								class="block text-sm font-medium text-gray-300 mb-1"
								>Country</label
							>
							<input
								v-model="userForm.country"
								type="text"
								required
								class="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
						</div>
						<div class="flex justify-end space-x-3 mt-6">
							<button
								type="button"
								@click="closeModal"
								class="px-4 py-2 text-sm font-medium text-gray-300 bg-gray-700 rounded-md hover:bg-gray-600 transition-colors duration-200"
							>
								Cancel
							</button>
							<button
								type="submit"
								class="px-4 py-2 text-sm font-medium text-white bg-blue-500 rounded-md hover:bg-blue-600 transition-colors duration-200"
							>
								{{ editingUser ? "Update" : "Create" }}
							</button>
						</div>
					</form>
				</div>
			</div>

			<!-- Delete Confirmation Modal -->
			<div
				v-if="showDeleteModal"
				class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50"
			>
				<div
					class="bg-gray-800 rounded-lg w-full max-w-md p-6"
					@click.stop
				>
					<h3 class="text-xl font-semibold text-white mb-4">
						Confirm Delete
					</h3>
					<p class="text-gray-300 mb-6">
						Are you sure you want to delete this user? This action
						cannot be undone.
					</p>
					<div class="flex justify-end space-x-3">
						<button
							@click="closeDeleteModal"
							class="px-4 py-2 text-sm font-medium text-gray-300 bg-gray-700 rounded-md hover:bg-gray-600 transition-colors duration-200"
						>
							Cancel
						</button>
						<button
							@click="deleteUser"
							class="px-4 py-2 text-sm font-medium text-white bg-red-500 rounded-md hover:bg-red-600 transition-colors duration-200"
						>
							Delete
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, reactive } from "vue";
import { useStore } from "vuex";

const store = useStore();
const culturaUsers = ref([]);
const showModal = ref(false);
const showDeleteModal = ref(false);
const editingUser = ref(null);
const userToDeleteId = ref(null);
const activeUserId = ref(null);

const userForm = reactive({
	fullname: "",
	email: "",
	country: "",
});

onMounted(async () => {
	await fetchUsers();
});

const fetchUsers = async () => {
	const res = await store.dispatch("fetchCulturaUsers");
	culturaUsers.value = res.data;
};

const openCreateModal = () => {
	editingUser.value = null;
	userForm.fullname = "";
	userForm.email = "";
	userForm.country = "";
	showModal.value = true;
};

const openEditModal = (user) => {
	editingUser.value = user;
	userForm.fullname = user.fullname;
	userForm.email = user.email;
	userForm.country = user.country;
	showModal.value = true;
};

const closeModal = () => {
	showModal.value = false;
	editingUser.value = null;
};

const submitUser = async () => {
	try {
		if (editingUser.value) {
			await store.dispatch("updateCulturaUser", {
				id: editingUser.value.id,
				userData: userForm,
			});
		} else {
			await store.dispatch("createCulturaUser", userForm);
		}
		await fetchUsers();
		closeModal();
	} catch (error) {
		console.error("Error submitting user:", error);
	}
};

const confirmDelete = (userId) => {
	userToDeleteId.value = userId;
	showDeleteModal.value = true;
};

const closeDeleteModal = () => {
	showDeleteModal.value = false;
	userToDeleteId.value = null;
};

const deleteUser = async () => {
	try {
		await store.dispatch("deleteCulturaUser", userToDeleteId.value);
		await fetchUsers();
		closeDeleteModal();
	} catch (error) {
		console.error("Error deleting user:", error);
	}
};
</script>
