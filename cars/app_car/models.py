from django.db import models

# Create your models here.


class Cars(models.Model):
    stamp_car = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.stamp_car} - {self.year} - {self.color} - {self.mileage} - {self.cost}'
