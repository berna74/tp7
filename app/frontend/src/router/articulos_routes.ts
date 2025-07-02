const articulos_routes = [
    {
        path: '/articulos', 
        name: 'articulos_list',
<<<<<<< HEAD
        component: ()=>import('../components/articulos/ArticulosList.vue')
=======
        component: ()=>import('../views/ArticulosView.vue')
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
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