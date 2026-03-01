from django.shortcuts import render
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})

def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car_detail.html', {'car': car})