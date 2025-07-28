def insertion_sort(arr, key, reverse=False):
    # ... (código idéntico al de la respuesta anterior)
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and (key(arr[j]) > key(key_item) if not reverse else key(arr[j]) < key(key_item)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def merge_sort(arr, key, reverse=False):
    # ... (código idéntico al de la respuesta anterior)
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L, key, reverse)
        merge_sort(R, key, reverse)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if (key(L[i]) < key(R[j])) if not reverse else (key(L[i]) > key(R[j])):
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1
    return arr

def quick_sort(arr, key, reverse=False):
    # ... (código idéntico al de la respuesta anterior)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    if not reverse:
        left = [x for x in arr if key(x) < key(pivot)]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) > key(pivot)]
    else:
        left = [x for x in arr if key(x) > key(pivot)]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) < key(pivot)]
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)