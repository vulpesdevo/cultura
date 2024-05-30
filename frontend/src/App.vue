<script>
import Login from './components/Login.vue';

export default {
    components: {
        Login
    },
    
}
</script>

<template>
    <main class="h-full">
        <router-view />
    </main>
</template>

<style >
:root{
    --text-color-a: #ffff ;
    --text-color-b:#B8A3E9;
    --text-color-b:#B8A3E9;
    --text-color-c: #2C4760;
    --bg-main-color: #2C4760;
    --bg-secondary-color: #2D313D;
    
    --purple: #564787;


    --dark-bg-theme: #1E1E1E;
    
}
.color-purple {
	background-color: var(--purple);
}
.text-purple{
	color: var(--purple);
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
