<template>
  <!-- Player -->
  <div v-if="currect_music !== null" class="fixed bottom-0 left-0 bg-white px-4 py-2 w-full">
    <!-- Track Info -->
    <div class="text-center">
      <span class="song-title font-bold">{{ currect_music.title }}</span>
    </div>
    <div class="flex flex-nowrap gap-4 items-center">
      <!-- Play/Pause Button -->
      <button type="button" @click.prevent="toggleAudio">
        <i class="fa text-gray-500 text-xl" :class="{ 'fa-pause' : playing, 'fa-play': !playing}"></i>
      </button>
      <!-- Current Position -->
      <div class="player-currenttime">{{ seek }}</div>
      <!-- Scrub Container  -->
      <div class="w-full h-2 rounded bg-gray-200 relative cursor-pointer" @click.prevent="updateSeek">
        <!-- Player Ball -->
        <span
          class="absolute -top-2.5 -ml-2.5 text-gray-800 text-lg"
          :style="{left: playerProgress}"
        >
            <i class="fas fa-circle"></i>
          </span>
        <!-- Player Progress Bar-->
        <span
          class="block h-2 rounded bg-gradient-to-r from-green-500 to-green-400"
          :style="{width: playerProgress}"
        ></span>
      </div>
      <!-- Duration -->
      <div class="player-duration">{{ duration }}</div>
    </div>
  </div>
</template>

<script>
import usePlayerStore from '@/stores/player.js'
import { mapActions, mapState } from 'pinia'
export default {
  name: "PlayerComponent",
  methods:{
    ...mapActions(usePlayerStore, ['toggleAudio', 'updateSeek']),
  },
  computed:{
    ...mapState(usePlayerStore, ['playing', 'seek', 'duration', 'playerProgress', 'currect_music'])
  }
}
</script>