<template>
    <div class="container">
      <h2>Crear Categoría</h2>
      <form @submit.prevent="crear">
        <label for="">Nueva Categoría</label>
        <input type="text" name="" v-model="categoria.nombre" />
        <button>Guardar</button>
      </form>
  
      <router-link :to="{ name: 'categorias_list' }">
        <button>Volver</button>
      </router-link>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs } from 'vue';
  import useCategoriaStore from '@/stores/categorias';
  
  const { categoria } = toRefs(useCategoriaStore());
  const { create } = useCategoriaStore(); 
  
  const crear = async () => { 
    if (!categoria.value.nombre) {
      alert('Por favor, ingrese un nombre para la categoría.');
      return;
    }
  
    try {
      const response = await create(categoria.value); 
      categoria.value.nombre = ''; 
      alert('Categoría creada exitosamente.');
    } catch (error) {
      console.error('Error al crear la categoría:', error);
      alert('Hubo un error al crear la categoría. Por favor, inténtalo de nuevo.');
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