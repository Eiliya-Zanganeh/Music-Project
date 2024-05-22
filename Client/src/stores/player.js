import { defineStore } from 'pinia'
import { Howl } from 'howler'

export default defineStore('player', {
  state: () => ({
    currect_music: null,
    sound: null,
    seek: '00:00',
    duration: '00:00',
    playerProgress: "0%"
  }),
  actions: {
    async newMusic(music) {
      if(this.sound instanceof Howl){
        this.sound.unload()
      }

      this.currect_music = music
      this.sound = new Howl({
        src: [music['music']],
        html5: true
      })
      this.sound.play()
      this.sound.on('play', () => {
        requestAnimationFrame(this.progress)
      })
    },
    progress() {
      this.seek = this.formatTime(this.sound.seek())
      this.duration = this.formatTime(this.sound.duration())

      this.playerProgress = `${this.sound.seek() / this.sound.duration() * 100}%`

      if (this.sound.playing()) {
        requestAnimationFrame(this.progress)
      }
    },
    async toggleAudio() {
      if (this.sound.playing) {
        if (this.sound.playing()) {
          this.sound.pause()
        } else {
          this.sound.play()
        }
      }
    },
    formatTime(time){
      const minutes = Math.floor(time / 60) || 0
      const seconds = Math.round((time - minutes * 60) || 0)
      return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`
    },
    updateSeek(event){
      if (this.sound.playing){
        const { x, width } = event.currentTarget.getBoundingClientRect()
        const clickX = event.clientX - x
        const percentage = clickX / width
        const seconds = this.sound.duration() * percentage

        this.sound.seek(seconds)
        this.sound.once("seek", this.progress)
      }
    }
  },
  getters: {
    playing: (state) => {
      try {
        if (state.sound.playing) {
          return state.sound.playing()
        }
        return false
      } catch {
        return false
      }
    }
  }
})