<template>
  <div class="container">
    <h2>Crear Marca</h2>
    <form @submit.prevent="crear">
      <label for="">Nueva Marca</label>
      <input type="text" name="" v-model="marca.nombre" />
      <button>Guardar</button>
    </form>

    <router-link :to="{ name: 'marcas_list' }">
      <button>Volver</button>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue';
import useMarcaStore from '@/stores/marcas';

const { marca } = toRefs(useMarcaStore());
const { create } = useMarcaStore(); // Corregido: eliminé el carácter inesperado

const crear = async () => { // Corregido: moví "async" al lugar correcto
  if (!marca.value.nombre) {
    alert('Por favor, ingrese un nombre para la marca.');
    return;
  }

  try {
    const response = await create(marca.value); // Usar "create" correctamente
    marca.value.nombre = ''; // Limpiar el campo después de crear
    alert('Marca creada exitosamente.');
  } catch (error) {
    console.error('Error al crear la marca:', error);
    alert('Hubo un error al crear la marca. Por favor, inténtalo de nuevo.');
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