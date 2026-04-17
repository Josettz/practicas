import time

def calcular_tiempo(function):

    def funcionModificada(n):
        inicio = time.time()
        function(n)
        final = time.time()
        tiempo = final - inicio 
        print(f"El tiempo de la ejecución del programa {tiempo} Segundos")

    return funcionModificada




@calcular_tiempo
def imprimir_nums(n):
    
    for i in range(n):
        print(i)

imprimir_nums(10020)



