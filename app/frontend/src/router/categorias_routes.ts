const categorias_routes = [
    {
        path: '/categorias', 
        name: 'categorias_list',
<<<<<<< HEAD
        component: ()=>import('../components/categorias/CategoriasList.vue')
=======
        component: ()=>import('../views/CategoriasView.vue')
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
    },
    {
        path: '/categorias/:id/show',
        name: 'categorias_show',
        component: ()=>import('../components/categorias/CategoriasShow.vue')
    },
        {
        path: '/categorias/create',
        name: 'categorias_create',
        component: ()=>import('../components/categorias/CategoriasCreate.vue')
    },
    {
        path: '/categorias/:id/edit',
        name: 'categorias_edit',
        component: ()=>import('../components/categorias/CategoriasUpdate.vue')
    }, 
]
export default categorias_routes