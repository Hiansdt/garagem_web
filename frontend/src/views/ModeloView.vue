<script setup>
import { ref, reactive, onMounted } from 'vue'
import ModelosApi from '@/api/modelos'
import MarcasApi from '@/api/marcas'
import CategoriasApi from '@/api/categorias'

const modelosApi = new ModelosApi()
const marcasApi = new MarcasApi()
const categoriasApi = new CategoriasApi()

const defaultModelo = { nome: '', marca: null, categoria: null }
const modelos = ref([])
const marcas = ref([])
const categorias = ref([])
const modelo = reactive({ ...defaultModelo })

onMounted(async () => {
  modelos.value = await modelosApi.buscarTodosOsModelos()
  marcas.value = await marcasApi.buscarTodasAsMarcas()
  categorias.value = await categoriasApi.buscarTodasAsCategorias()
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
  modelo.id = modelo_para_editar.id
  modelo.nome = modelo_para_editar.nome
  modelo.marca = modelo_para_editar.marca.id
  modelo.categoria = modelo_para_editar.categoria.id
}

async function excluir(id) {
  await modelosApi.excluirModelo(id)
  modelos.value = await modelosApi.buscarTodosOsModelos()
  limpar()
}
</script>

<template>
  <h1>Modelos</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="modelo.nome" placeholder="Nome" />
    <select v-model="modelo.marca">
      <option v-for="marca in marcas" :key="marca.id" :value="marca.id">
        {{ marca.nome }}
      </option>
    </select>
    <select v-model="modelo.categoria">
      <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">
        {{ categoria.descricao }}
      </option>
    </select>
    <button @click="salvar">Salvar</button>
    <button @click="limpar">Limpar</button>
  </div>
  <hr />
  <ul>
    <li v-for="modelo in modelos" :key="modelo.id">
      <span>
        ({{ modelo.id }}) - {{ modelo.nome }} - {{ modelo.marca.nome }} - {{modelo.categoria.descricao}}</span
      >
      <button @click="editar(modelo)">Editar</button>
      <button @click="excluir(modelo.id)">Excluir</button>
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
