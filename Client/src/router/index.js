import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import ManageView from '@/views/ManageView.vue'
import useServerStore from '@/stores/server.js'
import SongComponent from '@/views/SongView.vue'

const routes = [
  {
    name: 'home',
    path: '/',
    component: HomeView
  },
  {
    name: 'about',
    path: '/about',
    component: AboutView
  },
  {
    name: 'song',
    path: '/song/:id',
    component: SongComponent
  },
  {
    name: 'manage',
    // alias: ['/music', '/manage-music'],
    path: '/manage',
    component: ManageView,
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/:catchAll(.*)*',
    redirect: { name: 'home' }
  }
]


const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: 'text-yellow-500'
})

router.beforeEach((to, from, next) => {
  const serverStore = useServerStore()
  if(!to.meta.requireAuth || serverStore.username !== ''){
    next()
  } else {
    next({name: 'home'})
  }
})

export default router
