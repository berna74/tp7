import type {Proveedor} from '@/interfaces/Proveedor';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import ApiService from '../services/ApiService';

const url = '/proveedores';

const useProveedorStore = defineStore('proveedores',  () => {
  const proveedores = ref<Array<Proveedor>>([]);
  const proveedor = ref<Proveedor>({
    id: 0,
    nombre: '',
    telefono: '',
    direccion: '',
    email: ''   
  });


   async function getAll() {
    const data = await ApiService.getAll(url);
    if(data) {
      proveedores.value = data
     }
  }
         

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id);
    if(data) {
      proveedores.value = data
         }
        }

  async function create(proveedor: Proveedor) {
    const data = await ApiService.create(url, proveedor);
    if(data) {
      proveedores.value = data;
    }
  }
  async function update(proveedor: Proveedor) {
    if(proveedor.id) {
      const data = await ApiService.update(url, proveedor.id, proveedor);
      if(data) {
        proveedores.value = data;
      }
    }
  }

  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id);
    if(data) {
      proveedores.value = data;
    }
  }
  return {proveedores, proveedor, getAll, getOne, create, update, destroy};
})

export default useProveedorStore;