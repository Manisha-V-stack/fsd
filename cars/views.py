from django.shortcuts import render, redirect, get_object_or_404
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
@login_required
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


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'cars': cars})


# ---------------- ADD CAR ----------------
@login_required
def add_car(request):
    if request.method == 'POST':
        Car.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            brand=request.POST.get('brand'),
            year=request.POST.get('year'),
            price=request.POST.get('price'),
            fuel_type=request.POST.get('fuel_type'),
            transmission=request.POST.get('transmission'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            phone=request.POST.get('phone'),      # 🔥 IMPORTANT
            location=request.POST.get('location'),
        )
        return redirect('dashboard')

    return render(request, 'add_car.html')


# ---------------- EDIT CAR ----------------
@login_required
def edit_car(request, id):
    car = get_object_or_404(Car, id=id, user=request.user)

    if request.method == 'POST':
        car.title = request.POST.get('title')
        car.brand = request.POST.get('brand')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')
        car.fuel_type = request.POST.get('fuel_type')
        car.transmission = request.POST.get('transmission')
        car.description = request.POST.get('description')

        if request.FILES.get('image'):
            car.image = request.FILES.get('image')

        car.save()
        return redirect('dashboard')

    return render(request, 'edit_car.html', {'car': car})


# ---------------- DELETE CAR ----------------
@login_required
def delete_car(request, id):
    car = get_object_or_404(Car, id=id, user=request.user)
    car.delete()
    return redirect('dashboard')


# ---------------- REGISTER ----------------
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