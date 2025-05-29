from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "id", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "email", "id", "phone_number")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "id", "phone_number", "password1", "password2"),
        }),
    )
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
admin.site.register(User, CustomUserAdmin)
