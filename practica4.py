from typing import Any, Dict, List


class StockException(Exception):
    pass


class Producto:

    def __init__ (
        self, nombre: str, costo_unitario: float, stock: int
    ) -> None:
        self.nombre = nombre
        self.costo_unitario = costo_unitario
        self.stock = stock

    def __str__ (self) -> str:
        return f"{self.nombre}: {self.stock} en stock a un precio de {self.costo_unitario}"

    def actualizar_costo_unitario(self, costo_unitario: float):
        self.costo_unitario = costo_unitario
        
    def decrementar_stock(self, cantidad: int) -> None:
        if self.stock < cantidad:
            raise StockException("No existe el stock solicitado")

        self.stock -= cantidad

    @classmethod
    def obtener_productos_apartir_de_data_dict(cls, data: List[Any]):
        productos = [
            Producto(
                nombre=p["nombre"],
                costo_unitario=p["costo_unitario"],
                stock=p["stock"]
            ) for p in data
        ]
        return productos

class CarritoCompras:
    iva_porcentaje = 15

    def __init__(self, productos_db: list) -> None:
        self.productos_db = productos_db
        self.subtotal = 0
        self.impuestos = 0
        self.total = 0
        self.items = []
        self.status = "en_proceso"

    def __str__(self) -> str:
        return str(self.checkout())


    def get_producto_by_nombre(self, nombre: str) -> Producto:
        productos = [
            producto for producto in self.productos_db \
                if producto.nombre == nombre
        ]
        if not productos:
            raise Exception("producto no encontrado")
            
        return productos[0]


    def agregar_item(
        self, producto: Producto, cantidad: int
    ) -> bool:
        producto = self.get_producto_by_nombre(nombre=producto.nombre)
        try:
            producto.decrementar_stock(cantidad=cantidad)
            self.items.append({"producto": producto, "cantidad": cantidad})
            return True
        except StockException as e:
            print("Error al agregar el producto al carrito :c")
            return False

    def get_numero_productos(self):
        return len(self.items)

    def checkout(self) -> dict:
        self.subtotal = 0
        for item in self.items:
            self.subtotal += item["producto"].costo_unitario * item["cantidad"]
        
        self.impuestos = (self.subtotal * self.iva_porcentaje) / 100
        self.total = self.subtotal + self.impuestos
        return {
            "subtotal": self.subtotal,
            "impuestos": self.impuestos,
            "total": self.total,
            "numero_productos": self.get_numero_productos()
        }

    def pagar(self) -> None:
        self.status = "pagado"


# ejecucion de nuestro programa

productos = [
    {
        "nombre": "Computadora tech",
        "stock": 3,
        "costo_unitario": 4321
    },
    {
        "nombre": "Monitor 17 pulgadas",
        "stock": 2,
        "costo_unitario": 1490
    },
    {
        "nombre": "Teclado tech",
        "stock": 20,
        "costo_unitario": 200
    }
]


productos = Producto.obtener_productos_apartir_de_data_dict(data=productos)
carrito = CarritoCompras(productos_db=productos)
print(f"Este en nuestro carrito vacio: {carrito}")
print(f"Intentamo gregar 20 teclados al carrito")
producto_teclado = carrito.get_producto_by_nombre(nombre="Teclado tech")
print(f"Estock del teclado: {producto_teclado}")
success = carrito.agregar_item(producto=producto_teclado, cantidad=20)
assert success, "Tu programa debe dar True aqui"
msg = "teclado agregado exitosamente" if success else "Error al agregar al carrito los teclados"
print(msg)
print("agregando otro teclado al carrito")
success = carrito.agregar_item(producto=producto_teclado, cantidad=1)
assert not success, "Tu programa debe dar False aqui"
info = carrito.checkout()
print(f"El resumen del carrito es {info}")
assert int(info["total"]) == 4600, "El total debe ser 4600, validar el resultado."