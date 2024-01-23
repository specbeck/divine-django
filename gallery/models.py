from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     pass
class Memory(models.Model):
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.image} : {self.description}"
