from django.shortcuts import render
from .models import Car

def home(request):
    cars = Car.objects.all()

    keyword = request.GET.get('keyword')
    if keyword:
        cars = cars.filter(title__icontains=keyword)

    return render(request, 'home.html', {'cars': cars})
from django.shortcuts import render, get_object_or_404
from .models import Car

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {'car': car})
from .models import Contact
from django.shortcuts import get_object_or_404

def contact_seller(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == "POST":
        Contact.objects.create(
            car=car,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return render(request, "success.html")

    return render(request, "contact.html", {"car": car})