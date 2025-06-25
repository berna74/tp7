import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import marcas_routes from './marcas_routes'

const routes = [
  { path: '/', name: 'home', component: HomeView }, // nombre en minúscula
  ...marcas_routes,
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router