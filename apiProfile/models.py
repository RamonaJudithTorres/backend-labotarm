from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER=(
    ("male", "Másculino"),
    ("female", "Femenino"),
    ("Other", "Otro"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_profile=models.ImageField(upload_to='image_profile/', blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, choices=GENDER, blank=True, null=True, default="")
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f' {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  


class UserAddress(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f' {self.user.user.username}'
    

