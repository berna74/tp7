<template>
    <div class="container">
      <h2>Crear Artículo</h2>
      <form @submit.prevent="crear">
        <label for="">Nuevo Artículo</label>
        <input type="text" name="" v-model="articulo.descripcion" />
        <input type="number" name="" v-model="articulo.precio" />
        <input type="number" name="" v-model="articulo.stock" />
        <input type="number" name="" v-model="articulo.marca.id" />
        <input type="number" name="" v-model="articulo.proveedor.id" />
        <button>Guardar</button>
      </form>
  
      <router-link :to="{ name: 'articulos_list' }">
        <button>Volver</button>
      </router-link>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs } from 'vue';
  import useArticuloStore from '@/stores/articulos';
  
  const { articulo } = toRefs(useArticuloStore());
  const { create } = useArticuloStore(); 
  
  const crear = async () => { 
    if (!articulo.value.descripcion) {
      alert('Por favor, ingrese un nombre para el artículo.');
      return;
    }
  
    try {
      const response = await create(articulo.value); 
      articulo.value.descripcion = ''; 
      alert('Artículo creado exitosamente.');
    } catch (error) {
      console.error('Error al crear el artículo:', error);
      alert('Hubo un error al crear el artículo. Por favor, inténtalo de nuevo.');
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