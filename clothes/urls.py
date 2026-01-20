from django.urls import path
from . import views

urlpatterns = [
    # Путь будет пустой строкой, так как префикс 'clothes/' мы добавим в главном urls.py
    path('', views.ClothesListView.as_view(), name='clothes_list'),
]