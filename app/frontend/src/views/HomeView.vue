<template>
  <div class="home-container">
    <img src="@/assets/logo.svg" alt="Logo Tienda" class="logo" />
    <h1>Tienda de Informática</h1>
    <p>
      Bienvenido al sistema de control de stock de artículos de informática.<br>
      Administrá desde acá el inventario de artículos, las categorías, marcas y proveedores.
    </p>
    <div class="home-grid">
      <router-link to="/articulos" class="home-card">
        <v-icon name="fa-desktop" scale="2" />
        <strong>Artículos</strong>
        <small>Gestión de productos y stock</small>
      </router-link>
      <router-link to="/categorias" class="home-card">
        <v-icon name="fa-folder-open" scale="2" />
        <strong>Categorías</strong>
        <small>Organiza los artículos por tipo</small>
      </router-link>
      <router-link to="/marcas" class="home-card">
        <v-icon name="fa-tags" scale="2" />
        <strong>Marcas</strong>
        <small>Gestiona las marcas disponibles</small>
      </router-link>
      <router-link to="/proveedores" class="home-card">
        <v-icon name="fa-truck" scale="2" />
        <strong>Proveedores</strong>
        <small>Administra tus proveedores</small>
      </router-link>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.home-container {
  max-width: 700px;
  margin: 3rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  text-align: center;
}
.logo {
  width: 220px;
  margin-bottom: 0.5rem;
}
.home-container h1 {
  margin-bottom: 0.5rem;
  color: #1976d2;
}
.home-container p {
  color: #444;
  margin-bottom: 2rem;
}
.home-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.5rem;
}
.home-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #f6f8fa;
  border-radius: 8px;
  padding: 1.5rem 1rem;
  text-decoration: none;
  color: #e28c41;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  transition: background 0.2s, box-shadow 0.2s;
}
.home-card:hover {
  background: #e3f0fc;
  box-shadow: 0 2px 8px rgba(25,118,210,0.08);
}
.home-card span {
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
}
.home-card strong {
  font-size: 1.1rem;
  margin-bottom: 0.2rem;
}
.home-card small {
  color: #555;
}
</style>