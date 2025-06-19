const categorias_routes = [
    {
        path: '/categorias', 
        name: 'categorias_list',
        component: ()=>import('../views/CategoriasView.vue')
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