from django.db import models
from django.core.validators import MaxValueValidator

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
    name:models.CharField(max_length=20)
    email:models.email()
    phone:models.IntegerField(max_length=10)
    is_manager:models.BooleanField(default=False)

    def __str__(self):
        return self.name
