<script setup>
import SmallHeader from '@/components/templates/small/SmallHeader.vue'
import SmallFooter from '@/components/templates/small/SmallFooter.vue'
import SmallAside from '@/components/templates/small/SmallAside.vue'
</script>

<template>
  <header>
    <SmallHeader />
  </header>
  <main>
    <RouterView />
  </main>
  <aside>
    <SmallAside />
  </aside>
  <footer>
    <SmallFooter />
  </footer>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 5%;
  background-color: rgb(51, 51, 51);
  color: white;
  font-size: 0.8rem;
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
  width: 25%;
  color: white;
  background-color: rgb(51, 51, 51);
  font-size: 0.8rem;
  align-items: center;
  justify-content: center;
}

footer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 5%;
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
  height: 90%;
  margin: 12% 0% 0% 30%;
  color: white;
}
</style>
