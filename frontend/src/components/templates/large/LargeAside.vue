<script setup></script>

<template>
        <div class="links">
            <router-link :to="{ name: 'home' }">Home</router-link>
            <router-link to="/modelos">Modelos</router-link>
            <router-link to="/acessorios">Acessorios</router-link>
            <router-link to="/categorias">Categorias</router-link>
            <router-link to="/marcas">Marcas</router-link>
            <router-link to="/cores">Cores</router-link>
            <router-link to="/veiculos">Veiculos</router-link>
        </div>
</template>

<style scoped>

.links{
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

</style>