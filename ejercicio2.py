"""Ejercicio 2. Registro de notas con listas."""


def calcular_promedio(notas):
    return sum(notas) / len(notas)


def obtener_mayor(notas):
    return max(notas)


def obtener_menor(notas):
    return min(notas)


def pedir_nota(mensaje):
    """Pide una nota hasta que sea un número entre 0.0 y 5.0."""
    while True:
        try:
            nota = float(input(mensaje))
        except ValueError:
            print("  Escribe un número (ej. 3.5).")
            continue
        if 0.0 <= nota <= 5.0:
            return nota
        print("  La nota debe estar entre 0.0 y 5.0.")


def main():
    notas = [pedir_nota(f"Nota {i}: ") for i in range(1, 6)]
    promedio = calcular_promedio(notas)

    print(f"\nNotas: {notas}")
    print(f"Promedio: {promedio:.1f}")
    print(f"Nota mayor: {obtener_mayor(notas)}")
    print(f"Nota menor: {obtener_menor(notas)}")
    print("Estado:", "Aprobado" if promedio >= 3.0 else "Reprobado")


if __name__ == "__main__":
    # Prueba: [4.0, 3.5, 2.5, 5.0, 3.0] -> promedio 3.6
    assert round(calcular_promedio([4.0, 3.5, 2.5, 5.0, 3.0]), 1) == 3.6
    main()
