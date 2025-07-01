import type {Articulo} from '@/interfaces/Articulo';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import ApiService from '../services/ApiService';

const url = '/articulos';


const useArticuloStore = defineStore('articulos',  () => {
  const articulos = ref<Array<Articulo>>([]);
  const articulo = ref<Articulo>({
    id: 0,
    descripcion: '',
    precio: 0,
    stock: 0,
    marca: {
      id: 0,
      nombre: ''
    },
    proveedor: {
      id: 0,
      nombre: ''
    },
    categorias: []
  });
   async function getAll() {
    const data = await ApiService.getAll(url);
    if(data) {
      articulos.value = data
     }
  }
         

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id);
    if(data) {
      articulo.value = data
         }
        }

  async function create(articulo: Articulo) {
    const data = await ApiService.create(url, articulo);
    if(data) {
      articulos.value = data;
    }
  }
  async function update(articulo: Articulo) {
    if(articulo.id) {
      const data = await ApiService.update(url, articulo.id, articulo);
      if(data) {
        articulos.value = data;
       }
  }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id);
    if(data) {
      articulos.value = data;
    }
  }
  return {articulos, articulo, getAll, getOne, create, update, destroy};
});

export default useArticuloStore