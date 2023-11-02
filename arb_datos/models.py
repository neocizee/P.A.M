from django.db import models

# Create your models here.
class Vereda_estado(models.Model):
    estado = models.CharField(max_length=25)
    def __str__(self):
        return self.estado
    
class Arbol_estado(models.Model):
    estado = models.CharField(max_length=25)
    def __str__(self):
        return self.estado

class Arbol_especie(models.Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

class Arbol_area_detalles(models.Model):
    detalles = models.TextField(max_length=30)
    def __str__(self):
        return self.detalles


class Arbolado(models.Model):
    maps_long = models.FloatField()
    maps_lat = models.FloatField()
    observacion = models.TextField(max_length=200)
    fecha_act = models.DateField(auto_now=True, editable = False)
    
    arbol_area_detalles =  models.ForeignKey(Arbol_area_detalles, on_delete=models.CASCADE)
    arbol_especie = models.ForeignKey(Arbol_especie, on_delete=models.CASCADE)
    arbol_estado =  models.ForeignKey(Arbol_estado, on_delete=models.CASCADE)
    vereda_estado = models.ForeignKey(Vereda_estado, on_delete=models.CASCADE)

    altura_calle = models.IntegerField()
    ancho_vereda = models.FloatField()
    altura_aprox = models.IntegerField()
    circurns = models.FloatField()
    diametro = models.FloatField()


    tiene_clavel = models.BooleanField()
    vereda_damaged = models.BooleanField()
    vereda_levantada = models.BooleanField()
    element_rare = models.BooleanField()
    element_rare_type = models.TextField(max_length=50)
    element_rare_desc = models.TextField(max_length=200) 

    activo = models.BooleanField()


