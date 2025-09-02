from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, default="Unknown")
    price = models.IntegerField(validators=[MaxValueValidator(2000)])
    published_date = models.DateField()

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(
        validators=[
            MinValueValidator(1000000000),   # minimum 10-digit number
            MaxValueValidator(9999999999)    # maximum 10-digit number
        ]
    )
    is_manager=models.BooleanField(default=False)

    def __str__(self):
        return self.name
