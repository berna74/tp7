<template>
  <div class="container">
    <h1>Proveedores</h1>
    <form @submit.prevent="addProveedor">
      <input v-model="nuevo.nombre" placeholder="Nombre" required />
      <input v-model="nuevo.telefono" placeholder="Teléfono" required />
      <input v-model="nuevo.direccion" placeholder="Dirección" required />
      <input v-model="nuevo.email" type="email" placeholder="Email" required />
      <button type="submit">Agregar</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Teléfono</th>
          <th>Dirección</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proveedor in store.proveedores" :key="proveedor.id">
          <td>{{ proveedor.id }}</td>
          <td>{{ proveedor.nombre }}</td>
          <td>{{ proveedor.telefono }}</td>
          <td>{{ proveedor.direccion }}</td>
          <td>{{ proveedor.email }}</td>
          <td>
            <button @click="eliminarProveedor(proveedor.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProveedorStore } from '../stores/proveedor';

const store = useProveedorStore();
const nuevo = ref({
  nombre: '',
  telefono: '',
  direccion: '',
  email: ''
});

onMounted(() => {
  store.fetchProveedores();
});

function addProveedor() {
  store.createProveedor({ ...nuevo.value });
  nuevo.value = { nombre: '', telefono: '', direccion: '', email: '' };
}

function eliminarProveedor(id) {
  store.deleteProveedor(id);
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