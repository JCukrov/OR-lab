<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'

const { loginWithRedirect, isLoading } = useAuth0()

const handleLogin = async() => {
  await loginWithRedirect({
    appState: {target: '/profile'},
    
  })
}
</script>

<template>
  <button 
    @click="handleLogin" 
    class="button login"
    :disabled="isLoading"
  >
    {{ isLoading ? 'Loading...' : 'Log In' }}
  </button>
</template>
