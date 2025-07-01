<template>
    <div class="container">
      <h3>Modificar Marca</h3>
      <form @submit.prevent="modificar">
        <div class="input">
          <label for="">Nombre de la marca</label>
          <input type="text" name="" v-model="marca.nombre" />
        </div>
      </form>
      <div class="botonera">
        <RouterLink :to="{ name: 'marcas_list' }"><button>Volver</button> </RouterLink>
        <button>Modificar</button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useMarcaStore from '../../stores/marcas'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  
  const { marca, marcas } = toRefs(useMarcaStore())
  const { update } = useMarcaStore()
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    marca.value = marcas.value.find((marca) => marca.id == parseInt(id as string)) ?? {
      nombre: 'Marca no encontrada',
    }
  })
  
  const modificar = async () => {
    if (!marca.value.nombre) {
      alert('Por favor, complete el nombre')
    } else {
      const response = await update(marca.value)
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