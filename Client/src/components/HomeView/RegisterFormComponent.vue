<template>
  <VeeForm :validation-schema="schema" @submit="register" :initial-values="registerFormData">
    <div v-if="showAlert" class="text-white text-center font-bold p-4 mb-4 rounded" :class="alertBg">{{ alertText }}
    </div>
    <!-- Name -->
    <div class="mb-3">
      <label class="inline-block mb-2">Name</label>
      <VeeField name="name" :bails="false" v-slot="{ field, errors }">
        <input
          type="text"
          class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
          placeholder="Enter Name"
          v-bind="field"
        >
        <div class="text-red-600" v-for="error in errors" :key="error">{{ error }}</div>
      </VeeField>
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
    <!-- Age -->
    <div class="mb-3">
      <label class="inline-block mb-2">Age</label>
      <VeeField
        name="age"
        type="number"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
      />
    </div>
    <VeeErrorMessage class="text-red-600 block text-center" name="age" />
    <!-- Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">Password</label>
      <VeeField name="password" :bails="false" v-slot="{ field, errors }">
        <input
          type="password"
          class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
          placeholder="Password"
          v-bind="field"
        >
        <div class="text-red-600" v-for="error in errors" :key="error">{{ error }}</div>
      </VeeField>
    </div>
    <!-- Confirm Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">Confirm Password</label>
      <VeeField
        name="confrim_password"
        type="password"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Confirm Password"
      />
    </div>
    <VeeErrorMessage class="text-red-600 block text-center" name="confrim_password" />
    <!-- Country -->
    <div class="mb-3">
      <label class="inline-block mb-2">Country</label>
      <VeeField
        as="select"
        name="country"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
      >
        <option value="USA">USA</option>
        <option value="Mexico">Mexico</option>
        <option value="Germany">Germany</option>
        <option value="test">test</option>
      </VeeField>
    </div>
    <VeeErrorMessage class="text-red-600 block text-center" name="country" />
    <!-- TOS -->
    <div class="mb-3 pl-6">
      <VeeField
        name="tos"
        type="checkbox"
        class="w-4 h-4 float-left -ml-6 mt-1 rounded"
        value="1"
      />
      <label class="inline-block">Accept terms of service</label>
    </div>
    <VeeErrorMessage class="text-red-600 block text-center" name="tos" />
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
import { mapState } from 'pinia'

export default {
  name: 'RegisterFormComponent',
  data() {
    return {
      schema: {
        name: 'required|min:3|max:100|alpha_spaces',
        email: 'required|email',
        age: 'required|min_value:18|max_value:99',
        password: 'required|min:8|max:64|not_one_of:password',
        confrim_password: 'required|confirmed:@password',
        country: 'required|not_one_of:test',
        tos: 'required'
      },
      registerFormData: {
        country: 'USA'
      },
      showAlert: false,
      alertBg: 'bg-blue-500',
      alertText: 'Please wait! Your account is being create.'

    }
  },
  computed: {
    ...mapState(useServerStore, ['serverDomain'])
  },
  methods: {
    async register(values) {
      this.showAlert = true
      try {
        const result = await axios.post(`${this.serverDomain}/user/register/`, {
          name: values.name,
          email: values.email,
          age: values.age,
          password: values.password,
          country: values.country
        })
        this.alertBg = 'bg-green-500'
        this.alertText = 'Success! Your account has been create.'
        // console.log(result)
      } catch (e) {
        this.alertBg = 'bg-yellow-500'
        this.alertText = 'We Have Error! Try again later.'
        if (e.response.status === 400 && e.response.data['Error'] === 'User Already Exists') {
          this.alertText = 'We Have Error! User Already Exists'
        }
        // console.log(e)
      }
    }
  }
}
</script>
