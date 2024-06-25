<template>
    <div
        class="flex flex-col items-center align-middle w-full px-5 sm:px-8 py-5 sm:ml-64 overflow-auto h-screen bg-field pt-20 sm:pt-7">
        <div class="flex-col justify-start w-full text-prime bg-[#E8E8E8] p-7 mb-5 sm:mb-10 sm:p-7 sm:px-20 rounded-3xl">
            <h1 class="flex justify-center text-4xl sm:text-6xl text-prime font-bebas-neue">General Settings</h1>
            <div class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7 mb-3 sm:mb-5">
                <span class="material-icons-outlined text-3xl sm:text-5xl text-second">account_circle</span>
                <h1 class="text-2xl sm:text-4xl sm:ms-3 font-bold">Profile</h1>
            </div>
            <h1 class="text-prime font-montserrat text-xl mb-3 sm:text-3xl font-bold sm:ms-14 sm:mb-7">Profile
                Information</h1>
            <div class="sm:ms-32 sm:pe-28 text-prime">
                <form>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Username</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="John" disabled />
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Email
                            address</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="john.doe@company.com" disabled />
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Password</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="**************" disabled />
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Country</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="United States" disabled />
                    </div>
                    <div class="flex justify-end mb-10 sm:mt-10">
                        <button class="bg-[#7F7979] rounded-3xl text-white px-3 sm:px-6 py-2 sm:py-3">Cancel</button>
                        <button
                            class="bg-second rounded-3xl text-white ml-6 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3">Edit/Save</button>
                    </div>
                </form>
            </div>
            <h1 class="text-prime font-montserrat text-xl mb-3 sm:text-3xl font-bold sm:ms-14 sm:mb-7">Change Password
            </h1>
            <div class="sm:ms-32 sm:pe-28 text-prime">
                <form>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Old Password</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="**************" disabled />
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">New Password</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="**************" disabled />
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-prime">Confirm New Password</label>
                        <input type="email" id="email" class="text-prime text-sm rounded-3xl w-full p-2.5 pl-6 bg-field"
                            placeholder="**************" disabled />
                    </div>
                    <div class="flex justify-end mb-10 sm:mt-10">
                        <button class="bg-[#7F7979] rounded-3xl text-white px-3 sm:px-6 py-2 sm:py-3">Cancel</button>
                        <button
                            class="bg-second rounded-3xl text-white ml-6 sm:ml-6 px-3 sm:px-6 py-1 sm:py-3">Edit/Save</button>
                    </div>
                </form>
            </div>
            <div class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7 mb-3 sm:mb-5">
                <span class="material-icons-outlined text-3xl sm:text-5xl text-second">notifications</span>
                <h1 class="text-2xl sm:text-4xl sm:ms-3 font-bold">Notifications</h1>
            </div>
            <h1 class="text-[#887D7D] font-montserrat text-lg mb-3 sm:text-2xl sm:ms-14 sm:mb-10">Customize where you want your notifications to show up. </h1>
            <div class="flex-col w-full">
                <!-- test -->
                <!-- <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-14 sm:mb-7">In-app Notifications</span> -->
                <div class="flex sm:mb-4">
                    <label class="flex justify-end items-center cursor-pointer select-none text-dark dark:text-white">
                        <div class="flex w-screen justify-between">
                            <div class="flex w-1/2 justify-between">
                                <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-32 sm:mb-7">In-App Notifications</span>
                                <div class="relative">
                                    <input type="checkbox" class="sr-only" @change="handleCheckboxChangeInApp" />
                                    <div
                                        :class="{ '!bg-prime': isCheckedInApp }"
                                        class="block h-8 rounded-full box bg-second dark:bg-dark-2 w-14">
                                    </div>
                                    <div
                                        :class="{ 'translate-x-full !bg-primary dark:!bg-white': isCheckedInApp }"
                                        class="absolute flex items-center justify-center w-6 h-6 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </label>
                </div>
                <div class="flex sm:mb-4">
                    <label class="flex justify-end items-center cursor-pointer select-none text-dark dark:text-white">
                        <div class="flex w-screen justify-between">
                            <div class="flex w-1/2 justify-between">
                                <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-32 sm:mb-7">Banner Notifications</span>
                                <div class="relative">
                                    <input type="checkbox" class="sr-only" @change="handleCheckboxChangeBanner" />
                                    <div
                                        :class="{ '!bg-prime': isCheckedBanner }"
                                        class="block h-8 rounded-full box bg-second dark:bg-dark-2 w-14">
                                    </div>
                                    <div
                                        :class="{ 'translate-x-full !bg-primary dark:!bg-white': isCheckedBanner }"
                                        class="absolute flex items-center justify-center w-6 h-6 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </label>
                </div>
                <div class="flex sm:mb-4">
                    <label class="flex justify-end items-center cursor-pointer select-none text-dark dark:text-white">
                        <div class="flex w-screen justify-between">
                            <div class="flex w-1/2 justify-between">
                                <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-32 sm:mb-7">Vibration</span>
                                <div class="relative">
                                    <input type="checkbox" class="sr-only" @change="handleCheckboxChangeVibration" />
                                    <div
                                        :class="{ '!bg-prime': isCheckedVibration }"
                                        class="block h-8 rounded-full box bg-second dark:bg-dark-2 w-14">
                                    </div>
                                    <div
                                        :class="{ 'translate-x-full !bg-primary dark:!bg-white': isCheckedVibration }"
                                        class="absolute flex items-center justify-center w-6 h-6 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </label>
                </div>
                <div class="flex sm:mb-4">
                    <label class="flex justify-end items-center cursor-pointer select-none text-dark dark:text-white">
                        <div class="flex w-screen justify-between">
                            <div class="flex w-1/2 justify-between">
                                <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-32 sm:mb-7">Sound</span>
                                <div class="relative">
                                    <input type="checkbox" class="sr-only" @change="handleCheckboxChangeSound" />
                                    <div
                                        :class="{ '!bg-prime': isCheckedSound }"
                                        class="block h-8 rounded-full box bg-second dark:bg-dark-2 w-14">
                                    </div>
                                    <div
                                        :class="{ 'translate-x-full !bg-primary dark:!bg-white': isCheckedSound }"
                                        class="absolute flex items-center justify-center w-6 h-6 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </label>
                </div>
            </div>
            <div class="flex items-center w-full font-montserrat text-prime mt-4 sm:mt-7 mb-3 sm:mb-5">
                <span class="material-icons-outlined text-3xl sm:text-5xl text-second">contrast</span>
                <h1 class="text-2xl sm:text-4xl sm:ms-3 font-bold">Theme</h1>
            </div>
            <h1 class="text-[#887D7D] font-montserrat text-lg mb-3 sm:text-2xl sm:ms-14 sm:mb-10">Customize how you want CulturaLink to look like on your device</h1>
            <div class="flex sm:mb-4">
                <label class="flex justify-end items-center cursor-pointer select-none text-dark dark:text-white">
                    <div class="flex w-screen justify-between">
                        <div class="flex w-1/2 justify-between">
                            <span class="text-prime font-montserrat text-lg mb-3 sm:text-2xl sm:ms-32 sm:mb-7">Theme</span>
                            <div class="relative">
                                <input type="checkbox" class="sr-only" @change="handleCheckboxChangeTheme" />
                                <div
                                    :class="{ '!bg-prime': isCheckedTheme }"
                                    class="block h-8 rounded-full box bg-second dark:bg-dark-2 w-14">
                                </div>
                                <div
                                    :class="{ 'translate-x-full !bg-primary dark:!bg-white': isCheckedTheme }"
                                    class="absolute flex items-center justify-center w-6 h-6 transition bg-white rounded-full dot left-1 top-1 dark:bg-dark-5">
                                </div>
                            </div>
                        </div>
                    </div>
                </label>
            </div>
        </div>
        <footer>
            <div class="flex-col sm:ml-40 w-screen -mb-5 ">
                <div class="flex justify-normal w-full sm:px-36 py-5 bg-prime pe-3">
                    <div class="flex-col ps-3 sm:ps-3">
                        <img class="w-40 sm:w-96 h-auto -mt-7 sm:-mt-10" src="/public/ULTURALINK-DMLong.png" alt="">
                        <div class="w-6/7 sm:w-2/5 -mt-5 sm:-mt-16">
                            <p class="text-wrap text-white text-[9px] sm:text-xs">CulturaLink is a dynamic platform designed to foster cultural exchange and travel planning through user-generated content and itineraries. This project is proudly developed by students: Gabrentina, Galan, and Tecson as part of their academic pursuit,</p>
                        </div>
                    </div>
                    <div class="flex justify-start bg-second sm:-ms-[43rem] sm:h-44 w-0 sm:w-0.5"></div>
                    <div class="flex items-center ml-8 sm:ml-16">
                        <span class="material-icons-outlined sm:ml-3 text-second text-6xl sm:text-9xl">account_circle</span>
                        <span class="material-icons-outlined sm:ml-5 text-second text-6xl sm:text-9xl">email</span>
                        <span class="material-icons-outlined sm:ml-5 text-second text-6xl sm:text-9xl">call</span>
                    </div>
                </div>
                <div class="flex bg-second sm:-ms-5 h-7 justify-center items-center">
                    <h4 class="text-prime text-[12px] sm:text-sm">Copyright © 2024  | In Affiliation with <span class="text-white">St  Dominic College of Asia</span></h4>
                </div>
            </div>
        </footer>
    </div>
</template> 

<script>
    import { ref } from 'vue';
    export default{
        methods:{},
        setup(){
            const isCheckedInApp = ref(false)
            const isCheckedBanner = ref(false)
            const isCheckedVibration = ref(false)
            const isCheckedSound = ref(false)
            const isCheckedTheme = ref(false)

            const handleCheckboxChangeInApp = () => {
                isCheckedInApp.value = !isCheckedInApp.value
            }
            const handleCheckboxChangeBanner = () => {
                isCheckedBanner.value = !isCheckedBanner.value
            }
            const handleCheckboxChangeVibration = () => {
                isCheckedVibration.value = !isCheckedVibration.value
            }
            const handleCheckboxChangeSound = () => {
                isCheckedSound.value = !isCheckedSound.value
            }
            const handleCheckboxChangeTheme = () => {
                isCheckedTheme.value = !isCheckedTheme.value
            }
            
            return{handleCheckboxChangeInApp, handleCheckboxChangeBanner, handleCheckboxChangeVibration, handleCheckboxChangeSound, handleCheckboxChangeTheme, isCheckedInApp, isCheckedBanner, isCheckedVibration, isCheckedSound, isCheckedTheme}
        }
        };
</script>


<style>
</style>