def registrar(func_b):
    def func_c(*args, **kwargs):
        print(f"Ejecutando: {func_b.__name__}")
        resultado = func_b(*args, **kwargs)
        print(f"Terminó: {func_b.__name__}")
        return resultado
    return func_c
        

@registrar
def saludar(nombre):
    print(f"Hola, {nombre}!")

@registrar
def sumar(a, b):
    print(f"Resultado: {a + b}")

@registrar
def despedir(nombre):
    print(f"Adiós, {nombre}!")