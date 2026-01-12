<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue';
import LoginButton from './LoginButton.vue'
import LogoutButton from './LogoutButton.vue'
import { downloadCSV, return_JSON } from '../scripts/download';
import { cards } from '../scripts/constants';


const { isAuthenticated } = useAuth0()


const handleDownload = () => {
    return_JSON(cards.value)
    downloadCSV(cards.value)
}
</script>

<template>
    <div class="header-container">
        <h2>Home</h2>
        <div style="margin-left: auto;">
            <div v-if="!isAuthenticated">
                <LoginButton/>
            </div>
            <div v-else>
                <button @click="handleDownload">Osvježi preslike</button>
                <button @click="$router.push('/profile')">Profile</button>
                <LogoutButton/>
            </div>
        </div>
    </div>
</template>

<style lang="css">
.header-container{
    display: flex;
    height: 50px;
    width: 100%;
    border-bottom: 2px solid black;
    background-color: #303030;
    color: white; 
    align-items: center;
}
</style>