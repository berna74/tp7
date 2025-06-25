<template>
  <div class="container">
    <h1>Artículos</h1>
    <form @submit.prevent="addArticulo">
      <input v-model="nuevo.descripcion" placeholder="Descripción" required />
      <input v-model.number="nuevo.precio" type="number" step="0.01" placeholder="Precio" required />
      <input v-model.number="nuevo.stock" type="number" placeholder="Stock" required />
      <select v-model="nuevo.marca_id" required>
        <option value="" disabled selected>Seleccione Marca</option>
        <option v-for="marca in marcas" :key="marca.id" :value="marca.id">{{ marca.nombre }}</option>
      </select>
      <select v-model="nuevo.proveedor_id" required>
        <option value="" disabled selected>Seleccione Proveedor</option>
        <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">{{ proveedor.nombre }}</option>
      </select>
      <button type="submit">Agregar</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Marca</th>
          <th>Proveedor</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="articulo in store.articulos" :key="articulo.id">
          <td>{{ articulo.id }}</td>
          <td>{{ articulo.descripcion }}</td>
          <td>{{ articulo.precio }}</td>
          <td>{{ articulo.stock }}</td>
          <td>{{ getMarcaNombre(articulo.marca_id) }}</td>
          <td>{{ getProveedorNombre(articulo.proveedor_id) }}</td>
          <td>
            <button @click="eliminarArticulo(articulo.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useArticulosStore } from '../stores/articulos';
import api from '../services/api';

const store = useArticulosStore();
const nuevo = ref({
  descripcion: '',
  precio: '',
  stock: '',
  marca_id: '',
  proveedor_id: ''
});

const marcas = ref([]);
const proveedores = ref([]);

onMounted(async () => {
  await store.fetchArticulos();
  marcas.value = (await api.get('/marca')).data;
  proveedores.value = (await api.get('/proveedor')).data;
});

function addArticulo() {
  store.createArticulo({ ...nuevo.value });
  nuevo.value = { descripcion: '', precio: '', stock: '', marca_id: '', proveedor_id: '' };
}

function eliminarArticulo(id) {
  store.deleteArticulo(id);
}

function getMarcaNombre(id) {
  const marca = marcas.value.find(m => m.id === id);
  return marca ? marca.nombre : '';
}

function getProveedorNombre(id) {
  const proveedor = proveedores.value.find(p => p.id === id);
  return proveedor ? proveedor.nombre : '';
}
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
input, select, button {
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