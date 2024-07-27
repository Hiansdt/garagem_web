<script setup>
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<template>
    <div class="logged">
      <div v-if="authStore.loggedIn">
        <router-link to="/logout">Logout</router-link> |
        {{ authStore.user.email }}
      </div>
      <router-link v-else to="/login">Login</router-link>
    </div>
</template>

<style scoped>

.logged {
  margin-right: 5%;
}
</style>
