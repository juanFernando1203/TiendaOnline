def busqueda_binaria(arr, target_id):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].id == target_id: return arr[mid]
        elif arr[mid].id < target_id: low = mid + 1
        else: high = mid - 1
    return None

def busqueda_lineal_por_nombre(arr, subcadena):
    subcadena_lower = subcadena.lower()
    return [p for p in arr if subcadena_lower in p.nombre.lower()]