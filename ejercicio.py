# Clase Producto: Define las propiedades de un producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

# Clase Inventario: Gestiona la lista de productos
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Agregar un producto al inventario
        self.productos.append(producto)

    def eliminar_producto(self, producto_nombre):
        # Eliminar un producto según su nombre
        self.productos = [p for p in self.productos if p.nombre != producto_nombre]

    def mostrar_inventario(self):
        # Mostrar todos los productos en el inventario
        for producto in self.productos:
            producto.mostrar_detalles()


import unittest


class TestInventario(unittest.TestCase):

    def setUp(self):
        # Inicialización antes de cada prueba
        self.inventario = Inventario()
        self.producto1 = Producto("Manzanas", 0.5, 100)
        self.producto2 = Producto("Naranjas", 0.75, 80)

    def test_agregar_producto(self):
        # Prueba para verificar que se puede agregar un producto
        self.inventario.agregar_producto(self.producto1)
        self.assertIn(self.producto1, self.inventario.productos)

    def test_eliminar_producto(self):
        # Prueba para verificar que se puede eliminar un producto
        self.inventario.agregar_producto(self.producto1)
        self.inventario.eliminar_producto("Manzanas")
        self.assertNotIn(self.producto1, self.inventario.productos)

    def test_mostrar_inventario(self):
        # Prueba para verificar que se muestra el inventario correctamente
        self.inventario.agregar_producto(self.producto1)
        self.inventario.agregar_producto(self.producto2)
        self.inventario.mostrar_inventario()


if __name__ == "__main__":
    unittest.main()
