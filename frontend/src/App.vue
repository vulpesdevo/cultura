
<template>
	<main class="h-full">
		<router-view />
	</main>
</template>

<script>
import Login from "./components/Login.vue";
import Sidebar from "./components/Sidebar.vue";
export default {
	components: {
		Sidebar,
	},
};
</script>
<style>
:root {
	--text-color-a: #ffff;
	--text-color-b: #b8a3e9;
	--text-color-c: #2c4760;

	--bg-main-color: #2c4760;
	--bg-secondary-color: #2d313d;

	--purple: #564787;

	--dark-bg-theme: #1e1e1e;
}
.color-purple {
	background-color: var(--purple);
}
.text-purple {
	color: var(--purple);
}
.text-purple-light{
    color: var(--text-color-b);
}
.dark-bg-color{
    background: var(--dark-bg-theme);
}

.cultura-text,
.buttons,
.text-bebas {
	font-family: "Bebas Neue";
}

.slc,
input,
.text-mont {
	font-family: "Montserrat";
}
input::placeholder {
	color: var(--text-color-a);
}
</style>
