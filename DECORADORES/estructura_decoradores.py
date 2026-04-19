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


print(suma(n1=2,n2=3))

def suma(*args,):
    return args

print(suma(3,4,5,5,5,5,5,"hola"))