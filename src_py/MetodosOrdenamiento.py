class MetodosOrdenamiento:
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def burbujamejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(n - 1, i, -1):
                if arreglo[j] < arreglo[j - 1]:
                    arreglo[j], arreglo[j - 1] = arreglo[j - 1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo

    def seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            menor = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[menor]:
                    menor = j
            arreglo[i], arreglo[menor] = arreglo[menor], arreglo[i]
        return arreglo

    def shell_sort(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
