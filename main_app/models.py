from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    saga = models.TextField(max_length=250)
    move = models.TextField(max_length=250)


    def __str__(self):
        return f'{self.name} ({self.id})'