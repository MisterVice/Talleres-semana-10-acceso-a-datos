"""Ejercicio 5. Reto integrador: registro de estudiantes."""

ASIGNATURAS = ("Programación", "Matemáticas", "Inglés")


def calcular_promedio(notas):
    return sum(notas) / len(notas)


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


def registrar_estudiante(asignaturas):
    nombre = input("\nNombre del estudiante: ").strip()
    notas = [pedir_nota(f"  Nota de {asig}: ") for asig in asignaturas]
    return {"nombre": nombre, "notas": notas}


def mostrar_reporte(estudiantes, asignaturas):
    promedios = []
    for est in estudiantes:
        promedio = calcular_promedio(est["notas"])
        promedios.append(round(promedio, 2))

        print(f"\nEstudiante: {est['nombre']}")
        for asig, nota in zip(asignaturas, est["notas"]):
            print(f"{asig}: {nota}")
        print(f"Promedio: {promedio:.1f}")
        print("Estado:", "Aprobado" if promedio >= 3.0 else "Reprobado")

    # Si hay empate, se muestran todos los nombres
    mejor = max(promedios)
    ganadores = [e["nombre"] for e, p in zip(estudiantes, promedios) if p == mejor]
    etiqueta = "Promedio más alto" if len(ganadores) == 1 else "Empate en el promedio más alto"
    print(f"\n{etiqueta} ({mejor:.1f}): {', '.join(ganadores)}")


def main():
    estudiantes = [registrar_estudiante(ASIGNATURAS) for _ in range(3)]
    mostrar_reporte(estudiantes, ASIGNATURAS)


if __name__ == "__main__":
    main()
