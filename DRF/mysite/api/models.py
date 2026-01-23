from django.db import models

# Acá definimos los distintos modelos de base de datos que usaremos en el proyecto
# Se maneja la persistencia mediante un wrapper llamado ORM

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Título:" + self.title
    
