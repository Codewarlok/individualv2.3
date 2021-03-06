import profile
from django.db import models
from registration.models import Profile
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    author = models.ForeignKey(profile, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "deal"
        verbose_name_plural = "deals"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title