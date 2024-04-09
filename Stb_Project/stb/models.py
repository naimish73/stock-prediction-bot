from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

