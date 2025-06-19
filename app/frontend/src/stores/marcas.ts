import type {Marca} from '@/interfaces/Marca';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import ApiService from '../services/ApiService';

const url = '/marcas';

const useMarcaStore = defineStore('marcas',  () => {
  const marcas = ref<Array<Marca>>([]);
  const marca = ref<Marca>({
    id: 0,
    nombre: ''
  });


   async function getAll() {
    const data = await ApiService.getAll(url);
    if(data) {
      marcas.value = data
     }
  }
         

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id);
    if(data) {
      marcas.value = data
         }
        }

  async function create(marca: Marca) {
    const data = await ApiService.create(url, marca);
    if(data) {
      marcas.value = data;
    }
  }
  async function update(marca: Marca) {
    if(marca.id) {
      const data = await ApiService.update(url, marca.id, marca);
      if(data) {
        marcas.value = data;
      }
    }
  }

  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id);
    if(data) {
      marcas.value = data;
    }
  }
  return {marcas, marca, getAll, getOne, create, update, destroy};
})

export default useMarcaStore;