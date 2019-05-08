from django.contrib import admin

# Register your models here.
from .models import Temperature, Humidity

admin.site.register(Temperature)
admin.site.register(Humidity)
