<script setup>
import { ref, reactive, onMounted } from 'vue'
import MarcasApi from '@/api/marcas'
const marcasApi = new MarcasApi()

const defaultMarca = { id: null, nome: '', nacionalidade: ''}
const marcas = ref([])
const marca = reactive({ ...defaultMarca })

onMounted(async () => {
  marcas.value = await marcasApi.buscarTodasAsMarcas()
})

function limpar() {
  Object.assign(marca, { ...defaultMarca })
}

async function salvar() {
  if (marca.id) {
    await marcasApi.atualizarMarca(marca)
  } else {
    await marcasApi.adicionarMarca(marca)
  }
  marcas.value = await marcasApi.buscarTodasAsMarcas()
  limpar()
}

function editar(marca_para_editar) {
  Object.assign(marca, marca_para_editar)
}

async function excluir(id) {
  await marcasApi.excluirMarca(id)
  marcas.value = await marcasApi.buscarTodasAsMarcas()
  limpar()
}
</script>

<template>
    <h1>Marca</h1>
    <hr />
    <div class="form">
        <input type="text" v-model="marca.nome" placeholder="nome" />
        <input type="text" v-model="marca.nacionalidade" placeholder="nacionalidade" />
        <button @click="salvar">Salvar</button>
        <button @click="limpar">Limpar</button>
    </div>
    <hr />
    <ul>
        <li v-for="marca in marcas" :key="marca.id">
        <span>
            ({{ marca.id }}) - {{ marca.nome }} - {{marca.nacionalidade}} - 
        </span>
        <button @click="editar(marca)">Editar</button>
        <button @click="excluir(marca.id)">Excluir</button>
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