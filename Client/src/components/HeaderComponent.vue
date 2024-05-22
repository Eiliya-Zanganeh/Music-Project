<template>
  <!-- Header -->
  <header id="header" class="bg-gray-700">
    <nav class="container mx-auto flex justify-start items-center py-5 px-4">
      <!-- App Name -->
      <router-link
        exact-active-class="no-active"
        class="text-white font-bold uppercase text-2xl mr-4"
        :to="{name: 'home'}"
      >Music
      </router-link>

      <div class="flex flex-grow items-center">
        <!-- Primary Navigation -->
        <ul class="flex flex-row mt-1">
          <!-- Navigation Links -->
          <li v-if="username === ''">
            <a class="px-2 text-white" href="#" @click.prevent="toggleAuthModal">Login /
              Register</a>
          </li>
          <template v-else>
            <li>
              <router-link :to="{name: 'manage'}" class="px-2 text-white">Hi {{ username }}</router-link>
            </li>
            <li><a @click.prevent="logout" href="#" class="px-2 text-white">Logout</a></li>
          </template>
          <li>
            <router-link class="px-2 text-white" :to="{name: 'about'}">About</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapWritableState, mapState, mapActions } from 'pinia'
import useModalStore from '@/stores/modal.js'
import userServerStore from '@/stores/server.js'
import useServerStore from '@/stores/server.js'

export default {
  name: 'HeaderComponent',
  computed: {
    ...mapState(userServerStore, ['serverDomain', 'username']),
    ...mapWritableState(useModalStore, {
      showForm: 'isOpen'
    })
  },
  methods: {
    ...mapActions(useServerStore, ['getUsername']),
    toggleAuthModal() {
      this.showForm = !this.showForm
    },
    logout(){
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      this.getUsername()
      if(this.$route.meta.requireAuth){
        this.$router.push({name: 'home'})
      }
    }
  },
  mounted() {
    this.getUsername()
  }

}
</script>