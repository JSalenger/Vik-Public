from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(13)], null=True)
    avatar = models.ImageField(blank=True, null=True)
    activation_code = models.PositiveIntegerField(blank=True, null=True)
    is_activated = models.BooleanField(default=False)
