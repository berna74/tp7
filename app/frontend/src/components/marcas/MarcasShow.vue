<template>
    <div class="container">
      <h2>Detalle de la marca</h2>
      <h3>Nombre : {{ marca.nombre }}</h3>
      <h4>ID: {{ marca.id }}</h4>
  
      <RouterLink :to="{ name: 'marcas_list' }"><button>Volver</button> </RouterLink>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useMarcaStore from '../../stores/marcas'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const { marca, marcas } = toRefs(useMarcaStore())
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    marca.value = marcas.value.find((marca) => marca.id == parseInt(id as string)) ?? {
      nombre: '',
    }
  })
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