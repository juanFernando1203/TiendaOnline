class Producto:
    """
    Representa un producto en el catálogo de la tienda.
    """
    def __init__(self, id, nombre, precio, categoria, stock, calificacion_promedio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.calificacion_promedio = calificacion_promedio

    def __repr__(self):
        """
        Representación en cadena de texto del objeto para facilitar la visualización.
        """
        return (f"ID: {self.id} | {self.nombre} | Precio: ${self.precio:.2f} | "
                f"Categoría: {self.categoria} | Stock: {self.stock} | "
                f"Calificación: {self.calificacion_promedio:.1f} ★")