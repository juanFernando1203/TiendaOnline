import time
import copy
import random
from faker import Faker
from algoritmos.ordenamiento import insertion_sort, merge_sort, quick_sort
from algoritmos.busqueda import busqueda_binaria, busqueda_lineal_por_nombre

fake = Faker()

def analizar_ordenamiento(catalogo_original):
    """Mide, compara y muestra los resultados de los algoritmos de ordenamiento."""
    print("\n--- 2. Analizando Algoritmos de Ordenamiento ---")
    algoritmos = {"Insertion Sort": insertion_sort, "Merge Sort": merge_sort, "Quick Sort": quick_sort}
    criterios = {
        "Precio (ascendente)": {"key": lambda p: p.precio, "reverse": False},
        "Calificación (descendente)": {"key": lambda p: p.calificacion_promedio, "reverse": True}
    }
    
    resultados = []
    for nombre_alg, func_alg in algoritmos.items():
        for nombre_crit, crit_params in criterios.items():
            catalogo_a_ordenar = copy.deepcopy(catalogo_original)
            start_time = time.perf_counter()
            func_alg(catalogo_a_ordenar, **crit_params)
            end_time = time.perf_counter()
            duracion = (end_time - start_time) * 1000
            resultados.append((nombre_alg, nombre_crit, duracion))

    print("\nTabla de Tiempos de Ejecución (en milisegundos):")
    print(f"{'Algoritmo':<20} | {'Criterio de Ordenamiento':<30} | {'Tiempo (ms)':<15}")
    print("-" * 70)
    for res in resultados:
        print(f"{res[0]:<20} | {res[1]:<30} | {res[2]:<15.5f}")
    
    print("\nAnálisis de Rendimiento:")


def analizar_busqueda(catalogo_original):
    """Mide, compara y muestra los resultados de los algoritmos de búsqueda."""
    print("\n--- 3. Analizando Algoritmos de Búsqueda ---")

    # Búsqueda Binaria
    print("\n--- Búsqueda Binaria por ID ---")
    catalogo_ordenado_id = quick_sort(copy.deepcopy(catalogo_original), key=lambda p: p.id)
    ids_existentes = [random.randint(1, 50) for _ in range(10)]
    ids_inexistentes = [random.randint(100, 200) for _ in range(10)]
    
    start_time = time.perf_counter()
    for id_b in ids_existentes + ids_inexistentes:
        busqueda_binaria(catalogo_ordenado_id, id_b)
    end_time = time.perf_counter()
    print(f"Tiempo total para 20 búsquedas binarias: {(end_time - start_time) * 1000:.5f} ms")
    print("La búsqueda binaria es ideal para claves únicas en datos ordenados (O(log n)).")

    # Búsqueda Lineal
    print("\n--- Búsqueda Lineal por Nombre ---")
    nombres_existentes = [p.nombre[:3] for p in random.sample(catalogo_original, 10)]
    nombres_inexistentes = [fake.color_name() for _ in range(10)]
    
    start_time = time.perf_counter()
    for nombre in nombres_existentes + nombres_inexistentes:
        busqueda_lineal_por_nombre(catalogo_original, nombre)
    end_time = time.perf_counter()
    print(f"Tiempo total para 20 búsquedas lineales: {(end_time - start_time) * 1000:.5f} ms")
