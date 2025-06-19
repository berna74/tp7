import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './assets/main.css'
import App from './App.vue'
import router from './router'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { FaDesktop, FaTags, FaTruck, FaFolderOpen } from "oh-vue-icons/icons";

// Agrega los íconos seleccionados
addIcons(FaDesktop, FaTags, FaTruck, FaFolderOpen);


const app = createApp(App)

app.use(createPinia())
app.use(router)

app.component("v-icon", OhVueIcon)

app.mount('#app')
