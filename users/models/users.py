from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
