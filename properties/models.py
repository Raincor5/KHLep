from django.db import models


class Property(models.Model):
    """Property data."""
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    link = models.URLField()
    type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)


class PropertyCoordinates(models.Model):
    """Property coordinates."""
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)