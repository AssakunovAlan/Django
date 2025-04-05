from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100) #Принимает строку
    author = models.CharField(max_length=50)
    publication_date = models.DateField()

