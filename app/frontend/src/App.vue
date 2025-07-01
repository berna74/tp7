<template>
  <nav>
    <a href="/">
      <img src="../public/images/logo.svg" alt="Logo" class="logo" />
    </a>
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
  align-items: center;
  gap: 1.5rem;
  height: 4rem; /* Ajusta la altura del navbar */
}

nav a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
}

nav a.router-link-exact-active {
  text-decoration: underline;
}

.logo {
  width: 3.5rem; /* Ajusta el tamaño del logo */
  height: auto;
  margin: 0 1rem; /* Espacio entre el logo y los enlaces */
}
</style>