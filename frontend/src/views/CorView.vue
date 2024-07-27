<script setup>
import { ref, reactive, onMounted } from 'vue'
import CoresApi from '@/api/cores'
const coresApi = new CoresApi()

const defaultCor = { id: null, descricao: '' }
const cores = ref([])
const cor = reactive({ ...defaultCor })

onMounted(async () => {
  cores.value = await coresApi.buscarTodasAsCores()
})

function limpar() {
  Object.assign(cor, { ...defaultCor })
}

async function salvar() {
  if (cor.id) {
    await coresApi.atualizarCor(cor)
  } else {
    await coresApi.adicionarCor(cor)
  }
  cores.value = await coresApi.buscarTodasAsCores()
  limpar()
}

function editar(cor_para_editar) {
  Object.assign(cor, cor_para_editar)
} 

async function excluir(id) {
  await coresApi.excluirCor(id)
  cores.value = await coresApi.buscarTodasAsCores()
  limpar()
}
</script>

<template>
    <h1>Cor</h1>
    <hr />
    <div class="form">
        <input type="text" v-model="cor.nome" placeholder="Cor" />
        <button @click="salvar">Salvar</button>
        <button @click="limpar">Limpar</button>
    </div>
    <hr />
    <ul>
        <li v-for="cor in cores" :key="cor.id">
        <span>
            ({{ cor.id }}) - {{ cor.nome }} - 
        </span>
        <button @click="editar(cor)">Editar</button>
        <button @click="excluir(cor.id)">Excluir</button>
        </li>
    </ul>
</template>

<style scoped>
.form {
  margin-left: 1%;
  display: flex;
  width: 75%;
  flex-wrap: wrap;
  margin-top: 1%;
  margin-bottom: 1%;
}

h1 {
  text-align: center;
}

button {
  margin-left: 1%;
}

select {
  height: 40px;
}
</style>