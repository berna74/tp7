export interface Articulo{
     id?:number,
     descripcion:string,
     precio:number,
     stock:number,
     marca_id?:number,
     proveedor_id?:number,
     categoria?: string,
}

