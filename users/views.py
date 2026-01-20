from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomRegistrationForm
from .models import CustomUser

class RegisterView(CreateView):
    form_class = CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profiles')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class ProfileListView(ListView):
    model = CustomUser
    template_name = 'users/profiles.html'
    context_object_name = 'users'