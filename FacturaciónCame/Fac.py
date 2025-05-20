class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio_unitario:,.2f} COP"
class ItemFactura:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    def obtener_subtotal(self):
        return self.producto.precio_unitario * self.cantidad
    def mostrar_info(self):
        subtotal = self.obtener_subtotal()
        return (
            f"Producto: {self.producto.nombre}\n"
            f"Precio unitario: ${self.producto.precio_unitario:,.2f} COP\n"
            f"Cantidad: {self.cantidad}\n"
            f"Subtotal: ${subtotal:,.2f} COP\n"
            f"{'-'*30}"
        )
class Factura:
    def __init__(self):
        self.items = []
    def agregar_item(self, item):
        self.items.append(item)
    def mostrar_detalle(self):
        print("\n🧾 Factura:\n")
        for item in self.items:
            print(item.mostrar_info())
    def calcular_total(self):
        return sum(item.obtener_subtotal() for item in self.items)
    def mostrar_total(self):
        print(f"\n💰 Total a pagar: ${self.calcular_total():,.2f} COP")
def mostrar_catalogo(productos):
    print("\n Productos disponibles:")
    for i, prod in enumerate(productos):
        print(f"{i + 1}. {prod.mostrar_info()}")
def solicitar_entero(mensaje, minimo=1, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo or (maximo and valor > maximo):
                raise ValueError
            return valor
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.")
def main():
    catalogo = [
        Producto("Hm. Elvis Presley's ", 28900),
        Producto("Hm. Marilyn Monre's", 31900),
        Producto("Hm. Play boy", 32900),
        Producto("Hm. The beatles", 33900),
        Producto("Coca-Cola 350 ml", 5200),
        Producto("Pepsi 350 ml", 4800),
        Producto("Jugo en agua ", 6500),
        Producto("Jugo en leche", 8000)
    ]
    factura = Factura()
    print("Bienvenido al restaurante de Hamburguesas clasic\n")
    while True:
        mostrar_catalogo(catalogo)
        opcion = solicitar_entero("\nSeleccione el número del producto que desea comprar: ", 1, len(catalogo))
        producto = catalogo[opcion - 1]
        cantidad = solicitar_entero(f"Ingrese la cantidad de '{producto.nombre}' que desea: ", 1)
        factura.agregar_item(ItemFactura(producto, cantidad))
        print("\n¿Desea agregar otro producto o finalizar?")
        print("1. Agregar otro producto")
        print("2. Finalizar")
        siguiente = solicitar_entero("Seleccione una opción (1 o 2): ", 1, 2)
        if siguiente == 2:
            break
    factura.mostrar_detalle()
    factura.mostrar_total()
if __name__ == "__main__":
    main()
