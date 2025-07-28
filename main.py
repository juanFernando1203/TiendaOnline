# archivo: main.py

from generador_datos import generar_datos_prueba
from analisis import analizar_ordenamiento, analizar_busqueda
from algoritmos.ordenamiento import quick_sort
# 💡 Importamos las funciones de búsqueda
from algoritmos.busqueda import busqueda_binaria, busqueda_lineal_por_nombre
import copy

def mostrar_menu():
    """
    Imprime el menú principal de opciones en la consola.
    """
    print("\n--- 🛒 Menú Principal - Gestión de Tienda ---")
    print("1. Analizar rendimiento de algoritmos de Ordenamiento")
    print("2. Analizar rendimiento de algoritmos de Búsqueda (Pruebas automáticas)")
    print("3. Ver todos los productos del catálogo (con opciones de orden)")
    print("4. Buscar un producto") # ✅ Nueva opción
    print("0. Salir")
    print("-----------------------------------------------")

def ejecutar_simulacion_interactiva():
    """
    Punto de entrada que ejecuta un menú interactivo para la simulación de la tienda.
    """
    print("Cargando y generando catálogo de productos...")
    catalogo_productos = generar_datos_prueba(50)
    # Creamos una copia ordenada por ID para la búsqueda binaria
    catalogo_ordenado_id = quick_sort(copy.deepcopy(catalogo_productos), key=lambda p: p.id)
    print(f"¡Catálogo con {len(catalogo_productos)} productos listo!\n")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            analizar_ordenamiento(catalogo_productos)
        
        elif opcion == '2':
            analizar_busqueda(catalogo_productos)

        elif opcion == '3':
            # ... (El código para mostrar productos ordenados se queda igual) ...
            print("\n¿Cómo desea ordenar la lista de productos?")
            print("  1. Por calificación (de mayor a menor)")
            print("  2. Por precio (de menor a mayor)")
            print("  Cualquier otra tecla para volver al menú principal.")
            
            sub_opcion = input("  Elija una opción de ordenamiento: ")
            catalogo_a_mostrar = copy.deepcopy(catalogo_productos)
            lista_ordenada = []

            if sub_opcion == '1':
                print("\n--- Listado de Productos (ordenado por calificación) ---")
                lista_ordenada = quick_sort(catalogo_a_mostrar, key=lambda p: p.calificacion_promedio, reverse=True)
            elif sub_opcion == '2':
                print("\n--- Listado de Productos (ordenado por precio) ---")
                lista_ordenada = quick_sort(catalogo_a_mostrar, key=lambda p: p.precio, reverse=False)
            else:
                print("\nVolviendo al menú principal...")
                continue

            for producto in lista_ordenada:
                print(producto)

        elif opcion == '4':
            print("\n--- Menú de Búsqueda ---")
            print("1. Buscar por ID (exacto)")
            print("2. Buscar por nombre (contiene el texto)")
            print("Cualquier otra tecla para volver.")
            
            sub_opcion_busqueda = input("  Elija un método de búsqueda: ")

            if sub_opcion_busqueda == '1':
                try:
                    id_a_buscar = int(input("  Ingrese el ID del producto a buscar: "))
                    # Usamos el catálogo pre-ordenado por ID para la búsqueda binaria
                    resultado = busqueda_binaria(catalogo_ordenado_id, id_a_buscar)
                    print("\n--- Resultado de la Búsqueda ---")
                    if resultado:
                        print(f"✅ Producto encontrado: {resultado}")
                    else:
                        print(f"❌ No se encontró ningún producto con el ID {id_a_buscar}.")
                except ValueError:
                    print("❌ Error: Por favor, ingrese un número de ID válido.")

            elif sub_opcion_busqueda == '2':
                texto_a_buscar = input("  Ingrese el nombre o parte del nombre a buscar: ")
                # Usamos el catálogo original para la búsqueda lineal
                resultados = busqueda_lineal_por_nombre(catalogo_productos, texto_a_buscar)
                print("\n--- Resultado de la Búsqueda ---")
                if resultados:
                    print(f"✅ Se encontraron {len(resultados)} productos:")
                    for producto in resultados:
                        print(producto)
                else:
                    print(f"❌ No se encontró ningún producto que contenga '{texto_a_buscar}'.")
            
            else:
                print("\nVolviendo al menú principal...")
         
        elif opcion == '0':
            print("\nSaliendo del programa. ¡Hasta luego! 👋")
            break
        
        else:
            print("\n⚠️  Opción no válida. Por favor, elija una opción del menú.")

if __name__ == "__main__":
    ejecutar_simulacion_interactiva()