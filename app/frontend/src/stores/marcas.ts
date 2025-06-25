import { defineStore } from 'pinia';
import { ref } from 'vue';
import ApiService from '../services/ApiService';

const useMarcaStore = defineStore('marcas',  () => {
  const marcas = ref<Array<Marca>>([]);
  const marca = ref<Marca>({
    id: 0,
    nombre: ''
  });
   function getAll() {
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
