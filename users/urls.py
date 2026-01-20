from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CaptchaLoginForm  # Убедитесь, что это имя совпадает с формой в forms.py

urlpatterns = [
path('register/', views.RegisterView.as_view(), name='register'),
    
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=CaptchaLoginForm
    ), name='login'),
    
    # Замените views.profile_list_view на views.ProfileListView.as_view()
    path('profiles/', views.ProfileListView.as_view(), name='profiles'),
]