import time

def cronometrar(func_b):
    def func_c(*args, **kwargs):
        inicio = time.time()
        resultado = func_b(*args, **kwargs)
        final = time.time()
        print(f"tardo {final- inicio}")
        return resultado
    return func_c
    

@cronometrar
def contar_hasta(n):
    for i in range(n):
        pass
    print(f"Conté hasta {n}")

@cronometrar
def sumar_lista(numeros):
    print(f"Suma: {sum(numeros)}")

contar_hasta(1000000)
print("---")
sumar_lista([1, 2, 3, 4, 5])