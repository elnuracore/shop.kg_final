from django.db import models
from django.contrib.auth.models import User

class HorseTour(models.Model):
    destination = models.CharField(max_length=100)
    tour_name = models.CharField(max_length=100)

class TourRegistration(models.Model):
    # OneToOne гарантирует: 1 пользователь = 1 запись (1 тур и 1 место)
    user = models.OneToOneField(User, on_submitted=models.CASCADE)
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE)