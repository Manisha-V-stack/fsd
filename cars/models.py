from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    image=models.ImageField(upload_to='cars/', null=True,blank=True)
    
    description = models.TextField()

    def __str__(self):
        return self.title