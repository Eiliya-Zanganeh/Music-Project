<template>
  <main>
    <!-- Music Header -->
    <section class="w-full mb-8 py-14 text-center text-white relative">
      <div
        class="absolute inset-0 w-full h-full box-border bg-contain music-bg"
        style="background-image: url(/img/song-header.png)"
      ></div>
      <div class="container mx-auto flex items-center">
        <!-- Play/Pause Button -->
        <button
          @click.prevent="playMusic"
          type="button"
          class="z-50 h-24 w-24 text-3xl bg-white text-black rounded-full focus:outline-none"
        >
          <i class="fas fa-play"></i>
        </button>
        <div class="z-50 text-left ml-8">
          <!-- Song Info -->
          <div class="text-3xl font-bold">{{ title }}</div>
        </div>
      </div>
    </section>
    <!-- Form -->
    <section class="container mx-auto mt-6">
      <div
        class="bg-white rounded border border-gray-200 relative flex flex-col"
      >
        <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
          <!-- Comment Count -->
          <span class="card-title">Comments ({{ commentLen }})</span>
          <i class="fa fa-comments float-right text-green-400 text-2xl"></i>
        </div>
        <div class="p-6">
          <form>
            <textarea
              v-model="comment"
              class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded mb-4"
              placeholder="Your comment here..."
            ></textarea>
            <button
              type="submit"
              class="py-1.5 px-3 rounded text-white bg-green-600 block"
              @click.prevent="sendComment"
            >
              Submit
            </button>
          </form>
          <!-- Sort Comments -->
          <select
            v-model="order"
            class="block mt-4 py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
          >
            <option value="1">Latest</option>
            <option value="2">Oldest</option>
          </select>
        </div>
      </div>
    </section>
    <!-- Comments -->
    <ul class="container mx-auto">
      <li class="p-6 bg-gray-50 border border-gray-200" v-for="comment in comments" :key="comment">
        <!-- Comment Author -->
        <div class="mb-5">
          <div class="font-bold">{{ comment.user.username }}</div>
          <time>{{ comment.date.replace('T', ' | ').replace('Z', '').split('.')[0] }}</time>
        </div>

        <p>
          {{ comment.text }}
        </p>
      </li>
    </ul>
  </main>
</template>

<script>
import useServerStore from '@/stores/server.js'
import userPlayerStore from '@/stores/player.js'
import { mapActions, mapState } from 'pinia'

export default {
  name: 'SongComponent',
  data() {
    return {
      commentLen: 0,
      comment: '',
      order: '1',
      comments: null,
      title: null
    }
  },
  computed: {
    ...mapState(useServerStore, ['musicComments', 'musicData', 'serverDomain'])
  },
  methods: {
    ...mapActions(useServerStore, ['musicDetail', 'getUsername', 'addComment']),
    ...mapActions(userPlayerStore, ['newMusic']),
    async sendComment() {
      this.getUsername()
      const access = localStorage.getItem('access')
      if (access === null) {
        alert('You Most Be Logged In :| ')
      } else {
        await this.addComment(this.$route.params.id, this.comment)
        this.loadPage()

      }
    },
    async loadPage(){
      await this.musicDetail(this.$route.params.id)
      this.commentLen = this.musicComments.length
      this.comments = this.musicComments
      this.title = this.musicData.title
    },
    async playMusic(){
      const music = {
        title: this.musicData.title,
        music: this.serverDomain + this.musicData.music,
      }
      await this.newMusic(music)
    }
  },
  async mounted() {
    this.loadPage()
  },
  watch: {
    order() {
      this.comments = this.comments.reverse()
    }
  }
}
</script>