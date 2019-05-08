from django.db import models

# Create your models here.
class Temperature (models.Model):
    temp_id = models.IntegerField(primary_key=True, unique=True)
    temp_value = models.DecimalField(max_digits=4, decimal_places=2)
    date_created = models.DateField()

class Humidity (models.Model):
    humidity_id = models.IntegerField(primary_key=True, unique=True)
    humidity_value = models.DecimalField(max_digits=4, decimal_places=2)
    date_created = models.DateField()