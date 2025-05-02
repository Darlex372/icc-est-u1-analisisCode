import time
import random

class BenchMarking:
    def __init__(self):
        print("Benchmarking class initialized")

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    def build_arreglo(self, tamano):
        return [random.randint(0, 99999) for _ in range(tamano)]
