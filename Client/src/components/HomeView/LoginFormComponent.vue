<template>
  <VeeForm :validation-schema="schema" @submit="login">
    <div v-if="showAlert" class="text-white text-center font-bold p-4 mb-4 rounded" :class="alertBg">{{ alertText }}
    </div>
    <!-- Email -->
    <div class="mb-3">
      <label class="inline-block mb-2">Email</label>
      <VeeField
        name="email"
        type="email"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Enter Email"
      />
    </div>
    <VeeErrorMessage class="text-red-600 block text-center" name="email" />
    <!-- Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">Password</label>
      <VeeField
        name="password"
        type="password"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Password"
      />
      <VeeErrorMessage class="text-red-600 block text-center" name="password" />
    </div>
    <button
      :disabled="showAlert"
      :class="{'bg-purple-600': !showAlert, 'bg-gray-600': showAlert}"
      type="submit"
      class="block w-full text-white py-1.5 px-3 rounded transition hover:bg-purple-700"
    >
      Submit
    </button>
  </VeeForm>
</template>

<script>
import axios from 'axios'
import useServerStore from '@/stores/server.js'
import { mapState, mapActions } from 'pinia'

export default {
  name: 'LoginFormComponent',
  data() {
    return {
      schema: {
        email: 'required|email',
        password: 'required|min:8|max:64'
      },
      showAlert: false,
      alertBg: 'bg-blue-500',
      alertText: 'Please wait! We are logging you in.'
    }
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain']),
  },
  methods: {
    ...mapActions(useServerStore, ['getUsername']),
    async login(values) {
      this.showAlert = true
      try {
        const result = await axios.post(`${this.serverDomain}/user/token/`, {
          username: values.email,
          password: values.password
        })
        localStorage.setItem('access', result.data['access']);
        localStorage.setItem('refresh', result.data['refresh']);
        this.getUsername()
        this.alertBg = 'bg-green-500'
        this.alertText = 'Success! You are logged in.'
      } catch (e) {
        this.alertBg = 'bg-yellow-500'
        if (e.code === 'ERR_BAD_REQUEST') {
          this.alertText = 'We Have Error! User Not Found'
        } else {
          this.alertText = 'We Have Error! Try again later.'
        }
      }
    }
  }
}
</script>