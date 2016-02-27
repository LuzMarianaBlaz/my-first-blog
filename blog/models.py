from django.db import models		#las lineas from e import se usan para añadir cosas desde otros archuvos
from django.utils import timezone 


#esta linea define nuestro modelo, este es un objeto, esto esta definido por la palabra "class", el nombre de nuestro modelo es Post, notar que la primera letra es mayuscula, esto debe hacerse siempre al definir un objeto, models.Model significa que Post es un modelo de Django
class Post(models.Model): 		
#estas cosas son propiedades, y para cada una hay que definir un tipo de campo	
	author=models.ForeignKey('auth.User') #foreignKey es un vinculo con otro modelo
	title=models.CharField(max_length=200) #es un texto con un numero limitado de caracteres
	text=models.TextField() #este es un texto sin limite de espacios
	created_date=models.DateTimeField(
		default=timezone.now)
	published_date=models.DateTimeField(
		blank=True,null=True)

	#ahora definiremos un metodo, llamado publish, para los nombres de metodos se deben usar minusculas y ningun espacio
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def _str_(self):				#los guiones son dunders
		return self.title			#cuando usemos este metodo nos devolvera el titulo de Post