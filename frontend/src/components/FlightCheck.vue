<template>
	<div
		class="flex flex-col items-center align-middle sm:w-full px-5 sm:px-12 py-5 overflow-auto h-screen bg-field dark:bg-notif pt-14 sm:pt-0 text-interface"
	>
		<div v-if="loading">Loading...</div>
		<div v-if="error" class="error">{{ error }}</div>
		<div v-if="flights && flights.length">
			<h2>Flight Results:</h2>
			<ul>
				<li v-for="(flight, index) in flights" :key="index">
					<p><strong>Title:</strong> {{ flight.title }}</p>
					<p>
						<strong>Airports:</strong>
						<a :href="flight.link" target="_blank">{{
							flight.link
						}}</a>
					</p>
					<p><strong>Snippet:</strong> {{ flight.snippet }}</p>
					<div
						v-for="(segment, segIndex) in flight.flights"
						:key="segIndex"
					>
						<p>
							<strong>Segment {{ segIndex + 1 }}:</strong>
						</p>
						<p>
							<strong>Departure Airport:</strong>
							{{ segment.departure_airport.name }} ({{
								segment.departure_airport.id
							}})
						</p>
						<p>
							<strong>Arrival Airport:</strong>
							{{ segment.arrival_airport.name }} ({{
								segment.arrival_airport.id
							}})
						</p>
						<p>
							<strong>Departure Time:</strong>
							{{ segment.departure_airport.time }}
						</p>
						<p>
							<strong>Arrival Time:</strong>
							{{ segment.arrival_airport.time }}
						</p>
						<p>
							<strong>Duration:</strong>
							{{ segment.duration }} minutes
						</p>
						<p><strong>Airplane:</strong> {{ segment.airplane }}</p>
						<p><strong>Airline:</strong> {{ segment.airline }}</p>
						<img :src="segment.airline_logo" alt="Airline Logo" />
						<p>
							<strong>Travel Class:</strong>
							{{ segment.travel_class }}
						</p>
						<p>
							<strong>Flight Number:</strong>
							{{ segment.flight_number }}
						</p>
						<p><strong>Legroom:</strong> {{ segment.legroom }}</p>
						<p><strong>Extensions:</strong></p>
						<ul>
							<li
								v-for="(
									extension, extIndex
								) in segment.extensions"
								:key="extIndex"
							>
								{{ extension }}
							</li>
						</ul>
					</div>
					<div v-if="flight.layovers && flight.layovers.length">
						<p><strong>Layovers:</strong></p>
						<ul>
							<li
								v-for="(layover, layIndex) in flight.layovers"
								:key="layIndex"
							>
								<p>
									<strong>Layover {{ layIndex + 1 }}:</strong>
									{{ layover.name }} ({{ layover.id }})
								</p>
								<p>
									<strong>Duration:</strong>
									{{ layover.duration }} minutes
								</p>
							</li>
						</ul>
					</div>
					<p>
						<strong>Total Duration:</strong>
						{{ flight.total_duration }} minutes
					</p>
					<p>
						<strong>Carbon Emissions:</strong>
						{{ flight.carbon_emissions.this_flight }} kg
					</p>
					<p><strong>Price:</strong> ${{ flight.price }}</p>
					<img :src="flight.airline_logo" alt="Airline Logo" />
					<p><strong>Extensions:</strong></p>
					<ul>
						<li
							v-for="(extension, extIndex) in flight.extensions"
							:key="extIndex"
						>
							{{ extension }}
						</li>
					</ul>
				</li>
			</ul>
		</div>
		<div v-else-if="!loading && !error">
			<p>No flight results found.</p>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			apiKey: "5394dbdebc3e75f87956b173bc7ef5c974793bbd67b24d19f12e68125a8d94f7", // Replace with your actual API key
			csrfToken: "YOUR_CSRF_TOKEN", // Replace with your actual CSRF token
			flights: [],
			loading: false,
			error: null,
		};
	},
	methods: {
		async fetchFlightData() {
			this.loading = true;
			this.error = null;
			const url = `https://cors-anywhere.herokuapp.com/https://serpapi.com/search.json?engine=google_flights&departure_id=CDG&arrival_id=AUS&gl=us&hl=en&currency=USD&outbound_date=2024-09-20&return_date=2024-09-26&api_key=${this.apiKey}`;

			try {
				const response = await fetch(url, {
					headers: {
						"X-CSRF-Token": this.csrfToken,
					},
				});
				console.log("Response:", response);
				if (!response.ok) {
					throw new Error(
						`Network response was not ok: ${response.statusText}`
					);
				}
				const data = await response.json();
				console.log("Flight data:", data);
				this.flights = data.best_flights || [];
			} catch (error) {
				this.error = `Failed to fetch flight data: ${error.message}`;
				console.error("Failed to fetch flight data:", error);
			} finally {
				this.loading = false;
			}
		},
	},
	mounted() {
		this.fetchFlightData();
	},
};
</script>

<style scoped>
.error {
	color: red;
}
</style>
