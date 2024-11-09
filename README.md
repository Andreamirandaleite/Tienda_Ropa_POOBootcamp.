# Tienda_Ropa_POOBootcamp.
Este proyecto es un sistema de compras de ropa utilizando la programación orientada a objetos (POO). El sistema permite gestionar productos, categorías de productos, un carrito de compras y realizar una compra en una tienda. Además, los productos se cargan desde un archivo de texto.

Estructura del Proyecto
Clases
Producto: Representa un producto en la tienda. Incluye atributos como el nombre, el precio y la cantidad disponible. También tiene métodos para reducir la cantidad del producto y mostrar la información del mismo.

Categoria: Permite organizar productos en categorías (por ejemplo, "Ropa de Hombre" y "Ropa de Mujer"). Cada categoría contiene una lista de productos.

Tienda: Gestiona el inventario de productos y el carrito de compras. Permite agregar productos al carrito, mostrar los productos en el carrito, y procesar la compra.

Función leer_productos()
Esta función lee los productos desde un archivo de texto y los carga en el sistema. El archivo debe tener los productos en formato tabulado (nombre, precio, cantidad).

Instalación
Clona este repositorio:

git clone <URL del repositorio>
Asegúrate de tener Python instalado en tu sistema.

Coloca el archivo de texto con los productos (por defecto, se espera que esté en la ruta C:/Users/andre/OneDrive/Desktop/BOOTCAMP/Sistema de Compras de Ropas con POO/lista de articulos.txt).

Si deseas modificar la ruta del archivo, ajusta la variable nombre_archivo en el código.

Uso
Ejecuta el script en Python:

python nombre_del_script.py
El sistema mostrará los productos organizados en categorías y simulará una compra, mostrando el carrito de compras y el total a pagar.

Funcionalidades
Cargar productos desde archivo: Los productos se leen desde un archivo de texto y se agregan al inventario de la tienda.
Agregar productos al carrito: Se pueden agregar productos disponibles al carrito de compras.
Mostrar carrito y procesar compra: Se muestra el carrito con los productos seleccionados y el total a pagar. Luego, el carrito se limpia tras la compra.
Contribuciones
Si deseas contribuir al proyecto:

Haz un fork de este repositorio.
Crea tu rama con git checkout -b nombre-de-tu-rama.
Realiza los cambios y haz un commit con git commit -m 'Descripción de los cambios'.
Haz push a tu rama con git push origin nombre-de-tu-rama.
Abre un pull request.
Licencia
Este proyecto está bajo la Licencia MIT.

