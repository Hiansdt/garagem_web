<script setup>
import LargeHeader from '../components/templates/large/LargeHeader.vue'
import LargeFooter from '../components/templates/large/LargeFooter.vue'
import LargeAside from '../components/templates/large/LargeAside.vue'
</script>

<template>
  <div id="layout-large">
    <header>
      <LargeHeader />
    </header>
    <main>
      <RouterView />
    </main>
    <aside>
      <LargeAside />
    </aside>
    <footer>
      <LargeFooter />
    </footer>
  </div>
</template>

<style scoped>
#layout-large {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 10%;
  background-color: rgb(51, 51, 51);
  color: white;
  font-size: 1.2rem;
  position: absolute;
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
  min-height: 100%;
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
  bottom: 0;
  width: 100%;
  z-index: 100;
}

main {
  min-height: 85vh;
  margin: 6% 0% 0% 15%;
  color: white;
}
</style>
