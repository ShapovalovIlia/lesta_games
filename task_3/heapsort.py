def heap_sort(array):
    n = len(array)

    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if (l < n) and (array[i] < array[l]):
            largest = l
        if (r < n) and (array[largest] < array[r]):
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(n=n, i=largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n=n, i=i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(n=i, i=0)
