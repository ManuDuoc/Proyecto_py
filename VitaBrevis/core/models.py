from django.db import models

# Create your models here.

class Categoria(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name='Codigo de la Categoria')
    nombreCategoria = models.CharField(max_length=20, verbose_name='Categoria', blank=False, null=False)

    def __str__(self):
        return self.nombreCategoria


class Juego(models.Model):
    idJuego = models.IntegerField(primary_key = True, verbose_name= 'Id del juego')
    titulo = models.CharField(max_length = 30, verbose_name= 'Titulo del Juego')
    nombreJuego = models.CharField(max_length = 30, verbose_name= 'Nombre del Juego')
    precioJuego = models.IntegerField(verbose_name= 'Precio del Juego')
    foto = models.ImageField(upload_to="juegos", null= True)
    video = models.URLField(max_length=200, verbose_name= 'Video del Juego')
    descripcion = models.TextField(verbose_name = 'Descripcion del Juego')
    masInfo1 = models.TextField(verbose_name = 'Mas Informacion del Juego 1')
    masInfo2 = models.TextField(verbose_name = 'Mas Informacion del Juego 2')
    masInfo3 = models.TextField(verbose_name = 'Mas Informacion del Juego 3')
    masInfo4 = models.TextField(verbose_name = 'Mas Informacion del Juego 4')
    masInfo5 = models.TextField(verbose_name = 'Mas Informacion del Juego 5')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrejuego