import { defineStore } from 'pinia'
import axios from 'axios'


export default defineStore('server', {
  state: () => ({
    serverDomain: 'http://localhost:8000/',
    username: '',
    musics: null,
    allMusic: null,

    pageNext: null,
    pagePrevious: null,
    pageCount: null,

    musicComments: null,
    musicData: null
  }),
  actions: {
    async refreshToken() {
      try {
        const refresh = localStorage.getItem('refresh')
        if (refresh !== null) {
          const result = await axios.post(`${this.serverDomain}/user/token/refresh/`, {
            refresh: refresh
          })
          localStorage.setItem('access', result.data['access'])
          this.getUsername()
        } else {
          localStorage.removeItem('access')
          localStorage.removeItem('refresh')
        }
      } catch (e) {
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
      }
    },
    async getUsername() {
      try {
        const access = localStorage.getItem('access')
        if (access !== null) {
          const result = await axios.get(`${this.serverDomain}/user/`, {
            headers: {
              Authorization: `Bearer ${access}`
            }
          })
          this.username = result.data['first_name']
        } else {
          this.username = ''
          localStorage.removeItem('access')
          localStorage.removeItem('refresh')
        }
      } catch (e) {
        if (e.response.data.code === 'token_not_valid') {
          this.refreshToken()
        }
      }
    },
    async uploadFile(formData, process) {
      await this.getUsername()
      const access = localStorage.getItem('access')
      await axios.post(`${this.serverDomain}/user/upload/`, formData, {
        headers: {
          Authorization: `Bearer ${access}`,
          'Content-Type': 'multipart/form-data'
        },
        onUploadProgress: function(progressEvent) {
          const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total)
          process(percentCompleted)
        }
      })
        .then(response => {
          console.log('Ok', response.data)
        })
    },
    async getAllMusic() {
      await this.getUsername()
      const access = localStorage.getItem('access')
      await axios.get(`${this.serverDomain}/user/musics/`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((response) => {
        this.musics = response.data
      }).catch((error) => {
        console.log(error)
      })
    },
    async deleteMusic(id) {
      await this.getUsername()
      const access = localStorage.getItem('access')
      await axios.delete(`${this.serverDomain}/user/delete-music/${id}/`, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((response) => {
        console.log(response.data)
      }).catch((error) => {
        console.log(error)
      })
    },
    async updateMusic(id, title) {
      await this.getUsername()
      const access = localStorage.getItem('access')
      await axios.post(`${this.serverDomain}/user/update-music/`, {
        'id': id,
        'title': title
      }, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((response) => {
        console.log(response)
      }).catch((error) => {
        console.log(error)
      })
    },
    async getMusics(url) {
      if (url === null){
        url = `${this.serverDomain}/user/all-musics/`
      }
      await axios.get(url)
        .then((response) => {
          this.allMusic = response.data.results
          this.pageNext = response.data.next
          this.pagePrevious = response.data.previous
          this.pageCount = response.data.count
        }).catch((error) => {
          console.log(error)
        })
    },
    async musicDetail(id){
      await axios.get(`${this.serverDomain}/user/music-detail/${id}/`).
      then((response) => {
        this.musicComments = response.data.comments
        this.musicData = response.data.music
      }).catch((error) => {
        console.log(error)
      })
    },
    async addComment(music, comment){
      await this.getUsername()
      const access = localStorage.getItem('access')
      await axios.post(`${this.serverDomain}/user/add-comment/`, {
        music: music,
        comment: comment
      }, {
        headers: {
          Authorization: `Bearer ${access}`
        }
      }).then((response) => {
        console.log(response)
      }).catch((error) => (
        console.log(error)
      ))
    }
  }
})