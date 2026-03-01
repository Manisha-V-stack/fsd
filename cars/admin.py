from django.contrib import admin
from .models import Car
from .models import Contact

admin.site.register(Contact)

admin.site.register(Car)