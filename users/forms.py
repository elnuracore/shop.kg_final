from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser

class CustomRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'phone', 'experience', 'github_link', 'skills', 
            'expected_salary', 'education', 'preferred_lang', 
            'portfolio', 'telegram', 'about_me'
        )

class CaptchaLoginForm(AuthenticationForm):
    captcha = CaptchaField(label='Подтвердите, что вы не робот')