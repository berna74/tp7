<template>
    <div class="container">
    <h4>Proveedores</h4>
    <!-- renderizado del modulo Proveedores, lista, create, update, mostrar una en particular-->
    <RouterView />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()

onMounted(() => {
  //console.log('componente montado')
  router.push({ name: 'proveedores_list' })
})
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
form {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
  align-items: center;
}
input, button {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 1rem;
}
button {
  background: #1976d2;
  color: #fff;
  border: none;
  cursor: pointer;
  transition: background 0.2s;
}
button:hover {
  background: #1565c0;
}
table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
th, td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #eaeaea;
  text-align: left;
}
th {
  background: #f0f4f8;
  font-weight: 600;
}
tr:last-child td {
  border-bottom: none;
}
</style>