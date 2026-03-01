from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.title


class Contact(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name