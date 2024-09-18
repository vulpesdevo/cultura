<template>
    <div class="h-screen bg-gray-900 flex justify-center items-center absolute w-full top-0 left-0  px-8 z-50">
        <div class="flex-col sm:w-3/4 rounded-lg p-10 bg-interface dark:bg-dark-interface self-start mt-36 ">
            <p class="font-montserrat block text-white text-center text-5xl font-bold pb-4 border-b-[0.2px] border-white">Report</p>
            <p v-if="step !== 3" class="font-montserrat block text-white text-left text-xl font-bold pt-2 ">Why are you reporting this post?</p>
            <p v-if="step !== 3" class="font-montserrat block text-gray-400 text-left text-md pb-2 ">If you believe this post suggests someone is in immediate danger, contact local authorities first for help before reporting it to CulturaLink.</p>

        <!-- FIRST CONTAINER FOR STEP 1  -->
        <div v-if="step === 1" class="space-y-4 pt-5">
            <div>
            <label class="block text-white font-montserrat text-lg">
                <input type="radio" v-model="selectedCategory" value="Violent, hateful, or disturbing content" class="mr-2">
                Violent, hateful, or disturbing content
            </label>
            </div>
            <div>
            <label class="block text-white font-montserrat text-lg">
                <input type="radio" v-model="selectedCategory" value="Scam or false information" class="mr-2">
                Scam or false information
            </label>
            </div>
            <div>
            <label class="block text-white font-montserrat text-lg">
                <input type="radio" v-model="selectedCategory" value="Bullying, harassment or abuse" class="mr-2">
                Bullying, harassment or abuse
            </label>
            </div>
            <div>
            <label class="block text-white font-montserrat text-lg">
                <input type="radio" v-model="selectedCategory" value="Adult Content" class="mr-2">
                Adult Content
            </label>
            </div>
            <div class="pt-10 flex space-x-20 items-center justify-center">
                <button @click="goBack" class="bg-gray-500 text-white px-8 py-4 rounded-full text-lg font-montserrat font-bold">
                    Cancel
                </button>
                <button @click="nextStep" class="bg-second text-white px-10 py-4 rounded-full text-lg font-montserrat font-bold">
                    Next
                </button>
            </div>
        </div>

        <!-- SECOND CONTAINER FOR STEP 2  -->
        <div v-if="step === 2" class="mt-5 space-y-4">
            <h2 class="text-xl text-white font-montserrat">Please elaborate on the problem briefly. </h2>
            <textarea v-model="reportDetails" class="w-full p-2 border rounded font-montserrat" rows="7" placeholder="Please provide a brief explanation for your report and ensure it aligns with the category you selected"></textarea>
            <div class="pt-10 flex space-x-20 items-center justify-center">
                <button @click="goBack" class="bg-gray-500 text-white px-8 py-4 rounded-full text-lg font-montserrat font-bold">
                    Cancel
                </button>
                <button @click="nextStep" class="bg-second text-white px-10 py-4 rounded-full text-lg font-montserrat font-bold">
                    Next
                </button>
            </div>
        </div>
        
        <!-- THIRD CONTAINER FOR STEP 2  -->
        <div v-if="step === 3" class="">
            <p class="font-montserrat block text-white text-left text-xl font-bold pt-2 ">Confirm your report</p>
            <p class="font-montserrat block text-gray-400 text-justify text-md pb-10">Please review the details of your report carefully. Once submitted, the report cannot be changed or undone. Ensure that all information provided is accurate and truthful.</p>
            <p class="font-montserrat text-white text-justify text-lg pb-2"><strong>Category:</strong> {{ selectedCategory }}</p>
            <div class="max-h-40 overflow-y-auto">
                <p class="font-montserrat text-white text-justify text-lg"><strong>Details:</strong> {{ reportDetails }}</p>
            </div>
            <div class="pt-10 flex space-x-20 items-center justify-center">
                <button @click="goBack" class="bg-gray-500 text-white px-8 py-4 rounded-full text-lg font-montserrat font-bold">
                    Cancel
                </button>
                <button @click="nextStep" class="bg-second text-white px-10 py-4 rounded-full text-lg font-montserrat font-bold">
                    Submit
                </button>
            </div>
        </div>
    </div>
</div>
  </template>

<script>
export default {
    data() {
    return {
        step: 1,
        selectedCategory: '',
        reportDetails: ''
    };
    },
    methods: {
    nextStep() {
        if (this.step === 1 && this.selectedCategory) {
            this.step = 2;
        } else if (this.step === 2 && this.reportDetails) {
            this.step = 3;
        } else {
            console.log('Please complete the required fields');
        }
    },
    submitReport() {
        console.log('Selected Category:', this.selectedCategory);
        console.log('Report Details:', this.reportDetails);
        // Add your submission logic here
    },
    goBack() {
        if (this.step === 1) {
            this.$router.push('/dashboard');
        } else if (this.step === 2) {
            this.step = 1;
        } else if (this.step === 3) {
            this.step = 2;
        }
    }
}
};
</script>

<style scoped>
</style>