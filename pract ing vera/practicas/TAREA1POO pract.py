from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    
    @abstractmethod
    def agregar(self):
        pass
    
    @abstractmethod
    def listar(self):
        pass
    
    @abstractmethod
    def buscar(self, id):
        pass
    
    @abstractmethod
    def eliminar(self, id):
        pass
       
class Empleado:
    _contador = 1
    def __init__(self, nombre, sueldo):
        self.id = Empleado._contador
        Empleado._contador += 1
        self.nombre = nombre
        self.sueldo = sueldo
        self.valor_hora = self.sueldo / 240

    def __str__(self):
        return f"[{self.id}] {self.nombre} | Sueldo: {self.sueldo} | Valor hora: {self.valor_hora:.2f}"
    
        
class TipoPermiso:
    _contador = 1

    def __init__(self, descripcion, remunerado):
        self.id = TipoPermiso._contador
        TipoPermiso._contador += 1
        self.remunerado = remunerado.upper()
        self.descripcion = descripcion


    def es_remunerado(self):
        return self.remunerado == "S"


    def __str__(self):
        return f"{self.id} {self.descripcion} es {self.remunerado}"

class Permiso:
    _contador = 1

    def __init__(self, id_empleado, id_tipo_permiso, fecha_desde, 
                 fecha_hasta, tipo, tiempo):
        self.id = Permiso._contador
        Permiso._contador += 1
        self.id_empleado = id_empleado
        self.id_tipo_permiso = id_tipo_permiso
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta 
        self.tipo = tipo.upper()
        self.tiempo = tiempo
 

    def __str__(self):
        return f"[{self.id}] Emp:{self.id_empleado} | Tipo:{self.id_tipo_permiso} | {self.fecha_desde} → {self.fecha_hasta} | {self.tipo} | {self.tiempo}"

empleados = []
tipos_permiso = []
permisos = []

def agregar_empleado(nombre, sueldo):
    e = Empleado(nombre, sueldo)
    empleados.append(e)
    return e

def listar_empleados():
    for e in empleados:
        print(e)

def buscar_empleado(id):
    for e in empleados:
        if e.id == id:
            return e
    return None

def eliminar_empleado(id):
    e = buscar_empleado(id)
    if e:
        empleados.remove(e)
        return True
    return False

def agregar_tipo_permiso(descripcion,remunerado):
    tp = TipoPermiso(descripcion, remunerado)
    tipos_permiso.append(tp)
    return tp

def listar_tipos_permiso():
    for tp in tipos_permiso:
        print(tp)

def buscar_tipo_permiso(id):
    for tp in tipos_permiso:
        if tp.id == id:
            return tp  
    return None

def eliminar_tipo_permiso(id):
    tp = buscar_tipo_permiso(id)
    if tp:
        tipos_permiso.remove(tp)
        return True
    return False

def agregar_permiso( id_empleado, id_tipo_permiso, fecha_desde, 
                 fecha_hasta, tipo, tiempo):
    ap = Permiso(id_empleado, id_tipo_permiso, fecha_desde, 
                 fecha_hasta, tipo, tiempo)
    permisos.append(ap)
    return ap

def listar_permisos():
    for ap in permisos:
        print(ap)

def buscar_permiso(id):
    for ap in permisos:
        if ap.id == id:
          return ap
    return None

def eliminar_permiso(id):
    ap = buscar_permiso(id)
    if ap:
        permisos.remove(ap)
        return True
    return False
 


e = Empleado("Anita Chacon", 300)
print(e)

t1 = TipoPermiso("Enfermedad", "S")
t2 = TipoPermiso("Asuntos personales", "N")
print(t1)
print(t2)
print(t1.es_remunerado())  
print(t2.es_remunerado())  
p1 = Permiso(1, 2, "2025-01-10", "2025-01-12", "d", 3)
print(p1)

agregar_empleado("Anita Chacon", 300)
agregar_empleado("Luis Mendoza", 960)
listar_empleados()

agregar_tipo_permiso("Enfermedad", "S")
agregar_tipo_permiso("Asuntos personales", "N")
listar_tipos_permiso()

agregar_permiso(1, 2, "2025-01-10", "2025-01-12", "D", 3)
listar_permisos()