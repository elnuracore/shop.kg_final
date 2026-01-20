# clothes/admin.py
from django.contrib import admin
from .models import Brand, ClothesModel

admin.site.register(Brand)
admin.site.register(ClothesModel)