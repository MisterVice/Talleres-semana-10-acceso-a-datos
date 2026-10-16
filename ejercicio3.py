"""Ejercicio 3. Catálogo de productos con tuplas."""


def mostrar_productos(productos):
    print("\nCatálogo:")
    for codigo, nombre, precio in productos:  # desempaquetado
        print(f"  {codigo} - {nombre}: ${precio}")


def buscar_producto(productos, codigo):
    """Devuelve la tupla del producto o None si no existe."""
    for producto in productos:
        cod, _, _ = producto
        if cod == codigo.upper():
            return producto
    return None


def main():
    productos = [
        ("P01", "Teclado", 45000),
        ("P02", "Mouse", 25000),
        ("P03", "Memoria USB", 30000),
    ]
    mostrar_productos(productos)

    codigo = input("\nCódigo a buscar: ").strip()
    producto = buscar_producto(productos, codigo)
    if producto:
        _, nombre, precio = producto
        print(f"Encontrado: {nombre} - ${precio}")
    else:
        print(f"No existe un producto con el código '{codigo}'.")


if __name__ == "__main__":
    # Prueba: P02 -> Mouse, 25000
    assert buscar_producto([("P02", "Mouse", 25000)], "P02") == ("P02", "Mouse", 25000)
    main()
