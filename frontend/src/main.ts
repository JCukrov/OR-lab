import { createApp } from 'vue'
import { createAuth0, useAuth0 } from '@auth0/auth0-vue'
import { createRouter, createWebHistory } from 'vue-router'

import Home from './pages/Home.vue'
import UserProfile from './components/UserProfile.vue'

import App from './App.vue'
import './style.css'


const app = createApp(App)
app.use(createAuth0({
  domain: import.meta.env.VITE_OAUTH_DOMAIN,
  clientId: import.meta.env.VITE_OAUTH_CLIENT_ID,
  authorizationParams: {
    redirect_uri: window.location.origin
  },
  cacheLocation: 'localstorage',
  useRefreshTokens: true
}))

const routes = [
    {path: '/', component: Home},
    {path: '/profile', component: UserProfile, meta: {requiresAuth: true}},
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach(async (to, from, next) => {
  const {isAuthenticated} = useAuth0()

  if (to.meta.requiresAuth && !isAuthenticated.value){
    router.push('/')
  }
  next()
})

app.use(router)
app.mount('#app')
