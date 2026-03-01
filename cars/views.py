from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Car, Contact


# ---------------- HOME ----------------
def home(request):
    cars = Car.objects.all()

    keyword = request.GET.get('keyword')
    if keyword:
        cars = cars.filter(title__icontains=keyword)

    return render(request, 'home.html', {'cars': cars})


# ---------------- CAR DETAIL ----------------
def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {'car': car})


# ---------------- CONTACT SELLER ----------------
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


@login_required
def dashboard(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'cars': cars})
@login_required
def add_car(request):
    if request.method == 'POST':
        Car.objects.create(
            user=request.user,
            title=request.POST['title'],
            brand=request.POST['brand'],
            year=request.POST['year'],
            price=request.POST['price'],
            fuel_type=request.POST['fuel_type'],
            transmission=request.POST['transmission'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('dashboard')

    return render(request, 'add_car.html')
@login_required
def edit_car(request, id):
    car = Car.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        car.title = request.POST['title']
        car.brand = request.POST['brand']
        car.year = request.POST['year']
        car.price = request.POST['price']
        car.fuel_type = request.POST['fuel_type']
        car.transmission = request.POST['transmission']
        car.description = request.POST['description']
        if request.FILES.get('image'):
            car.image = request.FILES['image']
        car.save()
        return redirect('dashboard')

    return render(request, 'edit_car.html', {'car': car})
@login_required
def delete_car(request, id):
    car = Car.objects.get(id=id, user=request.user)
    car.delete()
    return redirect('dashboard')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    ...

@login_required
def add_car(request):
    ...

@login_required
def edit_car(request, id):
    ...

@login_required
def delete_car(request, id):
    ...

@login_required
def contact_seller(request, id):
    ...