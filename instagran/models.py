from django.db import models
from django.contrib import admin


class Desafio(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    pontos = models.IntegerField()


admin.site.register(Desafio)
