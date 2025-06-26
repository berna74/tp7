<template>
 <h4>Marcascaca123</h4>
 <RouterView />
 
 </template>

<script setup>

import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const route = useRouter();

onMounted(() => {
console.log('MarcasView montado'); 
route.push({ name: 'marcas_list' });
});

</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 2rem auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
</style>