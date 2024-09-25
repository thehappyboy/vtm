from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.forms import AdminCustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = AdminCustomUserCreationForm
    form = CustomUserChangeForm
    list_display = (
        "get_full_name", "username", "email", "department", "section", "is_serviceman", "is_engineer", "is_workman")
    list_filter = ("department", "section", "is_serviceman", "is_engineer", "is_workman")
    search_fields = ("username", "email", "department", "section", "is_serviceman", "is_engineer", "is_workman")
    ordering = ("username",)
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": (
            "is_engineer",
            "is_serviceman",
            "is_workman",
            "is_teamleader",
            "department",
            "section",
            "age",
            "phone")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email",)}),
    )
