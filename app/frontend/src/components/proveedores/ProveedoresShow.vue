<template>
    <div class="container">
      <h2>Detalle del proveedor</h2>
      <h3>Nombre : {{ proveedor.nombre }}</h3>
      <h4>ID: {{ proveedor.id }}
          Teléfono: {{ proveedor.telefono }}
          Dirección:{{ proveedor.direccion }}
          Email: {{ proveedor.email }}</h4>
  
      <RouterLink :to="{ name: 'proveedores_list' }"><button>Volver</button> </RouterLink>
    </div>
  </template>
  
  <script setup lang="ts">
  import { toRefs, onMounted } from 'vue'
  import useProveedorStore from '../../stores/proveedor'
  import { useRoute } from 'vue-router'
  
  const route = useRoute()
  const { proveedor, proveedores } = toRefs(useProveedorStore())
  
  onMounted(() => {
    const id = route.params.id
    console.log(id)
    proveedor.value = proveedores.value.find((proveedor) => proveedor.id == parseInt(id as string)) ?? {
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