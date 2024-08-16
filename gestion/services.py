from .models import Estudiante, Profesor, Curso, Direccion

#CREATE
def crear_curso(codigo, nombre, version=None, profesor=None):
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version, profesor=profesor)
    return curso

def crear_profesor(rut, nombre, apellido, activo=False, creado_por=""):
    profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=False, creado_por=""):
    estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    return estudiante

def crear_direccion(calle, numero, comuna, ciudad, region, estudiante, dpto=None):
    direccion = Direccion.objects.create(calle=calle, numero=numero, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante, dpto=dpto)
    return direccion

#GET
def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

#ASIGNACION
def agrega_profesor_a_curso(curso, profesor):
    curso.profesor = profesor
    curso.save()

def agrega_cursos_a_estudiante(estudiante, cursos):
    estudiante.cursos.set(cursos)
    estudiante.save()

def imprime_estudiante_cursos(estudiante):
    return estudiante.cursos.all()

def imprime_informacion_estudiante(estudiante):
    cursos = estudiante.cursos.all()
    for curso in cursos:
        profesor = curso.profesor
        print(f"Estudiante: {estudiante.nombre} {estudiante.apellido}")
        print(f"Curso: {curso.nombre}")
        print(f"Profesor: {profesor.nombre} {profesor.apellido}")
        print("-" * 40)

