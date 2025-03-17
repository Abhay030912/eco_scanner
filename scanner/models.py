from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product Name
    barcode = models.CharField(max_length=50, unique=True)  # Barcode
    eco_score = models.IntegerField()  # Sustainability Score (1-100)
    recyclability = models.CharField(max_length=255)  # Can it be recycled?
    alternative = models.TextField(blank=True, null=True)  # Eco-friendly Alternative

    def __str__(self):
        return self.name
