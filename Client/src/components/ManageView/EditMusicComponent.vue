<template>
  <div>
    <form>
      <div class="mb-3">
        <h1 class="text-2xl font-bold text-center">{{ title }}</h1>
        <label class="inline-block mb-2">Song New Title</label>
        <input
          type="text"
          class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
          placeholder="Enter Song Title"
          v-model="newTitle"
        />
      </div>
      <div class="flex justify-center">
        <button
          type="submit"
          class="py-1.5 px-3 rounded text-white bg-green-600 m-1"
          @click.prevent="editMusic"
        >
          Submit
        </button>
        <button
          type="button"
          class="py-1.5 px-3 rounded text-white bg-gray-600 m-1"
          @click.prevent="closeEdit"
        >
          Go Back
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'EditMusicComponent',
  data() {
    return {
      newTitle: this.title
    }
  },
  props: ['id', 'title'],
  emits: ['close-edit', 'edit-music'],
  methods: {
    closeEdit() {
      this.$emit('close-edit')
    },
    editMusic() {
      if (this.newTitle !== this.title && this.newTitle !== '') {
        this.$emit('edit-music', this.id, this.newTitle)
      }
    }
  }
}
</script>