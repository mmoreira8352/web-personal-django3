from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titutlo")
    description = models.TextField(verbose_name = "Descripcion")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    url = models.URLField(null= True, blank= True, verbose_name="url")


    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
    def _str_(self):
        return self.title
