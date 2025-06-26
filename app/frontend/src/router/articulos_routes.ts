const articulos_routes = [
    {
        path: '/articulos', 
        name: 'articulos_list',
        component: ()=>import('../views/MarcasView.vue')
    },
    {
        path: '/articulos/:id/show',
        name: 'articulos_show',
        component: ()=>import('../components/articulos/ArticulosShow.vue')
    },
    {
        path: '/articulos/create',
        name: 'articulos_create',
        component: ()=>import('../components/articulos/ArticulosCreate.vue')
    },
    {
        path: '/articulos/:id/edit',
        name: 'articulos_edit',
        component: ()=>import('../components/articulos/ArticulosUpdate.vue')
    }, 
]
export default articulos_routes