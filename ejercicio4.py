"""Ejercicio 4. Inventario con diccionarios."""


def consultar_stock(inventario, producto):
    return inventario.get(producto)  # None si no existe


def agregar_stock(inventario, producto, cantidad):
    """Suma stock; si el producto no existe, lo crea."""
    inventario[producto] = inventario.get(producto, 0) + cantidad


def vender_producto(inventario, producto, cantidad):
    """Devuelve True si la venta se realizó, False si fue rechazada."""
    if producto not in inventario:
        print(f"  '{producto}' no existe en el inventario.")
        return False
    if cantidad > inventario[producto]:
        print(f"  Venta rechazada: solo hay {inventario[producto]} de '{producto}'.")
        return False
    inventario[producto] -= cantidad
    return True


def pedir_cantidad():
    """Pide un entero positivo hasta que sea válido."""
    while True:
        texto = input("Cantidad: ").strip()
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("  Ingresa un entero positivo (1, 2, 3...).")


def main():
    inventario = {"cuadernos": 10, "lapices": 20, "borradores": 8}

    while True:
        print("\n1. Consultar  2. Agregar stock  3. Vender  4. Ver todo  5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            producto = input("Producto: ").strip().lower()
            stock = consultar_stock(inventario, producto)
            print(f"  Stock: {stock}" if stock is not None else "  No existe.")
        elif opcion == "2":
            producto = input("Producto (nuevo o existente): ").strip().lower()
            agregar_stock(inventario, producto, pedir_cantidad())
            print(f"  {producto}: {inventario[producto]}")
        elif opcion == "3":
            producto = input("Producto: ").strip().lower()
            if vender_producto(inventario, producto, pedir_cantidad()):
                print(f"  Venta realizada. Quedan {inventario[producto]}.")
        elif opcion == "4":
            for producto, stock in inventario.items():
                print(f"  {producto}: {stock}")
        elif opcion == "5":
            break
        else:
            print("  Opción inválida.")


if __name__ == "__main__":
    # Pruebas: vender 3 -> quedan 7; vender 15 -> rechazada
    inv = {"cuadernos": 10}
    assert vender_producto(inv, "cuadernos", 3) and inv["cuadernos"] == 7
    assert not vender_producto(inv, "cuadernos", 15) and inv["cuadernos"] == 7
    main()
