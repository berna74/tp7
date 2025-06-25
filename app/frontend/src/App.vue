<template>
  <nav>
    <RouterLink :to="{ name: 'home' }">HOME</RouterLink>
    <RouterLink :to="{ name: 'marcas_list' }">MARCAS</RouterLink>
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