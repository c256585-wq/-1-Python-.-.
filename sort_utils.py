def shell_sort(data, compare):
    """Сортировка методом Шелла с уменьшающимся шагом."""
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and compare(data[j - gap], temp):
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2