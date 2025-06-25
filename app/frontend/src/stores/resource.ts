import { defineStore } from 'pinia';
import api from '../services/api';

export const useResourceStore = defineStore('resource', {
  state: () => ({
    resources: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchResources() {
      this.loading = true;
      try {
        const res = await api.get('/resources');
        this.resources = res.data;
      } catch (err) {
        this.error = err;
      } finally {
        this.loading = false;
      }
    },
    async createResource(data) {
      try {
        const res = await api.post('/resources', data);
        this.resources.push(res.data);
      } catch (err) {
        this.error = err;
      }
    },
    async deleteResource(id) {
      try {
        await api.delete(`/resources/${id}`);
        this.resources = this.resources.filter(r => r.id !== id);
      } catch (err) {
        this.error = err;
      }
    }
  }
});