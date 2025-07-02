<template>
    <div class="container">
      <h3>Modificar Artículo</h3>
<<<<<<< HEAD
      <form @submit.prevent="modificar" v-if="articulo.id">
=======
      <form @submit.prevent="modificar">
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
        <div class="input">
          <label for="">Nombre del artículo</label>
          <input type="text" name="" v-model="articulo.descripcion" />
          <label for="">Precio</label>
          <input type="number" name="" v-model="articulo.precio" />
          <label for="">Stock</label>
          <input type="number" name="" v-model="articulo.stock" />
          <label for="">Marca</label>
          <input type="number" name="" v-model="articulo.marca.id" />
          <label for="">Proveedor</label>
          <input type="number" name="" v-model="articulo.proveedor.id" />
        
        </div>
<<<<<<< HEAD
        <div class="botonera">
          <RouterLink :to="{ name: 'articulos_list' }"><button type="button">Volver</button></RouterLink>
          <button type="submit">Modificar</button>
        </div>
      </form>
      <div v-else>
        <p>Cargando artículo...</p>
=======
      </form>
      <div class="botonera">
        <RouterLink :to="{ name: 'articulos_list' }"><button>Volver</button> </RouterLink>
        <button>Modificar</button>
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useArticuloStore from '../../stores/articulos'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  
  const { articulo, articulos } = toRefs(useArticuloStore())
  const { update } = useArticuloStore()
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    articulo.value = articulos.value.find((articulo) => articulo.id == parseInt(id as string)) ?? {
<<<<<<< HEAD
      id: 0,
      descripcion: 'Artículo no encontrado',
      precio: 0,
      stock: 0,
      marca: { id: 0, nombre: '' },
      proveedor: { id: 0, nombre: '' },
      categorias: []
=======
      descripcion: 'Marca no encontrada',
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
    }
  })
  
  const modificar = async () => {
    if (!articulo.value.descripcion) {
      alert('Por favor, complete el nombre')
    } else {
      const response = await update(articulo.value)
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