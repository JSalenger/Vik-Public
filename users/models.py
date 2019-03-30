from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)], null=True, blank=True)
    avatar = models.ImageField(blank=True)
