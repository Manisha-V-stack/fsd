from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
]