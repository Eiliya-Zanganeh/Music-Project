<template>
  <main>

    <!-- Introduction -->
    <section class="mb-8 py-20 text-white text-center relative">
      <div
        class="absolute inset-0 w-full h-full bg-contain introduction-bg"
        style="background-image: url(/img/header.png)"
      ></div>
      <div class="container mx-auto">
        <div class="text-white main-header-content">
          <h1 class="font-bold text-5xl mb-5">Listen to Great Music!</h1>
          <p class="w-full md:w-8/12 mx-auto">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
            et dolor mollis, congue augue non, venenatis elit. Nunc justo eros,
            suscipit ac aliquet imperdiet, venenatis et sapien. Duis sed magna
            pulvinar, fringilla lorem eget, ullamcorper urna.
          </p>
        </div>
      </div>

      <img
        class="relative block mx-auto mt-5 -mb-20 w-auto max-w-full"
        src="/img/introduction-music.png"
      />
    </section>

    <!-- Main Content -->
    <section class="container mx-auto">
      <div
        class="bg-white rounded border border-gray-200 relative flex flex-col"
      >
        <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
          <span class="card-title">Songs</span>
          <!-- Icon -->
          <i
            class="fa fa-headphones-alt float-right text-green-400 text-xl"
          ></i>
        </div>
        <!-- Playlist -->
        <ol id="playlist">
          <li
            v-for="music in allMusic"
            :key="music"
            class="flex justify-between items-center p-3 pl-6 cursor-pointer transition duration-300 hover:bg-gray-50"
          >
            <div>
              <router-link :to="{name: 'song', params: {id: music.id}}" class="font-bold block text-gray-600">
                {{ music.title }}
              </router-link>
            </div>

            <div class="text-gray-600 text-lg">
              <span class="comments">
                <i class="fa fa-comments text-gray-600"></i>
              </span>
            </div>
          </li>
        </ol>
        <div class="flex justify-center">
          <button @click.prevent="previous" v-if="pagePrevious !== null"
                  class="bg-purple-500 m-2 p-2 text-white rounded">Previous
          </button>
          <button @click.prevent="next" v-if="pageNext !== null" class="bg-purple-500 m-2 p-2 text-white rounded">Next
            ({{ pageCount }})
          </button>
        </div>
        <!-- .. end Playlist -->
      </div>
    </section>

  </main>
</template>

<script>
import useServerStore from '@/stores/server.js'
import { mapActions, mapState } from 'pinia'

export default {
  name: 'HomeView',
  computed: {
    ...mapState(useServerStore, ['allMusic', 'pageNext', 'pagePrevious', 'pageCount'])
  },
  methods: {
    ...mapActions(useServerStore, ['getMusics']),
    next() {
      this.getMusics(this.pageNext)
    },
    previous() {
      this.getMusics(this.pagePrevious)
    }
  },
  mounted() {
    this.getMusics(null)
  }
}
</script>