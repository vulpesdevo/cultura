import { onUnmounted } from "vue";

export function useGoogleMaps() {
	let autocomplete = null;

	const initializeAutocomplete = (inputElement) => {
		if (!window.google) {
			console.error("Google Maps JavaScript API not loaded");
			return;
		}

		autocomplete = new window.google.maps.places.Autocomplete(
			inputElement,
			{
				types: ["(regions)"],
			}
		);

		autocomplete.addListener("place_changed", () => {
			const place = autocomplete.getPlace();
			if (place.formatted_address) {
				inputElement.value = place.formatted_address;
			}
		});
	};

	onUnmounted(() => {
		if (autocomplete) {
			window.google.maps.event.clearInstanceListeners(autocomplete);
		}
	});

	return {
		initializeAutocomplete,
	};
}
