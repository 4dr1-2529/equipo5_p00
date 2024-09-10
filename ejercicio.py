
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")



class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):

        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al inventario.")

    def eliminar_producto(self, producto_nombre, cantidad_a_eliminar):

        for producto in self.productos:
            if producto.nombre == producto_nombre:
                if producto.cantidad > cantidad_a_eliminar:

                    producto.cantidad -= cantidad_a_eliminar
                    print(f"Se eliminaron {cantidad_a_eliminar} unidades de {producto.nombre}.")
                elif producto.cantidad == cantidad_a_eliminar:
                    self.productos.remove(producto)
                    print(f"Se eliminó completamente el producto {producto.nombre}.")
                else:
                    print(f"No hay suficientes unidades de {producto.nombre}. Cantidad disponible: {producto.cantidad}")
                return
        print(f"Producto {producto_nombre} no encontrado en el inventario.")
    def mostrar_inventario(self):

        if len(self.productos) == 0:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for producto in self.productos:
                producto.mostrar_detalles()


def gestionar_inventario():
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            nuevo_producto = Producto(nombre, precio, cantidad)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            cantidad = int(input(f"Ingrese la cantidad de {nombre} a eliminar: "))
            inventario.eliminar_producto(nombre, cantidad)

        elif opcion == "3":
            inventario.mostrar_inventario()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


gestionar_inventario()
