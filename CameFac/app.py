from flask import Flask, render_template, request
from decimal import Decimal
app = Flask(__name__)
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
        return {
            "nombre": self.producto.nombre,
            "precio": f"${self.producto.precio_unitario:,.2f}",
            "cantidad": self.cantidad,
            "subtotal": f"${subtotal:,.2f}"
        }
class Factura:
    def __init__(self):
        self.items = []
    def agregar_item(self, item):
        self.items.append(item)
    def calcular_total(self):
        return sum(item.obtener_subtotal() for item in self.items)
    def mostrar_items(self):
        return [item.mostrar_info() for item in self.items]
catalogo = [
    Producto("Hm. Elvis Presley's", 28900),
    Producto("Hm. Marilyn Monroe's", 31900),
    Producto("Hm. Play boy", 32900),
    Producto("Hm. The Beatles", 33900),
    Producto("Coca-Cola 350 ml", 5200),
    Producto("Pepsi 350 ml", 4800),
    Producto("Jugo en agua", 6500),
    Producto("Jugo en leche", 8000),
]
@app.route("/", methods=["GET", "POST"])
def index():
    factura = Factura()
    mensaje = None
    if request.method == "POST":
        for i in range(len(catalogo)):
            cantidad_str = request.form.get(f"producto_{i}")
            if cantidad_str and cantidad_str.isdigit():
                cantidad = int(cantidad_str)
                if cantidad > 0:
                    factura.agregar_item(ItemFactura(catalogo[i], cantidad))
        if not factura.items:
            mensaje = "Por favor, selecciona al menos un producto."
        else:
            items = factura.mostrar_items()
            total = f"${factura.calcular_total():,.2f}"
            return render_template("index.html", catalogo=catalogo, items=items, total=total)
    return render_template("index.html", catalogo=catalogo, mensaje=mensaje)
if __name__ == "__main__":
    app.run(debug=True)
