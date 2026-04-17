
def decorador(funcion):
    def funcion_modificada():
        print("hola, antes de modificar")

        funcion()
        print("hola despues de modficar")
    return funcion_modificada()

#def saludo():
#print("hola elian ")
#saludo_modificado = decorador(saludo)
#saludo_modificado()

@decorador
def saludo():
    print("hola como estas eli")