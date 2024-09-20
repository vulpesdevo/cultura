<template>
    <div
		class="profile-main flex flex-col items-center align-middle w-full pb-16 sm:pb-10 sm:px-8 py-5 sm:ml-64 overflow-auto overflow-x-hidden h-screen bg-field dark:bg-dark-notif pt-5 sm:pt-7"
	>
    <div class="w-screen sm:w-full p-3 mt-16 sm:mt-3 px-6 sm:mt-6 sm:px-9 sm:rounded-lg shadow-lg bg-interface dark:bg-dark-interface">
        <form @submit.prevent="handleSubmit">
          <div class="post-title flex justify-start items-center">
            <div class="flex w-[90%] items-center">
              <input
                v-model="post.title"
                type="text"
                class="font-bebas-neue text-lg bg-[#12182c41] m-2 p-5 rounded-lg text-prime dark:text-dark-prime sm:text-2xl focus:border-second focus:outline-none w-4/5 sm:w-full"
                placeholder="Enter post title"
              />
              <small class="text-second flex w-3/4 sm:w-[10%] justify-end relative">{{ timesince(post.date_posted) }}</small>
            </div>
            <div class="flex w-[10%] justify-end relative">
              <button type="button" @click="toggleMenu" class="">
                <span class="material-icons-outlined dark:text-dark-prime">
                  more_horiz
                </span>
              </button>
              <div
                v-if="isMenuOpen"
                class="absolute mt-5 w-48 bg-white border border-gray-200 rounded-md shadow-lg"
              >
                <a
                  href="#"
                  @click.prevent="handleSubmit"
                  class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
                >Save</a>
                <a
                  href="#"
                  @click.prevent="cancelEdit"
                  class="block px-4 py-2 text-gray-800 hover:bg-gray-100"
                >Cancel</a>
              </div>
            </div>
          </div>
          <div class="post-content flex w-full mt-4">
            <div class="w-14 h-14 mr-4">
              <img
                :src="post.author_user_photo"
                alt="Profile"
                class="rounded-full cursor-pointer object-cover"
              />
            </div>
            <div class="w-full">
              <div class="flex border-b-2 dark:border-gray-400">
                <small class="font-montserrat text-prime dark:text-dark-prime pr-5">
                  @{{ post.author }}
                </small>
                <small class="about-post font-montserrat dark:text-gray-400">
                  {{ post.category }} | {{ post.country }}
                </small>
              </div>
              <textarea
                v-model="post.content"
                class="font-montserrat w-full mt-3 bg-[#12182c41] p-5 rounded-lg resize-none text-sm text-justify dark:text-dark-prime bg-transparent border-none focus:outline-none"
                rows="6"
                placeholder="Enter post content"
              ></textarea>
              <button
                  type="button"
                  @click="$refs.fileInput.click()"
                  class="font-montserrat text-sm text-second dark:text-dark-prime border border-second rounded-md px-4 py-2 my-5 sm:mt-3 hover:bg-second hover:text-white transition duration-300"
                >
                  <span class="material-icons-outlined align-middle mr-2">add_photo_alternate</span>
                  {{ post.image ? 'Change Image' : 'Add Image' }}
                </button>
              <div class="sm:h-96 pb-2 sm:p-4" v-if="post.image">
                <img
                  :src="post.image"
                  alt=""
                  class="h-full object-contain rounded-lg"
                />
              </div>
              <div class="mt-4">
                <input
                  type="file"
                  @change="handleImageUpload"
                  accept="image/*"
                  class="hidden"
                  ref="fileInput"
                />
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const post = ref({
  _id: '',
  title: '',
  author: '',
  author_user_photo: '',
  category: '',
  country: '',
  content: '',
  image: null,
  date_posted: new Date(),
  is_liked: false,
  like_count: 0
})

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const handleImageUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      post.value.image = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const handleSubmit = () => {
  // Here you would typically send the updated post data to your backend
  console.log('Submitting updated post:', post.value)
  // You can add your API call or state management logic here
  isMenuOpen.value = false
}

const cancelEdit = () => {
  // Here you would typically reset the form or navigate away
  console.log('Cancelling edit')
  isMenuOpen.value = false
}

const timesince = (date) => {
  // Implement your timesince logic here
  return '2 hours ago' // Placeholder
}

onMounted(() => {
  // Fetch the existing post data here
  // For demonstration, we'll use placeholder data
  post.value = {
    _id: '1',
    title: 'Example Post Title',
    author: 'johndoe',
    author_user_photo: '/placeholder.svg?height=56&width=56',
    category: 'Travel',
    country: 'Japan',
    content: 'This is an example post content. Edit me!',
    image: '/placeholder.svg?height=300&width=500',
    date_posted: new Date(),
    is_liked: false,
    like_count: 42
  }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons+Outlined');

.font-bebas-neue {
  font-family: 'Bebas Neue', sans-serif;
}

.font-montserrat {
  font-family: 'Montserrat', sans-serif;
}

/* Add these custom color classes to match your theme */
.text-prime {
  @apply text-gray-900;
}

.dark .text-dark-prime {
  @apply text-white;
}

.text-second {
  @apply text-blue-500;
}

.bg-interface {
  @apply bg-white;
}

.dark .bg-dark-interface {
  @apply bg-gray-800;
}
</style>