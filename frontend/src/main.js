import { createApp } from 'vue';
import * as VueRouter from 'vue-router';
import './style.css';
import App from './App.vue';
import Authorize from './components/Authorization.vue';
import Main from './components/Main.vue';
import Home from './components/Home.vue';
import Members from './components/Members.vue';

const routes = [
    { path: '/', component: Authorize },
    { path: '/main', component: Main },
    { path: '/home', component: Home },
    { path: '/members', component: Members }
]

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes,
  })


createApp(App).use(router).mount('#app')
