from django.db import models

# Create your models here.
class Product(models.Model):
    sku=models.SlugField()
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField()
    sizes=(
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )
    size=models.CharField(max_length=1,choices=sizes)
    inventory=models.PositiveIntegerField()