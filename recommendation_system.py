"""Recomienda productos según la categoría y el presupuesto del usuario."""


# Catálogo de ejemplo con productos de distintas categorías y precios.
PRODUCTOS = [
    {"nombre": "Auriculares inalámbricos", "categoria": "tecnología", "precio": 49.99},
    {"nombre": "Teclado mecánico", "categoria": "tecnología", "precio": 79.99},
    {"nombre": "Altavoz Bluetooth", "categoria": "tecnología", "precio": 39.99},
    {"nombre": "Mochila urbana", "categoria": "accesorios", "precio": 34.99},
    {"nombre": "Botella térmica", "categoria": "accesorios", "precio": 19.99},
    {"nombre": "Lámpara de escritorio", "categoria": "hogar", "precio": 29.99},
    {"nombre": "Cafetera italiana", "categoria": "hogar", "precio": 24.99},
    {"nombre": "Zapatillas deportivas", "categoria": "deporte", "precio": 64.99},
]


def solicitar_categoria():
    """Solicita una categoría válida o permite elegir cualquiera."""
    categorias = sorted({producto["categoria"] for producto in PRODUCTOS})
    print("Categorías disponibles: " + ", ".join(categorias))
    print("Escribe 'cualquiera' si no tienes preferencia de categoría.")

    while True:
        categoria = input("¿Qué categoría prefieres? ").strip().lower()
        if categoria == "cualquiera" or categoria in categorias:
            return categoria
        print("Categoría no válida. Elige una de las opciones disponibles.")


def solicitar_presupuesto():
    """Solicita un presupuesto positivo y vuelve a preguntar si no es válido."""
    while True:
        try:
            presupuesto = float(input("¿Cuál es tu presupuesto máximo? $"))
        except ValueError:
            print("Ingresa una cantidad numérica válida.")
            continue

        if presupuesto > 0:
            return presupuesto
        print("El presupuesto debe ser mayor que cero.")


def calcular_similitud(producto, categoria, presupuesto):
    """Puntúa coincidencias de categoría y si el precio cabe en el presupuesto."""
    puntuacion = 0.0
    if categoria == "cualquiera" or producto["categoria"] == categoria:
        puntuacion += 1.0

    # Los productos dentro del presupuesto reciben un punto; los más caros
    # pierden puntuación proporcionalmente al exceso.
    exceso = max(0.0, producto["precio"] - presupuesto)
    puntuacion += max(0.0, 1.0 - exceso / presupuesto)
    return puntuacion


def recomendar_productos(categoria, presupuesto):
    """Devuelve hasta los tres productos con mayor similitud."""
    return sorted(
        PRODUCTOS,
        key=lambda producto: (
            calcular_similitud(producto, categoria, presupuesto),
            -producto["precio"],
        ),
        reverse=True,
    )[:3]


def main():
    """Ejecuta el flujo interactivo de recomendación desde la terminal."""
    print("=== Sistema de recomendación de productos ===")
    categoria = solicitar_categoria()
    presupuesto = solicitar_presupuesto()

    recomendaciones = recomendar_productos(categoria, presupuesto)
    print("\nTus tres recomendaciones:")
    for posicion, producto in enumerate(recomendaciones, start=1):
        print(
            f"{posicion}. {producto['nombre']} "
            f"({producto['categoria']}) - ${producto['precio']:.2f}"
        )


if __name__ == "__main__":
    main()