<template>
  <main>
    <!-- Main Content -->
    <section class="container mx-auto mt-6">
      <div class="md:grid md:grid-cols-3 md:gap-4">
        <div class="col-span-1">
          <upload-component />
        </div>
        <div class="col-span-2">
          <div
            class="bg-white rounded border border-gray-200 relative flex flex-col"
          >
            <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
              <span class="card-title">My Songs</span>
              <i
                class="fa fa-compact-disc float-right text-green-400 text-2xl"
              ></i>
            </div>
            <div class="p-6">
              <edit-music-component v-if="editShow" :id="editId" :title="editTitle" @close-edit="editClose" @edit-music="editMusic"/>
              <!-- Composition Items -->
              <div v-for="music in musics" :key="music" class="border border-gray-200 p-3 mb-4 rounded">
                <div>
                  <h4 class="inline-block text-2xl font-bold">{{ music.title }}</h4>
                  <button
                    class="ml-1 py-1 px-2 text-sm rounded text-white bg-red-600 float-right"
                    @click.prevent="delMusic(music.id)"
                  >
                    <i class="fa fa-times"></i>
                  </button>
                  <button
                    class="ml-1 py-1 px-2 text-sm rounded text-white bg-blue-600 float-right"
                    @click.prevent="editTitle = music.title; editShow = true; editId=music.id"
                  >
                    <i class="fa fa-pencil-alt"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import useServerStore from '@/stores/server.js'
import { mapActions, mapState } from 'pinia'
import UploadComponent from '@/components/ManageView/UploadComponent.vue'
import EditMusicComponent from '@/components/ManageView/EditMusicComponent.vue'

export default {
  name: 'ManageView',
  data(){
    return{
      editShow: false,
      editTitle: null,
      editId: null
    }
  },
  components: { EditMusicComponent, UploadComponent },
  computed: {
    ...mapState(useServerStore, ['musics'])
  },
  methods: {
    ...mapActions(useServerStore, ['getAllMusic', 'deleteMusic', 'updateMusic']),
    delMusic(idx) {
      if (confirm('Are Yor sure??')) {
        this.deleteMusic(idx)
        this.getAllMusic()
      }
    },
    editClose(){
      this.editTitle = null
      this.editShow = false
      this.editId = null
    },
    editMusic(id, newTitle){
      this.editClose()
      this.updateMusic(id, newTitle)
      this.getAllMusic()
    }
  },
  mounted() {
    this.getAllMusic()
  }
}
</script>