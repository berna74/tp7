import { defineStore } from 'pinia';
import api from '../services/api';

export const useCategoriaStore = defineStore('categoria', {
  state: () => ({
    categorias: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchCategorias() {
      this.loading = true;
      try {
        const res = await api.get('/categoria');
        this.categorias = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
    async createCategoria(data) {
      try {
        const res = await api.post('/categoria', data);
        this.categorias.push(res.data);
      } catch (err) {
        this.error = err;
      }
    },
    async deleteCategoria(id) {
      try {
        await api.delete(`/categoria/${id}`);
        this.categorias = this.categorias.filter(c => c.id !== id);
      } catch (err) {
        this.error = err;
      }
    }
  }
});