const proveedores_routes = [
    {
        path: '/proveedores', 
        name: 'proveedores_list',
<<<<<<< HEAD
        component: ()=>import('../components/proveedores/ProveedoresList.vue')
=======
        component: ()=>import('../views/ProveedoresView.vue')
>>>>>>> 44655ba784151407743993c5d33dcd7f4d2e6ccb
    },
    {
        path: '/proveedores/:id/show',
        name: 'proveedores_show',
        component: ()=>import('../components/proveedores/ProveedoresShow.vue')
    },
    {
        path: '/proveedores/create',
        name: 'proveedores_create',
        component: ()=>import('../components/proveedores/ProveedoresCreate.vue')
    },
    {
        path: '/proveedores/:id/edit',
        name: 'proveedores_edit',
        component: ()=>import('../components/proveedores/ProveedoresUpdate.vue')
    }, 
]
export default proveedores_routes