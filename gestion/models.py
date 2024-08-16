from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', related_name='estudiantes', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField(null=True, blank=True)
    profesor = models.OneToOneField(Profesor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} (v{self.version})"

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}"

