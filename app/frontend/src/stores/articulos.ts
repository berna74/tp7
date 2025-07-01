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
<<<<<<< HEAD
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
=======
    marca_id: 0,
    proveedor_id: 0,
    categoria: ''
  });


>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
   async function getAll() {
    const data = await ApiService.getAll(url);
    if(data) {
      articulos.value = data
     }
  }
         

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id);
    if(data) {
<<<<<<< HEAD
      articulo.value = data
=======
      articulos.value = data
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
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
<<<<<<< HEAD
});
=======
})
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb

export default useArticuloStore