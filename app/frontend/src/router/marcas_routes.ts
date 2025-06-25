const marcas_routes = [
    {
        path: '/marcas', 
        name: 'marcas_list',
        component: ()=>import('../views/MarcasView.vue')
    },
    {
        path: '/marcas/:id/show',
        name: 'marcas_show',
        component: ()=>import('../components/marcas/MarcasShow.vue')
    },
    {
        path: '/marcas/create',
        name: 'marcas_create',
        component: ()=>import('../components/marcas/MarcasCreate.vue')
    },
    {
        path: '/marcas/:id/edit',
        name: 'marcas_edit',
        component: ()=>import('../components/marcas/MarcasUpdate.vue')
    }, 
]
export default marcas_routes