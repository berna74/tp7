<template>
    <div class="container">
      <h3>Modificar Proveedor</h3>
      <form @submit.prevent="modificar">
        <div class="input">
          <label for="">Nombre del proveedor</label>
          <input type="text" name="" v-model="proveedor.nombre" />
          <label for="">Teléfono</label>
          <input type="text" name="" v-model="proveedor.telefono" />
          <label for="">Dirección</label>
          <input type="text" name="" v-model="proveedor.direccion" />
          <label for="">Email</label>
          <input type="text" name="" v-model="proveedor.email" />
         
        </div>
      </form>
      <div class="botonera">
        <RouterLink :to="{ name: 'prroveedores_list' }"><button>Volver</button> </RouterLink>
        <button>Modificar</button>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useProveedorStore from '../../stores/proveedor'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  
  const { proveedor, proveedores } = toRefs(useProveedorStore())
  const { update } = useProveedorStore()
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    proveedor.value = proveedores.value.find((proveedor) => proveedor.id == parseInt(id as string)) ?? {
      nombre: 'Proveedor no encontrado',
    }
  })
  
  const modificar = async () => {
    if (!proveedor.value.nombre) {
      alert('Por favor, complete el nombre')
    } else {
      const response = await update(proveedor.value)
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