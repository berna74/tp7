<template>
  <nav>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'articulos_list' }">Artículos</RouterLink>
    <RouterLink :to="{ name: 'marcas_list' }">Marcas</RouterLink>
    <RouterLink :to="{ name: 'proveedores_list' }">Proveedores</RouterLink>
    <RouterLink :to="{ name: 'categorias_list' }">Categorías</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style>
nav {
  background: #1976d2;
  padding: 1rem;
  display: flex;
  gap: 1.5rem;
}
nav a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
}
nav a.router-link-exact-active {
  text-decoration: underline;
}
</style>