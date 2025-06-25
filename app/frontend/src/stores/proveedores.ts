import { defineStore } from 'pinia';
import api from '../services/api';

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({
    proveedores: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchProveedores() {
      this.loading = true;
      try {
        const res = await api.get('/proveedor');
        this.proveedores = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
    async createProveedor(data) {
      try {
        const res = await api.post('/proveedor', data);
        this.proveedores.push(res.data);
      } catch (err) {
        this.error = err;
      }
    },
    async deleteProveedor(id) {
      try {
        await api.delete(`/proveedor/${id}`);
        this.proveedores = this.proveedores.filter(p => p.id !== id);
      } catch (err) {
        this.error = err;
      }
    }
  }
});