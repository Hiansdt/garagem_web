<script setup>
import MediumHeader from '../components/templates/medium/MediumHeader.vue'
import MediumFooter from '../components/templates/medium/MediumFooter.vue'
import MediumAside from '../components/templates/medium/MediumAside.vue'
</script>

<template>
  <header>
    <MediumHeader />
  </header>
  <main>
    <RouterView />
  </main>
  <aside>
    <MediumAside />
  </aside>
  <footer>
    <MediumFooter />
  </footer>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 10%;
  background-color: rgb(51, 51, 51);
  color: white;
  font-size: 1.2rem;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  justify-content: end;
}

aside {
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 15%;
  color: white;
  background-color: rgb(51, 51, 51);
  font-size: 1.2rem;
  align-items: center;
  justify-content: center;
}

footer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10%;
  background-color: rgb(51, 51, 51);
  color: white;
  font-size: 1.2rem;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 100;
}

main {
  height: 80%;
  margin-top: 15%;
  margin-left: 15%;
  color: white;
}
</style>
