<template>
    <div class="container">
      <h2>Crear Proveedor</h2>
      <form @submit.prevent="crear">
        <label for="">Nuevo Proveedor</label>
        <input type="text" name="" v-model="proveedor.nombre" />
        <input type="text" name="" v-model="proveedor.telefono" />
        <input type="text" name="" v-model="proveedor.direccion" />
        <input type="text" name="" v-model="proveedor.email" />
        <button>Guardar</button>
      </form>
  
      <router-link :to="{ name: 'proveedores_list' }">
        <button>Volver</button>
      </router-link>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs } from 'vue';
  import useProveedorStore from '@/stores/proveedor';
  
  const { proveedor } = toRefs(useProveedorStore());
  const { create } = useProveedorStore(); 
  
  const crear = async () => { 
    if (!proveedor.value.nombre) {
      alert('Por favor, ingrese un nombre para el proveedor.');
      return;
    }
  
    try {
      const response = await create(proveedor.value); 
      proveedor.value.nombre = ''; 
      alert('Proveedor creado exitosamente.');
    } catch (error) {
      console.error('Error al crear el proveedor:', error);
      alert('Hubo un error al crear el proveedor. Por favor, inténtalo de nuevo.');
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 700px;
    margin: 2rem auto;
    padding: 2rem;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  }
  </style>