from abc import ABC, abstractmethod
from datetime import datetime
import functools

# ==========================================================
# 1. DECORADORES
# ==========================================================
def decorador_interfaz(titulo):
    """Decorador para dar formato a los encabezados de las interfaces."""
    def wrapper(func):
        def inner(*args, **kwargs):
            print("=" * 40)
            print(f"{titulo.center(40)}")
            print("=" * 40)
            res = func(*args, **kwargs)
            return res
        return inner
    return wrapper


def manejar_errores(func):
    """Decorador: captura errores sin romper el programa."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"  ⚠  Error de valor: {e}")
        except FileNotFoundError as e:
            print(f"  ⚠  Error de archivo: {e}")
        except Exception as e:
            print(f"  ⚠  Error inesperado: {type(e).__name__} - {e}")
    return wrapper


# ==========================================================
# 2. MIXINS
# ==========================================================
class CalculosMixin:
    """Mixin para proveer funcionalidades de cálculo y validación."""
    def validar_fecha(self, fecha_str):
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            return None

    def calcular_descuento(self, tipo, tiempo, valor_hora, remunerado):
        if remunerado == 'S':
            return 0.0
        factor = 8 if tipo == 'D' else 1
        return round(float(tiempo) * factor * valor_hora, 2)

# ==========================================================
# 3. INTERFACES (CLASES ABSTRACTAS)
# ==========================================================
class ICrud(ABC):
    @abstractmethod
    def crear(self): pass

    @abstractmethod
    def consultar(self): pass

    @abstractmethod
    def eliminar(self): pass

# ==========================================================
# 4. ENTIDADES
# ==========================================================
class Empleado:
    secuencia = 0
    def __init__(self, nombre, sueldo):
        Empleado.secuencia += 1
        self.id = Empleado.secuencia
        self.nombre = nombre
        self.sueldo = float(sueldo)
        self.valor_hora = round(self.sueldo / 240, 2)

class TipoPermiso:
    secuencia = 0
    def __init__(self, descripcion, remunerado):
        TipoPermiso.secuencia += 1
        self.id = TipoPermiso.secuencia
        self.descripcion = descripcion
        self.remunerado = remunerado.upper()

class Permiso:
    secuencia = 0
    def __init__(self, emp_id, tipo_id, f_desde, f_hasta, tipo_dh, tiempo, descuento):
        Permiso.secuencia += 1
        self.id = Permiso.secuencia
        self.id_empleado = emp_id
        self.id_tipo_permiso = tipo_id
        self.fecha_desde = f_desde
        self.fecha_hasta = f_hasta
        self.tipo = tipo_dh.upper()
        self.tiempo = float(tiempo)
        self.descuento = descuento

# ==========================================================
# 5. CORE DEL SISTEMA (LÓGICA Y CRUD)
# ==========================================================

class SistemaGestion(ICrud, CalculosMixin):
    def __init__(self):
        self.empleados = []
        self.tipos_permisos = []
        self.permisos = []

    # ----------------------------------------------------------
    # CREAR
    # ----------------------------------------------------------
    @decorador_interfaz("REGISTRO DE EMPLEADO")
    @manejar_errores
    def crear_empleado(self):
        print(f"ID: {Empleado.secuencia + 1}")
        nombre = input("Nombre: ")
        sueldo = float(input("Sueldo: "))
        temp_emp = Empleado.__new__(Empleado)
        temp_emp.nombre = nombre
        temp_emp.sueldo = float(sueldo)
        temp_emp.valor_hora = round(float(sueldo) / 240, 2)
        print("-" * 40)
        print(f"Valor hora calculado: $ {temp_emp.valor_hora}")
        print("-" * 40)
        if input("¿Desea guardar? (1. Sí / 2. No): ") == "1":
            Empleado.secuencia += 1
            temp_emp.id = Empleado.secuencia
            self.empleados.append(temp_emp)
            print("Empleado guardado con éxito.")
            
    @decorador_interfaz("TIPO DE PERMISO")
    @manejar_errores
    def crear_tipo_permiso(self):
        print(f"ID: {TipoPermiso.secuencia + 1}")
        desc = input("Descripción: ")
        remu = input("¿Remunerado? (S/N): ").upper()
        if input("¿Guardar? (1. Sí / 2. No): ") == "1":
            self.tipos_permisos.append(TipoPermiso(desc, remu))
            print("Tipo de permiso registrado.")

    @decorador_interfaz("REGISTRO DE PERMISO")
    @manejar_errores
    def crear_permiso(self):
        emp_id = int(input("ID Empleado: "))
        tipo_id = int(input("ID Tipo Permiso: "))

        emp = next((e for e in self.empleados if e.id == emp_id), None)
        tp = next((t for t in self.tipos_permisos if t.id == tipo_id), None)

        if not emp or not tp:
            print("Error: Empleado o Tipo de Permiso no existe.")
            return

        f_desde_str = input("Fecha desde (DD/MM/YYYY): ")
        f_hasta_str = input("Fecha hasta (DD/MM/YYYY): ")

        f_desde = self.validar_fecha(f_desde_str)
        f_hasta = self.validar_fecha(f_hasta_str)

        if not f_desde or not f_hasta:
            print("Error: Formato de fecha inválido. Use DD/MM/YYYY.")
            return

        if f_hasta < f_desde:
            print("Error: La fecha hasta no puede ser anterior a la fecha desde.")
            return

        t_dh = input("Tipo (D/H): ").upper()
        if t_dh not in ('D', 'H'):
            print("Error: El tipo debe ser D (días) o H (horas).")
            return

        tiempo = float(input("Tiempo (cantidad): "))
        descuento = self.calcular_descuento(t_dh, tiempo, emp.valor_hora, tp.remunerado)

        print("-" * 40)
        print("Resumen:")
        print(f"  Empleado      : {emp.nombre}")
        print(f"  Tipo permiso  : {tp.descripcion}")
        print(f"  Fecha desde   : {f_desde_str}")
        print(f"  Fecha hasta   : {f_hasta_str}")
        print(f"  Tipo          : {'Días' if t_dh == 'D' else 'Horas'}")
        print(f"  Tiempo        : {tiempo}")
        print(f"  ¿Remunerado?  : {tp.remunerado}")
        print(f"  Descuento     : $ {descuento}")
        print("-" * 40)

        if input("¿Confirmar? (1. Sí / 2. No): ") == "1":
            nuevo_p = Permiso(emp_id, tipo_id, f_desde_str, f_hasta_str, t_dh, tiempo, descuento)
            self.permisos.append(nuevo_p)
            print("Permiso registrado correctamente.")

    # ----------------------------------------------------------
    # CONSULTAR
    # ----------------------------------------------------------
    def consultar(self):
        print("\n" + "=" * 40)
        print("LISTADO DE EMPLEADOS".center(40))
        print("=" * 40)
        if not self.empleados:
            print("  (Sin registros)")
        for e in self.empleados:
            print(f"  ID: {e.id} | {e.nombre} | Sueldo: $ {e.sueldo:.2f} | V/H: $ {e.valor_hora}")

        print("\n" + "=" * 40)
        print("LISTADO DE TIPOS DE PERMISO".center(40))
        print("=" * 40)
        if not self.tipos_permisos:
            print("  (Sin registros)")
        for t in self.tipos_permisos:
            print(f"  ID: {t.id} | {t.descripcion} | Remunerado: {t.remunerado}")

    @decorador_interfaz("CONSULTA DE PERMISOS")
    def consultar_permisos(self):
        if not self.permisos:
            print("  No hay permisos registrados.")
            return

        def detalle_permiso(p):
            emp = next((e for e in self.empleados if e.id == p.id_empleado), None)
            tp  = next((t for t in self.tipos_permisos if t.id == p.id_tipo_permiso), None)
            nombre_emp = emp.nombre if emp else "Desconocido"
            desc_tp    = tp.descripcion if tp else "Desconocido"
            tipo_label = "Días" if p.tipo == 'D' else "Horas"
            return (
                f"  ID: {p.id}\n"
                f"    Empleado     : {nombre_emp} (ID {p.id_empleado})\n"
                f"    Tipo permiso : {desc_tp} (ID {p.id_tipo_permiso})\n"
                f"    Desde        : {p.fecha_desde}  →  Hasta: {p.fecha_hasta}\n"
                f"    Tipo/Tiempo  : {tipo_label} — {p.tiempo}\n"
                f"    Descuento    : $ {p.descuento:.2f}"
            )

        lineas = list(map(detalle_permiso, self.permisos))
        for linea in lineas:
            print(linea)
            print("-" * 40)

    # ----------------------------------------------------------
    # ELIMINAR
    # ----------------------------------------------------------
    @decorador_interfaz("ELIMINAR REGISTRO")
    def eliminar(self):
        print("¿Qué desea eliminar?")
        print("  1. Empleado")
        print("  2. Tipo de Permiso")
        print("  3. Permiso")
        opc = input("Seleccione: ")
        if opc == "1":
            self._eliminar_empleado()
        elif opc == "2":
            self._eliminar_tipo_permiso()
        elif opc == "3":
            self._eliminar_permiso()
        else:
            print("Opción no válida.")

    def _eliminar_empleado(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return
        for e in self.empleados:
            print(f"  ID: {e.id} | {e.nombre}")
        try:
            emp_id = int(input("ID del empleado a eliminar: "))
            emp = next((e for e in self.empleados if e.id == emp_id), None)
            if not emp:
                print("Empleado no encontrado.")
                return
            vinculados = list(filter(lambda p: p.id_empleado == emp_id, self.permisos))
            if vinculados:
                print(f"Advertencia: este empleado tiene {len(vinculados)} permiso(s) registrado(s).")
            print(f"\nEmpleado a eliminar: {emp.nombre} | Sueldo: $ {emp.sueldo:.2f}")
            if input("¿Confirmar eliminación? (1. Sí / 2. No): ") == "1":
                self.empleados = list(filter(lambda e: e.id != emp_id, self.empleados))
                self.permisos = list(filter(lambda p: p.id_empleado != emp_id, self.permisos))
                print("Empleado (y sus permisos vinculados) eliminados correctamente.")
        except ValueError:
            print("ID inválido.")

    def _eliminar_tipo_permiso(self):
        if not self.tipos_permisos:
            print("No hay tipos de permiso registrados.")
            return
        for t in self.tipos_permisos:
            print(f"  ID: {t.id} | {t.descripcion} | Remunerado: {t.remunerado}")
        try:
            tp_id = int(input("ID del tipo de permiso a eliminar: "))
            tp = next((t for t in self.tipos_permisos if t.id == tp_id), None)
            if not tp:
                print("Tipo de permiso no encontrado.")
                return
            vinculados = list(filter(lambda p: p.id_tipo_permiso == tp_id, self.permisos))
            if vinculados:
                print(f"Advertencia: este tipo tiene {len(vinculados)} permiso(s) vinculado(s).")
            print(f"\nTipo a eliminar: {tp.descripcion} | Remunerado: {tp.remunerado}")
            if input("¿Confirmar eliminación? (1. Sí / 2. No): ") == "1":
                self.tipos_permisos = list(filter(lambda t: t.id != tp_id, self.tipos_permisos))
                self.permisos = list(filter(lambda p: p.id_tipo_permiso != tp_id, self.permisos))
                print("Tipo de permiso (y sus permisos vinculados) eliminados correctamente.")
        except ValueError:
            print("ID inválido.")

    def _eliminar_permiso(self):
        if not self.permisos:
            print("No hay permisos registrados.")
            return
        for p in self.permisos:
            emp = next((e for e in self.empleados if e.id == p.id_empleado), None)
            nombre = emp.nombre if emp else "Desconocido"
            print(f"  ID: {p.id} | Empleado: {nombre} | Desde: {p.fecha_desde} | Hasta: {p.fecha_hasta} | Descuento: $ {p.descuento:.2f}")
        try:
            per_id = int(input("ID del permiso a eliminar: "))
            per = next((p for p in self.permisos if p.id == per_id), None)
            if not per:
                print("Permiso no encontrado.")
                return
            emp = next((e for e in self.empleados if e.id == per.id_empleado), None)
            nombre = emp.nombre if emp else "Desconocido"
            print(f"\nPermiso a eliminar: ID {per.id} | {nombre} | Desde: {per.fecha_desde} | Descuento: $ {per.descuento:.2f}")
            if input("¿Confirmar eliminación? (1. Sí / 2. No): ") == "1":
                self.permisos = list(filter(lambda p: p.id != per_id, self.permisos))
                print("Permiso eliminado correctamente.")
        except ValueError:
            print("ID inválido.")

    # ----------------------------------------------------------
    # ESTADÍSTICAS
    # ----------------------------------------------------------
    @decorador_interfaz("ESTADÍSTICAS DE PERMISOS")
    def generar_estadisticas(self):
        total_emp = len(self.empleados)
        total_per = len(self.permisos)

        remu    = list(filter(lambda x: next((t.remunerado for t in self.tipos_permisos if t.id == x.id_tipo_permiso), 'N') == 'S', self.permisos))
        no_remu = list(filter(lambda x: next((t.remunerado for t in self.tipos_permisos if t.id == x.id_tipo_permiso), 'N') == 'N', self.permisos))

        total_tiempo     = functools.reduce(lambda a, b: a + b.tiempo, self.permisos, 0)
        total_descuentos = sum(map(lambda x: x.descuento, self.permisos))

        print(f"Total empleados              : {total_emp}")
        print(f"Total permisos               : {total_per}")
        print(f"Permisos remunerados         : {len(remu)}")
        print(f"Permisos no remunerados      : {len(no_remu)}")
        print(f"Total horas/días solicitados : {total_tiempo}")
        print(f"Monto total descontado       : $ {total_descuentos:.2f}")

    def crear(self): pass

# ==========================================================
# 6. MENÚ PRINCIPAL
# ==========================================================
def menu():
    sistema = SistemaGestion()
    while True:
        print("\n" + "=" * 40)
        print("SISTEMA DE GESTIÓN DE PERMISOS".center(40))
        print("=" * 40)
        print("1. Registrar Empleado")
        print("2. Registrar Tipo de Permiso")
        print("3. Registrar Permiso")
        print("4. Consultar Registros")
        print("5. Consultar Permisos")
        print("6. Eliminar Registro")
        print("7. Estadísticas")
        print("8. Salir")
        opc = input("Seleccione una opción: ")

        if   opc == "1": sistema.crear_empleado()
        elif opc == "2": sistema.crear_tipo_permiso()
        elif opc == "3": sistema.crear_permiso()
        elif opc == "4": sistema.consultar()
        elif opc == "5": sistema.consultar_permisos()
        elif opc == "6": sistema.eliminar()
        elif opc == "7": sistema.generar_estadisticas()
        elif opc == "8": break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()