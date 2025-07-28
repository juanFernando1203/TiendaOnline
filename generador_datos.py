import random
from faker import Faker
from producto import Producto

# Inicializar Faker para generar datos de prueba realistas
fake = Faker('es_ES')

# Diccionario con palabras clave por categoría
nombres_por_categoria = {
    "Electrónica": {
        "sustantivos": ["Teléfono", "Laptop", "Auriculares", "Teclado", "Monitor", "Smartwatch"],
        "adjetivos": ["Inteligente", "Inalámbrico", "Gaming", "Portátil", "4K", "LED"]
    },
    "Ropa": {
        "sustantivos": ["Camisa", "Pantalón", "Vestido", "Chaqueta", "Gorra", "Zapatos"],
        "adjetivos": ["de Algodón", "de Lino", "Slim Fit", "deportivo", "elegante", "de Cuero"]
    },
    "Libros": {
        "generos": ["La Crónica", "El Secreto", "El Viaje", "La Sombra", "El Código"],
        "sujetos": ["del Alquimista", "del Tiempo", "de las Estrellas", "del Olvido", "del Rey"]
    },
    "Hogar": {
        "sustantivos": ["Lámpara", "Sofá", "Mesa de centro", "Estantería", "Alfombra", "Jarrón"],
        "adjetivos": ["moderna", "rústico", "minimalista", "de madera", "elegante", "geométrica"]
    },
    "Deportes": {
        "sustantivos": ["Balón", "Raqueta", "Botella", "Mancuerna", "Esterilla de yoga", "Bicicleta"],
        "adjetivos": ["profesional", "de alta resistencia", "ergonómica", "antideslizante", "de montaña"]
    },
    "Juguetes": {
        "sustantivos": ["Cubo", "Muñeca", "Coche de carreras", "Set de construcción", "Rompecabezas"],
        "adjetivos": ["mágico", "articulada", "a control remoto", "educativo", "de 1000 piezas"]
    }
}


def generar_datos_prueba(cantidad=50):
    """
    Genera una lista de productos con datos aleatorios y nombres coherentes por categoría.
    """
    productos = []
    # Usamos las claves del diccionario como la lista de categorías
    categorias = list(nombres_por_categoria.keys())
    
    for i in range(1, cantidad + 1):
        # 1. Elegimos una categoría primero
        categoria_elegida = random.choice(categorias)
        
        # 2. Generamos un nombre basado en esa categoría
        nombre_producto = ""
        datos_categoria = nombres_por_categoria[categoria_elegida]

        if categoria_elegida == "Libros":
            # Caso especial para libros para crear títulos más realistas
            titulo = f"{random.choice(datos_categoria['generos'])} {random.choice(datos_categoria['sujetos'])}"
            nombre_producto = f'"{titulo}" de {fake.name()}'
        else:
            # Para el resto de categorías, combinamos sustantivo y adjetivo
            sustantivo = random.choice(datos_categoria['sustantivos'])
            adjetivo = random.choice(datos_categoria['adjetivos'])
            nombre_producto = f"{sustantivo} {adjetivo}"

        # 3. Creamos el objeto Producto
        producto = Producto(
            id=i,
            nombre=nombre_producto,
            precio=round(random.uniform(5.0, 500.0), 2),
            categoria=categoria_elegida,
            stock=random.randint(0, 100),
            calificacion_promedio=round(random.uniform(1.0, 5.0), 1)
        )
        productos.append(producto)
    return productos