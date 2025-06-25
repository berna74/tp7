<template>
  <div class="container">
    <h1>Categorías</h1>
    <form @submit.prevent="addCategoria">
      <input v-model="nuevo.nombre" placeholder="Nombre de la categoría" required />
      <button type="submit">Agregar</button>
    </form>
    <ResourceTable
      :items="store.categorias"
      :columns="['id', 'nombre']"
      @delete="eliminarCategoria"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCategoriaStore } from '../stores/categoria';
import ResourceTable from '../components/ResourceTable.vue';

const store = useCategoriaStore();
const nuevo = ref({ nombre: '' });

onMounted(() => {
  store.fetchCategorias();
});

function addCategoria() {
  store.createCategoria({ ...nuevo.value });
  nuevo.value.nombre = '';
}

function eliminarCategoria(id) {
  store.deleteCategoria(id);
}
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
</style>