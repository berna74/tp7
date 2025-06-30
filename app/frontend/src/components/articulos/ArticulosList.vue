<template>
    <div class="container">
    <h2>Artículos</h2>
    <router-link :to="{name: 'articulos_create'}"><button>Crear Artículo</button></router-link>
  <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th>ID</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Marca</th>
          <th>Proveedor</th>          
          <th>Categorías</th>          
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="articulo in articulos" :key="articulo.id">
          <td>{{ articulo.id }}</td>
          <td>{{ articulo.descripcion }}</td>
          <td>{{ articulo.precio }}</td> 
          <td>{{ articulo.stock }}</td>
          <td>{{ articulo.marca.nombre }}</td>
          <td>{{ articulo.proveedor.nombre }}</td>
                   
          <td>
           <router-link :to="{name: 'articulos_show', params: {id: articulo.id }}"><button>Mostrar</button></router-link>
           <router-link :to="{name: 'articulos_edit', params: {id: articulo.id }}"><button>Editar</button></router-link>
           <button @click.prevent="eliminar(articulo.id as number)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  </template>
  
  <script setup lang="ts">
  import useArticuloStore from '@/stores/articulos';
  import { onMounted } from 'vue';
  import { toRefs } from 'vue';
  
  const {articulos} = toRefs(useArticuloStore());
  const { getAll, destroy } = useArticuloStore();
  
  onMounted(async() => {
    await getAll();
  });
  
  async function eliminar (id: number) {
    if (confirm('¿Estás seguro de eliminar el artículo ' + id + '?')) {
      if (confirm('Esta acción no se puede deshacer. ¿Deseas continuar?')) {
        console.log('Eliminando artículo con ID:', id);
        await destroy(id);
        await getAll();
      } else {
        console.log('Eliminación cancelada por el usuario.');
      }
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