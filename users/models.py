from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # Добавьте этот импорт

class HorseTour(models.Model):
    destination = models.CharField(max_length=100, verbose_name="Местоположение")
    tour_name = models.CharField(max_length=100, verbose_name="Название тура")

    def __str__(self):
        return f"{self.tour_name} ({self.destination})"

class TourRegistration(models.Model):
    # Заменяем User на settings.AUTH_USER_MODEL
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь"
    )
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE, verbose_name="Выбранный тур")
    registration_date = models.DateTimeField(auto_now_add=True)
    
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    experience = models.IntegerField(default=0)
    github_link = models.URLField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    expected_salary = models.IntegerField(blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    preferred_lang = models.CharField(max_length=50, blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)