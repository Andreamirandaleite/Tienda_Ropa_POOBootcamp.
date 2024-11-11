# Clase Producto (base)
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.__cantidad = int(cantidad)  # Atributo privado

    def get_cantidad(self):
        return self.__cantidad

    def reducir_cantidad(self):
        if self.__cantidad > 0:
            self.__cantidad -= 1
        else:
            print(f"¡No hay más stock de {self.nombre}!")

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.__cantidad}")


# Subclases de Producto para diferentes tipos de productos, aplicando herencia y polimorfismo
class ProductoRopaHombre(Producto):
    def mostrar_info(self):
        # Polimorfismo: redefinir mostrar_info para incluir el tipo específico
        print(f"[Ropa de Hombre] Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.get_cantidad()}")


class ProductoRopaMujer(Producto):
    def mostrar_info(self):
        # Polimorfismo: redefinir mostrar_info para incluir el tipo específico
        print(f"[Ropa de Mujer] Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.get_cantidad()}")


# Clase Categoria (para organizar productos por tipo)
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\n--- Categoría: {self.nombre} ---")
        for producto in self.productos:
            producto.mostrar_info()


# Clase Tienda (gestiona el inventario y el carrito de compras)
class Tienda:
    def __init__(self):
        self.inventario = []  # Lista de productos en el inventario
        self.carrito = []  # Lista de productos en el carrito

    def agregar_al_carrito(self, producto):
        if producto.get_cantidad() > 0:
            self.carrito.append(producto)
            producto.reducir_cantidad()
            print(f"Agregado {producto.nombre} al carrito.")
        else:
            print(f"{producto.nombre} está agotado.")

    def mostrar_carrito(self):
        print("\n--- Carrito de compras ---")
        total = 0
        for producto in self.carrito:
            producto.mostrar_info()
            total += producto.precio
        print(f"Total a pagar: ${total}")

    def procesar_compra(self):
        print("\n--- Procesando compra ---")
        self.mostrar_carrito()
        self.carrito.clear()  # Limpia el carrito después de la compra


# Función para leer productos desde el archivo de texto y crear instancias de sus clases específicas
def leer_productos(archivo):
    productos = []
    try:
        with open(archivo, 'r') as file:
            next(file)  # Saltar la primera línea de encabezados
            for linea in file:
                datos = linea.strip().split('\t')
                if len(datos) == 3:  # nombre, precio, cantidad
                    nombre, precio, cantidad = datos
                    if "Hombre" in nombre:
                        producto = ProductoRopaHombre(nombre, precio, cantidad)
                    elif "Mujer" in nombre:
                        producto = ProductoRopaMujer(nombre, precio, cantidad)
                    else:
                        producto = Producto(nombre, precio, cantidad)
                    productos.append(producto)
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    return productos


# Ruta local del archivo
nombre_archivo = 'C:/Users/andre/OneDrive/Desktop/BOOTCAMP/Sistema de Compras de Ropas con POO/lista de articulos.txt'

# Crear la tienda y agregar productos desde el archivo
tienda = Tienda()
productos = leer_productos(nombre_archivo)

# Verificar si se cargaron productos correctamente
if not productos:
    print("No se cargaron productos desde el archivo.")
else:
    # Crear categorías y agregar productos a la tienda
    categoria_ropa_hombre = Categoria("Ropa de Hombre")
    categoria_ropa_mujer = Categoria("Ropa de Mujer")
    for producto in productos:
        if isinstance(producto, ProductoRopaHombre):
            categoria_ropa_hombre.agregar_producto(producto)
        elif isinstance(producto, ProductoRopaMujer):
            categoria_ropa_mujer.agregar_producto(producto)
        tienda.inventario.append(producto)  # Agregar al inventario general

    # Mostrar inventario y realizar una compra
    print("Bienvenido a la tienda de ropa!")
    categoria_ropa_hombre.mostrar_productos()
    categoria_ropa_mujer.mostrar_productos()

    # Simulación de compra
    if len(productos) > 0:
        tienda.agregar_al_carrito(productos[0])  # Agregar el primer producto al carrito
    if len(productos) > 3:
        tienda.agregar_al_carrito(productos[3])  # Agregar otro producto al carrito

    tienda.mostrar_carrito()
    tienda.procesar_compra()
