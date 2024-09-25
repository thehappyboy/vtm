from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminUserCreationForm
from accounts.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User



class CustomUserChangeForm(UserChangeForm):
    pass


class AdminCustomUserCreationForm(AdminUserCreationForm):
    pass