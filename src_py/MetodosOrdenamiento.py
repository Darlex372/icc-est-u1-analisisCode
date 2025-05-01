import random
import time


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
            for j in range(i+1, n):
                if arreglo[j] > arreglo[j]:
                    arreglo[j], arreglo[j] = arreglo[j], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo
    def seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            menor = i
            for j in range(i+1, n):
                if arreglo[j] < arreglo[menor]:
                    menor = j
            arreglo[i],arreglo