<template>
    <div class="container">
      <h3>Modificar Categoría</h3>
      <form @submit.prevent="modificar">
        <div class="input">
          <label for="">Nombre de la categoría</label>
          <input type="text" name="" v-model="categoria.nombre" />
        </div>
      </form>
      <div class="botonera">
        <RouterLink :to="{ name: 'categorias_list' }"><button>Volver</button> </RouterLink>
        <button>Modificar</button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useCategoriaStore from '../../stores/categorias'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  
  const { categoria, categorias } = toRefs(useCategoriaStore())
  const { update } = useCategoriaStore()
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    categoria.value = categorias.value.find((categoria) => categoria.id == parseInt(id as string)) ?? {
      nombre: 'Categoría no encontrada',
    }
  })
  
  const modificar = async () => {
    if (!categoria.value.nombre) {
      alert('Por favor, complete el nombre')
    } else {
      const response = await update(categoria.value)
      alert(response)
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
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}
</style>