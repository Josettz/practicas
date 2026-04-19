class FuncionesEjemplo:
    def ejecutar(self):

        # =========================
        # FUNCIÓN BÁSICA
        # =========================
        print("=== FUNCIÓN BÁSICA ===")

        def saludar():
            print("Hola mundo")

        saludar()

        # =========================
        # FUNCIÓN CON PARÁMETROS
        # =========================
        print("\n=== CON PARÁMETROS ===")

        def sumar(a, b):
            return a + b

        print(sumar(5, 3))

        # =========================
        # PARÁMETROS POR DEFECTO
        # =========================
        print("\n=== PARÁMETROS POR DEFECTO ===")

        def presentarse(nombre, edad=25):
            return f"{nombre} tiene {edad} años"

        print(presentarse("Ana"))
        print(presentarse("Luis", 30))

        # =========================
        # *args
        # =========================
        print("\n=== *args ===")

        def sumar_varios(*numeros):
            return sum(numeros)

        print(sumar_varios(1, 2, 3, 4))

        # =========================
        # **kwargs
        # =========================
        print("\n=== **kwargs ===")

        def mostrar_datos(**datos):
            for clave, valor in datos.items():
                print(clave, valor)

        mostrar_datos(nombre="Ana", edad=25)

        # =========================
        # FUNCIÓN LAMBDA
        # =========================
        print("\n=== LAMBDA ===")

        cuadrado = lambda x: x**2
        print(cuadrado(4))

        # =========================
        # RETORNO MÚLTIPLE
        # =========================
        print("\n=== RETORNO MÚLTIPLE ===")

        def dividir(a, b):
            return a / b, a % b

        cociente, resto = dividir(10, 3)
        print(cociente, resto)

        # =========================
        # RECURSIVIDAD
        # =========================
        print("\n=== RECURSIVIDAD ===")

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        print(factorial(5))

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        def doble(x):
            return x * 2

        print(doble(5))

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        def suma_lista(lista):
            return sum(lista)

        print(suma_lista([1, 2, 3, 4]))

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        def test(a, b=2):
            return a * b

        print(test(3))