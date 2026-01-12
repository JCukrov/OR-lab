<script setup lang="ts">
import { onMounted } from 'vue'
import { useAuth0 } from '@auth0/auth0-vue'
import { useRouter } from 'vue-router'

const { handleRedirectCallback } = useAuth0()
const router = useRouter()

onMounted(async () => {
  const result = await handleRedirectCallback()
  const targetUrl = result.appState?.target || '/'
  router.replace(targetUrl)
})
</script>

<template>
  <p>Logging in...</p>
</template>