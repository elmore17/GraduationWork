import { createApp } from 'vue';
import * as VueRouter from 'vue-router';
import './style.css';
import App from './App.vue';
import Authorize from './components/Authorization.vue';
import Home from './components/Home.vue';

const routes = [
    { path: '/', component: Authorize },
    { path: '/home', component: Home }
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes,
  })


createApp(App).use(router).mount('#app')
