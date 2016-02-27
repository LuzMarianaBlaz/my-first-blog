from django.contrib import admin
#importamos el modelo post
from .models import Post

#esto es para hacer nuestro modelo visible en la pagina del administrador
admin.site.register(Post)
