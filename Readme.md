# Aurelion

### 1. Tema

Optimización del inventario mediante análisis de productos más vendidos.

### 2. Definición del Problema ✒️

La tienda quiere saber cuáles son los productos más vendidos para optimizar su estrategia de ventas, lo que incluye mejorar la gestión de inventarios y el diseño de la tienda.

* ¿Quiénes son los principales usuarios del producto?

Los usuarios son los representantes de la tienda Aurelión quienes necesitan determinar cuáles son los productos mas vendidos, a fin de mantener el abastecimiento de los mismos.

* ¿Cuáles son los objetivos de estos usuarios en relación con el producto?

Los usuarios desean tener información útil, precisa y rápida.

### 3. Solución 🎯

* Desarrollar un algoritmo que permita predecir la cantidad de productos vendidos por periodo para optimizar el abastecimiento.

[![premium-photo-1682088309871-3cfc6f00f594.avif](https://i.postimg.cc/3w9H3XFT/premium-photo-1682088309871-3cfc6f00f594.avif)](https://postimg.cc/jWW1XJ1g)

### 4. Tecnologias 🛠️

 Trabajamos este proyecto haciendo uso de :

 * Python
 * Panda
   
### 5. Database

1. Clientes:
    * id_clinte: int
    * nombre_cliente: string
    * email: string
    * ciudad: string
    * fecha_alta: date

2.  Ventas:
    * id_venta: int
    * fecha: date
    * id_cliente: int
    * nombre_cliente: string
    * email: stirng
    * medio_pago: string

3. Productos:
    * id_producto: int
    * nombre_producto: string
    * categoria: string
    * precio_unitario: int

4.  Detalle_ventas:
    * id_venta: int
    * id_producto: int
    * nombre_producto: string
    * cantidad: int
    * precio_unitario: int
    * importe: int

### 6. Copilot:
Quiero crear una función en Python que muestre un menú interactivo, utilizando los datasets para obtener las ventas más altas por cliente o por producto.


