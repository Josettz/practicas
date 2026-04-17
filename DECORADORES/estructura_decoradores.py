#a(b) --> c

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs): 
        
        print("antes de la ejecución")
        resultado = funcion_b(*args, **kwargs)
        print("dsp de la ejecución")

        return resultado

    return funcion_c

# @funcion_a
# def saludar():
#     print("hola, saludando desde una función")

# saludar()

@funcion_a
def suma(n1,n2):
    return n1 + n2


print(suma(1,2))

