from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

class Person(models.Model):
    firts_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.firts_name + ' ' + self.last_name
