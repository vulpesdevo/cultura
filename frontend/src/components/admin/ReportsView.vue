<template lang="">
	<div class="h-screen bg-gray-50 dark:bg-gray-900 p-4 sm:p-6 lg:p-8">
		<div class="max-w-7xl mx-auto">
			<!-- Header -->
			<div class="mb-6 sm:mb-8">
				<h1
					class="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white"
				>
					Content Reports
				</h1>
				<p
					class="mt-2 text-sm sm:text-base text-gray-600 dark:text-gray-400"
				>
					Manage and review reported content
				</p>
			</div>

			<!-- Reports List -->
			<div class="bg-white dark:bg-gray-800 rounded-lg shadow-sm">
				<div class="overflow-hidden">
					<div v-if="loading" class="p-4 sm:p-6 text-center">
						<div
							class="animate-spin rounded-full h-10 w-10 sm:h-12 sm:w-12 border-b-2 border-gray-900 dark:border-gray-100 mx-auto"
						></div>
						<p
							class="mt-4 text-sm sm:text-base text-gray-600 dark:text-gray-400"
						>
							Loading reports...
						</p>
					</div>

					<div
						v-else-if="reports.length === 0"
						class="p-4 sm:p-6 text-center"
					>
						<DocumentTextIcon
							class="mx-auto h-10 w-10 sm:h-12 sm:w-12 text-gray-400"
						/>
						<h3
							class="mt-2 text-sm font-medium text-gray-900 dark:text-white"
						>
							No reports
						</h3>
						<p
							class="mt-1 text-sm text-gray-500 dark:text-gray-400"
						>
							There are no content reports to review at this time.
						</p>
					</div>

					<div
						v-else
						class="divide-y divide-gray-200 dark:divide-gray-700"
					>
						<div
							v-for="report in reports"
							:key="report._id"
							class="p-4 sm:p-6"
						>
							<!-- Report Card -->
							<div
								class="bg-white dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700"
							>
								<!-- Original Post Content -->
								<div
									if
									v-if="report.post"
									class="p-4 border-b border-gray-200 dark:border-gray-700"
								>
									<div class="flex items-start space-x-3">
										<div class="flex-shrink-0">
											<img
												:src="
													report.post?.author_data
														.user_photo ||
													`/placeholder.svg?height=40&width=40`
												"
												class="h-10 w-10 rounded-full"
												alt="User avatar"
											/>
										</div>
										<div class="min-w-0 flex-1">
											<p
												class="text-sm font-medium text-gray-900 dark:text-white"
											>
												{{
													report.post?.author_data
														.fullname
												}}
											</p>
											<p
												class="text-xs text-gray-500 dark:text-gray-400"
											>
												{{
													new Date(
														report.post?.date_posted
													).toLocaleString()
												}}
											</p>
										</div>
									</div>
									<h3
										class="mt-2 text-lg font-semibold text-gray-900 dark:text-white"
									>
										{{ report.post?.title }}
									</h3>
									<p
										class="mt-1 text-sm text-gray-700 dark:text-gray-300"
									>
										{{ report.post?.content }}
									</p>
									<div v-if="report.post?.image" class="mt-2">
										<img
											:src="report.post?.image"
											alt="Post image"
											class="w-auto h-56 rounded-lg object-scale-down"
										/>
									</div>
									<div
										class="mt-2 flex items-center text-sm text-gray-500 dark:text-gray-400"
									>
										<MapPinIcon class="mr-1 h-4 w-4" />
										{{ report.post?.country }}
									</div>
									<div
										class="mt-2 flex items-center text-sm text-gray-500 dark:text-gray-400"
									>
										<TagIcon class="mr-1 h-4 w-4" />
										{{ report.post?.category }}
									</div>
									<div
										class="mt-2 flex items-center text-sm text-gray-500 dark:text-gray-400"
									>
										<HeartIcon class="mr-1 h-4 w-4" />
										{{ report.post?.like_count }} likes
									</div>
								</div>

								<!-- Report Details -->
								<div class="p-4 bg-gray-50 dark:bg-gray-900">
									<div
										class="flex flex-col sm:flex-row sm:items-center sm:justify-between"
									>
										<div class="mb-2 sm:mb-0">
											<span
												class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200"
											>
												{{ report.category }}
											</span>
											<p
												class="mt-1 text-xs text-gray-500 dark:text-gray-400"
											>
												Report ID: {{ report._id }}
											</p>
											<p
												class="mt-1 text-xs text-gray-500 dark:text-gray-400"
											>
												Reported on:
												{{
													new Date(
														report.date_posted
													).toLocaleString()
												}}
											</p>
										</div>
										<div
											v-if="report.post"
											class="flex space-x-2"
										>
											<button
												@click="
													handleApprove(
														report.post._id
													)
												"
												class="inline-flex items-center px-2.5 py-1.5 border border-transparent text-xs font-medium rounded shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 dark:focus:ring-offset-gray-900"
											>
												<CheckIcon
													class="h-4 w-4 mr-1"
												/>
												Approve
											</button>
											<button
												@click="
													handleDelete(report._id)
												"
												class="inline-flex items-center px-2.5 py-1.5 border border-transparent text-xs font-medium rounded shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 dark:focus:ring-offset-gray-900"
											>
												<TrashIcon
													class="h-4 w-4 mr-1"
												/>
												Delete
											</button>
										</div>
									</div>
									<div class="mt-2">
										<h4
											class="text-sm font-medium text-gray-900 dark:text-white"
										>
											Report Details:
										</h4>
										<p
											class="mt-1 text-sm text-gray-700 dark:text-gray-300"
										>
											{{ report.details }}
										</p>
									</div>
									<div class="mt-2 relative">
										<button
											@mouseenter="
												showReporterInfo(report._id)
											"
											@mouseleave="hideReporterInfo"
											@focus="
												showReporterInfo(report._id)
											"
											@blur="hideReporterInfo"
											class="text-sm text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300 focus:outline-none"
										>
											View Reporter Info
										</button>
										<div
											v-if="
												activeReporterId === report._id
											"
											class="absolute z-10 w-64 p-4 mt-2 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700"
										>
											<h5
												class="font-semibold text-gray-900 dark:text-white"
											>
												Reporter Information
											</h5>
											<p
												class="mt-1 text-sm text-gray-600 dark:text-gray-400"
											>
												Name: {{ report.user.fullname }}
											</p>
											<p
												class="text-sm text-gray-600 dark:text-gray-400"
											>
												User ID: {{ report.user.id }}
											</p>
											<p
												class="text-sm text-gray-600 dark:text-gray-400"
											>
												Country:
												{{ report.user.country }}
											</p>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useStore } from "vuex";
import {
	DocumentTextIcon,
	CheckIcon,
	TrashIcon,
	MapPinIcon,
	TagIcon,
	HeartIcon,
} from "@heroicons/vue/24/outline";
import { useRouter } from "vue-router";
const router = useRouter();
const store = useStore();
const reports = ref([]);
const loading = ref(true);
const activeReporterId = ref(null);
const isLoading = ref(true);

onMounted(async () => {
	await store
		.dispatch("fetchUserData")
		.then(async (response) => {
			if (!response.profile.is_admin) {
				router.push({ name: "NotFound" });
			} else {
				await fetchReports();
			}
		})
		.catch((error) => {
			console.error("Error fetching user data:", error);
			router.push({ name: "NotFound" });
		});
});
const fetchReports = async () => {
	try {
		const data = await store.dispatch("fetchReports");
		reports.value = data.reverse();
	} catch (error) {
		console.error("Error fetching reports:", error);
	} finally {
		loading.value = false;
	}
};

const handleApprove = async (id) => {
	try {
		await store.dispatch("updateReport", {
			id,
		});
		await fetchReports();
	} catch (error) {
		console.error("Error approving report:", error);
	}
};

const handleDelete = async (id) => {
	try {
		await store.dispatch("deleteReport", id);
		await fetchReports();
	} catch (error) {
		console.error("Error deleting report:", error);
	}
};

const showReporterInfo = (reportId) => {
	activeReporterId.value = reportId;
};

const hideReporterInfo = () => {
	activeReporterId.value = null;
};
</script>
