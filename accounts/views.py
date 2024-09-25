from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.forms import CustomUserCreationForm
from accounts.models import User

# Create your views here.
class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

