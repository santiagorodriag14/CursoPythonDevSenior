# Sistema de Gestión de una Tienda de Videojuegos

Este proyecto consiste en el desarrollo de un programa en Python diseñado para administrar el inventario y las ventas de una tienda de videojuegos. El sistema permite gestionar los productos mediante una interfaz de consola basada en menús.

## Objetivo del Proyecto

El objetivo es aplicar los fundamentos de programación en Python, incluyendo:

- Variables y tipos de datos.
- Estructuras de control (condicionales y ciclos).
- Funciones con parámetros y valores de retorno.
- Estructuras de datos (diccionarios anidados y listas).
- Validación de datos de entrada.

## Estructura de Datos

La información de los productos se organiza en un diccionario donde cada clave es un código único de videojuego que contiene, a su vez, otro diccionario con sus atributos:

```python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}
```

## Funcionalidades del Menú

El sistema ofrece las siguientes operaciones a través de un menú interactivo:

1. **Agregar videojuego:** Registro de nuevos productos con validación de código único, precio positivo y cantidad positiva.
2. **Mostrar inventario:** Visualización completa de los videojuegos registrados.
3. **Buscar videojuego por código:** Consulta detallada de un producto específico.
4. **Actualizar precio:** Modificación del precio de venta para un código existente.
5. **Registrar venta:** Proceso de venta que verifica disponibilidad, actualiza el inventario y genera una factura con el total.
6. **Mostrar estadísticas:** Generación de un reporte que incluye cantidad total de productos, valor del inventario, productos destacados y promedio de precios.
7. **Eliminar videojuego:** Remoción de productos del catálogo mediante su código.
8. **Salir:** Cierre del programa.

## Requisitos Técnicos

El desarrollo exige la implementación de funciones específicas para modularizar la lógica del programa:

- `agregar_videojuego(videojuegos)`
- `mostrar_inventario(videojuegos)`
- `buscar_videojuego(videojuegos)`
- `actualizar_precio(videojuegos)`
- `registrar_venta(videojuegos)`
- `mostrar_estadisticas(videojuegos)`
- `eliminar_videojuego(videojuegos)`
- `menu()`
---

Este taller proporciona una base sólida para el manejo de datos en memoria y el flujo de control lógico en aplicaciones orientadas a la gestión de negocios pequeños.
```