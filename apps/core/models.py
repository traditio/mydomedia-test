from django.db import models

class Person(models.Model):
    name = models.CharField('Person', max_length=255)
