class Estudiante:
    def __init__(self, matricula, nombre, semestre_actual):
        self.matricula = matricula
        self.nombre = nombre
        self.semestre_actual = semestre_actual
    def solicitar_tutoria(self):
        print(f"El estudiante {self.nombre} ha solicitado una tutoría.")
    def cancelar_tutoria(self):
        print(f"El estudiante {self.nombre} ha cancelado su solicitud de tutoría.")
     
class Tutor:
    def __init__(self, materias_dominadas, horas_impartidas=0): 
        self.materias_dominadas = materias_dominadas 
        self.horas_impartidas = horas_impartidas
    def aceptar_tutoria(self):
        print("Tutoría aceptada exitosamente.")
    def registrar_asistencia(self):
        print("Asistencia registrada. Sumando horas impartidas...")
     
class SesionTutoria:
    def __init__(self, id_sesion, tema_a_revisar, fecha_hora, estado, aula_asignada):
        self.id_sesion = id_sesion
        self.tema_a_revisar = tema_a_revisar
        self.fecha_hora = fecha_hora
        self.estado = estado 
        self.aula_asignada = aula_asignada
    def reprogramar_sesion(self, nueva_fecha_hora):
        self.fecha_hora = nueva_fecha_hora
        print(f"La sesión {self.id_sesion} ha sido reprogramada para el {self.fecha_hora}.")
    def finalizar_sesion(self):
        self.estado = "Finalizada"
        print(f"La sesión sobre '{self.tema_a_revisar}' ha concluido.")