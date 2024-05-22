<template>
  <!-- Auth Modal -->
  <div class="fixed z-10 inset-0 overflow-y-auto" :class="hiddenClass" id="modal">
    <div
      class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
    >
      <div class="fixed inset-0 transition-opacity">
        <div class="absolute inset-0 bg-gray-800 opacity-75"></div>
      </div>

      <!-- This element is to trick the browser into centering the modal contents. -->
      <span class="hidden sm:inline-block sm:align-middle sm:h-screen"
      >&#8203;</span
      >

      <div
        class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
      >
        <!-- Add margin if you want to see some of the overlay behind the modal-->
        <div class="py-4 text-left px-6">
          <!--Title-->
          <div class="flex justify-between items-center pb-4">
            <p class="text-2xl font-bold">Your Account</p>
            <!-- Modal Close Button -->
            <div class="modal-close cursor-pointer z-50" @click.prevent="isOpen = false">
              <i class="fas fa-times"></i>
            </div>
          </div>

          <!-- Tabs -->
          <ul class="flex flex-wrap mb-4">
            <li class="flex-auto text-center">
              <a
                class="block rounded py-3 px-4 transition"
                href="#"
                @click.prevent="tab = 'login'"
                :class="{ 'hover:text-white text-white bg-blue-600' : tab === 'login'}"
              >Login</a
              >
            </li>
            <li class="flex-auto text-center">
              <a class="block rounded py-3 px-4 transition" href="#"
                 @click.prevent="tab = 'register'"
                 :class="{ 'hover:text-white text-white bg-blue-600' : tab === 'register'}"
              >Register</a
              >
            </li>
          </ul>
          <!-- Login Form -->
          <login-form-component v-if="tab === 'login'" />
          <!-- Registration Form -->
          <register-form-component v-if="tab === 'register'" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapWritableState } from 'pinia'
import useModalStore from '@/stores/modal.js'
import RegisterFormComponent from '@/components/HomeView/RegisterFormComponent.vue'
import LoginFormComponent from '@/components/HomeView/LoginFormComponent.vue'

export default {
  name: 'AuthComponent',
  components: { RegisterFormComponent, LoginFormComponent },
  data() {
    return {
      tab: 'login'
    }
  },
  computed: {
    ...mapState(useModalStore, ['hiddenClass']),
    ...mapWritableState(useModalStore, ['isOpen'])
  }
}
</script>