from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:id>/', views.car_detail, name='car_detail'),
    path('contact/<int:id>/', views.contact_seller, name='contact_seller'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_car, name='add_car'),
    path('edit/<int:id>/', views.edit_car, name='edit_car'),
    path('delete/<int:id>/', views.delete_car, name='delete_car'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('mark-sold/<int:id>/', views.mark_as_sold, name='mark_sold'),
]
