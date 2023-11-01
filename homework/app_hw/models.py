from django.db import models
from django.utils.text import slugify

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=50)
    abilities = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.abilities} - {self.description}'

    def get_absolute_url(self):
        return f'/characters/{self.pk}'


class MainCharacter(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.description}'

    def get_absolute_url(self):
        return f'/mainchar/{self.pk}'


class GuideGame(models.Model):
    num_floor = models.PositiveIntegerField()
    name_item = models.CharField(max_length=255)
    find_chest = models.CharField(max_length=255)
    description_items = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.num_floor} - {self.name_item} - {self.find_chest} - {self.description_items}'

    def get_absolute_url(self):
        return f'/guide/{self.pk}'


class Episode(models.Model):
    num_episode = models.PositiveIntegerField()
    heading = models.CharField(max_length=255)
    description_episode = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.num_episode} - {self.heading} - {self.description_episode}'

    def get_absolute_url(self):
        return f'/episode/{self.pk}'


class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/item/{self.pk}'