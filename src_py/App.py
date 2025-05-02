import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src_py.MetodosOrdenamiento import MetodosOrdenamiento
from src_py.benchmarking import BenchMarking

if __name__ == "__main__":
    print("funciona")
    bench = BenchMarking()
    metodosO = MetodosOrdenamiento()

    tamanios = [5000, 10000, 15000]

    metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "seleccion": metodosO.seleccion,
        "burbuja_mejorado": metodosO.burbujamejorado,
        "shell": metodosO.shell_sort
    }

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        resultados = []

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, método: {nombre}, tiempo: {tiempo:.6f} segundos")
