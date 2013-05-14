#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class ArticuloCategoria(models.Model):
	nombre = models.CharField(max_length=100)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre
		
class Banner(models.Model):
	titulo = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='banners')
	link = models.CharField(max_length=400)

	def __unicode__(self):
		return self.titulo

class DiarioCategoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class NoticiaCategoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Principal(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.TextField()
	imagen = models.ImageField(upload_to='principal')
	link = models.CharField(max_length=50)

	def __unicode__(self):
		return self.titulo

class Articulo(models.Model):
	articulista = models.ForeignKey(User)
	titulo = models.CharField(max_length=50)
	texto = models.TextField()

	def __unicode__(self):
		return self.titulo

class Diario(models.Model):
	categoria = models.ForeignKey(DiarioCategoria)
	titulo = models.CharField(max_length=50)
	texto = models.TextField()
	imagen = models.ImageField(upload_to='diario')
	link = models.CharField(max_length=50)

	def __unicode__(self):
		return self.titulo

class Noticia(models.Model):
	categoria = models.ForeignKey(NoticiaCategoria)
	titulo = models.CharField(max_length=50)
	texto = models.TextField()
	imagen = models.ImageField(upload_to='noticia')
	visitas = models.IntegerField(default=0)
	reportero = models.ForeignKey(User) #Tipo de usuario reportero
	aprobado= models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

#Galerías
class Video(models.Model):
	nombre = models.CharField(max_length=100)
	link = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class FotoCategoria(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Foto(models.Model):
	categoria = models.ForeignKey(FotoCategoria)
	nombre = models.CharField(max_length=100)
	foto = models.ImageField(upload_to='fotogaleria')

	def __unicode__(self):
		return self.nombre

class Audio(models.Model):
	nombre = models.CharField(max_length=100)
	mp3 = models.FileField(upload_to='audiogaleria')

	def __unicode__(self):
		return self.nombre

class Publicidad(models.Model):
	POSICIONES = (
		(1,'Superior'),
		(2,'Inferior'),
		(3,'Derecha 1'),
		(4,'Derecha 2'),
		(5,'Izquierda'),
	)
	posicion = models.IntegerField(choices=POSICIONES)
	titulo = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='publicidad')
	link = models.CharField(max_length=100)

	def __unicode__(self):
		return self.pk

class UserProfile(models.Model):
	AREAS = (
        (1, 'Editor'),
        (2, 'Reportero'),
        (3, 'Publicista'),
        (4, 'Articulista')
    )
	user = models.OneToOneField(User)
	area = models.IntegerField(choices=AREAS)
	foto = models.ImageField(upload_to='fotos')
	bio = models.TextField()

	def __str__(self):  
		return "%s's profile" % self.user  

