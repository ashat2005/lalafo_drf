from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=100,
        verbose_name="Номер телефона"
    )
    profile_image = models.ImageField(
        upload_to='profile_image/',
        verbose_name="Фото профиля"
    )
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"