<template>
  <div
    class="bg-white rounded border border-gray-200 relative flex flex-col"
  >
    <div v-if="uploadEnd" class="text-white text-center font-bold p-4 mb-4 rounded" :class="alertBg">{{ alertText }}</div>
      <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
      <span class="card-title">Upload</span>
      <i class="fas fa-upload float-right text-green-400 text-2xl"></i>
    </div>
    <div class="p-6">
      <!-- Upload Dropbox -->
      <div
        class="w-full px-10 py-20 rounded text-center cursor-pointer border border-dashed border-gray-400 text-gray-400 transition duration-500 hover:text-white hover:bg-green-400 hover:border-green-400 hover:border-solid"
        :class="{'bg-green-400 border-green-400 border-solid': is_drag}"
        @drag.prevent.stop=""
        @dragstart.prevent.stop=""
        @dragend.prevent.stop="is_drag = false"
        @dragover.prevent.stop="is_drag = true"
        @dragenter.prevent.stop="is_drag = true"
        @dragleave.prevent.stop="is_drag = false"
        @drop.prevent.stop="upload"
      >
        <h5>Drop your files here</h5>
      </div>
      <input @input="upload" multiple class="block" type="file">
      <hr class="my-6" />
      <!-- Progess Bars -->
      <div class="mb-4" v-for="upload in uploads" :key="upload">
        <div class="font-bold text-sm">{{ upload.name }}</div>
        <div class="flex h-4 overflow-hidden bg-gray-200 rounded">
          <div
            class="transition-all progress-bar" :class="{'bg-blue-400': !uploadEnd, 'bg-green-400': uploadEnd}"
            :style="{width: upload.result + '%'}"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import useServerStore from '@/stores/server.js'
import { mapActions } from 'pinia'

export default {
  name: 'UploadComponent',
  data() {
    return {
      is_drag: false,
      uploads: [],
      uploadEnd: false,
      alertBg: '',
      alertText: '',
    }
  },
  methods: {
    ...mapActions(useServerStore, ['uploadFile', 'getAllMusic']),
    async upload(event) {
      this.is_drag = false
      // console.log(event)
      // const { files } = event.dataTransfer
      // console.log(files)
      const files = event.dataTransfer ? [...event.dataTransfer.files] : [...event.target.files]
      const formData = new FormData()
      let uploadFiles = true
      this.uploads = []
      this.uploadEnd = false

      files.forEach((file, idx) => {
        if (file.type === 'audio/mpeg') {
          formData.append(String(idx), file)
          this.uploads.push({ name: file.name, result: 0 })
        } else {
          uploadFiles = false
        }
      })

      if (uploadFiles) {
        try {
          await this.uploadFile(formData, this.updateProcess)
          this.alertBg = 'bg-green-400'
          this.alertText = 'Files Uploaded'
          this.getAllMusic()
        } catch (e) {
          this.alertBg = 'bg-red-400'
          this.alertText = 'Error: Files Not Uploaded'
          this.uploads = []
        }
      } else {
        this.alertBg = 'bg-yellow-400'
        this.alertText = 'Files Is Not Audio'
        this.uploads = []
      }
      this.uploadEnd = true
    },
    updateProcess(newVal){
      this.uploads.forEach((upload, idx) => {
        this.uploads[idx].result = newVal
      })
    }
  }
}
</script>
