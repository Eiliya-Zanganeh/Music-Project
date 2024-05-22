<template>

  <header-component />

  <router-view v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>

  <player-component />

  <auth-component />

</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import AuthComponent from '@/components/AuthComponent.vue'
import PlayerComponent from '@/components/PlayerComponent.vue'

export default {
  name: 'App',
  components: { PlayerComponent, AuthComponent, HeaderComponent }
}
</script>

<style>
.fade-enter-from{
  opacity: 0;
}

.fade-enter-active{
  transition: all 0.5s linear;
}

.fade-leave-to{
  transition: all 0.5s linear;
  opacity: 0;
}
</style>