<template>
  <div class="container">
  <h2>Marcas</h2>
  <router-link :to="{name: 'marcas_create'}"><button>Crear Marca</button></router-link>
<table class="table table-striped mt-3">
    <thead>
      <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="marca in marcas" :key="marca.id">
        <td>{{ marca.id }}</td>
        <td>{{ marca.nombre }}</td>
        <td>
         <router-link :to="{name: 'marcas_show', params: {id: marca.id }}"><button>Mostrar</button></router-link>
         <router-link :to="{name: 'marcas_edit', params: {id: marca.id }}"><button>Editar</button></router-link>
         <button @click.prevent="eliminar(marca.id as number)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>

<script setup lang="ts">
import useMarcaStore from '@/stores/marcas';
import { onMounted } from 'vue';
import { toRefs } from 'vue';

const {marcas} = toRefs(useMarcaStore());
const { getAll, destroy } = useMarcaStore();

onMounted(async() => {
  await getAll();
});

async function eliminar (id: number) {
  if (confirm('¿Estás seguro de eliminar la marca ' + id + '?')) {
    if (confirm('Esta acción no se puede deshacer. ¿Deseas continuar?')) {
      
      console.log('Eliminando marca con ID:', id);
    } else {
      console.log('Eliminación cancelada por el usuario.');
      return;
    }
    
       await destroy(id);
       await getAll();
    }
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
button {
  margin: 5px;
}
</style>