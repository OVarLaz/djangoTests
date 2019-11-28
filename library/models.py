from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sbs = models.CharField(max_length=20)

class Biblioteca(models.Model):
    biblio = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sbs = models.CharField(max_length=20)
    colegio = models.CharField(max_length=20)
    enfermeria = models.CharField(max_length=20)
    bodega = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()

# Create your models here.
