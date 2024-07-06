<script setup>
import { ref, reactive, onMounted } from 'vue'
import ModelosApi from '@/api/modelos'
import MarcasApi from '@/api/marcas'

const modelosApi = new ModelosApi()
const marcasApi = new MarcasApi()

const defaultModelo = { id: null, nome: '', marca: null}
const modelos = ref([])
const marcas = ref([])
const modelo = reactive({ ...defaultModelo })

onMounted(async () => {
  modelos.value = await modelosApi.buscarTodosOsModelos()
  marcas.value = await marcasApi.buscarTodasAsMarcas()
})

function limpar() {
  Object.assign(modelo, { ...defaultModelo })
}

async function salvar() {
  if (modelo.id) {
    await modelosApi.atualizarModelo(modelo)
  } else {
    await modelosApi.adicionarModelo(modelo)
  }
  modelos.value = await modelosApi.buscarTodosOsModelos()
  limpar()
}

function editar(modelo_para_editar) {
  modelo.nome = modelo_para_editar.nome
  modelo.marca = modelo_para_editar.marca.id
}

async function excluir(id) {
  await modelosApi.excluirModelo(id)
  modelos.value = await modelosApi.buscarTodosOsModelos()
  limpar()
}
</script>

<template>
  <h1>Modelo</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="modelo.nome" placeholder="Nome" />
    <select v-model="modelo.marca">
      <option v-for="marca in marcas" :key="marca.id" :value="marca.id">
        {{ marca.nome }}
      </option>
    </select>
    <button @click="salvar">Salvar</button>
    <button @click="limpar">Limpar</button>
  </div>
  <hr />
  <ul>
    <li v-for="modelo in modelos" :key="modelo.id">
      <span @click="editar(modelo)">
        ({{ modelo.id }}) - {{ modelo.nome }} - {{ modelo.marca.nome }}</span
      >
      <button @click="excluir(modelo.id)">X</button>
    </li>
  </ul>
</template>
