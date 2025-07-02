export interface Marca {
    id: number;
    nombre: string;
}

export interface Proveedor {
    id: number;
    nombre: string;
}

export interface Categoria {
    id: number;
    nombre: string;
}

export interface Articulo {
    id?: number;
    descripcion: string;
    precio: number;
    stock: number;
    marca: Marca;
    proveedor: Proveedor;
    categorias: Categoria[];
}
