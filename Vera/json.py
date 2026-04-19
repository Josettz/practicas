import json


class ArchivosEjemplo:
    def ejecutar(self):

        print("=== ARCHIVOS ===")

        # =========================
        # ESCRITURA (write)
        # =========================
        print("\n=== WRITE ===")

        with open("archivo.txt", "w") as f:
            f.write("Hola mundo\n")
            f.write("Segunda línea\n")

        # =========================
        # LECTURA (read)
        # =========================
        print("\n=== READ ===")

        with open("archivo.txt", "r") as f:
            contenido = f.read()
            print(contenido)

        # =========================
        # LECTURA POR LÍNEAS
        # =========================
        print("\n=== READLINES ===")

        with open("archivo.txt", "r") as f:
            lineas = f.readlines()
            print(lineas)

        # =========================
        # APPEND
        # =========================
        print("\n=== APPEND ===")

        with open("archivo.txt", "a") as f:
            f.write("Nueva línea agregada\n")

        # =========================
        # JSON WRITE
        # =========================
        print("\n=== JSON WRITE ===")

        datos = {
            "nombre": "Juan",
            "edad": 25,
            "activo": True
        }

        with open("datos.json", "w") as f:
            json.dump(datos, f)

        # =========================
        # JSON READ
        # =========================
        print("\n=== JSON READ ===")

        with open("datos.json", "r") as f:
            data = json.load(f)
            print(data)

        # =========================
        # JSON COMPLEJO
        # =========================
        print("\n=== JSON COMPLEJO ===")

        usuarios = [
            {"nombre": "Ana", "edad": 20},
            {"nombre": "Luis", "edad": 30}
        ]

        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f)

        with open("usuarios.json", "r") as f:
            print(json.load(f))

        # =========================
        # EJERCICIO 1
        # =========================
        print("\n=== EJERCICIO 1 ===")

        with open("test.txt", "w") as f:
            f.write("Python\n")

        with open("test.txt", "r") as f:
            print(f.read())

        # =========================
        # EJERCICIO 2
        # =========================
        print("\n=== EJERCICIO 2 ===")

        datos = {"x": 10, "y": 20}

        with open("ejemplo.json", "w") as f:
            json.dump(datos, f)

        with open("ejemplo.json", "r") as f:
            print(json.load(f))

        # =========================
        # EJERCICIO 3 (ANÁLISIS)
        # =========================
        print("\n=== EJERCICIO 3 ===")

        with open("archivo.txt", "r") as f:
            print(type(f.read()))