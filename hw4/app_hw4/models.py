from django.db import models

# Create your models here.


class Furniture(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return f'name {self.name} - {self.cost} руб'


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'name {self.name} - {self.author}(автор)'


class Phone(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()

    def __str__(self):
        return f'name {self.name} - {self.cost}сум'
