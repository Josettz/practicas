def validar_positivos(func_b):
    def func_c(*args, **kwargs):


        if all(a > 0 for a in args):
            return func_b(*args, **kwargs)
        else:
            print("Error: todos los argumentos deben ser positivos")

    return func_c


@validar_positivos
def calcular_area(base, altura):
    print(f"Área: {base * altura / 2}")

@validar_positivos
def calcular_descuento(precio, porcentaje):
    print(f"Precio final: {precio - (precio * porcentaje / 100)}")

calcular_area(2,4)
calcular_descuento(200,10)