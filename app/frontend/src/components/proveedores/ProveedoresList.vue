<template>
    <div class="container">
    <h2>Proveedores</h2>
    <router-link :to="{name: 'proveedores_create'}"><button>Crear Proveedor</button></router-link>
  <table class="table table-striped mt-3">
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Teléfono</th>
          <th>Dirección</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proveedor in proveedores" :key="proveedor.id">
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre }}</td>
          <td>{{ proveedor.telefono }}</td>
          <td>{{ proveedor.direccion }}</td>
          <td>{{ proveedor.email }}</td>

          <td>
           <router-link :to="{name: 'proveedores_show', params: {id: proveedor.id }}"><button>Mostrar</button></router-link>
           <router-link :to="{name: 'proveedores_edit', params: {id: proveedor.id }}"><button>Editar</button></router-link>
           <button @click.prevent="eliminar(proveedor.id as number)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  </template>
  
  <script setup lang="ts">
  import useProveedorStore from '@/stores/proveedor';
  import { onMounted } from 'vue';
  import { toRefs } from 'vue';
  
  const {proveedores} = toRefs(useProveedorStore());
  const { getAll, destroy } = useProveedorStore();
  
  onMounted(async() => {
    await getAll();
  });
  
  async function eliminar (id: number) {
    if (confirm('¿Estás seguro de eliminar el proveedor ' + id + '?')) {
      if (confirm('Esta acción no se puede deshacer. ¿Deseas continuar?')) {
        
        console.log('Eliminando proveedor con ID:', id);
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