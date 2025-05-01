import random
import time
from src_py.MetodosOrdenamiento import MetodosOrdenamiento


class BenchMarking:
    def __init__(self):
        print("Benchmarking class initialized")
        self.mO = MetodosOrdenamiento()

        arreglo = self.build_arreglo(5000)

        tarea = lambda: self.mO.sort_bubble(arreglo)

        tiempoM = self.contar_con_current_time_milles(tarea)
        tiempoN = self.contar_con_nano_time(tarea)

        print(f"Tiempo con currentTimeMillis (ns): {tiempoM}")
        print(f"Tiempo con nanosegundos B: {tiempoN}")

        tarea_mejorada = lambda: self.mO.burbujamejorado(arreglo)
        tiempoN_mejorada = self.contar_con_nano_time(tarea_mejorada)
        print(f"Tiempo en nanosegundos BM {tiempoN_mejorada:.0f} ns")
        
        tarea_seleccion = lambda: self.mO.seleccion(arreglo)
        tiempoN_seleccion = self.contar_con_nano_time(tarea_seleccion)
        print(f"Tiempo en nanosegundos SEL: {tiempoN_seleccion:.0f} ns")

    def build_arreglo(self, tamano):
        return [random.randint(0, 99999) for _ in range(tamano)]

    def contar_con_current_time_milles(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return fin - inicio

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) * 1_000_000_000.0
